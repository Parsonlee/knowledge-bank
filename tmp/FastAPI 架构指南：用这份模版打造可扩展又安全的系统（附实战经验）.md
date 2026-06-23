# FastAPI 架构指南：用这份模版打造可扩展又安全的系统（附实战经验）

[mp.weixin.qq.com](https://mp.weixin.qq.com/s/K7bbrvMRdUejCJu-vLlE-g)AI研究生 PyTorch研习社


我在生产环境中将这套结构打磨用于支持 500+ 并发用户；它扩展轻松、维护不累、生产力全速输出。

如果你只想直接在项目中使用该模板的 FastAPI 结构，请查看这个 GitHub repo，内含完整项目结构：https://github.com/brianobot/fastAPI_project_structure
![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fsz_mmbiz_png%2F6Ex6Atic0gTy3u4Bia2PTSsOfJn7zmJowReuO912HWkJhXMRdV4NZlgOSZjotlFoSUREOA5uLtJibc4JTQ10zmv9A%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%26tp%3Dwebp%26wxfrom%3D5%26wx_lazy%3D1%23imgIndex%3D0&valid=false)

## 简介

过去一年里我几乎每天都在使用 FastAPI。在此过程中，我总结出了一套标准项目结构：既能让我保持对改动与新增功能的积极性，又能很好地扩展。在这篇文章里，我会拆解我的 FastAPI "Go-To architecture" 的每个部分------这是我在新项目启动或旧项目重构时优先优化的那一套。不管你是想更快迭代想法、梳理日益增长的代码库，还是强化应用安全性，这套结构都能帮你自信构建，并像专业人士一样进化你的项目。


### 项目结构

### App 目录

App 目录是应用的引擎与核心，包含支撑大多数后端基础设施用例所需的全部模块与代码。下面我会解释该目录中的每个子目录与模块，并说明它们的使用理由，指出常见问题，以及为提升代码质量与开发者体验所做的改进。

**init** .py：在每个 Python 包中放置一个 **init** .py 是标准做法，它用于将文件夹声明为常规 Python Package。

api_router.py：我用它作为应用中统一管理全部 routers 的中心模块，这样可以方便实现版本控制（如 /v1/users、/v2/users），并让代码库保持清晰易读。

    # apps/api_router.py

    from fastapi import APIRouter

    api_v1 = APIRouter(prefix="/v1")
    api_v2 = APIRouter(prefix="/v2")

    # include routes to a root route
    # from app.routers import routers as user_routers
    # api_v1.include_router(users_routers)

logger.py：Logging 是每个软件应用的关键部分，它能提供运行时可见性，并在问题与 bug 出现时帮助定位与解决（它们终究会出现）。与其被繁杂配置淹没，这个模板在我几乎所有项目中都非常好用；你也可以拓展它，比如接入外部 handler，将日志发送到可视化面板或分析工具。这里的配置通过 TimedRotatingFileHandler 按天归档日志，让调试更高效。

    # apps/logger.py

    import logging
    import json

    from logging.handlers import TimedRotatingFileHandler

    logger = logging.getLogger()


    classJsonFormatter(logging.Formatter):
        defformat(self, record):
            log_record = {
                "timestamp": self.formatTime(record, self.datefmt),
                "level": record.levelname,
                "module": record.module,
                "funcName": record.funcName,
                "lineno": record.lineno,
                "message": record.getMessage(),
            }
            return json.dumps(log_record)


    file_handler = TimedRotatingFileHandler(
        "logs/app.log", when="midnight", interval=1 / 86400, backupCount=7
    )

    file_handler.setFormatter(JsonFormatter())

    logger.handlers = [file_handler]
    logger.setLevel(logging.INFO)

main.py：主模块是应用的入口点，应用的大部分安全策略与规则都在这里设置。

    # apps/mains.py

    from contextlib import asynccontextmanager
    from datetime import datetime, UTC
    from fastapi import FastAPI

    from starlette.middleware.trustedhost import TrustedHostMiddleware
    from starlette.middleware.base import BaseHTTPMiddleware
    from fastapi.middleware.gzip import GZipMiddleware
    from fastapi.middleware.cors import CORSMiddleware
    from fastapi.responses import RedirectResponse
    from fastapi.responses import JSONResponse
    from fastapi.requests import Request
    from fastapi import HTTPException
    from fastapi import FastAPI

    from slowapi import Limiter
    from slowapi.util import get_remote_address

    from redis import asyncio as aioredis

    from app.logger import logger
    from app.api_router import api
    from app.settings import Settings
    from app.middlewares import log_request_middleware

    settings = Settings()


    @asynccontextmanager
    asyncdeflifespan(app: FastAPI):
        yield


    definitiate_app():
        app = FastAPI(
            title="FastAPI Sample Project",
            summary="API for FastAPI Sample Project",
            lifespan=lifespan,
        )

        origins = [
            # Add allowed origins here
        ]

        app.add_middleware(
            CORSMiddleware,
            allow_origins=origins,
            allow_credentials=True,
            allow_methods=["*"],
            allow_headers=["*"],
        )

        # tweak this to see the most efficient size
        app.add_middleware(GZipMiddleware, minimum_size=100)
        app.add_middleware(
            TrustedHostMiddleware,
            allowed_hosts=[
                # Add allowed hosts here, this controls host that the application can be hosted on
            ],
        )
        app.add_middleware(BaseHTTPMiddleware, dispatch=log_request_middleware)
        
        # this handles rate limiting protecting the API from abuse or Denial of Service Attacks
        limiter = Limiter(key_func=get_remote_address)
        app.state.limiter = limiter

        app.include_router(api)
        return app


    app = initiate_app()


    @app.exception_handler(HTTPException)
    asyncdefhttp_exception_handler(request: Request, exc: HTTPException):
        return JSONResponse(
            status_code=exc.status_code,
            content={
                "detail": exc.detail,
                "path": request.url.path,
                "timestamp": datetime.now(UTC).isoformat(),
            },
        )


    @app.exception_handler(Exception)
    asyncdefglobal_exception_handler(request: Request, exc: Exception):
        logger.error(f"Unexpected error: {str(exc)}")

        return JSONResponse(
            status_code=500,
            content={
                "detail": "An unexpected error occurred",
                "path": request.url.path,
            },
        )


    @app.get("/", tags=["Root"])
    asyncdefroot():
        # this redirects root requests to the docs page
        return RedirectResponse("/docs")

settings.py：我发现使用 pydantic 的 BaseSettings 处理环境变量既简单又干净。你可以为环境变量定义类型，这些类型会在应用启动时验证；对于可选环境变量，还可以提供默认值。

    #apps/settings.py

    from pydantic_settings import BaseSettings
    from pydantic import ConfigDict, AnyUrl


    classSettings(BaseSettings):
        model_config = ConfigDict(env_file=".env")

        example_secret: str = "example secret value"

        JWT_SECRET: str# required environment variable 
        JWT_ALGORITHM: str = "HS256"# optional environement variable with default value 

dependencies.py：我用这个模块来集中管理自定义的路由依赖。像 get_db 这类常用依赖（例如获取与数据库交互的 Session）都可以在这里声明。单独的依赖模块能让代码组织更清晰、更模块化（不同路由通常都会依赖这些依赖项），测试也更方便，因为逻辑可以被隔离验证。

middlewares.py：我用这个模块来集中管理应用的自定义 middlewares。为依赖模块所述的模块化优势，这里同样适用。

**目录**

Routers 目录：我倾向于为每个逻辑路由分组创建独立模块，使开发更愉悦、更简单。例如，用一个 auth.py 模块来放与用户认证和用户资料管理相关的全部路由；用 products.py 放与商品管理相关的路由；用 admin.py 放与管理员 API 相关的全部路由。我尽量让路由函数不超过 2 行代码：路由函数只负责声明路由、定义依赖与请求参数；每个路由的业务逻辑放在对应的 service 函数中。

    #apps/routers/auth.py

    from typing import Annotated

    from pydantic import EmailStr
    from fastapi.routing import APIRouter
    from sqlalchemy.ext.asyncio import AsyncSession
    from fastapi import Depends, Body, BackgroundTasks

    from app.dependencies import get_db
    from app.schemas import auth as auth_schemas
    from app.services import auth as auth_services

    router = APIRouter(prefix="/auth", tags=["Authentication"])


    EmailBody = Annotated[EmailStr, Body(embed=True)]
    DBDep = Annotated[AsyncSession, Depends(get_db)]


    @router.post("/signup", response_model=auth_schemas.UserModel)
    asyncdefsignup(
        db: DBDep,
        bg_task: BackgroundTasks,
        request_data: auth_schemas.UserSignUpData,
    ):
        returnawait auth_services.signup_user(request_data, db, bg_task)


这样的路由函数看起来更清爽，业务逻辑由 service 函数处理；路由本身只关注依赖、请求体或查询参数等要求。

Schema 目录：我把所有 pydantic models 放在 schema 模块。与 Routers 目录类似，Schema 目录中包含全部 schemas 模块。通常我会让每个路由模块与一个对应的 schema 模块和一个 service 模块相匹配。这样应用的每个组件都能以非常逻辑化、可预期的方式归档。例如 auth.py 的一个 schema 模型如下：

    # apps/schemas/auth.py
    from uuid import UUID
    from datetime import datetime
    from typing import Annotated

    from pydantic import BaseModel, EmailStr, Field


    classUserSignUpData(BaseModel):
        password: Annotated[str, Field(min_length=8)]
        email: Annotated[EmailStr, Field(max_length=254)]


    classUserModel(BaseModel):
        id: UUID

        email: EmailStr
        date_created: datetime
        date_updated: datetime

Service 目录：Service 目录存放实际的业务逻辑模块，比如调用第三方 API、对数据库发起查询等。将它们这样分离可以把路由对 API 的声明性需求与具体实现进行关注点分离。与 Routers 和 Schemas 目录一样，我会让它们在组件维度上一一对应。以下以 auth 组件为例：

    # apps/services/auth.py

    from datetime import timedelta

    from fastapi import HTTPException
    from passlib.context import CryptContext
    from fastapi.security import OAuth2PasswordBearer

    from sqlalchemy import select
    from sqlalchemy.ext.asyncio import AsyncSession

    from app.settings import Settings
    from app.models import User as UserDB
    from app.schemas import auth as auth_schema

    settings = Settings()

    JWT_SECRET = settings.JWT_SECRET
    JWT_ALGORITHM = settings.JWT_ALGORITHM

    ACCESS_TOKEN_LIFESPAN = timedelta(days=2)
    REFRESH_TOKEN_LIFESPAN = timedelta(days=5)

    pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
    oauth2_scheme = OAuth2PasswordBearer(tokenUrl="v1/auth/token")


    defverify_password(plain_password: str, hashed_password: str):
        return pwd_context.verify(plain_password, hashed_password)


    defget_password_hash(password: str):
        return pwd_context.hash(password)


    asyncdefget_user(email: str, session: AsyncSession) -> UserDB | None:
        stmt = select(UserDB).where(UserDB.email == email)
        result = await session.execute(stmt)
        return result.scalar_one_or_none()


    asyncdefcreate_user(
        user_data: auth_schema.UserSignUpData,
        session: AsyncSession,
    ):
        result = await session.execute(
            select(UserDB).where(UserDB.email == user_data.email)
        )
        if result.scalar_one_or_none():
            raise HTTPException(status_code=400, detail="Email already registered")

        result = await session.execute(
            select(UserDB).where(UserDB.email == user_data.email)
        )
        if result.scalar_one_or_none():
            raise HTTPException(status_code=400, detail="Username already used")

        hashed_password = get_password_hash(user_data.password)
        new_user = UserDB(
            email=user_data.email,
            password=hashed_password,
            username=user_data.email,
        )

        session.add(new_user)
        await session.commit()
        await session.refresh(new_user)
        return new_user


    asyncdefsignup_user(
        data: auth_schema.UserSignUpData,
        session: AsyncSession,
    ):
        returnawait create_user(data, session)


除了核心的 Python 后端部分，我也很推荐使用 Makefile 这类工具，来简化常见命令行工具的调用，比如启动 FastAPI server、运行 pytest 等。

    # Makefile

    run-local:
     fastapi dev app/main.py

    test-local:
     pytest -s --cov

    coverage-report:
     coverage report

    coverage-html:
     coverage report && coverage html

要使用 make，需要先在你的电脑上安装它。

在项目根目录放置好这个文件后，每当我想启动 FastAPI server，只需运行：

    make run-local

这样就不用每次都敲完整命令了，对于频繁执行的命令工具，能显著提升效率。

### 总结

在这份模板中，我没有包含数据库连接的设置。维护一个模块化的项目结构和代码库，会在后续带来超出预期的收益：可预期、合理的功能与工具组织，会让代码库的"美感"超越功能本身。尽管这一套模式在过去一年里显著提升了我的生产力，我仍在持续学习并拥抱更好的后端架构方式与实践。这份模板的完整代码可在 Github 查看：https://github.com/brianobot/fastAPI_project_structure


[Read in Cubox](https://cubox.pro/web/card/7382725346631617891)

# 目标

保证准确率的情况下，ner识别到的占整体的比例越来越大

![图标 描述已自动生成](media/image1.png){width="6.299407261592301in"
height="2.9166174540682417in"}

# 流程

1.  去除非药盒，或者ocr无法识别文字的图片 \@顾倩

2.  图片去除白框@杨子豪

3.  ocr识别上1/3内容，排除无内容的图片 \@杨子豪

4.  ocr识别图片的全部文字

5.  ner找到文字中的品牌 （5/10训练）@侯庆

注：以上数据测试数据为图灵1000条

  ------------------------------------ -------------------- ----------------------
  指标                                 概率（之前）         概率（之后）

  准确率（识别到且识别正确的）         40.5%（199/492）     

  ocr识别率（ocr识别文字中有品牌的）   50.2%(502/1000)      

  ner识别到的占整体的比例              49.2%(492/1000)      
  ------------------------------------ -------------------- ----------------------

- clip之后保留了739条数据，对这堆数据进行ner，找出来654个，其中正确的有396，最后60.55%的准确率

- ocr上1/3有无文字方案，保留了852条数据，对这堆数据进行ner，找出来757个，正确的有364，准确率48%

- ocr上1/3有无文字 + CLIP
  方案：保留了662条数据，对这堆数据进行ner，找出来596个，正确的有364，准确率61%

- ocr上1/3有无文字 + CLIP
  方案：保留了662条数据，对这堆数据进行ner新模型，找出来456个，正确的有320，准确率70.2%

- ocr直接ner方案：对这堆数据进行ner新模型，找出来594个，正确的有444，准确率75%（发现clip方法和1/3方法效果不限制）

- 

# 待办事项

## OCR

  ------------------------------------------- -------------
  事项                                        是否完成

  低质量、图片模糊                            

  背景裁剪                                    done

  上1/3无字不用                               done

  对于无商标 和 识别为 口罩，测温仪等都剔除   

                                              

                                              
  ------------------------------------------- -------------

## NER

  ------------------------------------------- -------------
  事项                                        是否完成

                                              

  中英文对照表                                

  对于无商标 和 识别为 口罩，测温仪等都剔除   

                                              

                                              
  ------------------------------------------- -------------

# 过程

5/14

清理库，然后撞库来做base

这个base可能很难超

结论：其实挺好超的，因为库太大了，经常出现一个应该refuse的，但是他能撞到别的品牌，导致错误率太高

5/15

中英文对照大概会影响有5%的准确率。这个能找到的话，还挺重要的

ocr_hit: 品牌在ocr里

ner_hit: ner返回品牌

ner_correct: ner返回正确品牌

ner_bad_hit: ner返回错误品牌，并且品牌不在ocr里

ner_wrong_hit: ner返回错误品牌，并且品牌在ocr里

ner_accuracy: ner准确率

不撞库：

ocr_hit: 765

ner_hit: 713

ner_correct: 551

ner_bad_hit: 79

ner_wrong_hit: 83

ner_accuracy: 0.7728

撞库：

ocr_hit: 765

ner_hit: 492

ner_correct: 463

ner_bad_hit: 15

ner_wrong_hit: 14

ner_accuracy: 0.9411

再练一版

未校正，不撞库

ocr_hit: 711

ner_hit: 739

ner_correct: 443

ner_bad_hit: 135

ner_wrong_hit: 163

ner_accuracy: 0.5995

矫正+不撞库

ocr_hit: 749

ner_hit: 739

ner_correct: 563

ner_bad_hit: 97

ner_wrong_hit: 87

ner_accuracy: 0.7618

矫正+撞库

ocr_hit: 749

ner_hit: 469

ner_correct: 458

ner_bad_hit: 5

ner_wrong_hit: 7

ner_accuracy: 0.9765

同一数据对比1000条训练模型

不撞库：

ocr_hit: 749

ner_hit: 705

ner_correct: 521

ner_bad_hit: 91

ner_wrong_hit: 100

ner_accuracy: 0.739

撞库：

ocr_hit: 749

ner_hit: 450

ner_correct: 423

ner_bad_hit: 6

ner_wrong_hit: 22

ner_accuracy: 0.94

有提升

5-20

ocr_hit: 302

ner_hit: 250

ner_correct: 233

ner_false_hit: 9

ner_wrong_hit: 8

ner_accuracy: 0.932

5-22

ocr_hit: 395

ner_hit: 280

ner_correct: 265

ner_false_hit: 7

ner_wrong_hit: 8

ner_accuracy: 0.9464

待办：

品牌库找相似

训练数据品牌全换成中文

文字处理：

纱布

口罩

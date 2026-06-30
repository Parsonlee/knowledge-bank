---
title: Linux 命令分类速查
type: concept
confidence: high
tags:
  - Skill/linux
---

# 概念：Linux 命令分类速查

## 定义

将 Linux 命令按功能场景（系统/文件/网络/软件包等）分类组织的速查体系，便于按需快速定位命令，而非按字母或学习顺序排列。

## 28 大功能分类（来自来源全文）

### 系统与硬件信息
- 基本命令：`uname`/`dmidecode`/`hdparm`/`arch`/`cat /proc/cpuinfo|meminfo|version`
- 系统常用：`ps`/`top`/`free`/`kill`/`systemctl`
- 文件系统分析：`fdisk`/`fsck`

### 文件与目录
- 文件和目录：`cd`/`ls`/`mkdir`/`cp`/`mv`/`rm`/`ln`
- 文件搜索：`find`/`locate`/`whereis`/`which`
- 查看文件内容：`cat`/`more`/`less`/`head`/`tail`
- 查看文件类型：`file`
- 文件权限：`chmod`/`chown`/`chgrp`
- 文件特殊属性：`chattr`/`lsattr`

### 文本处理
- `grep`/`sed`/`awk`/`sort`/`cut`/`paste`/`tr`
- 字符设置与格式转换：`iconv`/`dos2unix`

### 磁盘与文件系统
- 磁盘空间：`df`/`du`
- 挂载文件系统：`mount`/`umount`/`fuser`
- 初始化文件系统：`mkfs`/`mke2fs`
- SWAP：`mkswap`/`swapon`/`swapoff`

### 用户与权限
- 用户和群组：`useradd`/`userdel`/`groupadd`/`passwd`/`chage`

### 打包压缩与备份
- 打包压缩：`tar`/`gzip`/`bzip2`/`zip`/`unzip`
- 备份：`dump`/`restore`/`rsync`/`dd`
- 光盘：`cdrecord`/`mkisofs`

### 软件包管理
- RPM：`rpm -ivh/-e/-qa/-qi`
- YUM：`yum install/update/remove/search`
- DEB：`dpkg`/`apt-get`

### 网络
- `ifconfig`/`ip`/`route`/`netstat`/`ss`/`iptables`

### 编辑器
- VIM：`vi`/`vim` 操作快捷键

## 关机命令
- `shutdown -h now`/`init 0`/`reboot`/`logout`/`shutdown -c`（取消预定关机）

## 使用建议
- 适合作为运维速查手册，按场景分组查找
- 不适合从零系统学习 Linux

## 来源
- [[600条Linux命令速查手册]] — 28 大类约 600 条命令完整整理

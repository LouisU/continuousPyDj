# continuousPyDj 
![](media/img/python.png "python") 
![](media/img/docker.png "docker") 
![](media/img/django.png "django") 

## 通过一个后端项目，持续练习学习以下开发技能:
### [1. Python](#1-python)

### [2. Django](#2-django)

### [3. Django REST API](#3-django-rest-api)

### [4. Celery](#4-celery)

### [5. Docker](#5-docker)

### [6. Git](#6-git)

### [7. Github](#7-github)

### [8. MarkDown](#8-markdown)

***
### 编写README文档的原则和顺序:
  1. 一切从需求出发，先解决问题。
  2. 解决问题后，回头将需要了解原理的步骤深入了解。

***
## 1. Python
    Python的基础篇
    Python的魔法函数

## 2. Django

## 3. Django REST API

## 4. Celery

## 5. Docker

## 6. Git
  ### 1. 对本地仓库的操作
    git init # 初始化
    git add FILE_NAME/DIRECTORY_NAME  # 添加指定的文件/文件夹更新到本地仓库
    git add . # 添加所有的更新到本地仓库
    git commit -m "This is first commit"
    git branch # 查看当前处于的本地分支
    git branch test # 创建本地分支test, 指正Head不变，之前指哪还是指哪
    git checkout -b readdev # 基于当前本地分支(master)创建新的分支(readdev), Head指针指向新分支readdev
    git checkout master # 切换回到本地的master分支
    git branch -d test # 删除test分支，删除test分支的时候Head指针不能指向test分支。
    git branch -r -d origin/master # 删除本地的远程分支origin/master。只是删除了开发本地的远程分支，不是删除github上面的master分支。
    git checkout -b readme origin/dev # 创建新的本地分支readme, 并且让该本地分支追踪远程分支origin/dev.
    git branch -u origin/dev # 设置当前分支追踪远程分支origin/dev
    git branch -vv # 查看当前分支的追踪情况
    git branch -u origin/dev # 设置当前本地追踪远程分支origin/dev
      # Todo 设置追踪关系有什么作用和意义？
      追踪origin/dev后，当运行git status命令时，会提醒当前分支和origin/dev分支的先后关系。是否本地版本落后于origin/dev(远程有跟新，但本地没拉取), 或者先于origin/dev(本地有更新，但没有推送到远程)。
    git branch --unset-upstream # 解除当前本地分支和远程分支的追踪关系
    git diff <source_branch> <target_branch>  # 查看当前分支和目标分支的区别
    git remote -v  # 下面显示了可抓取和推送的origin的地址。如果没有推送权限，就看不到push的地址。
      origin  https://github.com/wangmingshun/studygit.git (fetch)
      origin  https://github.com/wangmingshun/studygit.git (push)
      # Todo 如何使得project clone下来之后没有push权限？

    git config color.ui true # 彩色的输出
    git config format.pretty oneline # 显示历史记录时，只显示一行注释信息
    git tag 1.0.0 1b2e1d63ff # 为分支1b2e1d63ff打上版本标签
    # Todo Git中的tag命令和Github上的版本管理如何联系起来？
    
  
  ### 2. 对远程仓库的操作
    git remote add cpd https://github.com/LouisU/continuousPyDj.git  # 添加远程仓库，命名远程仓库的名字为cpd
    git remote rename cpd origin # 修改本地的远程仓库cpd的名字，将cpd改成了origin
    git fetch cpd # 拉取远程仓库的文件
    git merger cpd/master # 将远程分支cpd/master合并到当前分支
    git pull cpd/master # 将远程的分支拉取下来并且合并到当前分支
    
    git push cpd master cpd/master 

  ~~### 3. 本地远程之间操作：
    git fetch xxx
    git merge xxx~~
  
    # Todo 改版本的git操作分类是本地和远程操作。这样的分类也无法分类清晰。
    # Todo 后期将改成：基本操作、高阶操作、场景应用

## 7. Github
    1. 设置不可直接推送到github master分支。
      project registory -> branches -> master分支上的change default branch -> add rule

      添加保护master的规则: Require pull request reviews before merging. 只能push到其他分支，然后发pull request. 

      注意: Branch name pattern需要填一个能匹配上master的模型。（我这里直接写成master）

## 8. MarkDown
详情参照： https://github.com/guodongxiaren/README#readme  
    1. 标题语法 “#” “##” “###”

    2. 页内跳转
          锚点语法: 跳转点的语法 [锚点内容](#跳转点的标题)
          锚点目标: 目标点的语法 #标题

    3. 有序列表的语法: 数字 + 英文句号 + 空格 + 列表内容
       举个栗子: 
        1. 安装
        2. 配置

    4. 无序列表的语法: -/* + 空格 + 列表内容
        * 水果
        * 服饰

    5. 链接图片语法 ![Alt](URL title)
        Alt 是指图片显示失败时显示的内容
        URL 可以是网络图片http url，也可以是该项目中相对路径
        title 是鼠标悬停在图片上提示的消息
        文章底百度log是网络图片 二维码是相对路径

    6. 显示横线效果语法: *** / --- 

***  
![baidu](https://camo.githubusercontent.com/15675678891dead0d516b6ee7a57ed12101ce69a/687474703a2f2f7777772e62616964752e636f6d2f696d672f62646c6f676f2e676966 "百度logo")  
欢迎扫码加好友一起学习讨论：  
![](./media/img/qrcode.jpg "微信扫码加好友")


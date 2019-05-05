# Git 命令

##### [Git好文参考: Guthub上arslanbilal/git-cheat-sheet项目](https://github.com/arslanbilal/git-cheat-sheet/blob/master/README.md )
   
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
```
# Todo 设置追踪关系有什么作用和意义？  
追踪origin/dev后，当运行git status命令时，会提醒当前分支和origin/dev分支的先后关系。是否本地版本落后于origin/dev(远程有跟新，但本地没拉取), 或者先于origin/dev(本地有更新，但没有推送到远程)。  
```
git branch --unset-upstream # 解除当前本地分支和远程分支的追踪关系  
git diff <source_branch> <target_branch> # 查看当前分支和目标分支的区别  
git remote -v # 下面显示了可抓取和推送的origin的地址。如果没有推送权限，就看不到push的地址。  
  ```
  origin  https://github.com/wangmingshun/studygit.git (fetch)  
  origin  https://github.com/wangmingshun/studygit.git (push)  
  # Todo 如何使得project clone下来之后没有push权限？
  ```
    

git config color.ui true # 彩色的输出  
git config format.pretty oneline # 显示历史记录时，只显示一行注释信息  
git tag 1.0.0 1b2e1d63ff # 为分支1b2e1d63ff打上版本标签  
```
# Todo Git中的tag命令和Github上的版本管理如何联系起来？
```

git log --oneline --abbrev-commit --all --graph --decorate --color # 可以CMD命令行中看到分支的情况，且用彩色的图形表示出来。可以直接采用 [`SourceTree`](https://www.sourcetreeapp.com ) 开源软件来学习和观察分支在开发中变化情况。
    
  
### 2. 对远程仓库的操作
    git remote add cpd https://github.com/LouisU/continuousPyDj.git  # 添加远程仓库，命名远程仓库的名字为cpd
    git remote rename cpd origin # 修改本地的远程仓库cpd的名字，将cpd改成了origin
    git fetch cpd # 拉取远程仓库的文件
    git merger cpd/master # 将远程分支cpd/master合并到当前分支
    git pull cpd/master # 将远程的分支拉取下来并且合并到当前分支
    
    git push cpd master cpd/master  # 将远程分支cpd/master拉取并合并到本地master分支上
    git reset --hard 1234abcd # 重新返回id为1234abcd的commit处

  ~~### 3. 本地远程之间操作：
    git fetch xxx
    git merge xxx~~
  
    
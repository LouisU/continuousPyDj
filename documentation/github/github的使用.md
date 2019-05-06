# github的使用

1. 设置不可直接推送到github master分支。
      project registory -> branches -> master分支上的change default branch -> add rule

      添加保护master的规则: Require pull request reviews before merging. 只能push到其他分支，然后发pull request. 

      注意: Branch name pattern需要填一个能匹配上master的模型。（我这里直接写成master）

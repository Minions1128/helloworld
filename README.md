# helloworld

This project is for testing.

![](https://github.com/Minions1128/helloworld/blob/master/jpg/minions_18318978.jpg)

## Git 简单命令

### 配置Git

http://www.runoob.com/w3cnote/git-guide.html

### 添加文件

touch test.txt
git add test.txt
git commit -m "add a file"
git push

### 删除文件

git rm test.txt
git commit -m "remote a file"
git push

### 删除本地所有未提交的更改

1. git clean -df
2. git reset --hard

## windows 教程

### 安装Tortoise

www.google.com.hk

### Pull第一个项目

新建文件 -- 右击 -- Git这里创建版本库
选择Pull一个项目，如：

git@github.com:Minions1128/helloworld.git

选择putty秘钥，公钥粘贴在

https://github.com/settings/keys

的New SSH key里；私钥自己保存。

### Push一个项目

编辑完文件之后，先要commit，然后再进行push

### 管理远端

右击 -- 设置 -- Git -- 远端 进行管理

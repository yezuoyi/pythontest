#!/usr/bin/python3

# 打开文件
fo = open("test.txt", "w")
print("文件名为: ", fo.name)
seq = ["菜鸟教程 1", "菜鸟教程 2", "菜鸟教程 3 ", "菜鸟教程 4", "菜鸟教程 5", "菜鸟教程 6"]

seq.reverse()

seq = [str(x)+"\n" for x in seq]

fo.writelines(seq)

# 关闭文件
fo.close()

#!/usr/bin/python3

# 计算面积函数
def area(width, height):
    return width * height
 
def print_welcome(name):
    print("Welcome", name)

print_welcome("Runoob")
w = 4
h = 5
print("width =", w, " height =", h, " area =", area(w, h))


def ChangeInt(a):
    a = 10


b = 2
ChangeInt(b)
print(b)  # 结果是 2


# 可写函数说明
def changeme(mylist):
   "修改传入的列表"
   mylist.append([1, 2, 3, 4])
   print("函数内取值: ", mylist)
   return


# 调用changeme函数
mylist = [10, 20, 30]
changeme(mylist)
print("函数外取值: ", mylist)


#可写函数说明
def printme(str):
   "打印任何传入的字符串"
   print(str)
   return


#调用printme函数
printme(str="菜鸟教程")


''' #可写函数说明
def printinfo(name, age):
   "打印任何传入的字符串"
   print("名字: ", name)
   print("年龄: ", age)
   return


#调用printinfo函数
printinfo(age=50, name="runoob") '''


#可写函数说明
def printinfo(name, age=35):
   "打印任何传入的字符串"
   print("名字: ", name)
   print("年龄: ", age)
   return


#调用printinfo函数
printinfo(age=50, name="runoob")
print("------------------------")
printinfo(name="runoob")

list3 = []
list1 = [[1,2],[3,4]];
list2 = [[5,6],[7,8]];
list1.extend(list2)
print(list1)

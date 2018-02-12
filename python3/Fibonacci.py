#!/usr/bin/python3

# Fibonacci series: 斐波纳契数列
# 两个元素的总和确定了下一个数
a, b = 0, 1
while b < 1000:
    print(b, end=',')
    a, b = b, a + b
print("----------")

#!/usr/bin/python3
var1 = 'Hello World!'
var2 = "Runoob"

print("var1[0]: ", var1[0])
print("var2[1:5]: ", var2[1:5])

print("----------")
#!/usr/bin/python3
var3 = '123456789!'
print("已更新字符串 : ", var3[:6] + 'Runoob!')

print("----------")
#!/usr/bin/python3

a = "Hello"
b = "Python"

print("a + b 输出结果：", a + b)
print("a * 2 输出结果：", a * 2)
print("a[1] 输出结果：", a[1])
print("a[1:4] 输出结果：", a[1:4])

if("H" in a):
    print("H 在变量 a 中")
else:
    print("H 不在变量 a 中")

if("M" not in a):
    print("M 不在变量 a 中")
else:
    print("M 在变量 a 中")

print(r'\n')
print(R'\n')

print("我叫 %s 今年 %d 岁!" % ('小明', 10))

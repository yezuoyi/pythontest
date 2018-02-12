squares = [1,4,9,16,25]
print(squares[0],squares[-1],squares[-3])
print(squares[:])

squares = squares+[36,49,64,81,100]
print(squares[:])

cubes = [1, 8, 27, 65, 125]
cubes[3]=64;
print(cubes)

cubes.append(216)
cubes.append(7**3)
print(cubes)
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
print(letters)

letters[2:5]=['C','D','E']
print(letters)
print(len(letters))

letters[:]=[]

print(letters)

a = ['a', 'b', 'c']
n = [1, 2, 3]
x = [a, n]
print(x);
print(x[0][2])

a,b = 0,1
while b<10:
    print(b)
    a,b = b,a+b


def scope_test ():
    def do_local ():
        spam = " local ␣spam"
    def do_nonlocal ():
        nonlocal spam
        spam = " nonlocal ␣spam"
    def do_global ():
        global spam
        spam = " global ␣spam"
    spam = "test␣spam"
    do_local ()
    print(" After ␣ local ␣ assignment :", spam)
    do_nonlocal ()
    print(" After ␣ nonlocal ␣ assignment :", spam)
    do_global ()
    print(" After ␣ global ␣ assignment :", spam)
scope_test ()
print("In␣ global ␣ scope :", spam)

0 0 4-5 ? * *

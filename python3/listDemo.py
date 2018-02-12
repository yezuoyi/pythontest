li = ["a", "b", "mpilgrim", "z", "example"]
print(li)
print(li[1])
print(li[-1])
li.append("new")
print(li)
print(li.index("z"))
li.remove("z")
print(li)

li = li + ['example', 'new']

print(li)

params = {"server": "mpilgrim", "database": "master",
          "uid": "sa", "pwd": "secret"}

strPar = ["%s=%s" % (k, v) for k, v in params.items()]

print(strPar)

maps = ";".join(["%s=%s" % (k, v) for k, v in params.items()])

print(maps)


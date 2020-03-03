a = True
b = False

c = a and b
d = a or b
print("A and B is " + str(c))
print("A or B is " + str(d))

e = (True and True) or False
f = True or (True and False)

print(e)
print(f)

print("Comparison operator: e and f")
g = (e == f)
print(g)

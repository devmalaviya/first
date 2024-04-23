#dict

x = {1:"Hello",2:"python",3:"ruby",4:"callme"}
x.update({3:"C++"})
print(x)

for b in x:
    print(b)

#sets

y = {1,2,3,4,5,6,78,9,10,23,34,45,56,67}

print(y)

y.add(111)
print(y)

y.copy()
print(y)

y.discard(3)
print(y)

y.remove(111)
print(y)

y.pop()
print(y)

y.update({89,80})
print(y)

print(type(x))
print(type(y))

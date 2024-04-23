#dict

a = {3:"hello","dev":"malaviya",1:2,"priyam":2}
print(a)
print(type(a))

b = {1:[1,2,3],2:(1,2,3),3:{1,2,3}}
print(b)
print(type(b))

#modules

a = {1:"python",2:"java",3:"Ruby",4:"hello"}
print(a)

b = a.copy()
print(b)

b.clear()
print(b)

a.update({3:'hellooo'})
print(a)

print(a.items())

print(a.keys())

print(a.values())

print(a.get(1))

a.pop(2)
print(a)

a.popitem()
print(a)

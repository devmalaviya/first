#python lambda function


# def hello(x):
#     return x*2
# print(hello(4))


# x = lambda y:y*2
# print(x(5))


# multipal value using lambda function

# x = lambda a,b:(a+b)*2
# print(x(5,10))


#return using lambda function

# def myfunction(b):
#     return lambda x:x*b
# hello = myfunction(3)
# print(hello(10))



def myfunction(b):
    return lambda x:x*b
hello = myfunction(3)
demo = myfunction(5)
print(hello(10))
print(demo(15))
 
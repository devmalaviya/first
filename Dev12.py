# comparision operator
# ==,!=,>,<,>=,<=
x = 10
y  = 9

if x==y:
    print("right")
else:
    print("wrong")

if x>y:
    print("right")
else:
    print("wrong")

if x>=y:
    print("right")
else:
    print("wrong")

#Logical operator
# and,or,not

x = 10
y = 20

print(x==10 and x<y and y==20) #all condition are true-> return true
print(x==10 and x<y and x>y)

print(x==10 or x<y or x>y)  #any one condition are true-> return true
print(x==11 or x<y or x>y)

print(not(x==10 and y == 20))#condition true-> return false
print(not(x==11 or y == 10))#condition false-> return true
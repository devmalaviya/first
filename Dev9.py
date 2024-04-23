# string
# singleine string

x = "Dev"
print(x)

# multiline string

y = """
My
name
is
Dev
Malaviya.
"""
print(y)

# string lenth

x = "hello"
print(len(x))

# particular string reverse
y = "My name is Dev"
print(y[::-1])
print(y[4::1])
print(y[5::-1])

# loping string

for x in "hello":
    print(x)

y = "hello"
print(y[::-1])
print(y[3::1])
print(y[2::-1])

# STRING-in or not in

x = "My name is Dev"
print("Dev"in x)

x = "My name is hello"

if "hello" in x:
    print("right")
else:
    print("wrong")

if "hello" not in x:
    print("right")
else:
    print("wrong")
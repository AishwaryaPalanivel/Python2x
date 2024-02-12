# String concat
string1 = 'Hello'
string2 = 'world'
string3 = string1 + string2
print(string3)

a = 'Aish'
b = 25
c = a + str(b)
# c=a+b #TypeError: can only concatenate str (not "int") to str
print(c)

g = 'Hello'
g += 'World'
g = g + "World"
print(g)

# Increment and Decrement ++ and --
x = 5
x += 1
print(x)

x = 5
x -= 1
print(x)

# Negation
x = 10
y = 20
result = (x == y)
print(result)


x = 10
y = 20
result = (x != y)
print(result)
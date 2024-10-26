# strings
print("Hello")
print('Hello')

# quotes
print("It's alright")
print("He is called 'Johnny'")
print('He is called "Johnny"')

# Multiline Strings
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)
a = '''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.'''
print(a)

# Strings are arrays!
a = "hello, worlds!"
print(a[1])

# loop through strings
for z in "jojo":
    print(z)

# string length
a = "hello, worlds!"
print(len(a))

# chekcing for a string 
txt = "Joseph is the best jojo"
print("Joseph" in txt)

# using if statement
txt = "Joseph is the best jojo"
if "Joseph" in txt:
    print("Yes")
else:
    print("No")

# using check if not
txt = "Joseph is the best jojo"
print("Jotaro" not in txt)
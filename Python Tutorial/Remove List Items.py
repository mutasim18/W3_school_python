# remove()
thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)

# pop()
thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)
# If you do not specify the index, the pop() method removes the last item.
thislist = ["apple", "banana", "cherry"]
thislist.pop()
print(thislist)

# The del keyword also removes the specified index
thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)
# The del keyword can also delete the list completely
del thislist

# clear()
thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)


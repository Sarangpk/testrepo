thislist = ["apple", "banana", "cherry"]
print(thislist)
print(thislist[1])
thislist[1] = "black currant"
print(thislist)

for x in thislist:
 print(x)

print(len(thislist))

thislist.append("orange")
print(thislist)

thislist.insert(1, "pineapple")
print(thislist)

thislist.remove("orange")
print(thislist)


n = int(input("enter the number of integers you'd like to enter"))
print()
a = list()
    
    
for i in range(n):
    x = int(input("enter the integer: "))
    a.append(x)
    print()
print()

nl = tuple(a)

print(nl, "is your given tuuple")

print()

print(max(nl), "is the highet value in the tuple.")

print()

print(min(nl), "is the lowest value in tuple")

print()

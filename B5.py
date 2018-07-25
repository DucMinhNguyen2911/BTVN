#a1
print(*range(20), sep = ' ')
#a2
n = int(input("Enter a number:"))
print(*range(n), sep = ' ')
#b1
for i in range(10):
    print("1 0", end = ' ')
#b2
m = int(input("Enter a number:"))
for i in range(m):
    if i % 2 == 0:
        print(1,end = ' ')
    else:
        print(0, end = ' ')

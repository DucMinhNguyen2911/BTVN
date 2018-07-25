n = int(input("Please input factorial you would like to calculate: "))
answer = 1
for i in range(1,n+1,1):
    answer = answer*i
print("Answer:",answer)
sum, counter = 0,1
n = int(input("Please enter a number :"))
while counter <= n:
    sum = sum + counter
    counter +=1

print("1 to %d have a total number  %d." %(n,sum))

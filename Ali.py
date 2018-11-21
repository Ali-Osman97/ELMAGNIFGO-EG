l=1
h=100
while l != h:
    mid=int((l+h)/2)
    ans=input("is your guess > " + str(mid)+" ")
    if ans == "y":
        l=mid+1
    else:
        h=mid
print ("your guess =", l)
        
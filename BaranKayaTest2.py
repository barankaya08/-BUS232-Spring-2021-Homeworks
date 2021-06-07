def topVoteNeeded(myList, majority):
    total = 0
    c = 0
    for i in myList:
        total = total + i
        if (total >= majority):
            return c +1
        c = c + 1

val = 1
mylist = []

while val != 0:
    val = int(input("Plase enter the number of shares:"))
    mylist.append(val)
    total = sum(mylist)

majority = ( total / 2 ) + 1
mylist.sort(reverse=True)
votesNeeded = topVoteNeeded(mylist, majority)
print("Thank you, there is a total of ", total, "shares represented here.")
print("Shared needed for majority vote is ", int(majority))
print("You need the support of top ", votesNeeded, " shareholders for this number of votes")

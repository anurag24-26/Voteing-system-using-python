from collections import defaultdict

names=[]
votes=defaultdict(int)
result="ok"
number_of_canditates=int(input("enter number of candidates: "))
for i in range(number_of_canditates):
    n=input(f"Enter the name of candidate #{i + 1}: ")
    names.append(n)
while True:
    voter_name=input('Enter your name or for results type"ok": ')
    if voter_name==result:
        break
    print("names: ")
    for i, candidate in enumerate(names):
        print(f"{i + 1}. {names}")
    count_vote=int(input("Enter the number of your candidate- "))
    count_index=count_vote-1

    if count_index>=0 and count_index<len(names):
        candi=names[count_index]
        votes[candi] += 1
        print("Your voting has been done")
    else:
        print("no valid arguments")

print("voting ends here results are: ")
for candi,count in votes.items():
    print(f"{candi}:{count} votes")

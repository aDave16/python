'''#24. ""Voting System:"" Dictionary with candidates as keys and vote count as values. Write functions to:
* Cast a vote
* Show live results
* Find the winner'''
vote_name={"ami":0,"sneha":0,"riya":0}
def vote(candidate):
    if candidate in vote_name.keys():
        vote_name[candidate]+=1
    else:
        print("candidate not found")

def result():
    for i,j in vote_name.items():
        print(i, j)

def winner():
    win=max(vote_name,key=vote_name.get)
    print(win,vote_name[win])

while True:
    print("1.cast vote")
    print("2.show result")
    print("3.show winner")
    print("4.exit")
    ch=int(input("enter ur choice: "))
    
    match ch:
        case 1:
            print(vote_name)
            candidate=input("enter name of candidate to vote: ")
            vote(candidate)
        case 2:
            result()        
        case 3:
            winner()
        case 4:break
        case _:
            print("invalid choice")
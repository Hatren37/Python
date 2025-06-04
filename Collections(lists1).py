n=int(input("Enter the number of players: "))
scores = []
for i in range(n):
    r = int(input(f"Enter score {i+1}: "))
    scores.append(r)
print("Total score: ",sum(scores))
print("maximum score: ",max(scores))
print("minimum score: ",min(scores))
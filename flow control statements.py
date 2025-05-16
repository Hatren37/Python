# if, elif, else example
num = 7
if num < 5:
    print("num is less than 5")
elif num == 5:
    print("num is equal to 5")
else:
    print("num is greater than 5")

# for loop with break and continue
for x in range(1, 10):
    if x == 3:
        print("Skipping 3")
        continue  # skip the rest of the loop for x == 3
    if x == 7:
        print("Breaking at 7")
        break  # exit the loop when x == 7
    print(f"For loop value: {x}")

# while loop with pass
count = 0
while count < 5:
    if count == 2:
        pass  # does nothing, just a placeholder
    print(f"While loop value: {count}")
    count += 1
while True:
    word = input("Before reverse: \n")
    if word == "done":
        break
    if word[0] == "#":
        continue
    reversed = ""
    for letter in word:
        reversed=letter+ reversed
    print("After reverse:", reversed)
print("Done")

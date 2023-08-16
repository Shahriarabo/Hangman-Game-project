
word = "rasel"
chances = 5
GuessLetter = []
done = False

while not done:
    for letter in word:
        if letter.lower() in GuessLetter:
            print(letter, end=" ")
        else:
            print("_", end=" ")

    UserGuess = input(f"Your chance {chances}, Enter your GuessLetter: ")
    GuessLetter.append(UserGuess.lower())

    if UserGuess.lower() not in word.lower():
        chances -= 1
        if chances == 0:
            break

    done = True
    for letter in word:
        if letter.lower() not in GuessLetter:
            done = False

if done:
    print("You have won the game!")
else:
    print("You have not won the game, please try again.")






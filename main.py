import random
MAX_ATTEMPT = 5

def init():
    #get the file open it read line by line and put the words in the dictinary
    #return the dictionary
    dictionary = set()
    f = open("sample_dictionary.txt", "r")
    for line in f:
        word = line.strip()
        dictionary.add(word)
    return dictionary

def checkGuess(random_word,game_dict,input_word: str):
    if len(input_word) > 4:
        return f"Words should only be length 4!"
    if input_word not in game_dict:
        return f"Word not in the current game"
    
    return checkWordPos(random_word,input_word)

    

def checkWordPos(random_word,input_word):
    guess = []
    for i in range(4):
        if input_word[i] == random_word[i]:
            guess.append("1")
        elif input_word[i] in random_word[i]:
            guess.append("0")
        else:
            guess.append("-")
    return "".join(guess)


if __name__ == "__main__":
    game_dict = init()
    #get the word at random
    random_word = random.choice(list(game_dict))
    print(random_word)
    while MAX_ATTEMPT > 0:
        user_input = input("Please Enter Guess")
        print(user_input)
        res = checkGuess(random_word,game_dict,user_input)
        print(res)
        if res != "1111":
             MAX_ATTEMPT -= 1
        else:
            print("You Won!")
            break
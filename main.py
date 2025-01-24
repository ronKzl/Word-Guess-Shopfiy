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

if __name__ == "__main__":
    game_dict = init()
    #get the word at random
    print(game_dict)
    while MAX_ATTEMPT < 0:
        user_input = input("Please Enter Guess")

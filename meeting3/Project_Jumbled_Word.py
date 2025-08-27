import random
  
score = 0
player_name = input(“Please enter your name: ”) 

while True:
        
    words = ["python", "computer", "programming",
             "condition", "else", "break", "input",
             "print", "while", "for"] 
    pick = random.choice(words)

    random_word = random.sample(pick, len(pick)) 
    jumbled = "".join(random_word)
    print("Jumbled word is :", jumbled)

    answer = input("what is in your mind? ")
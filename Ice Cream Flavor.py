answer = "oreo"
#Creates variable of answer
hints = ["HINT: It usually has a base of vanilla ice cream", "HINT: There is a mixin of one of your favorite snacks", "HINT: The mixin is choclatey", "HINT: The mixin has the same name as the ice cream flavor", "ANSWER: The answer is oreo"]
#Creates list of hints and final answer

def ice_cream():
#Creates function of ice cream
    x = 0
    #Creates first index value
    global answer
    #Makes answer inside of the function
    
    for loop in hints:
    #Creates loop to iterate through guesses and hints
        guess = input("Guess my favorite ice cream: ").lower()
        #Creates input to see seperate guesses
        
        if guess == answer:
        #The guess is correct
            print("Correct, that is my favorite ice cream!")
            #Prints the guess as correct
            break
            #Doesn't keep looping
        
        else:
        #The guess is correct
            print("Wrong guess!")
            #Prints the guess as wrong
            print(hints[x])
            #Prints the hint assigned to the certain x value
            x = x + 1
            #Goes to the next loop and hint
            
            if x == 5:
            #To many chance
                print("You lose!")
                #You Lose
                
ice_cream()
#Calls the function
from game_pkg import word_defs
"""""Game made by Quanayzia Garden for my Numcap portfolio"""




# function to start the game
def game():
    game_on=True
    word_defs.menu_display()
    word_defs.make_body()
    word_defs.showBody()
#while loop to loop the game over and over again if the user chooses to want to play again 
    while game_on:
        not_pass=True

        while True:
            uInput=input("Please choose a category: ")
            if uInput=="1" or uInput=="2" or uInput=="3":
                break
            elif uInput=="4":
                not_pass=False
                break
        

        word_to_hold=word_defs.categories(uInput) #stores the randomized word
        

        while not_pass: # while loop to interate through compare function
            print("Your word has ",len(word_to_hold),"letters in it")
            userin=input("\nWrite down your word here: ").lower()
            not_pass=word_defs.compare(word_to_hold,userin)
            if not_pass is not True: # breaks out of loop when user guesses the word
                break
            if word_defs.showLength()==0: # when there are no more items in the stack it shows the randomized word and breaks out of the loop
                print("The word was",word_to_hold)
                break
        
        userChoice=input("\npress any button to continue or Q to quit: ").lower() # allows user to either replay or quit the game
        if userChoice=="q":
            game_on=False
        else:
            word_defs.make_body() # resets the hangman images 
            word_defs.showBody()

        


game()



    


    


        



        
import random

from game_pkg import class_linked_list

def menu_display():
    print("""                  HangMan Game!!!
             ------------------------------
            |                              |
            |  1) Fruits and Vegetables    |
            | -----------------------------|
            |  2)Animals                   |
            |------------------------------|
            |   3) Car Brands              |
            |------------------------------|
            |   4) Exit Game               |
             ------------------------------""")
    return None

def make_body():
    global lims
    lims=class_linked_list.linked_list()
    lims.push("""
            +---|
            |   O
            |  
            |  
            ===""")
    lims.push("""
            +---|
            |   O
            |   |
            |  
            ===""")
    lims.push("""
            +---|
            |   O
            |  /|
            |  
            ===""")
    lims.push("""
            +---|
            |   O
            |  /|\.
            |   
            ===""")
    lims.push(""""
            +---|
            |   O
            |  /|\.
            |  / 
            ===""")
    lims.push("""
            +---|
            |   O
            |  /|\.
            |  / \ 
            ===""")



def random_Mamals():
    animals=["bear","koala","lion","elephant","deer","dolphin","kangaroo","rabbit","chimpanzee","mouse"]
    return random.choice(animals)



def random_car_brands():
    brands=["BMW","acura","honda","toyota","jeep","nissan","kia","tesla","ford","mustang"]
    return random.choice(brands)


def random_fruits_and_veggies():
    food=["apple","bananas","oranges","berries","carrots","broccoli","asparagus","grapes","cabbage","kale"]
    return random.choice(food)

def categories(userInput):
    options={
            "1":random_fruits_and_veggies(),
            "2":random_Mamals(),
            "3":random_car_brands(),
            "4":None
        }
   
    return options[userInput]


def showBody():
    lims.show()

def showLength():
    return lims.length()


def compare(words,userInput):
    word_holder=""
    correct=0
    count=0

    for aletter,bletter in zip(words,userInput):
        if bletter in words:
            correct+=1
            if aletter==bletter:
                word_holder+=bletter  
        else:
            word_holder+="-"

    if word_holder == words:
        print("congradulations! You got it correct")
        return False
    elif correct>0:
        print("you got",correct,"letters correct")
        print(">>>>>>>>",word_holder,"<<<<<<<<<<")
        return True
    else:
        lims.show()
        print("\n>>>>>>>>",word_holder,"\n")
        print("letters correct",correct)
        lims.pop()
        lims.show()
        return True
        
   
       



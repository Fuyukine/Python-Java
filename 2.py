# Aufgabe 1

def firstFunction(list):
    sum = 0
    for i in list:
        sum = i+sum

    print(sum)

# Aufgabe 2

def secondFunction():
    import random
    randomTake = random.randint(1,20)

    #(b)(d)
    liste = ['one try!',"two tries!","three tries!"]

    #(b)(e)
    dictio = {1:"one", 2:"second", 3:"third"}


    trials = 0
    while (trials < 3):
        guess = int(input("What is your guess? a little hint: The number is between 1 and 20. Good luck!"))
        
        while (guess >= 21 or guess <= 0): #(a) checkt den Wertebereich
            print("The number you entered does not lie between 1 and 20. Please try again.")
            guess = int(input("What is your guess? a little hint: The number is between 1 and 20. Good luck!"))
        
        if (guess == randomTake): #(b)(c)
            if(trials == 0):
                print("Yay, you won after only " + liste[0])
            elif(trials == 1):
                print("Yay, you won on your " + dicitio[2] + " try!")
            else:
               print("Yay, you won on your third try!")
            return
        
        elif (guess < randomTake):
                print ("The number you chose is too small")
                trials += 1
        else:
            print ("The number you chose is too big")
            trials += 1






#Aufgabe 3
def a(n):
    for i in range(n):
        for j in range(n):
            if (j-i) % 5 == 0:
                print ('\\', end = '')
            else:
                print(' ', end = '')
        print()


def b(n):
    for i in range(8):
        if(i % 2 == 1):
            print( n//8 * (4 *(n//8 * "#" + n//8 * " ") + "\n" ), end = '')
        else:
            print( n//8 * (4 *(n//8 * " " + n//8 * "#") + "\n" ), end = '')

            
b(20)
a(20)

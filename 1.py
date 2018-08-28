import 

def helloName():

    print("Hello!")
    print("May I ask what Your first name is dear user?")
    firstName = str(input())
    print("And Your last name please?")
    lastName = input()
    print("Welcome to the system " + firstName + " " + lastName + ".")

def areaCalculation():

   n = input("Number of sides ")
   s = input("length of sides ")
   a = float(s/(2*tan(pi/n)))
   area = float((n * s * a)/2)
   print(area)

areaCalculation()

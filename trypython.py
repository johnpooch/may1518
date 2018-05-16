# userInput = input("Enter some text: ")

# # [begin:end:step]
# print (userInput [::-1])



# Write a program that allows the user to input a number.
# If the number is 10 or less, print "Small"
# otherwise, print "Big"

# userInput = input("Enter a number: ")

# if int(userInput) > 10: 
#     print("Big")
    
# else: 
#     print("Small")


# Write a program that allows the user to input two numbers.
# If the numbers are the same, print "Same"
# otherwise print "Different"

# num1 = int(input("Enter a number: "))
# num2 = int(input("Enter another number: "))

# if num1 == num2: 
#     print("Same")
    
# else: 
#     print("Different")





# Write a program that allows the user to enter a number.

# If 1 is entered, ask the user to enter their name e.g. Tom, and print
# Your Name is Tom

# If 2 is entered, ask the user to enter their age, e.g. 21 and print
# Your Age is 21




# userInput = int(input("Enter a number: "))

# if userInput == 1:
#     userInput = input("Enter your name: ")
#     print ("Your name is " + userInput)
# elif userInput == 2:
#     userInput = input("Enter your age: ")
#     print ("Your age is " + userInput)
# else: 
#     print("You must enter '1' or '2'")





# result = 0
# for i in range(10):
#     userInput = int(input("Enter a number: "))
#     result += userInput
    
# print(result)

# i = 0

# while i < 100:
#     i += 2
#     print(i)





# def add (a, b):
#     result = a + b
#     return result
    
# print(add(3, 5))




# def add (a, b):
#     result = a + b
#     return result

# num1 = int(input("Enter first number: "))
# num2 = int(input("Enter second number: "))

# print(add(num1, num2))




# n = int(input("Enter a number: "))

# if(n%2 == 0):
#     print("even")
# else:
#     print("odd")




# def message(): 
#     return "This is the message"
    
# print(message)
# print(message())

# sum = 0

# for i in range(1, 7): 
#     sum += i
    
# print(sum)





# numList = [] 

# i = 0

# for i in range(100):
#     numList.append(i)
    
# print(numList)





# numList = [] 

# i = 0

# for i in range(10, 51, 2):
#     numList.append(i)
    
# print(len(numList))




# outList = [] 

# for i in range(1, 7):
#     inList = []
#     for j in range(i):
#         inList.append(j)
#     outList.append(inList)
    
# print(outList[4][2])





# evens = []

# for i in range(0, 11, 2):
#     evens.append(i)
    
# print(evens)





# myList = []

# for i in range(10): 
#     myList.append(i)
    

# print(myList[0])
# print(myList[-1:])
# print(myList[1:])
# print(myList[:-1])




musicians = {
    "John": {"name": "John", "nationality": "Irish", "gender": "Male", "bands": ["Nirvana", "The Beatles", "Joy Division"], "instruments": [{"guitar": "99"}, {"piano": "22"}, {"drums": "55"}]},
    "Xav": {"name": "Xav", "nationality": "French", "gender": "Male", "bands": ["Sex Pistols", "Daft Punk", "Arctic Monkeys"], "instruments": [{"guitar": "6"}, {"piano": "23"}, {"drums": "80"}]},
    "Michael": {"name": "Michael", "nationality": "Korean", "gender": "Male", "bands": ["Queen", "The Fall", "Gorillaz", "Beard Seeking Missile"], "instruments": [{"guitar": "60"}, {"piano": "2"}, {"drums": "65"}]}
}



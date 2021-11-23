#Python program to simulate a queue at a bank

#Initializing a list
names = []

#variable for first while loop counter
x = 0

#Repeat 10 times
while x < 10:
    #set acceptedName to the name they input
    acceptedName = input('Input the name of the next person in line: ')
    #add acceptedName to the end of the names queue
    names.append(acceptedName)
    #add 1 to the counter
    x = x+1

#Introduce the list that will be printed out
print('\nHere is the order that those people will reach the front of the line:')

#for the length of the queue
while len(names):
    #pop out the names of the queue
    print(names.pop(0))

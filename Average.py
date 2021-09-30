#This is the program for the Averaging Test Scores Algorithm

#First declare variables that will be used and set equal to 0
average = 0.0
howManyEntered = 0
total = 0

#Take in the amount of test scores to average as an int
howMany = int(input('How many test scores would you like to average? '))

#Repeat these steps as long as the amount of scores entered so far
#is less than the amount of scores they said they wanted to average
while howManyEntered < howMany:

    #Take in an entered test score as an int
    testScore = int(input('Enter test score: '))
    
    #Add the input to the total that will be averaged later
    total = total + testScore
    
    #Add 1 to the counter for how many scores have been entered so far
    howManyEntered = howManyEntered + 1

#After the while loop is complete, compute the average
average = total / howMany

#Output the final average of their test scores
print('The average for the test scores you entered is: ')
print(average)

#Weather conditions program with inputting temperatures

#Declare temp variable
temp = 0

#If temp is not 999, repeat asking to enter temperature
#If temp is 999, this wil not loop and the program will end
while temp != 999:
    temp = int(input('Please enter the current temperature: '))

#Based on input, output either program end or recommendation based on the temp
    if temp == 999:
        print('Program end.')
    elif temp > 90:
        print('Wear shorts.')
    elif temp > 70:
        print('Short sleeves are fine.')
    elif temp > 50:
        print('Wear a jacket.')
    elif temp > 32:
        print('Wear a heavy coat.')
    else:
        print('Stay inside.')
        
    #print a blank line to add space before asking question again
    print(' ')


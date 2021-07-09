#imports that make this project easier. 
import hashlib
import turtle
import random
import time
from statistics import variance, mean, median, median_high, median_low, mode, geometric_mean, harmonic_mean
import math
import datetime

#Creating varibales, and setting up the loop. Also, the 
accounts = [] # stores usernames and passwords.
endloop = True
accs_file = open('accs.txt', 'w')

# main loop, only ends if a user logs in.
while endloop != False:

    #User is able to choose if they want to login or sign up. 
    choice = input('Would you like to sign up or login?: ')
    
    #If statement that makes up the sign up and sets up the account.
    if choice == 'sign up':
        username = input('what would you like your username to be?: ')
        if username in accounts:
            print ('User already exists. ')
            
        else: 
            accounts.append(username)

            password = input('What would you like your password to be?: ')
            
            #Encrypts the password basically. 
            accounts.append(hash(password))
            print ('You are stored as a User, you may now login.')


 #This elif statement does the login work when a user chooses to login.
    elif choice == 'login':

            name = input('enter your username: ')
            
            #Checks if the login information is on file. 
            if name in accounts:
                # get the index of the username in the list 'accounts'
                for i in accounts:
                    if i == name:
                        user = accounts.index(i)
                passwd = hash(input('Please enter your password (This case is sensetive!): '))
                

            #Unhashes the password and write it down etc. 
                if accounts [user+1] == passwd:
                    print('You are now logged in. ')
                    endloop = False
                    status_off = False
                    accounts = str(accounts)
                    accs_file.write(accounts)
                    accs_file.close()
                else:
                    print('incorrect')

            else:
                print ('incorrect')
    #loop ends if the user is loggedin.
    else:
        endloop = False

#A new loop that contains everything. This makes it so that everything is redoable. (If that a word)
while status_off != True:   

    #A user can choose what tasks they want done, or do. I've implemented some of my older projects and written new ones. 
    todo = input('Do you want to draw SHAPES or use the CALCulator or PLAY or FLIP or RPSS or AGE?: ')
    
    # if statements that help control what the user wants.
    if todo == 'SHAPES':

        side = int(input('enter sides. 3 or above: '))
        loadwindow = turtle.Screen()
        turtle.speed(0)
        sides = side
        size = int(input('enter size'))
        #Automating the task for turtle drawing.
        def shape(size, sides):
            for i in range (sides):
                turtle.fd(size)
                turtle.lt(360/sides)

        for i in range(100):
            shape(3*i, sides)
            turtle.lt(i)
#Simple elif statement for fliping a coil. 
    elif todo == 'FLIP':
        coin = ['Heads', 'Tales']
        side = random.choice (coin)
        print (side)
#Simple elif statement for play rock paper scissors. 
    elif todo == 'RPSS':
        print ('Rock, Paper, Sissors, Shoot!')
        RPS = ['Rock', 'Paper', 'Sissors']
        pick = random.choice (RPS)
        time.sleep(3)
        print (pick)
#This is the Guessing game project implemented into this long code. 
    elif todo == 'PLAY': 
        choice_1= int(input('Pick the first number you want your guess in between: '))
        choice_2 = int(input('Pick the second number you want you guess in between: '))
        secret = random.randint(choice_1, choice_2)
#loop for the guessing and checking the numbers
        while True:
            guess = int(input('Take a Guess!: '))
            if guess == secret:
                print ('You Win!')
                break
            elif guess < secret:
                print (guess, 'is too low')
            else:
                print (guess, 'is too high')
#This is the calculator project imbeded into this system.
    elif todo == 'CALC':
        #A list to hold the numbers.
        numbers_list = []

        #A loop enabling a calculation after calculation.
        while True:
            numbers = input('Enter a numbers: ')
        #If statements that have certain letters assigned to execute certain tasks in the calculator. Ex. pressing 'a' adds the numbers in the list.
            if numbers == 'a':
                ans = sum(numbers_list)
                print(ans)
                numbers_list = []
            
            elif numbers == 's':
                ans = numbers_list[0] - sum(numbers_list[1:])
                print(ans)
                numbers_list = []

            elif numbers == 'm':
                ans = math.prod(numbers_list)
                print(ans)
                numbers_list = []

            elif numbers == 'v':
                ans = variance(numbers_list)
                print(ans)
                numbers_list = []

            elif numbers == 'mn':
                ans = mean(numbers_list)
                print(ans)
                numbers_list = []

            elif numbers == 'med':
                ans = median(numbers_list)
                print(ans)
                numbers_list = []
            
            elif numbers == 'medl':
                ans = median_low(numbers_list)
                print(ans)
                numbers_list = []

            elif numbers == 'medh':
                ans = median_high(numbers_list)
                print(ans)
                numbers_list = []

            elif numbers == 'mode':
                ans = mode(numbers_list)
                print(ans)
                numbers_list = []

            elif numbers == 'gm':
                ans = geometric_mean(numbers_list)
                print(ans)
                numbers_list = []

            elif numbers == 'hm':
                ans = harmonic_mean(numbers_list)
                print(ans)
                numbers_list = []
            #If pressed then the calculator ends breaking the loop.
            elif numbers == 'quit':
                break
            #If it is a number it is sent to the list.
            else:   
                numbers_list.append(float(numbers))
    #Elif statement for guessing your age. It gives year, month, and day. 
    elif todo == 'AGE':
        birth_month = int(input('Enter your birth month: '))
        birth_day = int(input('Enter your birth date: '))
        birth_year = int(input('Enter your birth year: '))

        now = datetime.datetime.now()
        month = int(now.strftime("%m"))
        day = int(now.strftime('%d'))
        year = int(now.strftime('%Y'))

        print ('You are', year - birth_year, 'years', month - birth_month, 'months', 'and', day - birth_day, 'days old!')
    #keeps the program moving
    else:
        status = True
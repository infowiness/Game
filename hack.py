# UPI cyberarm@ybl
# Devloped By Info Winess


from os import system, name
import itertools
import threading
import time
import sys 
import datetime
from base64 import b64decode,b64encode
from datetime import date  
   
expirydate = datetime.date(2022, 11, 28)
#expirydate = datetime.date(2021, 8, 30)
today=date.today()
  
def hero():

    def chalo():
        done = False
        #here is the animation
        def animate():
            for c in itertools.cycle(['|', '/', '-', '\\']) :
                if done:
                    break
                sys.stdout.write('\rHacking in the Parity Server for next colour---- ' + c)
                sys.stdout.flush()
                time.sleep(0.1)
            sys.stdout.write('\rDone!     ')

        t = threading.Thread(target=animate)
        t.start()

        #long process here
        time.sleep(10)
        done = True

    def chalo1():
        done = False
        #here is the animation
        def animate():
            for c in itertools.cycle(['|', '/', '-', '\\']):
                if done:
                    break
                sys.stdout.write('\r---------Getting the color Please wait --------- ' + c)
                sys.stdout.flush()
                time.sleep(0.1)
            sys.stdout.write('\rDone!  ')

        t = threading.Thread(target=animate)
        t.start()

        #long process here
        time.sleep(10)
        done = True

    def clear():
        # for windows
        if name == 'nt':
            _ = system('cls')
        # for mac and linux(here, os.name is 'posix')
        else:
            _ = system('clear')

    clear()
    y=1
    newperiod=period 
    banner='figlet RXCE'
    m=0
    i=1
   # thisway=[1,2,4,6,7,8,15,14,16,17,18]
   # thatway=[3,5,9,10,11,12,13,19,20]
    
    thisway=[0, 1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59, 61, 63, 65, 67, 69, 71, 73, 75, 77, 79, 81, 83, 85, 87, 89, 91, 93, 95, 97, 99]
    thatway=[2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64, 66, 68, 70, 72, 74, 76, 78, 80, 82, 84, 86, 88, 90, 92, 94, 96, 98, ]
    numbers=[]
    while(y):
        clear()
        system(banner)
        print("\n*************************************************")
        print("Contact me on telegram @black_cannon")
        print("\n--------------------------------------------------")
        print("Enter ",newperiod," Parity Price :")
        print("\n*************************************************")
        current=input("Enter Hear:- " ) 
        print("\n*************************************************")
        current=int(current)
        #chalo()
        chalo()
        print('\n')
        print("---------Successfully hacked the server----------")
         
        #chalo1()
        chalo1()
        print('\n')
        print("---------Successfully got the color------------")
        print('\n')
        def getSum(n):
            sum=0
            for digit in str(n):
                sum += int(digit)
            return sum
        if i in thisway:
            m=getSum(current)
            n=int(current)%10
            if((m%2==0 and n%2==0) or (m%2==1 and n%2==1)):
                if current in numbers:
                    print("Your Next Round ", newperiod+1,"color Result is  : RED \U0001F534 ")
                else:
                    print("Your Next Round ", newperiod+1,"color Result is  : GREEN \U0001F7E2 ")
            else:
                if current in numbers:
                    print("Your Next Round ", newperiod+1,"color Result is  : GREEN \U0001F7E2 ")
                else:
                    print("Your Next Round ", newperiod+1,"color Result is  : RED \U0001F534 ")
        if i in thatway:
            m=getSum(current)+1
            n=int(current)%10
            if((m%2==0 and n%2==0) or (m%2==1 and n%2==1)):
                if current in numbers:
                    print("Your Next Round ", newperiod+1,"color Result is : RED \U0001F534 ")
                else:
                    print("Your Next Round ", newperiod+1,"color Result is : GREEN \U0001F7E2 ")
            else:
                if current in numbers:
                    print("Your Next Round ", newperiod+1,"color Result is : GREEN \U0001F7E2 ")
                else:
                    print("Your Next Round ", newperiod+1,"color Result is : RED \U0001F534 ")
        i=i+1
        newperiod+=1
        numbers.append(current)
        
        print('\n')
        print("Happy Haking \U0001f600 \U0001f600 \U0001f600 \U0001f600 \U0001f600")
        y=input("Do you want to play : Press 1 and 0 to exit \n")
        if(y==0):
            y=False
        if (len(numbers)>11):
            clear()
            system('figlet Thank you!!')
            print("Play on next specified time!!")
            print("-----------Current Time UP----------")
            sys.exit(" \n \n \n Contact on Telegram @black_cannon")
            #print(numbers)
            


if(expirydate>today):
    now = datetime.datetime.now()
    First = now.replace(hour=10, minute=55, second=0, microsecond=0)
    Firstend = now.replace(hour=11, minute=35, second=0, microsecond=0)
    Second = now.replace(hour=13, minute=55, second=0, microsecond=0)
    Secondend = now.replace(hour=14, minute=35, second=0, microsecond=0)
    Third = now.replace(hour=16, minute=55, second=0, microsecond=0)
    Thirdend = now.replace(hour=17, minute=35, second=0, microsecond=0)
    Final = now.replace(hour=19, minute=55, second=0, microsecond=0)
    Finalend = now.replace(hour=20, minute=35, second=0, microsecond=0)


    #----------------------------------------------------------------------------------------------

    #For Round 
    now =  datetime.datetime.now() 

    current_time_H = now.strftime("%H")
    current_time_M = now.strftime("%M")
    #print(now.strftime("%H")) 
    #print("Current Time =", current_time_H) 
    #print("Current Time =", current_time_M)

    #Totle Minit
    Min =1440

    #curent Houre
    Sum_H = int(current_time_H)
    Totle_min = Sum_H * 60
    #print(Totle_min) 

    #curent Minit
    Sum_M = int(current_time_M)
    Sum_min = Sum_M + Totle_min

    #Current_Perity = int(Sum_min/3+1)
    period = int(Sum_min/3)
 
    
    # ---------------------------------------------------------------------------------------------    

    if (True):
            period
            hero()
    elif(False):
            period=280
            hero()
    elif(False):
            period=343
            hero()
    elif(now>Final and now<Finalend):
            period=400
            hero()
    else:
        banner='figlet RXCE'
        print("Hi!! Thanks for buying the hack")
        print("----------Your play time-----------")
        print(" Yesterday Server Error , So Play today" )
        print("22nd oct 2021, 08:00 PM- 08:30 PM")
        print("Please play on the given time, and ")
        print("If you think it is an error contact")
        print(" admin on telegram @black_cannon ")



else:
    banner='figlet RXCE'
    system(banner)
    print("Your hack has expired--- Please contact")
    print(" on telegram -----------@black_cannon")

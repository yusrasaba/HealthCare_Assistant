# import required modules
from pygame import mixer
from time import time
from time import sleep
from time import *

# get all the required data
def date():
               
               # get the current date and time 
               import datetime
               return (str(datetime.datetime.now()))

# conditions for music
def song(stopper):
               mixer.init()
               mixer.music.load("My Heart.mp3")


               # playing the music for user
               mixer.music.play()

               sleep(2)
               print("\nYour timer starts now...\n")
               sleep(1)
                       
               while True:
                              # countdown for drinking water
                              
                              for i in range(10,0,-1):
                                  print(i,end=" ")
                                  sleep(1)
                              print(" Timer Stopped..!\nYou are now done with your rest..")
                       
                              x = input("\nPlease type STOP to stop the alarm or EXIT to stop the program : ")
                              
                              # stopping the music
                              if (x.upper() == stopper):
                                             print("\nAwesome!! Now you can get to your coding..!\n")
                                             mixer.music.stop()
                                             return True
                                             break
                              
                              # terminating the program
                              elif (x.upper() == "EXIT"):
                                             return False


# variables initialized with 0 for counting total
# number of exercises and water drank in a day
tot_water = 0
tot_phy_ex = 0
tot_eye_ex = 0

if __name__ == '__main__':
                                                            
               print()
               print("**"*40)
               print("\tHello there, Programmer. I am your Personal Health Care Alarm.!\n\t I would take care of your health while you code for a day long...!")
               print("**"*40)
               phy_o_clock = time()
               drink_o_clock = time()
               eyes_o_clock = time()

               eyes_gap = 5
               drink_gap = 10
               phy_gap = 20

               while(True):
                              
                              # Drink water condition.
                              if (time() - drink_o_clock > drink_gap):

                                             print("--"*40)
                                             print("\nHey I know you are working but it's time for you to take 2 mins rest.!\nHave some water(atleast 150ml) and continue your work..!")

                                             
                                             
                                             # Checking the user input so that music can be stopped.
                                                             
                                             if(song("STOP")):
                                                            pass
                                             else:
                                                            break

                                             # reinitializing the variable
                                             drink_o_clock = time()
                                             
                                             
                                             # incrementing the value
                                             tot_water += 150
                                             
                                             # opening the file and putting the data into that file
                                             
                                             f = open("drank.txt", "at")
                                             f.write("[ " + date() + " ] \n")
                                             f.close()
                                             

                              # Eye exercise condition.
                              if (time() - eyes_o_clock > eyes_gap):

                                             print("--"*40)
                                             print("\nHey I know you are working but it's time for you to relax a bit.!\nDo some eye exercises, let your eyes feel a bit of ease and continue your work.!")

                                             

                                             if (song("STOP")):
                                                            pass
                                             else:
                                                            break

                                             eyes_o_clock = time()
                                             
                                             tot_eye_ex += 1
                                             f = open("eye.txt", "at")
                                             f.write("[ " + date() + " ] \n")
                                             f.close()
                                             

                                             

                              # Physical exercise condition.
                              if (time() - phy_o_clock > phy_gap):
                                             print("--"*40)
                                             print("\nHey I know you are working but it's time for you to let up for some time.!\nDo some physical exercises to lighten your body from the stress and continue your work..!")

                                             

                                             if (song("STOP")):
                                                            pass
                                             else:
                                                            break

                                             phy_o_clock = time()
                                             
                                             tot_phy_ex += 1
                                             f = open("phy_exer.txt", "at")
                                             f.write("[ " + date() + " ] \n")
                                             f.close()
                                             

                                             

               print()
               print("--"*40)
               print(f"Total water you've taken today : {tot_water} ml.")
               
               try:
                              f = open("drank.txt", "rt")
                              print("\nDetails :")
                              print(f.read())
                              f.close()
               except:
                              print("Details not found!")

               print(f"Total eye exercise you've done today : {tot_eye_ex}.")
               
               try:
                              f = open("eye.txt", "rt")
                              print("\nDetails :")
                              print(f.read())
                              f.close()
               except:
                              print("Details not found!")

               print(f"Total physical exercises you've done today : {tot_phy_ex}.")
               
               try:
                              f = open("phy_exer.txt", "rt")
                              print("\nDetails :")
                              print(f.read())
                              f.close()
               except:
                              print("Details not found!")

               sleep(1)

print("--"*40)
print("\nHope you had an easy with your coding.\nLet's meet again soon..!\n")
print("**"*40)

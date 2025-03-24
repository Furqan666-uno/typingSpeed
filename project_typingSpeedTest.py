import random
import time

def type_check(userinput,test):
    error= 0
    for i in range(len(test)):
        try:
            if (userinput[i] != test[i]):
                error+= 1
        except:
            error+= 1 # to make sure that indexing error also get counted 
    return error + abs(len(userinput) - len(test)) # include lenght diff. (word not completed) error
                # abs= if the value is negative, it converts it to positive value

def timeTaken(time1,time2,userinput):
    delay= round(time2-time1,2) # round(t,2)= round-off the ans by 2 decimal points
    speed= len(userinput)/delay
    return round(speed)

text=["She first heard it while she was making coffee.The morning was already off to a rough start. ",
      "The elderly lady shuffled the few remaining steps to the park bench and sat down, happy to catch her breath and rest for a moment. ",
      "What follows is a transcript of an apology to the people of Earth, and specifically the residents of Silver Lake, Indiana. "]

time1= time.time()
test= random.choice(text)
print("-------------------------TYPING SPEED TEST-------------------------------")
print(test)
print()
print()
print("Start typing")
userinput= input("")
time2= time.time()
print(f"Number of errors: {timeTaken(time1,time2,userinput)}")
print(f"Typing speed: {type_check(userinput,test)}w/s")

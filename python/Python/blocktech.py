import time
import random
random = random.randint(1,1000)
x = 10
while True:
    y = int(input("..."))
    if(random<y):
        time.sleep(0.5)
        print("down")
        x-=1
    elif(random>y):
        time.sleep(0.5)
        print("up")
        x-=1
        
    elif(y==random):
        time.sleep(0.5)
        print("congrats")
        break
    if(x==0):
        print("over")
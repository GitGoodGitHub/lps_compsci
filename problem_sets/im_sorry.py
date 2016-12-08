import random
mynum = random.randint(1, 1000)
print("Try to guess my number because you have nothing better to do with your life, it's a number from 1 to 1000, good luck!")
score = int(0)
num = int(0)
while num != mynum:
        num = int(raw_input())
        if num < mynum:
                print("That number is as small as your D!$%, try again.")
        else:
                print("That number is as big as your mom, try again.")
        score = score + 1
        if num == mynum:
                print("You finally guessed correctly, about time. You failed " + str(score) + " times, you failure.")
# Mr. Flax I’m sorry if you were offended by this, I was playing around ;-;

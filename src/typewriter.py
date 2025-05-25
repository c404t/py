from time import sleep
import random

def simple_writer(seq):
    for index, letter in enumerate(seq):
        if index%13==0 or index%19==0:
            sleep(0.2)
        if index%23==0:
            sleep(0.5)
        if letter == ' ':
            sleep(0.08)
        print(letter, end='', flush=True)
        sleep(0.09)

def better_writer(seq):
    index = 0
    ran = False
    while 0 <= index < len(seq):
        if index%13==0 or index%19==0:
            sleep(0.2)
        if index%23==0:
            sleep(0.5)
        if seq[index] == ' ':
            sleep(0.08)
        print(seq[index], end='', flush=True)
        sleep(0.09)
        if index%21==0 and index!=0 and not ran:
            rand = random.choice([4, 6, 8])
            sleep(0.5)
            for i in range(rand):
                print("\b \b", end='', flush=True)
                sleep(0.2)
            index=index-rand+1
            ran = True
            sleep(0.3)
        else:
            index += 1

text1 = "some random words that come to my mind right now..."
text2 = "omg cats are pretty cute btw!!"

simple_writer(text1)
print()
better_writer(text2)
sleep(1)

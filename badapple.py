# bad apple
import sys, time, os
import pygame


def player():
    with open('data/badapple.txt', 'r') as file:
        while True:
            video_file = file.read(1)
            if not video_file:
                break

            # print 1 char
            print(video_file, end="")

            # if char is S, wait and clear the screen
            if video_file == "S":
                time.sleep(.0858)
                os.system('clear')


def music():
    pygame.init()
    pygame.mixer.init()
    pygame.mixer.music.load('data/badapple.ogg')
    pygame.mixer.music.play()


# set terminal window to 101x29 chars
sys.stdout.write("\x1b[8;29;101t")

music()
player()
print("Finished")

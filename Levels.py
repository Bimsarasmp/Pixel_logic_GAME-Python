# Beginning of level.py File
import random

#bamboo
level_1 = [
[1,1,0,0,1,1,0,0,1,1],
[1,1,0,1,1,1,0,0,1,1],
[1,1,0,1,1,1,0,1,1,1],
[1,1,0,0,1,1,0,1,1,1],
[1,1,0,0,1,1,0,0,1,1],
[1,1,1,0,1,1,0,0,1,1],
[1,1,1,0,1,1,1,0,1,1],
[1,1,0,0,1,1,1,0,1,1],
[1,1,0,0,1,1,0,0,1,1],
[1,1,0,0,1,1,0,0,1,1]]

#monkey
level_2 = [
[0,1,1,0,0,0,0,1,1,1],
[1,1,1,0,0,0,0,1,0,1],
[1,1,1,0,0,0,0,0,0,1],
[0,0,1,1,1,1,1,1,1,1],
[0,0,1,1,1,1,1,1,0,0],
[0,1,1,1,0,0,1,1,0,0],
[0,1,0,1,0,0,1,1,1,0],
[0,0,0,1,0,0,0,0,1,0],
[1,1,1,1,1,1,1,1,1,1],
[1,1,1,1,1,1,1,1,1,1]]

#HEART

level_3 = [
[0,0,1,0,0,0,0,1,0,0],				
[0,1,1,1,0,0,1,1,1,0],
[1,1,1,1,1,1,1,1,1,1],
[1,1,1,1,1,1,1,1,1,1],
[1,1,1,1,1,1,1,1,1,1],
[0,1,1,1,1,1,1,1,1,0],
[0,0,1,1,1,1,1,1,0,0],
[0,0,0,1,1,1,1,0,0,0],
[0,0,0,1,1,1,1,0,0,0],
[0,0,0,0,1,1,0,0,0,0]]

#japanese castle

level_4 = [
[0,0,0,0,1,1,0,0,0,0],				
[0,0,0,1,1,1,1,0,0,0],
[1,0,1,1,1,1,1,1,0,1],
[1,1,1,1,1,1,1,1,1,1],
[1,1,1,1,1,1,1,1,1,1],
[0,1,1,1,1,1,1,1,1,0],
[0,0,1,1,1,1,1,1,0,0],
[0,0,1,1,1,1,1,1,0,0],
[0,0,1,1,1,1,1,1,1,0],
[1,1,1,1,1,1,1,1,1,1]]

#medium levels
#cat
level_5 = [
[0,0,0,0,0,0,0,0,1,1],
[1,0,0,0,1,0,0,1,1,0],
[1,1,1,1,1,0,0,1,1,0],
[1,0,1,0,1,0,0,1,1,0],
[1,1,1,1,1,0,0,0,1,1],
[1,1,1,1,1,0,0,0,1,1],
[0,1,1,1,1,1,1,1,1,1],
[0,1,1,1,1,1,1,1,1,0],
[0,1,1,1,1,1,1,1,1,0],
[0,1,0,0,1,0,0,0,1,0]
]

#tree with sun
level_6 = [
[1,1,1,0,0,0,0,0,0,0],
[1,0,1,0,0,0,0,0,0,0],
[1,1,1,0,0,0,1,1,0,0],
[0,0,0,0,0,1,1,1,1,0],
[0,0,0,0,1,1,1,1,1,1],
[0,0,0,0,0,0,1,1,0,0],
[0,0,0,0,0,0,1,1,0,0],
[0,0,0,0,0,0,1,1,0,0],
[1,1,1,1,1,1,1,1,1,1],
[1,1,1,1,1,1,1,1,1,1]]


#hard levels

#bee
level_7 = [
[1,0,0,0,0,0,0,0,0,1],
[0,1,0,0,0,0,0,0,1,0],
[0,0,1,0,0,0,0,1,0,0],
[0,0,0,1,1,1,1,0,0,0],
[0,0,1,0,1,1,0,1,0,0],
[0,0,1,0,1,1,0,1,0,0],
[0,0,0,1,1,1,1,0,0,0],
[1,1,1,1,1,1,1,1,1,1],
[1,0,0,1,0,0,1,0,0,1],
[1,0,0,1,1,1,1,0,0,1]
]

#key
level_8 = [
[0,0,0,0,1,1,1,0,0,0],
[0,0,1,1,0,0,0,1,1,0],
[0,0,1,0,0,0,0,0,1,0],
[0,1,0,1,1,1,0,0,0,1],
[0,1,1,0,0,0,1,0,0,1],
[0,1,1,0,1,0,1,0,0,1],
[0,0,1,0,0,0,1,0,1,0],
[0,1,1,1,1,1,0,1,1,0],
[1,1,1,0,1,1,1,0,0,0],
[1,1,0,0,0,0,0,0,0,0]
]


All_Levels = [level_1, level_2, level_3, level_4, level_5, level_6, level_7, level_8]
# generating a random number to pick a level
level_indx = random.randint(0, 7)
Level = All_Levels[level_indx]
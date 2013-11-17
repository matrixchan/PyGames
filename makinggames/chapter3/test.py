import sys

'''
for boxx in range(10):
    for boxy in range(7):
        print (boxx,boxy)

'''
#print range(10)
BOARDWIDTH = 11
BOARDHEIGHT = 7
assert (BOARDWIDTH * BOARDHEIGHT) % 2 == 0, 'Board needs to have an even number of boxes for pairs of matches.'

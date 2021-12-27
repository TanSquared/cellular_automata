import random
from time import sleep

def neighbour(lifearr, xindex, yindex, sizex, sizey):
	ans = 0
	for i in range (-1, 2, 1):
		for j in range (-1, 2, 1):
			if (i == 0 and j == 0):
				pass
			else:
				valuex = xindex + i
				valuey = yindex + j
				if (valuex > -1 and valuey > -1 and valuex < sizex and valuey < sizey and lifearr[valuex][valuey] == 1):
					ans = ans + 1
	return ans


rsize = int(input("Enter the number of rows you want "))
csize = int(input("Enter the number of columns you want "))

life1 = [[random.randint(0, 1) for i in range(csize)] for j in range(rsize)]
life2 = [[0 for i in range(csize)] for j in range(rsize)]
for k in range(0, 100, 1):
    for i in range(rsize):
        for j in range(csize):
            val = neighbour(life1, i, j, rsize, csize)
            if(life1[i][j] == 1 and val < 2):
                life2[i][j] = 0
            elif(life1[i][j] == 1 and val > 3):
                life2[i][j] = 0
            elif(life1[i][j] == 0 and val == 3):
                life2[i][j] = 1
            else:
                life2[i][j] = life1[i][j]
            if(life2[i][j] == 1):
                print("*", end = '')
            else:
                print('', end = ' ')
        print('')
    sleep(0.3)
    print('--------------------------------------------------------------------------------------------------------------------------------------')
    temp = life1
    life1 = life2
    life2 = temp

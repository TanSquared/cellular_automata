import random as rn
from time import sleep


def findgap(arr, columnsize, i, j):
    ret = 0
    original_index = j
    while(1):
        if original_index == ((j + 1) % columnsize):
            #in case the whole list is empty
            return ret
        if j + 1 == columnsize:
            #in case we reach the last index of the list, since it is a circular lattice we go to the first index after that
            j = -1
        if arr[i][j + 1] > 0:
            return ret
        else:
            j = j + 1
            ret = ret + 1


def fixnewposition(arr, speed, columnsize, i, old_row, old_index, gap):
    if gap > speed:
        #a pedestrain can only move at a speed less than or equal to his prescribed speed. 
        gap = speed
    new_index = (old_index + gap) % columnsize
    while (arr[i][new_index] > 0 and gap > 0):
        #since there are different types of pedestrians, it is possible that the new position has already been occupied by another pedestrian. in that case, the gap has to be reduced
        gap = gap - 1
        new_index = (old_index + gap) % columnsize
    if (gap == 0 and arr[i][new_index] > 0):
        arr[old_row][j] = speed
    else:
        arr[i][new_index] = speed


rowsize = int(input('Enter row size '))
columnsize = int(input('Enter column size '))

#this is our virtual lattice
old_array = [[0 for i in range(columnsize)] for j in range(rowsize)]
density = float(input('Enter your desired density between 0 and 1 '))

N = int(density * rowsize * columnsize)
#classes are in order to ensure that we have a set of different kinds of pedestrians(different speeds)
classes = []
pedestrian_fraction = 0
index = 0
while(pedestrian_fraction < 100):
    speed = int(input(f'Enter speed of pedestrian class {index + 1} '))
    percentage = int(input(f'Enter the percentage of pedestrian class {index + 1} '))
    classes.append((0, 0))
    #the below lines ensure that the current class of pedestrians doesn't exceed 100% of total pedestrians
    if pedestrian_fraction + percentage > 100:
        percentage = 100 - pedestrian_fraction
    pedestrian_fraction = pedestrian_fraction + percentage
    classes[index] = ((int(percentage * N * 0.01) + 1, speed))
    index = index + 1

#now we would randomly place the pedestrians in our lattice
for i in range(0, index, 1):
    (number, speed) = classes[i]
    temp = number
    while(temp > 0):
        (x, y) = (rn.randint(0, rowsize - 1), rn.randint(0, columnsize - 1))
        if old_array[x][y] == 0:
            old_array[x][y] = speed
            temp = temp - 1
for i in range(rowsize):
    for j in range(columnsize):
        print(old_array[i][j], end=' ')
    print(' ')


iteration = 100
while(iteration > 0):

    sleep(0.3)
    #in each iteration, new_array is the current lattice whose values would be determined by the values in the old lattice, i.e., old_array
    new_array = [[0 for i in range(columnsize)] for j in range(rowsize)]

    for i in range(0, rowsize, 1):
        for j in range(0, columnsize, 1):
            if(old_array[i][j] > 0):
                gap1 = gap2 = gap3 = 0
                #the 3 gaps are to find the gaps in current lane(row) and adjacent ones
                #we're only interested in adjacent lanes if the adjacent lane and it's own adjacent lane are vacant in that position
                gap2 = findgap(old_array, columnsize, i, j)

                if i - 1 < 0:
                    pass
                elif old_array[i - 1][j] > 0:
                    pass
                else:
                    if ((i - 2 >= 0 and old_array[i - 2][j] == 0) or (i - 2 < 0)):
                        gap1 = findgap(old_array, columnsize, i - 1, j)
                    else:
                        pass

                if i + 1 >= rowsize:
                    pass
                elif old_array[i + 1][j] > 0:
                    pass
                else:
                    if ((i + 2 < rowsize and old_array[i + 2][j] == 0) or (i + 2 >= rowsize)):
                        gap3 = findgap(old_array, columnsize, i + 1, j)
                    else:
                        pass

                if (gap1 > gap2 and gap1 > gap3):
                    fixnewposition(
                        new_array, old_array[i][j], columnsize, i - 1, i, j, gap1)
                elif (gap2 > gap1 and gap2 > gap3):
                    fixnewposition(
                        new_array, old_array[i][j], columnsize, i, i, j, gap2)
                elif (gap3 > gap1 and gap3 > gap2):
                    fixnewposition(
                        new_array, old_array[i][j], columnsize, i + 1, i, j, gap3)
                elif (gap1 > gap2 and gap1 == gap3):
                    key = rn.choices([1, -1], weights=[1, 1], k=1)[0]
                    fixnewposition(
                        new_array, old_array[i][j], columnsize, i + key, i, j, gap1)
                elif(gap2 > gap1 and gap2 == gap3):
                    key = rn.choices([1, 0], weights=[1, 1], k=1)[0]
                    fixnewposition(
                        new_array, old_array[i][j], columnsize, i + key, i, j, gap2)
                elif (gap1 > gap3 and gap1 == gap2):
                    key = rn.choices([-1, 0], weights=[1, 1], k=1)[0]
                    fixnewposition(
                        new_array, old_array[i][j], columnsize, i + key, i, j, gap1)
                elif (gap1 == 0 and gap2 == 0 and gap3 == 0):
                    new_array[i][j] = old_array[i][j]
                else:
                    key = rn.choices([-1, 1, 0], weights=[1, 1, 8], k=1)[0]
                    fixnewposition(
                        new_array, old_array[i][j], columnsize, i + key, i, j, gap1)

    print(f'Now running {iteration}th simulation')

    for i in range(rowsize):
        for j in range(columnsize):
            if new_array[i][j] == 0:
                print('', end=' ')
            else:
                print('*', end='')
            old_array[i][j] = new_array[i][j]
        print('')

    iteration = iteration - 1

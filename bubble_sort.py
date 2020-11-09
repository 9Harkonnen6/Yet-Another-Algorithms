from random import *

random_array = []
def generate():
    for i in range(10):
        random_array.append(randrange(0,20,1))
    return random_array
    
def bubble_sort(random_array):
    for i in range(len(random_array)-1, 0, -1):
        for j in range(i):
            if random_array[j] > random_array[i]:
                random_array[j], random_array[i] = random_array[i], random_array[j]
    return random_array

generate()
print(bubble_sort(random_array))
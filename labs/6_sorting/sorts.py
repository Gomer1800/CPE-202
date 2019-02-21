import random
import time

def selection_sort(list):
    if list is None:
        raise ValueError
    start_index = len(list)
    comps = 0
    comps = selection_sort_helper(list, start_index, comps)
    print(comps)
    return comps

def selection_sort_helper( list, i , comps):
    if i <= 1: return comps
    print(list)
    largest_pos = 0
    for j in range(1,i):
        comps += 1
        if list[j] > list[largest_pos]:
            largest_pos = j
    list[largest_pos], list[i-1] = list[i-1], list[largest_pos]
    return selection_sort_helper( list, i-1, comps)
    
def insertion_sort(list):
    if list is None:
        raise ValueError
   

def main():
    # Give the random number generator a seed, so the same sequence of 
    # random numbers is generated at each run
    random.seed(1234) 
    
    # Generate 5000 random numbers from 0 to 999,999
    randoms = random.sample(range(1000000), 5000)
    start_time = time.time() 
    comps = selection_sort(randoms)
    stop_time = time.time()
    print(comps, stop_time - start_time)

if __name__ == '__main__': 
    main()


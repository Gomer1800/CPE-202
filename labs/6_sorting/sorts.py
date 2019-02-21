import random
import time

def selection_sort(list):
    if list is None:
        raise ValueError
    start_index = len(list)
    comps = 0
    comps = selection_sort_helper(list, start_index, comps)
    #print(comps)
    return comps

def selection_sort_helper( list, i , comps):
    if i <= 1:
        return comps
    #print(list)
    largest_pos = 0
    # iterate through list, search for largest int up index i
    for j in range(1,i):
        comps += 1
        # selects the largest elem
        if list[j] > list[largest_pos]:
            largest_pos = j
    # now place largest value in correct position, i-1
    list[largest_pos], list[i-1] = list[i-1], list[largest_pos]
    return selection_sort_helper( list, i-1, comps)
    
def insertion_sort(list):
    if list is None:
        raise ValueError
    comps = 0
    # my hacky way of not derefencing list pointer, couldnt figure this out otherwise
    copy = list[1:]
    if len(list) > 1:
        del list[1:]
    return insertion_sort_helper( list, copy, comps)

def insertion_sort_helper( list, unsorted_list, comps):
    # print(unsorted_list)
    if unsorted_list == []:
        return comps
    # print(list)
    pos = -1
    # iterate through sorted list, find position to first elem of unsorted list
    for i in range(len(list)):
        comps += 1
        if unsorted_list[0] < list[i]:
            pos = i
            break
    if pos == -1:
        list.append(unsorted_list.pop(0))
    else: 
        list.insert(pos, unsorted_list.pop(0))
    return insertion_sort_helper( list, unsorted_list, comps)

def main():
    # Give the random number generator a seed, so the same sequence of 
    # random numbers is generated at each run
    random.seed(1234) 

    # Generate 5000 random numbers from 0 to 999,999
    randoms = random.sample(range(1000000), 100)
    start_time = time.time() 
    comps = selection_sort(randoms)
    stop_time = time.time()
    print("SS 100: ",comps, stop_time - start_time)
    
    # Generate 5000 random numbers from 0 to 999,999
    randoms = random.sample(range(1000000), 100)
    start_time = time.time() 
    comps = insertion_sort(randoms)
    stop_time = time.time()
    print("IS: 100",comps, stop_time - start_time)

    # Generate 5000 random numbers from 0 to 999,999
    randoms = random.sample(range(1000000), 200)
    start_time = time.time() 
    comps = selection_sort(randoms)
    stop_time = time.time()
    print("SS 200: ",comps, stop_time - start_time)
    
    # Generate 5000 random numbers from 0 to 999,999
    randoms = random.sample(range(1000000), 200)
    start_time = time.time() 
    comps = insertion_sort(randoms)
    stop_time = time.time()
    print("IS: 200",comps, stop_time - start_time)

    # Generate 5000 random numbers from 0 to 999,999
    randoms = random.sample(range(1000000), 400)
    start_time = time.time() 
    comps = selection_sort(randoms)
    stop_time = time.time()
    print("SS 400: ",comps, stop_time - start_time)
    
    # Generate 5000 random numbers from 0 to 999,999
    randoms = random.sample(range(1000000), 400)
    start_time = time.time() 
    comps = insertion_sort(randoms)
    stop_time = time.time()
    print("IS: 400",comps, stop_time - start_time)

    # Generate 5000 random numbers from 0 to 999,999
    randoms = random.sample(range(1000000), 800)
    start_time = time.time() 
    comps = selection_sort(randoms)
    stop_time = time.time()
    print("SS 800: ",comps, stop_time - start_time)
    
    # Generate 5000 random numbers from 0 to 999,999
    randoms = random.sample(range(1000000), 800)
    start_time = time.time() 
    comps = insertion_sort(randoms)
    stop_time = time.time()
    print("IS: 800",comps, stop_time - start_time)


if __name__ == '__main__': 
    main()


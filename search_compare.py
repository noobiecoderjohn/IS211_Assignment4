import time
import random

def get_me_random_list(n):
    """Generate list of n elements in random order
    
    :params: n: Number of elements in the list
    :returns: A list with n elements in random order
    """
    a_list = list(range(n))
    random.shuffle(a_list)
    return a_list

def sequential_search(a_list, item):
    pos = 0
    found = False

    while pos < len(a_list) and not found:
        if a_list[pos] == item:
            found = True
        else:
            pos = pos + 1

    return found

def ordered_sequential_search(a_list, item):
    pos = 0
    found = False
    stop = False
    while pos < len(a_list) and not found and not stop:
        if a_list[pos] == item:
            found = True
        else:
            if a_list[pos] > item:
                stop = True
            else:
                pos = pos + 1

    return found

def binary_search_iterative(a_list,item):
    first = 0
    last = len(a_list) - 1
    found = False
    while first <= last and not found:
        midpoint = (first + last) // 2
        if a_list[midpoint] == item:
            found = True
        else:
            if item < a_list[midpoint]:
                last = midpoint - 1
            else:
                first = midpoint + 1

    return found

def binary_search_recursive(a_list,item):
    if len(a_list) == 0:
        return False
    else:
        midpoint = len(a_list) // 2
        if a_list[midpoint] == item:
            return True
        else:
            if item < a_list[midpoint]:
                return binary_search_recursive(a_list[:midpoint], item)
            else:
                return binary_search_recursive(a_list[midpoint + 1:], item)

def main():
    list_sizes = [500, 1000, 5000]
    iterations = 100
    target = 99999999

    for size in list_sizes:
        total_time_seq = 0
        total_time_ordered = 0
        total_time_binary_iter = 0
        total_time_binary_rec = 0

        for _ in range(iterations):
            random_list = get_me_random_list(size)
            random_list.sort()

            start_time = time.time()
            sequential_search(random_list, target)
            total_time_seq += time.time() - start_time

            start_time = time.time()
            ordered_sequential_search(random_list, target)
            total_time_ordered += time.time() - start_time

            start_time = time.time()
            binary_search_iterative(random_list, target)
            total_time_binary_iter += time.time() - start_time

            start_time = time.time()
            binary_search_recursive(random_list, target)
            total_time_binary_rec += time.time() - start_time

        avg_time_ordered = total_time_ordered / iterations

        print(f"Ordered Sequential Search took {avg_time_ordered:10.7f} seconds to run, on average")

if __name__ == "__main__":
    main()

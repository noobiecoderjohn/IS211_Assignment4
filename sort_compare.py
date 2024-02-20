import random
import time

def get_me_random_list(n):
    """Generate list of n elements in random order
    
    :params: n: Number of elements in the list
    :returns: A list with n elements in random order
    """
    a_list = list(range(n))
    random.shuffle(a_list)
    return a_list

def insertion_sort(a_list):
    for index in range(1, len(a_list)):
        current_value = a_list[index]
        position = index

        while position > 0 and a_list[position - 1] > current_value:
            a_list[position] = a_list[position - 1]
            position = position - 1

        a_list[position] = current_value

def shell_sort(a_list):
    sublist_count = len(a_list) // 2
    while sublist_count > 0:
        for start_position in range(sublist_count):
            gap_insertion_sort(a_list, start_position, sublist_count)
        sublist_count = sublist_count // 2

def gap_insertion_sort(a_list, start, gap):
    for i in range(start + gap, len(a_list), gap):
        current_value = a_list[i]
        position = i
        while position >= gap and a_list[position - gap] > current_value:
            a_list[position] = a_list[position - gap]
            position = position - gap
        a_list[position] = current_value

def python_sort(a_list):
    """
    Use Python built-in sorted function

    :param a_list:
    :return: the sorted list
    """
    start_time = time.time()
    sorted_list = sorted(a_list)
    end_time = time.time()
    return sorted_list, end_time - start_time

def main():
    list_sizes = [500, 1000, 5000]

    for size in list_sizes:
        print(f"For list size {size}:")
        
        total_time_insertion = 0
        total_time_shell = 0
        total_time_python = 0

        for _ in range(100):
            random_list = get_me_random_list(size)

            start_time = time.time()
            insertion_sort(random_list.copy())
            total_time_insertion += time.time() - start_time

            start_time = time.time()
            shell_sort(random_list.copy())
            total_time_shell += time.time() - start_time

            start_time = time.time()
            python_sort(random_list.copy())
            total_time_python += time.time() - start_time

        avg_time_insertion = total_time_insertion / 100
        avg_time_shell = total_time_shell / 100
        avg_time_python = total_time_python / 100

        print(f"Insertion Sort took {avg_time_insertion:10.7f} seconds to run, on average")
        print(f"Shell Sort took {avg_time_shell:10.7f} seconds to run, on average")
        print(f"Python Sort took {avg_time_python:10.7f} seconds to run, on average")

if __name__ == "__main__":
    main()

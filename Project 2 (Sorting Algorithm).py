# -*- coding: utf-8 -*-
"""
Created on Mon Feb 17 11:40:52 2025

@author: victo
"""

import time
import random

def bubble_sort(blist):
    cmpcount, swapcount = 0, 0
    n = len(blist)
    while True:
        swapped = False
        for i in range(1, n):
            cmpcount += 1
            if blist[i-1] > blist[i]:
                swapcount += 1
                blist[i-1], blist[i] = blist[i], blist[i-1]
                swapped = True
        n -= 1
        if not swapped:
            break
    return cmpcount, swapcount

def merge_sort(mlist):
    if len(mlist) <= 1:
        return mlist
    mid = len(mlist) // 2
    left = merge_sort(mlist[:mid])
    right = merge_sort(mlist[mid:])
    return merge(left, right)

def merge(left, right):
    merged, left_index, right_index = [], 0, 0
    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1
    merged.extend(left[left_index:])
    merged.extend(right[right_index:])
    return merged

def quick_sort(qlist):
    stack = [(0, len(qlist) - 1)]
    while stack:
        left, right = stack.pop()
        if left >= right:
            continue
        # Random pivot selection
        pivot_index = random.randint(left, right)
        qlist[pivot_index], qlist[right] = qlist[right], qlist[pivot_index]
        pivot = qlist[right]
        partition_index = left
        for i in range(left, right):
            if qlist[i] < pivot:
                qlist[i], qlist[partition_index] = qlist[partition_index], qlist[i]
                partition_index += 1
        qlist[partition_index], qlist[right] = qlist[right], qlist[partition_index]
        stack.append((left, partition_index - 1))
        stack.append((partition_index + 1, right))
    return qlist  

def selection_sort(array):
    size = len(array)
    for ind in range(size):
        min_index = ind
        for j in range(ind + 1, size):
            if array[j] < array[min_index]:
                min_index = j
        array[ind], array[min_index] = array[min_index], array[ind]
    return array

def measure_time(sort_function, data):
    start_time = time.time()
    sort_function(data.copy())
    end_time = time.time()
    return end_time - start_time

def generate_test_cases(size):
    return {
        'best': sorted(range(size)),
        'worst': sorted(range(size), reverse=True),
        'average': random.sample(range(size), size)
    }

def menu():
    algorithms = {'1': ('Bubble Sort', bubble_sort), '2': ('Merge Sort', merge_sort), '3': ('Quick Sort', quick_sort), '4': ('Selection Sort', selection_sort)}
    test_sizes = [1000, 10000, 100000]
    while True:
        print("\nWelcome to the test suite of selected sorting algorithms!")
        print("1. Bubble Sort\n2. Merge Sort\n3. Quick Sort\n4. Selection Sort\n5. Exit")
        choice = input("Select a sorting algorithm (1-5): ")
        if choice == '5':
            print("Bye!")
            break
        elif choice in algorithms:
            name, func = algorithms[choice]
            while True:
                print(f"\nCase Scenarios for {name}\n1. Best Case\n2. Average Case\n3. Worst Case\n4. Exit {name} test")
                case_choice = input("Select the case (1-4): ")
                if case_choice == '4':
                    break
                elif case_choice in ['1', '2', '3']:
                    case_map = {'1': 'best', '2': 'average', '3': 'worst'}
                    for n in test_sizes:
                        test_data = generate_test_cases(n)[case_map[case_choice]]
                        time_taken = measure_time(func, test_data)
                        print(f"For N = {n}, it takes {time_taken:.6f} seconds")
                    while True:
                        another = input("Do you want to input another N (Y/N)? ").strip().lower()
                        if another != 'y':
                            break
                        n = int(input("What is the N? "))
                        test_data = generate_test_cases(n)[case_map[case_choice]]
                        time_taken = measure_time(func, test_data)
                        print(f"For N = {n}, it takes {time_taken:.6f} seconds")
        else:
            print("Invalid selection. Please try again.")

if __name__ == "__main__":
    menu()

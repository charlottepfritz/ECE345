#!/usr/bin/env python3

import matplotlib.pyplot as plt
import time
import subprocess
import random
import os
import math




def generate_random_input_file(size):
    with open("inputfile.csv", "w") as file:
        for _ in range(size):
            sort_key = random.randint(1, 1000)
            values = [random.randint(1, 100) for _ in range(10)]  # Adjust the range and number of values as needed
            row = [str(sort_key)] + list(map(str, values))
            file.write(','.join(row) + '\n')



def measure_runtime(script, input_size):
    generate_random_input_file(input_size)

    start_time = time.time()
    subprocess.run(["python", script, "inputfile.csv"])  # Adjust "python" if needed
    end_time = time.time()

    return end_time - start_time



if __name__ == "__main__":
    input_sizes = [10, 50, 100, 200, 500, 1000, 5000, 7500, 10000]  # Adjust the input sizes as needed

    bubble_sort_runtimes = []
    optimized_bubble_sort_runtimes = []
    merge_sort_runtimes=[]
    quick_sort_runtimes=[]


    for input_size in input_sizes:

        #script_path = os.path.abspath(__file__)
        #quick_sort_path = os.path.join(os.path.dirname(script_path), "quick_sort.py")
  
        runtime_bubble_sort = measure_runtime("./bubble_sort.py", input_size)
        runtime_quick_sort = measure_runtime("./quick_sort.py", input_size)
        runtime_merge_sort = measure_runtime("./merge_sort.py", input_size)

        bubble_sort_runtimes.append(runtime_bubble_sort)
        quick_sort_runtimes.append(runtime_quick_sort)
        merge_sort_runtimes.append(runtime_merge_sort)

        print(f"Input Size: {input_size}")
        print(f"Bubble Sort Runtime: {runtime_bubble_sort:.6f} seconds")
        print(f"Quick Sort Runtime: {runtime_quick_sort:.6f} seconds")
        print(f"Merge Sort Runtime: {runtime_merge_sort:.6f} seconds")
        print()

    # Plotting
    fig, axs = plt.subplots(2,2, sharex=True, sharey='row')
    axs[0,0].plot(input_sizes, bubble_sort_runtimes, 'tab:blue', label='Bubble Sort')
    axs[1,0].plot(input_sizes, quick_sort_runtimes, 'tab:orange', label='Quick Sort')
    axs[1,1].plot(input_sizes, merge_sort_runtimes, 'tab:green', label='Merge Sort')
    fig.suptitle('Experimental runtime complexities')

    for ax in axs.flat:   
        ax.set_xlabel('Input Size')
        ax.set_ylabel('Runtime (seconds)')
        ax.legend()

    nlog = lambda n : n*math.log(n)

    fig2, axs2= plt.subplots(2,2,sharex=True, sharey=False)
    axs2[0,0].plot(input_sizes, bubble_sort_runtimes, 'tab:blue', label='Bubble Sort')
    axs2[0,0].plot(input_sizes, [1e-4*nlog(inp) for inp in input_sizes] , 'tab:red', label='c=1e-4')
    axs2[1,0].plot(input_sizes, quick_sort_runtimes, 'tab:orange', label='Quick Sort')
    axs2[1,0].plot(input_sizes, [1e-5*nlog(inp) for inp in input_sizes]  , 'tab:red', label='c=1e-5')
    axs2[1,1].plot(input_sizes, merge_sort_runtimes, 'tab:green', label='Merge Sort')
    axs2[1,1].plot(input_sizes, [1e-4*(inp^2) for inp in input_sizes]  , 'tab:red', label='c=1e-4')
    fig2.suptitle('Determining constants')
    fig2.tight_layout()

    for ax in axs2.flat:   
        ax.set_xlabel('Input Size')
        ax.set_ylabel('Runtime (seconds)')
        ax.legend()

    plt.show()


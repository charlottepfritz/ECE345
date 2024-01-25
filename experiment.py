# import time
# import random
# import subprocess

# def generate_random_input_file(size):
#     with open("inputfile.csv", "w") as file:
#         for _ in range(size):
#             sort_key = random.randint(1, 1000)
#             values = [random.randint(1, 100) for _ in range(10)]  # Adjust the range and number of values as needed
#             row = [str(sort_key)] + list(map(str, values))
#             file.write(','.join(row) + '\n')

# def measure_runtime(script, input_size):
#     #generate_random_input_file(input_size)

#     start_time = time.time()
#     subprocess.run([script, "inputfile.csv"])
#     end_time = time.time()

#     return end_time - start_time

# if __name__ == "__main__":
#     input_sizes = [10, 50, 100, 200, 500, 1000, 5000, 7500, 10000]  # Adjust the input sizes as needed

#     for input_size in input_sizes:
#         runtime_bubble_sort = measure_runtime("./bubble_sort.py", input_size)
#         runtime_optimized_bubble_sort = measure_runtime("./optimized.py", input_size)

#         print(f"Input Size: {input_size}")
#         print(f"Bubble Sort Runtime: {runtime_bubble_sort:.6f} seconds")
#         print(f"Optimized Bubble Sort Runtime: {runtime_optimized_bubble_sort:.6f} seconds")
#         print()

import matplotlib.pyplot as plt
import time
import subprocess
import random

import numpy as np
# Function to calculate n^2 for given input sizes
def n_squared(input_sizes):
    return np.square(input_sizes)


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
    subprocess.run([script, "inputfile.csv"])
    end_time = time.time()

    return end_time - start_time

if __name__ == "__main__":
    input_sizes = [10, 50, 100, 200, 500, 1000, 5000, 7500, 10000]  # Adjust the input sizes as needed

    bubble_sort_runtimes = []
    optimized_bubble_sort_runtimes = []

    for input_size in input_sizes:
        runtime_bubble_sort = measure_runtime("./bubble_sort.py", input_size)
        runtime_optimized_bubble_sort = measure_runtime("./optimized.py", input_size)

        bubble_sort_runtimes.append(runtime_bubble_sort)
        optimized_bubble_sort_runtimes.append(runtime_optimized_bubble_sort)

        print(f"Input Size: {input_size}")
        print(f"Bubble Sort Runtime: {runtime_bubble_sort:.6f} seconds")
        print(f"Optimized Bubble Sort Runtime: {runtime_optimized_bubble_sort:.6f} seconds")
        print()


    # Plotting
    plt.plot(input_sizes, bubble_sort_runtimes, label='Bubble Sort')
    plt.plot(input_sizes, optimized_bubble_sort_runtimes, label='Optimized Bubble Sort')

    plt.xlabel('Input Size')
    plt.ylabel('Runtime (seconds)')
    plt.title('Bubble Sort vs Optimized Bubble Sort')
    plt.legend()
    plt.show()


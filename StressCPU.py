#code written by Harmanjot Singh. 
#Proj AY
#CPU stress test
#You can change the duration of the Test

import psutil
import multiprocessing
import time

def stress_core(core):
    while True:
        2 + 2  # Perform a simple computation to stress the CPU

def cpu_stress_test(duration_seconds=50):
    print(f"Starting CPU stress test for {duration_seconds} seconds...")

    # Get the number of available CPU cores
    num_cores = multiprocessing.cpu_count()

    # Start a process for each CPU core
    processes = []
    for core in range(num_cores):
        process = multiprocessing.Process(target=stress_core, args=(core,))
        process.start()
        processes.append(process)

    try:
        # Let the stress test run for the specified duration
        time.sleep(duration_seconds)
    finally:
        # Terminate all processes when the test is done
        for process in processes:
            process.terminate()

        print("CPU stress test completed.")

if __name__ == "__main__":
    # Specify the duration of the stress test in seconds (default is 10 seconds)
    test_duration = 100
    cpu_stress_test(test_duration)

import multiprocessing
import keyboard  # You need to install the 'keyboard' module using pip

# Define flags to signal the processes to exit
exit_flag_process1 = multiprocessing.Event()
exit_flag_process2 = multiprocessing.Event()

# Define functions for the processes
def process1():
    print("Process 1 is running. Press 'x' to exit.")
    
    # Wait for the 'x' key to be pressed
    keyboard.wait('x')
    
    # Set the exit flag for process 1 to signal it to exit
    exit_flag_process1.set()
    print("Process 1 is exiting")

def process2():
    print("Process 2 is running. Press 'z' to exit.")
    
    # Wait for the 'z' key to be pressed
    keyboard.wait('z')
    
    # Set the exit flag for process 2 to signal it to exit
    exit_flag_process2.set()
    print("Process 2 is exiting")

if __name__ == "__main__":
    # Create two process objects
    p1 = multiprocessing.Process(target=process1)
    p2 = multiprocessing.Process(target=process2)

    # Start the processes
    p1.start()
    p2.start()

    # Wait for the first process to finish
    p1.join()

    # Set the exit flag for the second process to signal it to exit
    exit_flag_process2.set()

    # Wait for the second process to finish
    p2.join()

    print("Both processes have completed")

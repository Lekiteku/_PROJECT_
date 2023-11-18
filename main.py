from display import Display

import threading
import time

Display.gif_to_bmp("test1.gif")
Display.gif_to_bmp("TEST2.gif")
Display.gif_to_bmp("test3.gif")
Display.run_animation()
# Start the threads
thread1 = threading.Thread(target=Display.run_animation)
thread2 = threading.Thread(target=Display.welcome_message)

thread1.start()
thread2.start()

# Wait for all threads to finish
thread1.join()
thread2.join()
print("yesdee")

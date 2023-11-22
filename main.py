from display import Display
from status import StatusManager

import threading
import time

Display.gif_to_bmp("test1.gif")
Display.gif_to_bmp("TEST2.gif")
Display.gif_to_bmp("TEST3.gif")
Display.gif_to_bmp("test4.gif")
Display.gif_to_bmp("test5.gif")

# Start the threads
thread1 = threading.Thread(target=Display.run_animation)
thread2 = threading.Thread(target=Display.welcome_message)
thread3 = threading.Thread(target=StatusManager.send_status)

thread1.start()
thread2.start()
thread3.start()

# Wait for all threads to finish
thread1.join()
thread2.join()
thread3.join()
print("yesdee")

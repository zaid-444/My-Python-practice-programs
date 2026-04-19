# Program for Demonstrating Finding Default Thread

import threading

tname = threading.current_thread().name

print("Default Thread Name: {}".format(tname))
print("Defualt Number of Threads: {}".format(threading.active_count()))
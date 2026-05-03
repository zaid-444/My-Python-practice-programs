# Program for Finding Number of threads actively running by default

import threading

noact = threading.active_count()

print("Number of Threads Running =",noact)
print("-------------------OR-------------------")
print("Number of Threads Running =",threading.active_count())
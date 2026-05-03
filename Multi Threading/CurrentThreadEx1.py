# This Program Obtains Current Thread in Python Environment

import threading

t = threading.current_thread()
print(t)
print(t.name)
print(t.native_id)
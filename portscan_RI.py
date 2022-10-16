import socket
import threading
from queue import Queue

socket.setdefaulttimeout(1)
object_lock = threading.Lock()

destination = input("Enter a destination: ")
hostIP = socket.gethostbyname(destination)
print("Scanning the host IP: ", hostIP)

def portscan(port):
    soxx = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        connect = soxx.connect((hostIP, port))
        with object_lock:
            print("The port", port, "is currently open.")
        connect.close()
    except:
        pass

def threader():
    while True:
        worker_node = q.get()
        portscan(worker_node)
        q.task_done()

q = Queue()

for x in range(2000):
    t = threading.Thread(target = threader)
    t.daemon = True
    t.start()

for worker_node in range (1, 10000):
    q.put(worker_node)

q.join()    
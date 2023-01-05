import socket
import threading
from queue import Queue

socket.setdefaulttimeout(2)
object_lock = threading.Lock()

destination = input ("Enter the destination:")
hostIP = socket.gethostbyname(destination)
print("Scanning the host IP: ", hostIP)

def portscanner(ports):
    soxx = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        connection = soxx.connect((hostIP, ports))
        with object_lock:
            print("The port", ports, "is currently open.")
        connection.close()
    except:
        pass

que = Queue()

def threader():
    while True:
        nodes = que.get()
        portscanner(nodes)
        que.task_done()

for ports in range(150):
    threads = threading.Thread(target= threader)
    threads.daemon = True
    threads.start()

for nodes in range (1, 1000):
    que.put(nodes)

que.join()    

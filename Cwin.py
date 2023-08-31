import time
import socket
import threading
def Prog(iterable, total=None, prefix='', length=30, fill='█', print_end='\r'):
    total = total or len(iterable)
    start_time = time.time()
    
    def print_progress(iteration):
        percent = (iteration / total) * 100
        filled_length = int(length * iteration // total)
        bar = fill * filled_length + '-' * (length - filled_length)
        
        print(f'\r{prefix} |{bar}|', end=print_end)
    
    for i, item in enumerate(iterable):
        yield item
        print_progress(i + 1)
    
    print_progress(total)
    print()
def receive_messages(client_socket):
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            print(message)
        except:
            break
print('KNetwork v1.7.7')
items = range(1, 101)
for item in Prog(items, prefix='Checking Network', length=50):
    time.sleep(10**-10)
print('---------------Done--------------')
for item in Prog(items, prefix='Checking dattime', length=50):
    time.sleep(10**-10)
print('---------------Done--------------')
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1', 12345))

name = input("Enter your name: ")
client.send(name.encode('utf-8'))

receive_thread = threading.Thread(target=receive_messages, args=(client,))
receive_thread.start()

while True:
    message = input()
    if message.lower() == 'exit':
        break
    client.send(message.encode('utf-8'))

client.close()

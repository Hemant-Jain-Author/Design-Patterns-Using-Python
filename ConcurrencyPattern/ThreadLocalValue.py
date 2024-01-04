import threading

# Thread-local storage
tls_var = threading.local()

# Function to set thread-local value
def set_tls_value(value):
    tls_var.value = value

# Function to get thread-local value
def get_tls_value():
    return tls_var.value

# Worker thread function
def worker_thread():
    set_tls_value("Thread-specific value")
    print(get_tls_value())

# Create and start multiple worker threads
threads = []
for _ in range(3):
    t = threading.Thread(target=worker_thread)
    t.start()
    threads.append(t)

# Wait for all threads to complete
for t in threads:
    t.join()

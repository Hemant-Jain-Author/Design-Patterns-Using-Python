import threading

class Barrier:
    def __init__(self, count):
        self.count = count
        self.barrier_lock = threading.Lock()
        self.barrier_cond = threading.Condition(self.barrier_lock)

    def wait(self):
        with self.barrier_lock:
            self.count -= 1
            if self.count > 0:
                self.barrier_cond.wait()
            else:
                self.barrier_cond.notify_all()


def worker(barrier, id):
    print(f"Worker {id} started")
    # Simulating some work
    for i in range(3):
        print(f"Worker {id} working...")
        # Simulating some computation
    print(f"Worker {id} finished")
    barrier.wait()


# Client code.
num_workers = 3
barrier = Barrier(num_workers)

threads = []
for i in range(num_workers):
    t = threading.Thread(target=worker, args=(barrier, i))
    t.start()
    threads.append(t)

for t in threads:
    t.join()

print("All workers finished. Proceeding to the next step.")


"""
Worker 0 started
Worker 0 working...
Worker 0 working...
Worker 0 working...
Worker 0 finished
Worker 1 started
Worker 1 working...
Worker 1 working...
Worker 1 working...
Worker 1 finished
Worker 2 started
Worker 2 working...
Worker 2 working...
Worker 2 working...
Worker 2 finished
All workers finished. Proceeding to the next step.
"""
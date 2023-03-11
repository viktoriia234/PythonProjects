import os
import threading
import concurrent.futures
import queue
def read_names(filename, queue):
    with open(filename, "r") as f:
        for line in f:
            name = line.strip()
            path = os.path.join("output", f"{name}.txt")
            queue.put(path)

def create_file(queue):
    while not queue.empty():
        path = queue.get()
        with open(path, "w") as f:
            f.write(f"Привет, {os.path.splitext(os.path.basename(path))[0]}!")

if __name__ == "__main__":
    queue = queue.Queue()


    read_thread = threading.Thread(target=read_names, args=("Names.txt", queue))
    read_thread.start()
    read_thread.join()


    with concurrent.futures.ThreadPoolExecutor() as executor:
        tasks = []
        while not queue.empty():
            path = queue.get()
            tasks.append(executor.submit(create_file, queue))

    print("Все файлы созданы!")

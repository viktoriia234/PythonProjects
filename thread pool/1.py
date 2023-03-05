import queue
import concurrent.futures
from time import *

student_queue = queue.Queue()

def add_surname_to_queue():
    while True:
        surname = input()
        if surname == "off":
            break
        student_queue.put(surname)

def remove_student_from_queue():
    while True:
        if not student_queue.empty():
            surname = student_queue.get()
            print("Студент", surname, "отчислен")
        else:
            break

student_queue.put("Хильков")
student_queue.put("")

with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
    future1 = executor.submit(add_surname_to_queue)
    future2 = executor.submit(remove_student_from_queue)

    concurrent.futures.wait([future1, future2])

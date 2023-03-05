import threading
import time
def reminder():
    message = input("Что вы хотите, чтобы я вам напомнила? ")
    seconds = int(input("Через сколько секунд вы хотите, чтобы я вам напомнила об этом? "))

    timer = threading.Timer(seconds, lambda: print(message))
    timer.start()

thread = threading.Thread(target=reminder)
thread.start()

time.sleep(10)

print("Программа закончена"

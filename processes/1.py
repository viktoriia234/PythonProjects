import multiprocessing

def count_even(start, end):
    total = 0
    for num in range(start, end+1):
        if num % 2 == 0:
            total += num
    print(total)

def count_odd(start, end):
    total = 0
    for num in range(start, end+1):
        if num % 2 != 0:
            total += num
    print(total)


if __name__ == '__main__':
    start = 1
    end = 1000000

    even_process = multiprocessing.Process(target=count_even, args=(start, end))
    odd_process = multiprocessing.Process(target=count_odd, args=(start, end))

    even_process.start()
    odd_process.start()

    even_process.join()
    odd_process.join()

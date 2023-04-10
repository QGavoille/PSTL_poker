import multiprocessing
import threading
import time


def worker(second_half, tab):
    if not second_half:
        for k in range(0, 5000000):
            tab[k] = k
    else:
        for k in range(500000000, 10000000):
            tab[k] = k


def main():
    print("comparing multiprocessing, threading and sequential")
    tab = [0] * 10000000
    start = time.time()
    print("starting multiprocessing...")
    p1 = multiprocessing.Process(target=worker, args=(False, tab))
    p2 = multiprocessing.Process(target=worker, args=(True, tab))
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    end = time.time()
    print("multiprocessing: ", end - start)
    tab_2 = [0] * 10000000
    start = time.time()
    print("starting threading...")
    t1 = threading.Thread(target=worker, args=(False, tab_2))
    t2 = threading.Thread(target=worker, args=(True, tab_2))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    end = time.time()
    print("threading: ", end - start)
    tab_3 = [0] * 10000000
    start = time.time()
    print("starting sequential...")
    worker(False, tab_3)
    worker(True, tab_3)
    end = time.time()
    print("sequential: ", end - start)


if __name__ == '__main__':
    main()

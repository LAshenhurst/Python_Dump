from multiprocessing import Process, Array, Queue
def f(n, a):
    for i in range(len(a)):
        a[i] *= n

if __name__ == '__main__':
    q = Queue()
    test = Array('i', range(10))
    results = [Process(target=f, args=(x, test)) for x in range(1, 5)]
    for p in results: p.start()
    for p in results: p.join()
    print(test[:])
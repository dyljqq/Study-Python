# coding: utf-8

import os
import multiprocessing
import time
import random


class Consumer(multiprocessing.Process):
    def __init__(self, task_queue, result_queue):
        multiprocessing.Process.__init__(self)
        self.task_queue = task_queue
        self.result_queue = result_queue

    def run(self):
        while True:
            next_task = self.task_queue.get()
            if next_task is None:
                self.task_queue.task_done()
                return
            matches = next_task
            self.task_queue.task_done()
            self.result_queue.put(matches)


def queue():
    tasks = multiprocessing.JoinableQueue()
    results = multiprocessing.Queue()

    num_consumers = 4

    consumers = [Consumer(tasks, results) for i in range(num_consumers)]
    [consumer.start() for consumer in consumers]

    [tasks.put(i) for i in range(100)]
    [tasks.put(None) for i in range(num_consumers)]

    tasks.join()

    while not results.empty():
        print results.get()
    results.close()


def task(data):
    print 'run task: %s, %s' % (data, os.getpid())
    start = time.time()
    time.sleep(random.random() * 3)
    end = time.time()
    print 'Task %s runs %0.2f seconds.' % (data, (end - start))


def use_poop():
    p = multiprocessing.Pool()
    [p.apply_async(task, (i,)) for i in range(10)]
    p.close()
    p.join()
    print 'pool end...'


if __name__ == '__main__':
    queue()
    use_poop()

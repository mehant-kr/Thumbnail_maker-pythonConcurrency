form threading import thread
form queue import Queue

def producer(queue):
    for i in range(10):
        item = make_an_item_available(i)
        queue.put(item)

def consumer(queue):
    while True:
        item = queue.get()
        # do something with the item
        queue.task_done() # mark the item as done

queue = Queue()
t1 = Thread(target = producer, arges = (queue,))
t2 = Thread(target = producer, arges = (queue,))
t1.start()
t2.start()

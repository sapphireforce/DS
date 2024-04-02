from listQueue import ListQueue
import threading
import time
import queue

class Producer:
    def __init__(self, items):
        self.__alive = True
        self.items = items
        self.pos = 0
        self.worker = threading.Thread(target=self.run)

    def get_item(self):
        if self.pos < len(self.items):
            item = self.items[self.pos]
            self.pos += 1
            return item
        else:
            return None

    def run(self):
        while True:
            time.sleep(0.2)
            if self.__alive:
                item = self.get_item()
                if item == None:
                    continue
                print("Arrived", item[1])
                globalQueue.put(item)
            else:
                break

    def start(self):
        self.worker.start()

    def finish(self):
        self.__alive = False
        self.worker.join()

class Consumer:
    def __init__(self):
        self.__alive = True
        self.worker = threading.Thread(target=self.run)

    def run(self):
        while True:
            time.sleep(0.5)
            if self.__alive:
                if not globalQueue.empty():
                    print("Boarding : ", globalQueue.get()[1])
                
            else:
                break
        print("Consumer is dying.")
    def start(self):
        self.worker.start()

    def finish(self):
        self.__alive = False
        self.worker.join()

if __name__ == "__main__":
    
    customers = []
    with open("H:/ds_2024-main/producer_consumer/customer.txt", 'r') as file:
        lines = file.readlines()
        for line in lines:
            customer = line.split()
            customers.append(customer)

    # FIFO
    names = queue.Queue()
    globalQueue = queue.Queue()
    #names = []
    for c in customers:
        names.put(c[1])

    producer = Producer(names)

    # Priority 
    producer = Producer(customers)
    consumer = Consumer()    
    producer.start()
    consumer.start() 
    time.sleep(30) #의도적으로 늘림
    producer.finish()
    consumer.finish()

from listQueue import ListQueue
import threading
import time
import queue

class Producer:
    def __init__(self, items):
        self.__alive = True
        self.items = items
        self.pos = 0
        self.worker = threading.Thread(target=self.run) #쓰레드 생성(?) 아마도

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
                print("Arrived", item) #버그 다발 지역(왜인지는 몰루? 내 직감이 이 부분을 말함)
                #print("Arrived", item[1])
                globalQueue.put(((-(int)(item[0])), item[1])) 
                
            else:
                break

    def start(self):
        self.worker.start()

    def finish(self):
        self.__alive = False
        self.worker.join() #join

class Consumer:
    def __init__(self):
        self.__alive = True
        self.worker = threading.Thread(target=self.run)

    def run(self):
        while True:
            time.sleep(0.5) #디버깅에 용이하도록 의도적으로 늘림 + 크래쉬 걱정떄문에 늘림
            if self.__alive:
                if not globalQueue.empty():
                    item =globalQueue.get()
                    print("Boarding : ", -(int)(item[0]) , item[1])
                    #print("Boarding :", item[1]) #버그 조심!

                
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
    with open("H:/ds_2024-main/producer_consumer/customer.txt", 'r') as file:  #경로조심
        lines = file.readlines()
        for line in lines:
            customer = line.split()
            customers.append(customer)

    # FIFO
    customerList = queue.Queue()
    globalQueue = queue.PriorityQueue() #여러 쓰레드가 참조할 글로벌 큐 선언 -> 내부 구조가 뭐지? RW lock인가? 아니면 LockFreeQueue? 뭐지?
                                        #사실상 무조건 크래쉬 터저야 정상인데 파이썬이라 상관 없는건가?
    #names = []
    for c in customers:
        customerList.put(c)

    producer = Producer(customerList)

    # Priority 
    producer = Producer(customers)
    consumer = Consumer()    
    producer.start()
    consumer.start()
    time.sleep(30) #의도적으로 늘림
    producer.finish()
    consumer.finish()

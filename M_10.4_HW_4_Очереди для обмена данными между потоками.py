import threading
import time
import queue

class Table:
    def __init__(self, number):
        self.number = number
        self.is_busy = False

class Cafe:
    def __init__(self, tables):
        self.tables = tables
        self.queue = queue.Queue()

    def customer_arrival(self):
        for i in range(1, 21):  # 20 посетителей
            print(f"Посетитель номер {i} прибыл")
            customer = threading.Thread(target=self.serve_customer, args=(i,))
            customer.start()
            time.sleep(1)

    def serve_customer(self, customer_number):
        for table in self.tables:
            if not table.is_busy:
                table.is_busy = True
                print(f"Посетитель номер {customer_number} сел за стол {table.number} (начало обслуживания)")
                time.sleep(5)  # Время обслуживания 5 секунд
                print(f"Посетитель номер {customer_number} покушал и ушёл (конец обслуживания)")
                table.is_busy = False
                if not self.queue.empty():
                    next_customer = self.queue.get()
                    self.serve_customer(next_customer)
                return
        print(f"Посетитель номер {customer_number} ожидает свободный стол (помещение в очередь)")
        self.queue.put(customer_number)

if __name__ == "__main__":
    table1 = Table(1)
    table2 = Table(2)
    table3 = Table(3)
    tables = [table1, table2, table3]

    cafe = Cafe(tables)

    customer_arrival_thread = threading.Thread(target=cafe.customer_arrival)
    customer_arrival_thread.start()
    customer_arrival_thread.join()

# здесь работаем с модулем psutil (который позволит получать данные о CPU-RAM)
import psutil as pt
from time import sleep

class CpuBar:

    def __init__(self):
        self.cpu_count = pt.cpu_count(logical=False)
        self.cpu_count_logical = pt.cpu_count()
        # print(self.cpu_count) #сколько ядер (у меня 2)
        # print(self.cpu_count_logical) #сколько всего потоков (у меня 4)
    def cpu_percent_return(self):
        return pt.cpu_percent(percpu=True)
    def cpu_one_return(self):
        return pt.cpu_percent()
    def ram_usage(self):
        return pt.virtual_memory()

if __name__ == '__main__':
    # x = CpuBar()
    #
    # for i in range(10):
    #     print(x.cpu_percent_return())
    #     sleep(0.5)
    print(CpuBar().ram_usage())
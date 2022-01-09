import time
from time import perf_counter as my_timer
import random
def index_add(index=0, erstes_mal=False):
    if erstes_mal:
        return index
    if index == 6:
        index = -1
    return index + 2





input("Press enter to start: ")
time.sleep(random.random())
# Creates list and Dict, initializes timers
if True:
    mylist = ["start_perf", "end_perf", "start_time", "end_time", "start_monotonic", "end_monotonic", "start_process", "end_process"]
    mydict = dict.fromkeys(mylist)
    index = index_add(erstes_mal=True)
    mydict[list(mydict)[index]] = time.perf_counter()
    index = index_add(index)
    mydict[list(mydict)[index]] = time.time()
    index = index_add(index)
    mydict[mylist[index]] = time.monotonic()
    index = index_add(index)
    mydict[mylist[index]] = time.process_time()
# index = 0
# mydict[list(mydict)[index]] = time.perf_counter()
# index += 2
# mydict[mylist[index]] = time.time()
# index += 2
# mydict[mylist[index]] = time.monotonic()
# index += 2
# mydict[mylist[index]] = time.process_time()


print(mydict)
input("Press enter to stop: ")
# Ends timers
if True:
    index = index_add(index)
    mydict[list(mydict)[index]] = time.perf_counter()
    index = index_add(index)
    mydict[list(mydict)[index]] = time.time()
    index = index_add(index)
    mydict[mylist[index]] = time.monotonic()
    index = index_add(index)
    mydict[mylist[index]] = time.process_time()
print(mydict)

print()
# print("Start: " + time.strftime("%X", time.localtime(mydict["start_time"])))
# print("End: " + time.strftime("%X", time.localtime(mydict["end_time"])))
# print("Reaction was {} seconds.".format(mydict["end_time"]-mydict["start_time"]))



for i in range(0,8,2):
    print("Start: " + time.strftime("%X", time.localtime(mydict[list(mydict)[i]])))
    print("End: " + time.strftime("%X", time.localtime(mydict[list(mydict)[i+1]])))
    print("Reaction was {} seconds.".format(mydict[list(mydict)[i+1]] - mydict[list(mydict)[i]]))
    print()
print()
print(time.get_clock_info("perf_counter"))
print(time.get_clock_info("time"))
print(time.get_clock_info("monotonic"))
print(time.get_clock_info("process_time"))


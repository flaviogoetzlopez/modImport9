import time

# print(time.gmtime(0)) # grenwich mean is utc
# print(time.localtime())
# print(time.localtime(time.time()))
# print(time.time())

# time_here = time.localtime()
# print(time_here)
#
# print(f"Year: {time_here[0]} {time_here.tm_year}")
# print(f"Month {time_here[1]} {time_here.tm_mon}")
# print(f"Day: {time_here[2]} {time_here.tm_mday}")
# print(time.strftime("%X", time.localtime()))



"""
import time, datetime, calendar, random

# print(time.gmtime(0))
# print(time.gmtime()) # default value is time.time()
# print()
#
# print(time.localtime(0))
# print(time.localtime()) # default value is time.time()
# print()
#
# print(time.time())
# print(time.time() / (60 * 60 * 24 * 365))
# print()
#
# print(time.localtime(time.time()))
# print()


# time_here = time.localtime() # default value is time.time()
# print(time_here)
# print(f"Year: {time_here[0]} {time_here.tm_year}")
# print(f"Month: {time_here[1]} {time_here.tm_mon}")
# print(f"Day: {time_here[2]} {time_here.tm_mday}")


import time
from time import time as my_timer

input("Press ENTER to start: ")
time_wait = random.randint(1, 6)
time.sleep(time_wait)
time_start = my_timer()
input("PRESS ENTER NOW")
time_end = my_timer()

print(f"Started at: {time.localtime(time_start)[3]}:{time.localtime(time_start)[4]}:{time.localtime(time_start)[5]}")
print(f"Ended at: {time.localtime(time_end)[2]}:{time.localtime(time_end)[3]}:{time.localtime(time_end)[4]}")

print(f"Reaction time was {time_end - time_start} seconds.")

"""


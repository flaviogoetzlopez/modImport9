"""ahora  quiero saber la diferencia en segundos
para no depender de un tonto metodo, para hacerlo yo mismo con localtimee o una locura asi
"""

import time, datetime, pytz
from project_pytz_functions import country_times

"""Problem
I had a datetime.datetime object generated in correct india time
I wanted a struct time or seconds since epoch
Code like:
# india_timezone = pytz.timezone("Asia/Kolkata")
# unformated_time_india = datetime.datetime.now(india_timezone)
# seconds_since_epoch_india = datetime.datetime.timestamp(unformated_time_india)
# struct_time_object_india = time.localtime(seconds_since_epoch_india)
# print("The time in india is: " + time.strftime("%c", struct_time_object_india))
But the time that came was current berlin time
It was because no matter which argument you gave to datetime.datetime.now it gave you the current time, although the \
documentation sais that it has a timezone argument. it was as if it ignored it 


Other code, also dont work:
gm_timezone = pytz.utc
unformated_time_gm = datetime.datetime.now(gm_timezone)
seconds_since_epoch_gm = datetime.datetime.timestamp(unformated_time_gm)
print(time.localtime(seconds_since_epoch_gm))


Then i proceeded to google the time offset, and write them down as variables, in a more bodgy kind of approach.

"""

utc_offset_position = 3600
utc_offset_india = 3600 * 5.5


function_return = country_times(utc_offset_position, utc_offset_india, time.time())
thetime = time.localtime(function_return)
print("The time in india is: " + time.strftime("%c", thetime))


"""
Research:
THe last thing that needs to be integrated, is the time difference of each country as an accessible class variable \
self. which is in seconds

print(time.time())
print(india.seconds_epoch)

print(abs(time.time() - india.seconds_epoch) / 3600) # difference of 4.49999 hours, flippin bits and, correct difference
"""

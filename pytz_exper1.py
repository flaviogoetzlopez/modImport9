import datetime, time, pytz
# print(*pytz.all_timezones, sep="\n")
from project_pytz_functions import country_times
from project_pytz_functions import timezone_properties



india = timezone_properties("Asia/Kolkata")
india.say_time()
india.say_time_chavista()
print()
print("*" * 80)
print()
deutschland = timezone_properties("Europe/Berlin")
deutschland.say_time()
deutschland.say_time_chavista()
print()
print("*" * 80)
print()
gm = timezone_properties("utc")
gm.say_time()
gm.say_time_chavista()




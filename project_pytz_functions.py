import time, datetime, pytz


def country_times(country_located: float = 0, country_converting: float = 0, time_to_convert: float = time.time()) -> \
        float:

    """
    this function tells you the time difference.


    :param country_located: this is the offset time in the country where you are located in either int or float, if \
    ignored it will be set to 0, assuming you are in london
    :param country_converting: offset time from utc of country investigating
    :param time_to_convert: default, current time, otherwise, seconds since epoch to investigate
    :return: the current or searched for time in the country of destiny
    """

    diff = country_converting - country_located
    return time_to_convert + diff

class timezone_properties():
    def __init__(self, timezone_string):
        self.timezone_name = pytz.timezone(timezone_string)
        self.unformated_datetime_struct = datetime.datetime.now(self.timezone_name) # esto esta bien
        self.unformated_string = str(self.unformated_datetime_struct)
        print("Unformated datetime struct string", self.unformated_string, sep=": ")
        # print(self.unformated_datetime_struct.date())



        # Cuando era invalido escribi este codigo, por que no lograba hacer un struct time object correctamente ni tener el time since epoch.
        # ya no es necesario
        self.timelist = []
        self.timelist.append(self.unformated_string[0:4])
        self.timelist.append(self.unformated_string[5:7])
        self.timelist.append(self.unformated_string[8:10])
        self.timelist.append(self.unformated_string[11:13])         # depinga
        self.timelist.append(self.unformated_string[14:16])
        self.timelist.append(self.unformated_string[17:19])
        print("Formated list", self.timelist)



        self.struct_time = self.unformated_datetime_struct.timetuple()
        print(self.struct_time)


        self.seconds_epoch = time.mktime(self.struct_time)
        print("Time since epoch", self.seconds_epoch, sep=": ")

        self.utc_diff = self.seconds_epoch - time.time()

        # uncorrect way to create seconds since epoch, because its not international, it uses utc time
        # self.seconds_epoch = self.unformated_datetime_struct.timestamp() # ERROR AQUI # only for utc
        # self.seconds_epoch = datetime.datetime.timestamp(self.unformated_datetime_struct)
        # print("Seconds since epoch f up", self.seconds_epoch, sep=": ")
        # self.struct_time = time.localtime(self.seconds_epoch)


    def say_time(self):
        print(f"The time in {self.timezone_name} is: {time.strftime('%c', self.struct_time)}.")

    def say_time_chavista(self):
        seconds_in_india = time.time() + self.utc_diff
        struct_time = time.localtime(seconds_in_india)

        print(f"The time in {self.timezone_name} is: {time.strftime('%c', struct_time)}.")


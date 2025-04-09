class HourClock():
    def __init__(self, hours):
        self.test = hours

    def set_time(self, time_):
        if isinstance(time_, int) and 1 <= time_ <= 12:
            self._hours = time_
        else:
            raise ValueError("Некорректное время")

    def get_time(self):
        return self._hours

    test = property(get_time, set_time)

try:
    HourClock('pizza time 🕷')
except ValueError as e:
    print(e)
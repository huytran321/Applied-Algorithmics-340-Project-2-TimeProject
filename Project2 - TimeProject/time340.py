# Huy Tran
# CSS 340
#Goal: Create a TimeSpan Class that does Operator Overload


class TimeSpan():
    def __init__(self, seconds = 0, minutes = 0, hours = 0):
        self.__seconds = seconds
        self.__minutes = minutes
        self.__hours = hours

    def getSeconds(self):
        return self.__seconds

    def getMinutes(self):
        return self.__minutes

    def getHours(self):
        return self.__hours

    def totalSeconds(self):
        return (self.__seconds) + (self.__minutes * 60) + (self.__hours * 3600)

    def simplify(self):
        negativeValue = False
        seconds = self.totalSeconds()
        if(seconds < 0):
           seconds = (seconds * -1)
           negativeValue = True
        hours = seconds // 3600
        minutes = (seconds - (hours * 3600)) // 60
        seconds = (seconds - (hours * 3600) - (minutes * 60))
        if(negativeValue):
            self.__seconds = seconds * -1
            self.__minutes = minutes * -1
            self.__hours = hours * -1
        else:
            self.__seconds = seconds
            self.__minutes = minutes
            self.__hours = hours

    def setTime(self, seconds, minutes, hours):
        self.__seconds = seconds
        self.__minutes = minutes
        self.__hours = hours
        self.simplify()

    def __add__(self, time):
        timeTotal = TimeSpan(time.getSeconds(), time.getMinutes(), time.getHours())
        timeTotal.setTime(self.getSeconds() + time.getSeconds(), self.getMinutes() + time.getMinutes(), self.getHours() + time.getHours())
        return timeTotal

    def __sub__(self, time):
        timeTotal = TimeSpan(time.getSeconds(), time.getMinutes(), time.getHours())
        timeTotal.setTime(self.getSeconds() - time.getSeconds(), self.getMinutes() - time.getMinutes(), self.getHours() - time.getHours())
        return timeTotal

    def __neg__(self):
        timeTotal = TimeSpan(-1 * self.getSeconds(),-1 * self.getMinutes(), -1 * self.getHours())
        return timeTotal

    def __eq__(self, time):
        selfTotalSeconds = self.totalSeconds()
        timeTotalSeconds = time.totalSeconds()
        if selfTotalSeconds == timeTotalSeconds:
            return True
        else:
            return False

    def __ne__(self, time):
        selfTotalSeconds = self.totalSeconds()
        timeTotalSeconds = time.totalSeconds()
        if selfTotalSeconds != timeTotalSeconds:
            return True
        else:
            return False

    def __lt__(self, time):
        selfTotalSeconds = self.totalSeconds()
        timeTotalSeconds = time.totalSeconds()
        if selfTotalSeconds < timeTotalSeconds:
            return True
        else:
            return False

    def __le__(self, time):
        selfTotalSeconds = self.totalSeconds()
        timeTotalSeconds = time.totalSeconds()
        if selfTotalSeconds < timeTotalSeconds or selfTotalSeconds == timeTotalSeconds:
            return True
        else:
            return False

    def __gt__(self, time):
        selfTotalSeconds = self.totalSeconds()
        timeTotalSeconds = time.totalSeconds()
        if selfTotalSeconds > timeTotalSeconds:
            return True
        else:
            return False

    def __ge__(self, time):
        selfTotalSeconds = self.totalSeconds()
        timeTotalSeconds = time.totalSeconds()
        if selfTotalSeconds > timeTotalSeconds or selfTotalSeconds == timeTotalSeconds:
            return True
        else:
            return False

    def __str__(self):
        self.setTime(self.__seconds, self.__minutes, self.__hours)
        return "Hours: " + str(round(self.__hours)) + ", Minutes: " + str(round(self.__minutes)) + ", Seconds: " + str(round(self.__seconds))




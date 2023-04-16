class Date:
    DAYS_IN_LEAP_YEAR = 366
    DAYS_IN_YEAR = 365
    WEEKDAYS = {0:"sunday", 1:"monday", 2:"tuesday", 3:"wednesday", 4:"thursday", 5:"friday", 6:"saturday"}
    FIRST_MONTH_AND_DAY = 1
    LAST_MONTH = 12
    FEBRUARY = 2
    START_YEAR = 1900
    LAST_YEAR = 2050


    def __init__(self, day: int, month: int, year: int):
        '''Validar día, mes y año. Se comprobará si la fecha es correcta
        (entre el 1-1-1900 y el 31-12-2050); si el día no es correcto, lo pondrá a 1;
        si el mes no es correcto, lo pondrá a 1; y si el año no es correcto, lo pondrá a 1900.
        Ojo con los años bisiestos.
        '''

        self.year = year if 1900 <= year <= 2050 else 1900
        self.month = month if 0 < month <= 12 else 1
        self.leap = Date.is_leap_year(self)
        february_days = 29 if self.leap else 28
        self.DAYS_IN_MONTH = [
        {"days":31, "month_number": 1, "month_name":"january"}, {"days": february_days, "month_number": 2, "month_name":"february"}, 
        {"days":31, "month_number": 3, "month_name":"march"}, {"days":30, "month_number": 4, "month_name": "april"},
        {"days":31, "month_number": 5, "month_name":"may"}, {"days":30, "month_number": 6, "month_name": "june"}, 
        {"days":31, "month_number": 7, "month_name":"july"}, {"days":31, "month_number": 8, "month_name":"august"},
        {"days":30, "month_number": 9, "month_name":"september"}, {"days":31, "month_number": 10, "month_name":"october"},  
        {"days":30, "month_number": 11, "month_name":"november"},{"days":31, "month_number": 12, "month_name":"december"}
        ]
        self.day = day if day <= self.DAYS_IN_MONTH[self.month]["days"] else 1

    @staticmethod
    def is_leap_year(other, year=0) -> bool:
        year = other.year if not year else year
        return year % 4 == 0 and year % 100 != 0 or year % 400 == 0

    def days_in_month(self) -> int:
        if self.is_leap_year(self) and self.month == self.FEBRUARY:
            return self.DAYS_IN_MONTH[self.month - 1]["days"] + 1 
        return self.DAYS_IN_MONTH[self.month - 1]["days"]

    def add_days_in_month(self) -> int:
        days = 1 if self.month >= self.FEBRUARY and self.leap else 0
        for month in range(self.FIRST_MONTH_AND_DAY, self.month):
            days += self.DAYS_IN_MONTH[month - 1]["days"]
        return days

    def add_days_in_year(self):
        days = 0
        for year in range(self.START_YEAR, self.year):
            if Date.is_leap_year(self, year):
                days += self.DAYS_IN_LEAP_YEAR
            else:
                days += self.DAYS_IN_YEAR
        return days

    def delta_days(self) -> int:
        '''Número de días transcurridos desde el 1-1-1900 hasta la fecha'''
        days = 0
        if self.year == self.START_YEAR:
            days += self.day - self.FIRST_MONTH_AND_DAY
            days += self.add_days_in_month()
            return days
        days = self.DAYS_IN_MONTH[self.month]["days"] - self.day 
        days += self.add_days_in_year()
        days += self.add_days_in_month()
        return days

    def weekday(self) -> int:
        '''día de la semana de la fecha (0 para domingo, ..., 6 para sábado).
        El 1-1-1900 fue domingo.'''
        day_calc = self.delta_days() % 7
        return f"The day {self.day}/{self.month}/{self.year} was {self.WEEKDAYS[day_calc]}"

    def is_weekend(self) -> bool:
        day_calc = self.delta_days() % 7
        return day_calc == 0 or day_calc == 6 

    def short_date(self) -> str:
        '''02/09/2003'''
        return f"{self.day}/{self.month}/{self.year}"

    def __eq__(self, other):
        return self.month == other.month and self.day == other.day and self.year == other.year
    
    def __gt__(self, other):
        if self.year > other.year:
            return True
        if self.year == other.year and self.month > other.month:
            return True
        if self.year == other.year and self.month == other.month and self.day > other.day:
            return True
        return False

    def __lt__(self, other):
        if self.__eq__(other):
            return False
        return not self.__gt__(other)

    def __add__(self, n_of_days):
        n_of_months = 0
        n_of_years = 0
        enough_days = True
        while enough_days:
            for i in range(self.month, len(self.DAYS_IN_MONTH) + 1):
                month = i - 1
                if n_of_days - self.DAYS_IN_MONTH[month]["days"] <= 0:
                    enough_days = False
                    break
                n_of_days -= self.DAYS_IN_MONTH[month]["days"]
                n_of_months += 1
        new_month = (self.month + n_of_months) % 13
        self.month = new_month if new_month != 0 else new_month + 1
        if n_of_days != 0:
            new_day = self.day + n_of_days
            self.days = new_day % self.DAYS_IN_MONTH[self.month - 1]["days"] + 1
            self.month = self.month if self.day % self.DAYS_IN_MONTH[self.month - 1]["days"] != self.day else self.month + 1
        self.year = self.year + 1 if self.month % 13 != self.month else self.year
        return self.day, self.month, self.year

#        year = self.year
#        month = self.month
#        day_calc = divmod(self.day + n_of_days, self.DAYS_IN_MONTH[self.month]["days"] + 1)
#        months, days = day_calc
#        #day_amount = 1 if day_calc < self.day else 0
#        #day = day_calc + day_amount
#        month = (self.month + 1) % 13 + months % 13
#        if month < self.month:
#            year += 1

    def __str__(self):
        '''martes 2 de septiembre de 2003'''
        pass


date = Date(27,2,1904)

february_days = 28


#print(date.leap)
#print(date.days_of_year)
#date2 = Date(15,2,1900)
#print(date.day)
#print(date.month)
#print(date.year)
#print(date == date2)
#print(date < date2)
#print(date > date2)
#print(date.delta_days())
#print(date.weekday())
#print(date.is_weekend())
print(date + 300)

    # operador + suma días a la fecha
    # operador - resta días a la fecha o calcula la diferencia entre dos fechas
    # operador == dice si dos fechas son iguales
    # operador > dice si una fecha es mayor que otra
    # operador < dice si una fecha es menor que otra
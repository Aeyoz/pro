class Date:
    DAYS_IN_LEAP_YEAR = 366
    DAYS_IN_YEAR = 365
    DAYS_IN_MONTH = {
        1:31, 2:28, 3:31, 4:30,
        5:31, 6:30, 7:31, 8:31,
        9:30, 10:31, 11:30, 12:31}
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
        self.leap = True if Date.is_leap_year(self) and self.month == self.FEBRUARY else False
        self.day = day if day <= self.DAYS_IN_MONTH[self.month] + int(self.leap) else 1

    @staticmethod
    def is_leap_year(other, year=0) -> bool:
        year = other.year if not year else year
        return year % 4 == 0 and year % 100 != 0 or year % 400 == 0

    def days_in_month(self) -> int:
        if self.is_leap_year(self) and self.month == self.FEBRUARY:
            return self.DAYS_IN_MONTH[self.month] + 1 
        return self.DAYS_IN_MONTH[self.month]

    def add_days_in_month(self) -> int:
        days = 1 if self.month >= self.FEBRUARY and Date.is_leap_year(self) else 0
        for month in range(self.FIRST_MONTH_AND_DAY, self.month):
            days += self.DAYS_IN_MONTH[month]
        return days

    def add_days_in_year(self):
        days = 0
        for year in range(self.START_YEAR, self.year):
            if Date.is_leap_year(year):
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
        days = self.DAYS_IN_MONTH[self.month] - self.day 
        days += self.add_days_in_year()
        days += self.add_days_in_month()
        return days

    def weekday(self) -> int:
        '''día de la semana de la fecha (0 para domingo, ..., 6 para sábado).
        El 1-1-1900 fue domingo.'''
        pass

    def is_weekend(self) -> bool:
        pass

    def short_date(self) -> str:
        '''02/09/2003'''
        pass

    def __eq__(self, other):
        return self.month == other.month and self.day == other.day and self.year == other.year
    
    def __gt__(self, other):
        match self, other:
            case self.year if self.year > other.year:
                return True
            case self.month if self.month > other.month:
                return True
            case self.day if self.day > other.day:
                return True
            case _:
                return False

    def __str__(self):
        '''martes 2 de septiembre de 2003'''
        pass


date = Date(30,2,1800)
date2 = Date(15,2,1940)
print(date.day)
print(date.month)
print(date.year)
#print(date == date2)
#print(date > date2)
#print(date.delta_days())

    # operador + suma días a la fecha
    # operador - resta días a la fecha o calcula la diferencia entre dos fechas
    # operador == dice si dos fechas son iguales
    # operador > dice si una fecha es mayor que otra
    # operador < dice si una fecha es menor que otra
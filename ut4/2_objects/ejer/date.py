class Date:
    DAYS_IN_LEAP_YEAR = 366
    DAYS_IN_YEAR = 365
    DAYS_IN_MONTH = {
        1:31, 2:28, 3:31, 4:30,
        5:31, 6:30, 7:31, 8:31,
        9:30, 10:31, 11:30, 12:31}
    FIRST_MONTH = 1
    FEBRUARY = 2
    LAST_MONTH = 12
    START_YEAR = 1900
    LAST_YEAR = 2050
    def __init__(self, day: int, month: int, year: int):
        '''Validar día, mes y año. Se comprobará si la fecha es correcta
        (entre el 1-1-1900 y el 31-12-2050); si el día no es correcto, lo pondrá a 1;
        si el mes no es correcto, lo pondrá a 1; y si el año no es correcto, lo pondrá a 1900.
        Ojo con los años bisiestos.
        '''
        self.day = day
        self.month = month
        self.year = year

    def is_leap_year(self) -> bool:
        return self.year % 4 == 0 and self.year % 100 != 0 or self.year % 400 == 0

    def check_leap_year(self, year):
        return year % 4 == 0 and year % 100 != 0 or year % 400 == 0

    def days_in_month(self) -> int:
        if self.check_leap_year() and self.month == self.FEBRUARY:
            return self.DAYS_IN_MONTH[self.month] + 1 
        return self.DAYS_IN_MONTH[self.month]

# CAMBIAR
    def add_days_in_month(self) -> int:
        for month in range(self.month + 1, self.LAST_MONTH + 1):
            if self.check_leap_year(year) and month == self.FEBRUARY:
                added_days = 0 if self.month != self.FEBRUARY else 1
                days += self.DAYS_IN_MONTH[month] + added_days
            days += self.DAYS_IN_MONTH[month]
        pass

    def delta_days(self) -> int:
        '''Número de días transcurridos desde el 1-1-1900 hasta la fecha'''
        days = self.DAYS_IN_MONTH[self.month] - self.days
        for month in range(self.month + 1, self.LAST_MONTH + 1):
            if self.check_leap_year(self.year) and month == self.FEBRUARY:
                added_days = 0 if self.month != self.FEBRUARY else 1
                days += self.DAYS_IN_MONTH[month] + added_days
            days += self.DAYS_IN_MONTH[month]
        for year in range(self.START_YEAR, self.year):
            if self.check_leap_year(year):
                days += self.DAYS_IN_LEAP_YEAR
            else:
                days += self.DAYS_IN_YEAR

    def weekday(self) -> int:
        '''día de la semana de la fecha (0 para domingo, ..., 6 para sábado).
        El 1-1-1900 fue domingo.'''
        pass

    def is_weekend(self) -> bool:
        pass

    def short_date(self) -> str:
        '''02/09/2003'''
        pass

    def __str__(self):
        '''martes 2 de septiembre de 2003'''
        pass


date = Date(1,1,1900)
print(date.is_leap_year())


    # operador + suma días a la fecha
    # operador - resta días a la fecha o calcula la diferencia entre dos fechas
    # operador == dice si dos fechas son iguales
    # operador > dice si una fecha es mayor que otra
    # operador < dice si una fecha es menor que otra


#bisiesto
#year = input("Introduzca la el año: ")
#
#if year.isnumeric():
#    year = int(year)
#    if (year % 4 == 0 and year % 100 != 0) or year % 400 ==0:
#        print("El año es bisiesto")
#    else:
#        print("El año no es bisiesto")
#else:
#    print("Formato no valido")

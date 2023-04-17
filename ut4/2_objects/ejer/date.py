class Date:
    DAYS_IN_LEAP_YEAR = 366
    DAYS_IN_YEAR = 365
    WEEKDAYS = {0:"DOMINGO", 1:"LUNES", 2:"MARTES", 3:"MIERCOLES", 4:"JUEVES", 5:"VIERNES", 6:"SABADO"}
    FIRST_MONTH_AND_DAY = 1
    LAST_MONTH = 12
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
        {"days":31, "month_name":"ENERO"}, 
        {"days": february_days, "month_name":"FEBRERO"}, 
        {"days":31, "month_name":"MARZO"}, 
        {"days":30, "month_name": "ABRIL"},
        {"days":31, "month_name":"MAYO"}, 
        {"days":30, "month_name": "JUNIO"}, 
        {"days":31, "month_name":"JULIO"}, 
        {"days":31, "month_name":"AGOSTO"},
        {"days":30, "month_name":"SEPTIEMBRE"}, 
        {"days":31, "month_name":"OCTUBRE"},  
        {"days":30, "month_name":"NOVIEMBRE"},
        {"days":31, "month_name":"DICIEMBRE"}]
        self.day = day if day <= self.DAYS_IN_MONTH[self.month - 1]["days"] else 1

    @staticmethod
    def is_leap_year(item) -> bool:
        year = item.year if not isinstance(item, int) else item
        return year % 4 == 0 and year % 100 != 0 or year % 400 == 0

    @property
    def days_in_month(self) -> int:
        return self.DAYS_IN_MONTH[self.month - 1]["days"]

    def add_days_in_month(self) -> int:
        days = 0
        for month in range(self.FIRST_MONTH_AND_DAY, self.month):
            days += self.DAYS_IN_MONTH[month - 1]["days"]
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
            days += self.day - self.FIRST_MONTH_AND_DAY + self.add_days_in_month()
            return days
        days += self.day - self.FIRST_MONTH_AND_DAY + self.add_days_in_month() + self.add_days_in_year()
        return days

    @property
    def weekday(self) -> int:
        '''día de la semana de la fecha (0 para domingo, ..., 6 para sábado).
        El 1-1-1900 fue domingo.'''
        day_calc = (self.delta_days() + 1) % 7
        day = day_calc if day_calc in self.WEEKDAYS else 0
        return day

    @property
    def is_weekend(self) -> bool:
        day_calc = (self.delta_days() + 1) % 7
        day = day_calc if day_calc in self.WEEKDAYS else 0
        return day == 0 or day > 5

    @property
    def short_date(self) -> str:
        '''02/09/2003'''
        day = str(self.day) if len(str(self.day)) >= 2 else f"0{self.day}"
        month = str(self.month) if len(str(self.month)) > 2 else f"0{self.month}"
        return f"{day}/{month}/{self.year}"

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
        month = self.month
        year = self.year
        total_days = self.day + n_of_days
        total_days_month = self.days_in_month
        while total_days > total_days_month:
            total_days -= total_days_month
            month += self.FIRST_MONTH_AND_DAY
            if month > self.LAST_MONTH:
                month = 1
                year += 1
            total_days_month = self.DAYS_IN_MONTH[month - 1]["days"] + int(self.leap and month == 2)
        return Date(total_days, month, year)
    
    def __sub__(self, other: int) -> int:
        if isinstance(other, int):
            month = self.month
            year = self.year
            total_days = self.day - other
            total_days_month = self.days_in_month
            while total_days < self.FIRST_MONTH_AND_DAY:
                month -= 1
                if month < self.FIRST_MONTH_AND_DAY:
                    month = self.LAST_MONTH
                    year -= 1
                total_days_month = self.DAYS_IN_MONTH[month - 1]["days"] + int(self.leap and month == 2)
                total_days += total_days_month
            return Date(total_days, month, year)
        else:
            return self.delta_days() - other.delta_days()

    def __str__(self):
        '''martes 2 de septiembre de 2003'''
        return f"{self.WEEKDAYS[self.weekday]} {self.day} DE {self.DAYS_IN_MONTH[self.month - 1]['month_name']} DE {self.year}"

#date = Date(20,9,2002)
#print(date.short_date())
#print(date)

    # operador - resta días a la fecha o calcula la diferencia entre dos fechas
import calendar

class MyCalendario(calendar.Calendar):
    def count_weekday_in_year(self, year, weekday):
        current_month = 1
        numero_de_dias = 0
        while(current_month <= 12):
            for data in self.monthdays2calendar(year, current_month):
                if data[weekday][0] !=0:
                    numero_de_dias = numero_de_dias + 1

                current_month = current_month + 1
        return numero_de_dias

my_calendar = MyCalendario()
numero_de_dias = my_calendar.count_weekday_in_year(2000, calendar.SATURDAY)

print(numero_de_dias)

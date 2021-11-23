# import datetime datetime es el paquete y datetime es una funcion llamada igual dentro de datetime
from datetime import datetime


# datetime.utcnow()
my_time = datetime.now()  # devuelve la hora en UTC (Universal Cordinated Time)
print(my_time)

my_day = datetime.today()
print(my_day)
print(f'Year: {my_day.year}')
print(f'Month: {my_day.month}')
print(f'Day: {my_day.day}')

#  Formateo de fechas
# tabla de codigo de formato (Elementos mas populares)
# %Y - Year
# %m - month
# %d - daylight
# %H - Hour
# %M - Minute
# %S - Seconds

my_datetime = datetime.now()
print(my_datetime)

my_str = my_datetime.strftime('%d/%m/%Y')
print(f'Formato LATAM: {my_str}')

my_str = my_datetime.strftime('%m/%d/%Y')
print(f'Formato USA: {my_str}')

my_str = my_datetime.strftime('Estamos en el año: %Y')
print(f'Formato Random: {my_str}')




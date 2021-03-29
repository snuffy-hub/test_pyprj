import datetime as dt

born_time = dt.datetime(1987, 12, 13)
current_time = dt.datetime.utcnow()

print(born_time)
print(current_time)

age = current_time - born_time

print(f'Мой возраст {age}')

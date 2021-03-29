friends_names = ['Аня', 'Коля', 'Лёша', 'Лена', 'Миша']
friends_cities = ['Владивосток', 'Красноярск', 'Москва', 'Обнинск', 'Чебоксары']

friends = {}

# допишите ваш код сюда
#for i in friends_names:
#    for j in friends_cities:
#        string = f'{friends_names[i]} : {friends_cities[j]}'
#    friends.append(string)
#print(friends)

#for names, cities in zip(friends_names, friends_cities):
#    friends[names] = cities
#print(friends)
#print(f"Лена живёт в городе {friends['Лена']}")

for i in range(0, len(friends_names)):
    friends[friends_names[i]] = friends_cities[i]
#print(friends)
print(f"Лена живёт в городе {friends['Лена']}")

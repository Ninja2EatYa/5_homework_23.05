my_list = ['tea', 'coffee', 'sandwich', 'cola', 'whiskey', 'water']
print('Список:', my_list)
print(("Первый и последний элементы списка:"), (my_list[0],my_list[-1]))
print(("Подсписок с 3 по 5 элемент:"), (my_list[2:5]))
my_list[2] = 'soup'
print(("Замена произвольного элемента:"), (my_list))

my_dict = {"Mouse": "Мышь", "Elephant": "Слон", "Bird": "Птиц", "Dog": "Собака"}
print(("Словарь:"), (my_dict))
print(("Перевод 'Dog':"), (my_dict["Dog"]))
my_dict["Dog"] = "Пес"
print(("Замена слова 'Собака':"), (my_dict))
my_dict["Stone"] = "Камень"
print(("Добавление слова 'Камень':"), (my_dict))

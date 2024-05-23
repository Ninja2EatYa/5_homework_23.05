my_dict = {'Peter': 2000, 'Alice': 2001, 'Josh': 2002, 'Frankie': 1999}
print(('B-Day dictionary:'), (my_dict))
print(("Peter's B-day:"), (my_dict['Peter']))
print(("Maria's B-day:"), (my_dict.get('Maria')))
my_dict['Billie'] = 1990
my_dict.update({'Craig': 2010})
del my_dict['Peter']
print(my_dict.get('Peter'))
print(('Modified B-Day dictionary:'), (my_dict))

my_set = {1, 2, 3, 3, 2, 1, 'Cola', True, False, False}
print(('Set:'), (my_set))
my_set.add(4)
my_other_set = {12, 12, 'Cola'}
my_set.update(my_other_set)
my_set.discard('Cola')
print(('Modified set:'), (my_set))

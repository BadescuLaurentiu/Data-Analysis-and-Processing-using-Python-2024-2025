# Creati urmatoarea lista intr-o singura linie de comanda

# Varianta 1
my_list = ["1", "2", "3", "4"]
my_list = list(range(1,5))
print(list(map(lambda x: str(x), my_list)))

# Varianta 2
my_list = list(map(str , range(1, 5)))
print(my_list)

# Varianta 3
my_list = [str(i) for i in range(1,5)]
print(my_list)
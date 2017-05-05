from itertools import groupby

vehicles = [('Ford', 'Taurus'), ('Dodge', 'Durango'), ('Chevrolet', 'Cobalt'), ('Ford', 'F150'),
            ('Dodge', 'Charger'), ('Ford', 'GT')]
sorted_vehicles = sorted(vehicles)
print(sorted_vehicles)

for key, group in groupby(vehicles, lambda make: make[0]):
    # print(key, group)
    for make, model in group:
        # pass
        print("{model} is made by {make}".format(model=model, make=make))
    print("****end of group******")

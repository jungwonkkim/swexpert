furniture = {'TV': 2000, 'sofa' : 3000, 'fridge':15000, 'board' : 800, ' bottle' : 30}

furniture_sorted = {key:furniture[key] for key in sorted(furniture, key =furniture.get, reverse = True)}
print(furniture_sorted)
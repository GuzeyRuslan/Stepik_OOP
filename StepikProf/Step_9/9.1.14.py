names = ['Moana', 'Cars', 'Zootopia', 'Ratatouille', 'Coco', 'Inside Out', 'Finding Nemo', 'Frozen']
budgets = [150000000, 120000000, 150000000, 150000000, 180000000, 175000000, 94000000, 150000000]
box_offices = [643331111, 462216280, 1023784195, 620702951, 807082196, 857611174, 940335536, 1280802282]

result = map(lambda string: f"{string[0]}: {string[1]}$", sorted(list(map(lambda data: (data[0], data[2] - data[1]), zip(names, budgets, box_offices)))))
print(*result, sep='\n')
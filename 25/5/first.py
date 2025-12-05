text = open('input', 'r')


lines = text.readlines()
ranges = []
for i in range(169): # 169 | 4
    id_range = [int(x) for x in lines[i][:-1].split('-')]
    ranges.append(id_range)

available_ingredient_ids = []
for j in range(170, 1170): # 170, 1170 | 5,11
    available_ingredient_ids.append(int(lines[j][:-1]))


def is_fresh(ingredient_id):
    for fresh_id_range in ranges:
        if fresh_id_range[0] <= ingredient_id <= fresh_id_range[1]:
            return True
    return False


fresh_ingredients_count = 0
for available_id in available_ingredient_ids:
    if is_fresh(available_id):
        fresh_ingredients_count += 1

print(fresh_ingredients_count)

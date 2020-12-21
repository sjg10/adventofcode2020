def find_allergens(foods, safe_ingredients):
    # find the canonical list of allergens, ignoring the safe ingredients in the search
    # will change 'foods'
    ingredients = set().union(*[f[0] for f in foods])
    allergens = set().union(*[f[1] for f in foods])
    for f in foods:
        f[0] -= safe_ingredients

    allergen_opts = {}
    discovered = {}
    for a in allergens:
        i = ingredients.copy()
        for f in foods:
            if a in f[1]: i &= f[0]
        allergen_opts[a] = i

    while len(allergens) > 0:
        for a in allergen_opts:
            i = allergen_opts[a]
            if len(i) == 1:
                ing = next(iter(i))
                discovered[a] = ing
                allergens.remove(a)
                for a in allergen_opts:
                    if ing in allergen_opts[a]:
                        allergen_opts[a].remove(ing)
    k = sorted(discovered.keys())
    return ",".join(discovered[a] for a in k)


def find_safe_ingredients(food):
    # Find the safe ingredients that match no allergen
    ingredients = set().union(*[f[0] for f in foods])
    allergens = set().union(*[f[1] for f in foods])
    matches = {a:set(ingredients) for a in allergens}
    for f in food:
        for a in f[1]:
            matches[a] &= f[0]
    return(ingredients - set().union(*list(matches.values())))

def parse_foods(lines):
    foods = []
    for l in lines:
        s = l.split(" (contains ")
        foods.append([set(s[0].split(" ")), set(s[1].strip()[:-1].split(", "))])
    return foods

if __name__ == "__main__":
    with open("input.txt") as fd:
        foods = parse_foods(fd.readlines())

    safe_ingredients = find_safe_ingredients(foods)
    s = sum(sum(1 for f in foods if i in f[0]) for i in safe_ingredients)
    print(s)
    print(find_allergens(foods, safe_ingredients))

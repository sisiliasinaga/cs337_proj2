def replace_ingredients(ingrObjects, replacement):
    new_ingredients = ingrObjects.copy()
    for ingr in new_ingredients:
        for repl in replacement:
            if ingr.name.lower() in repl:
                ingr.name = replacement[repl]

    return new_ingredients

def replace_instructions(steps, replacement):

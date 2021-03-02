def replace_ingredients(ingrObjects, replacement):
    new_ingredients = ingrObjects.copy()
    for ingr in range(len(new_ingredients)):
        for repl in replacement:
            if repl in new_ingredients[ingr].lower():
                new_ingredients[ingr] = ingrObjects[ingr].replace(repl, replacement[repl])

    return new_ingredients


def replace_instructions(steps, replacement):
    new_steps = steps.copy()
    for step in range(len(new_steps)):
        for repl in replacement:
            if repl in steps[step].lower():
                new_steps[step] = steps[step].replace(repl, replacement[repl])

    return new_steps

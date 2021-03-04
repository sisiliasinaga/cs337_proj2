def replace_ingredients(ingrObjects, replacement):
    new_ingredients = ingrObjects.copy()
    for ingr in range(len(new_ingredients)):
        for repl in replacement:
            if repl in new_ingredients[ingr].lower():
                new_ingredients[ingr] = ingrObjects[ingr].replace(repl, replacement[repl])

    return new_ingredients


def replace_instructions(steps, replacement, ingrObjects, transformType):
    if transformType == "vegetarian":
        new_steps = replace_vegetarian(steps, replacement, ingrObjects)
    else:
        new_steps = steps.copy()
        for step in range(len(new_steps)):
            for repl in replacement:
                if repl in steps[step].lower():
                    new_steps[step] = steps[step].replace(repl, replacement[repl])

    return new_steps


def replace_vegetarian(steps, replacement, ingrObjects):
    gBeef = False
    for item in ingrObjects:
        if "ground beef" in item:
            gBeef = True
            break

    new_steps = steps.copy()
    for step in range(len(new_steps)):
        for repl in replacement:
            if repl in new_steps[step].lower():
                if repl is "beef" and gBeef is True:
                    new_steps[step] = steps[step].replace(repl, replacement['ground beef'])
                else:
                    new_steps[step] = steps[step].replace(repl, replacement[repl])

    return new_steps

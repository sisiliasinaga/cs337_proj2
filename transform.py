def replace_ingredients(ingrObjects, replacement):
    new_ingredients = ingrObjects.copy()
    for ingr in range(len(new_ingredients)):
        for repl in replacement:
            if repl in new_ingredients[ingr].lower():
                if repl is "sausage" and "veggie sausage" in new_ingredients[ingr].lower():
                    continue
                if repl is "burger" and "bun" in new_ingredients[ingr].lower():
                    continue
                new_ingredients[ingr] = new_ingredients[ingr].lower().replace(repl, replacement[repl])

    return new_ingredients


def replace_instructions(steps, replacement, ingrObjects, transformType):
    if transformType == "vegetarian":
        new_steps = replace_vegetarian(steps, replacement, ingrObjects)
    else:
        new_steps = steps.copy()
        for step in range(len(new_steps)):
            for repl in replacement:
                if repl in new_steps[step].lower():
                    new_steps[step] = new_steps[step].replace(repl, replacement[repl])

    return new_steps


def replace_vegetarian(steps, replacement, ingrObjects):
    gBeef = False
    chicken_thighs = False
    pork_loin = False
    corned_beef = False
    for item in ingrObjects:
        if "ground beef" in item:
            gBeef = True
        if "chicken thigh" in item:
            chicken_thighs = True
        if "pork tenderloin" or "pork loin" in item:
            pork_loin = True
        if "corned beef" in item:
            corned_beef = True

    new_steps = steps.copy()
    for step in range(len(new_steps)):
        for repl in replacement:
            if repl in new_steps[step].lower():
                if repl is "sausage" and "veggie sausage" in new_steps[step].lower():
                    continue
                if repl is "burger" and "bun" in new_steps[step].lower():
                    continue
                if repl is "beef" and gBeef is True:
                    new_steps[step] = new_steps[step].replace(repl, replacement['ground beef'])
                if repl is "pork" and pork_loin is True:
                    new_steps[step] = new_steps[step].replace(repl, replacement['pork loin'])
                else:
                    new_steps[step] = new_steps[step].replace(repl, replacement[repl])
        if "thigh" in new_steps[step] and chicken_thighs is True:
            new_steps[step] = new_steps[step].replace("thigh", replacement["chicken"])
        if "brisket" in new_steps[step] and corned_beef is True:
            new_steps[step] = new_steps[step].replace("brisket", replacement["corned beef"])

    return new_steps

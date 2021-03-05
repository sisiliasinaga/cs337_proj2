import re


def replace_ingredients(ingrObjects, replacement):
    new_ingredients = ingrObjects.copy()
    for ingr in range(len(new_ingredients)):
        for repl in replacement:
            if repl in new_ingredients[ingr].lower():
                if repl is "sausage" and "veggie sausage" in new_ingredients[ingr].lower():
                    continue
                if repl is "fried chicken" and "vegetarian fried chicken" in new_ingredients[ingr].lower():
                    continue
                if repl is "hot dog" and "vegetarian hot dog" in new_ingredients[ingr].lower():
                    continue
                if repl is "burger" and "bun" in new_ingredients[ingr].lower():
                    continue
                new_ingredients[ingr] = new_ingredients[ingr].lower().replace(repl, replacement[repl])

    return new_ingredients


def replace_instructions(steps, replacement, ingrObjects, transformType):
    if transformType == "vegetarian":
        new_steps = replace_vegetarian(steps, replacement, ingrObjects)
    elif transformType == "non-vegetarian":
        new_steps = replace_nonvegetarian(steps, replacement, ingrObjects)
    else:
        new_steps = steps.copy()
        for step in range(len(new_steps)):
            for repl in replacement:
                if repl in new_steps[step].lower():
                    len_diff = len(replacement[repl]) - len(repl)
                    all_index = [m.start() for m in re.finditer(repl, new_steps[step].lower())]
                    for i in range(len(all_index)):
                        index = all_index[i] + len_diff * i
                        new_steps[step] = new_steps[step][:index] + replacement[repl] + new_steps[step][index + len(repl):]

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
                elif repl is "burger" and "bun" in new_steps[step].lower():
                    continue
                elif repl is "fried chicken" and "vegetarian fried chicken" in new_steps[step].lower():
                    continue
                elif repl is "hot dog" and "vegetarian hot dog" in new_steps[step].lower():
                    continue
                elif repl is "beef" and gBeef is True:
                    new_steps[step] = new_steps[step].replace(repl, replacement['ground beef'])
                elif repl is "pork" and pork_loin is True:
                    new_steps[step] = new_steps[step].replace(repl, replacement['pork loin'])
                else:
                    len_diff = len(replacement[repl]) - len(repl)
                    all_index = [m.start() for m in re.finditer(repl, new_steps[step].lower())]
                    for i in range(len(all_index)):
                        index = all_index[i] + len_diff * i
                        new_steps[step] = new_steps[step][:index] + replacement[repl] + new_steps[step][index + len(repl):]
        if "thigh" in new_steps[step] and chicken_thighs is True:
            new_steps[step] = new_steps[step].replace("thigh", replacement["chicken"])
        if "brisket" in new_steps[step] and corned_beef is True:
            new_steps[step] = new_steps[step].replace("brisket", replacement["corned beef"])

    return new_steps


def replace_nonvegetarian(steps, replacement, ingrObjects):
    seitan_chicken = False
    seitan_beef = False
    bella = False
    oyster = False
    portobello = False
    for item in ingrObjects:
        if "seitan" in item and "chicken" in item:
            seitan_chicken = True
        elif "seitan" in item and "beef" in item:
            seitan_beef = True
        if "mushroom" in item and "bella" in item:
            bella = True
        elif "mushroom" in item and "oyster" in item:
            oyster = True
        elif "mushroom" in item and "portobello" in item:
            portobello = True

    new_steps = steps.copy()
    for step in range(len(new_steps)):
        for repl in replacement:
            if repl in new_steps[step].lower():
                if repl is "seitan" and seitan_chicken is True:
                    new_steps[step] = new_steps[step].replace(repl, replacement["chicken-style seitan"])
                elif repl is "seitan" and seitan_beef is True:
                    new_steps[step] = new_steps[step].replace(repl, replacement["seitan beef"])
                if repl is "mushroom" and bella is True:
                    new_steps[step] = new_steps[step].replace(repl, replacement["baby bella mushrooms"])
                elif repl is "mushroom" and oyster is True:
                    new_steps[step] = new_steps[step].replace(repl, replacement["oyster mushroom"])
                elif repl is "mushroom" and portobello is True:
                    new_steps[step] = new_steps[step].replace(repl, replacement["portobello mushrooms"])
                else:
                    len_diff = len(replacement[repl]) - len(repl)
                    all_index = [m.start() for m in re.finditer(repl, new_steps[step].lower())]
                    for i in range(len(all_index)):
                        index = all_index[i] + len_diff * i
                        new_steps[step] = new_steps[step][:index] + replacement[repl] + new_steps[step][
                                                                                        index + len(repl):]

    return new_steps

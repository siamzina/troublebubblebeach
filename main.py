import requests

drink_recipe_url = "https://www.thecocktaildb.com/api/json/v1/1/search.php?s="
random_drink_url = "https://www.thecocktaildb.com/api/json/v1/1/random.php"


def get_random_drink():
    response = requests.get(random_drink_url)
    data = response.json()
    name = data.get("drinks")[0].get("strDrink")
    return name


def transform_drink_name(name):
    name = name.lower()
    new_name = []
    for i in name:
        if i == " ":
            new_name.append("_")
        else:
            new_name.append(i)
    return "".join(new_name)


def get_drink_recipe(name):
    response = requests.get(drink_recipe_url + name)
    data = response.json()
    drink_data = {"instructions": data.get("drinks")[0].get("strInstructions"),
                  "image": data.get("drinks")[0].get("strDrinkThumb"), "ingredients": []}
    for i in range(16):
        ingredient_name = data.get("drinks")[0].get("strIngredient" + str(i))
        if ingredient_name is not None:
            drink_data["ingredients"].append(ingredient_name)
    return drink_data


drink_name = get_random_drink()
print(get_random_drink())
print(get_drink_recipe(transform_drink_name(drink_name)))

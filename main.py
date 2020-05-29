import random
import requests
import webbrowser

drink_recipe_url = "https://www.thecocktaildb.com/api/json/v1/1/search.php?s="
random_drink_url = "https://www.thecocktaildb.com/api/json/v1/1/random.php"
random_dog_image_url = "https://dog.ceo/api/breeds/image/random"
random_fox_image_url = "https://randomfox.ca/floof/?ref=apilist.fun"


def menu():
    print("Welcome to the \"Troublebubblebeach\"")
    print("Options:\n"
          "Play - 1\n"
          "Rules - 2\n"
          "Finish the program - 3")
    try:
        action = int(input("Enter an option number: ").strip())
        print()
        if action == 1:
            random_picture()
        elif action == 2:
            print("Rules\n"
                  "When the program starts - you get the random photo of a cat, dog or fox.\n"
                  "If you got a photo of a cat - you get the name and the recipe of a cocktail which you need to "
                  "drink.\n"
                  "If you got a photo of a dog  - you play the «Never Have I Ever» game only ones, where you create "
                  "your own task. Losers drink a random cocktail.\n"
                  "If you got a photo of a fox - you get the «Truth or Dare» game, where you get the task randomly.\n"
                  "Players start the game one by one.\n")
            menu()
        elif action == 3:
            print("Good bye!")
            exit()
        else:
            print("There is no such option\n")
            menu()
    except ValueError:
        print("\nInput error\n")
        menu()


def random_picture():
    inp = input("Enter \"Exit\" to finish the game or anything else to play: ").strip().lower()
    if inp == "exit":
        print()
        menu()
    else:
        print("Loading...\n")
        number = random.randrange(0, 3)
        if number == 0:
            print("dog image")
            get_random_dog_image()
            print("Now let's play the game of \"Never have I ever\".\n"
                  "If it's your turn, you lead. Who loses, drinks.\n")
            drink_name = get_random_drink()
            print("Drink name:", drink_name)
            transformed_drink_name = transform_drink_name(drink_name)
            drink_info = get_drink_recipe(transformed_drink_name)
            print("Image:", drink_info.get("image"))
            print("Ingredients:")
            for i in drink_info.get("ingredients"):
                print(i)
            print("Cook instructions:", drink_info.get("instructions"))
        elif number == 1:
            print("fox image")
            get_random_fox_image()
            truth_dare = random.randrange(0, 2)
            if truth_dare == 0:
                print("Truth")
            elif truth_dare == 1:
                print("Dare")
        elif number == 2:
            print("cat image")
            drink_name = get_random_drink()
            print("Drink name:", drink_name)
            transformed_drink_name = transform_drink_name(drink_name)
            drink_info = get_drink_recipe(transformed_drink_name)
            print("Image:", drink_info.get("image"))
            print("Ingredients:")
            for i in drink_info.get("ingredients"):
                print(i)
            print("Cook instructions:", drink_info.get("instructions"))
        random_picture()


def get_random_drink():
    response = requests.get(random_drink_url)
    data = response.json()
    name = data.get("drinks")[0].get("strDrink")
    return name


def get_random_dog_image():
    response = requests.get(random_dog_image_url)
    data = response.json()
    print("Dog image:", data.get("message"), "\n")
    webbrowser.open(data.get("message"))


def get_random_fox_image():
    response = requests.get(random_fox_image_url)
    data = response.json()
    print("Fox image:", data.get("image"), "\n")
    webbrowser.open(data.get("image"))


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


menu()


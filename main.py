import requests
import random
import webbrowser

drink_recipe_url = "https://www.thecocktaildb.com/api/json/v1/1/search.php?s="
random_drink_url = "https://www.thecocktaildb.com/api/json/v1/1/random.php"
random_dog_image_url = "https://dog.ceo/api/breeds/image/random"
random_fox_image_url = "https://randomfox.ca/floof/?ref=apilist.fun"
random_cat_image_url = "https://api.thecatapi.com/v1/images/search"

truth = [
    "What was the last thing you searched for on your phone?",
    "If you had to choose between going naked or having your thoughts appear in thought bubbles above your head for "
    "everyone to read, which would you choose?",
    "After you've dropped a piece of food, what's the longest time you've left it on the ground and then ate it?",
    "Have you ever tasted a booger?",
    "Have you ever played Cards Against Humanity with your parents?",
    "What's the first thing you would do if you woke up one day as the opposite sex?",
    "Have you ever peed in the pool?",
    "Who do you think is the worst dressed person in this room?",
    "Have you ever farted in an elevator?",
    "Of the people in this room, who do you want to trade lives with?",
    "What are some things you think about when sitting on the toilet?",
    "Did you have an imaginary friend growing up?",
    "Do you cover your eyes during a scary part in a movie?",
    "Have you ever practiced kissing in a mirror?",
    "Did your parents ever give you the “birds and the bees” talk?",
    "What is your guilty pleasure?",
    "What is your worst habit?",
    "Has anyone ever walked in on you when going #2 in the bathroom?",
    "Have you ever had a wardrobe malfunction?",
    "Have you ever walked into a wall?",
    "Do you pick your nose?",
    "Do you sing in the shower?",
    "Have you ever peed yourself?",
    "What was your most embarrassing moment in public?",
    "Have you ever farted loudly in class?",
    "Do you ever talk to yourself in the mirror?",
    "You’re in a public restroom and just went #2, then you realized your stall has no toilet paper. What do you do?",
    "What would be in your web history that you’d be embarrassed if someone saw?",
    "Have you ever tried to take a sexy picture of yourself?",
    "Do you sleep with a stuffed animal?",
    "Do you drool in your sleep?",
    "Do you talk in your sleep?",
    "Who is your secret crush?",
    "Do you think [fill in the name] is cute?",
    "Who do you like the least in this room, and why?",
    "What does your dream boy or girl look like?",
    "What is your go-to song for the shower?",
    "Who is the sexiest person in this room?",
    "How would you rate your looks on a scale of 1 to 10?",
    "What don't you like about me?",
    "What was the last thing you texted?",
    "If you were rescuing people from a burning building and you had to leave one person behind from this room, "
    "who would it be?",
    "Do you think you'll marry your current girlfriend/boyfriend?",
    "How often do you wash your undergarments?",
    "Have you ever tasted ear wax?",
    "Have you ever farted and then blamed someone else?",
    "Have you ever tasted your sweat?",
    "What is the most illegal thing you have ever done?",
    "Who is your favorite? Mom or Dad?",
    "Would you trade your sibling in for a million dollars?",
    "Would you trade in your dog for a million dollars?",
    "What is your biggest pet peeve?",
    "If you were allowed to marry more than one person, would you? Who would you choose to marry?",
    "Would you choose to save 100 people without anyone knowing about it or not save them but have everyone praise "
    "you for it?",
    "If you could only hear one song for the rest of your life, what would it be?",
    "If you lost one day of your life every time you said a swear word, would you try not to do it?",
    "Who in this room would be the worst person to date? Why?",
    "Would you rather live with no internet or no A/C or heating?",
    "If someone offered you $1 million to break up with your girlfriend/boyfriend, would you do it?",
    "If you were reborn, what decade would you want to be born in?",
    "If you could go back in time in erase one thing you said or did, what would it be?",
    "Has your boyfriend or girlfriend ever embarrassed you?",
    "Have you ever thought about cheating on your partner?"
]
dare = ["Take an embarrassing selfie and post it as your profile picture.",
        "Remove your socks with your teeth.",
        "Stop a car that is going down the street and tell them that their wheels are turning.",
        "Fill your mouth with water, and each person in the group must tell the funniest joke they know. If you spit "
        "up the water, you have to eat a spoonful of dirt.",
        "Go next door with a measuring cup and ask for a cup of sugar.",
        "Let the group choose an item for you to brush your teeth with."
        "Write your name on the floor with your tongue.",
        "Go outside and pick exactly 40 blades of grass with a pair of tweezers.",
        "Stick a Hot Cheeto in your nose, and leave it there for five minutes.",
        "Open Facebook, go to the account of the first person you see, and like every post on their wall going back "
        "to a year.",
        "Eat a whole piece of paper.",
        "Lick a car tire.",
        "Open your front door and howl like a wolf for 30 seconds.",
        "Let the person to your right put duct tape on any part of your body they choose and rip it off.",
        "I dare you to tie your hands to your ankles for the rest of the game.",
        "Put a bunch of honey on your nose and coat it with flour.",
        "Until the next round, talk super loud, like nobody can hear you.",
        "Call your crush.",
        "Take a shot of pickle juice.",
        "Talk to a pillow like it’s your crush.",
        "Pretend you’re a bird and eat cereal off the floor using only your mouth.",
        "Make out with your hand.",
        "Let someone else style your hair and keep it that way for the rest of the day.",
        "Use a brush like you’re talking into a microphone each time you speak.",
        "Color one of your front teeth black. (Eyeliner works!)",
        "Pick your friend’s nose.",
        "Lick the bottom of your shoe.",
        "Fake cry.",
        "Make repulsive sounds while eating and drinking.",
        "Cross your eyes when talking.",
        "Talk without closing your mouth.",
        "Act like an animal of the group’s choosing.",
        "Get into a debate with a wall.",
        "Squirt your face with a squirt gun continuously while talking.",
        "See how many grapes you can stuff in your mouth.",
        "Hiccup in between each word.",
        "Burp the alphabet.",
        "Draw on your face with permanent marker.",
        "Dip your sock-covered feet in the toilet, and don't dry them off for the rest of the game.",
        "Dump a bunch of LEGOs on the floor and walk over them with your bare feet.",
        "Eat a spoonful of mustard.",
        "Jump into a dumpster.",
        "Lift up the couch cushions, and if there is anything under it, you need to put it in your mouth for 10 "
        "seconds.",
        "Spin around 10 times and try to walk straight.",
        "Eat a raw egg.",
        "Write a letter to your doctor describing an embarrassing rash you have, and post it on Facebook.",
        "Let the group choose three random things from the refrigerator and mix them together. "
        "Then you have to eat it.",
        "Stand up and do jumping jacks until your next turn.",
        "Rub your armpits and then smell your fingers.",
        "Dig through the trash and name everything you find."
        ]


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
            get_random_fox_image()
            truth_dare = random.randrange(0, 2)
            if truth_dare == 0:
                print("Truth")
                print(truth[random.randrange(0, len(truth))])
            elif truth_dare == 1:
                print("Dare")
                print(dare[random.randrange(0, len(dare))])
        elif number == 2:
            get_random_cat_image()
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


def get_random_cat_image():
    response = requests.get(random_cat_image_url)
    data = response.json()
    print("Cat image:", data[0].get("url"), "\n")
    webbrowser.open(data[0].get("url"))


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

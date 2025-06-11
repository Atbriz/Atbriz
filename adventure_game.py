# Jungle Temple Adventure Game
# i added the fourth level to the game 
# i added morethan two distinct choices on the moon part
print("\nWelcome to the Jungle Temple Adventure!\n")
#valid and invalid inputs traker 1= true and 0=false
valid_choice = 1 

# Initial choice: Map or Machete
game = input(
    "You arrive at the edge of the legendary jungle that hides the Temple of Darnork. "
    "It's humid, buzzing with unseen insects, and ancient trees tower over you. "
    "On the ground lies a faded MAP, and nearby a rusty MACHETE hangs from a low branch. "
    "What will you choose to protect yourself? (MAP/MACHETE): "
)
print()

# MAP Path
if game.lower() == "map":
    choice = input(
        "The map guides you to a rickety bridge over a misty ravine or a narrow ledge trail. "
        "Do you CROSS the bridge or TAKE the path? (CROSS/TAKE): "
    )
    print()

    if choice.lower() == "cross":
        action = input(
            "Halfway across, the bridge groans. Ropes begin to snap. "
            "Do you RUN or DROP and cling to the roadside? (RUN/DROP): "
        )
        print()

        if action.lower() == "run":
            mural = input(
                "You dive to the other side just as the bridge collapses. "
                "Inside the archway, you find an ancient mural with glowing symbols. "
                "Do you TOUCH the mural or IGNORE it? (TOUCH/IGNORE): "
            )
            print()

            if mural.lower() == "touch":
                riddle = input(
                    "The symbols shift beneath your fingers. A spirit appears: "
                    "'Answer my riddle to pass, or remain here forever. "
                    "I have mountains but no trees, and water but no fish. Who am I?' "
                    "(OCEAN/PLANET): "
                )
                print()

                if riddle.lower() == "ocean":
                    print("The spirit nods. A golden staircase descends: You win! Congratulations!\n")
                else:
                    print("The mural seals behind you. Trapped in time. Game over.\n")

            else:
                print("You walk into a pressure trap. Spears spring from the floor. Game over.\n")

        else:
            print("You cling to a rope, but it breaks. You plummet into the ravine. Game over.\n")

    elif choice.lower() == "take":
        path_choice = input(
            "You take the narrow ledge. The wind howls, but you make it safely. "
            "At the far end lies a sealed temple door and a stone sundial. "
            "Do you PRESS the door carvings or INSPECT the sundial? (PRESS/INSPECT): "
        )
        print()

        if path_choice.lower() == "press":
            print(
                "The door rumbles open, revealing a chamber of glittering artifacts. "
                "But the air grows thin, and you are locked inside. Game over.\n"
            )
        else:
            print(
                "A beam of sunlight triggers a hidden platform to rise from the ground, "
                "leading to a crystal compass. The temple doors open in welcome: "
                "You win! Congratulations!\n"
            )
    else:
        valid_choice = 0
# MACHETE Path
elif game.lower() == "machete":
    choice_marche = input(
        "You slash through the brush. A jaguar leaps into your path, growling low. "
        "Do you FIGHT or CLIMB a nearby tree? (FIGHT/CLIMB): "
    )
    print()

    if choice_marche.lower() == "fight":
        response = input(
            "You fend it off, bleeding but alive. Deeper in the jungle, you reach "
            "two temple entrances: one marked with a SUN, the other with a MOON. "
            "Which do you take? (SUN/MOON): "
        )
        print()

        if response.lower() == "sun":
            print(
                "The chamber glows with gold, but as you step forward, "
                "the heat rises and a fire trap ignites. Game over.\n"
            )

        elif response.lower() == "moon":
            action_moon = input(
                "A gentle glow leads you into a quiet chamber with three ancient artifacts:\n"
                "1. A glowing ORB of starlight\n"
                "2. A weathered SCROLL with strange symbols\n"
                "3. A ceremonial DAGGER encrusted with gems\n"
                "Which do you examine? (ORB/SCROLL/DAGGER): "
            )
            print()

            if action_moon.lower() == "orb":
                print(
                    "Your mind floods with visions of ancient knowledge. "
                    "You leave the temple wiser and honored: You win! Congratulations!\n"
                )
            elif action_moon.lower() == "scroll":
                decipher = input(
                    "The symbols begin to move and form a question: "
                    "'What walks on four legs at dawn, two at noon, and three at twilight?' "
                    "Do you answer HUMAN or SPHINX? (HUMAN/SPHINX): "
                )
                print()
                if decipher.lower() == "human":
                    print("The scroll glows brightly and reveals a hidden passage to the temple's treasure. You win!\n")
                else:
                    print("The scroll disintegrates in your hands. The chamber walls begin to close in. Game over.\n")
            elif action_moon.lower() == "dagger":
                print(
                    "As you pick up the dagger, ghostly warriors materialize around you. "
                    "They consider this act of greed unforgivable. Game over.\n"
                )
            else:
                print("Indecision paralyzes you. The chamber doors seal shut. Game over.\n")

    elif choice_marche.lower() == "climb":
        response_climb = input(
            "From the tree, you spot a campfire in the distance. "
            "Do you APPROACH the hidden tribal camp or SNEAK past? (APPROACH/SNEAK): "
        )
        print()

        if response_climb.lower() == "approach":
            response_approach = input(
                "The tribe welcomes you. The elder offers a final challenge: "
                "'In our temple, one hallway leads to truth, the other to illusion. "
                "The guard before them always lies or tells the truth, but you don't know which. "
                "Do you ASK which door the other guard would say leads to illusion, "
                "or choose RANDOMLY?' (ASK/RANDOM): "
            )
            print()

            if response_approach.lower() == "ask":
                print("You solve the puzzle and choose the correct path. You win!\n")
            else:
                print("You walk into endless mirrored halls. Game over.\n")

        elif response_climb.lower() == "sneak":
            print("You avoid the camp but consistent with earlier pit of spikes. Game over.\n")
    else:
        valid_choice = 0

# Invalid Input
if not valid_choice:
    print("\nInvalid response! Please restart and choose a correct option.")
else:
    print("\nThanks for playing!")
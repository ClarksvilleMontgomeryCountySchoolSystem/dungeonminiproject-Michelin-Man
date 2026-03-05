torch_lit = False
if not torch_lit:
    outcome = "Doom: You wake up on a cold, hard, and uncomfortably moist floor... 'Rocky' you say.\n The cave has no light and you're in complete darkness.\n You Scramble around for items; you're feeling around on the floor and \nwalls of the cave, searching for something--anything.\n"
else:
    outcome = "Flicker: You wake up on a cold, hard, and uncomfortably moist floor... 'Rocky' you say. You see a torch just a couple of feet away from you.\n You light your torch with a some rocks you found on the cave floor--you look around."
print(outcome)
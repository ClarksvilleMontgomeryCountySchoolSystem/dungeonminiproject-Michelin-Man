print("You find a key on the ground and are now looking for the door.\n After scrambling for a bit you find a door with a lock,\n and it may or may not be the lock to your key.\n")
has_key = True
if has_key:
    outcome = "Click: 'The key works!' you shout in excitment, feeling the relif from the \ninitial fear after waking up. You walk through the door.\n"
else:
    outcome = "Doom: 'Crap' you say. What to do now?\n"
print(outcome)
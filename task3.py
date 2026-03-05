print("You walk down the corridoor and see a guard, you can't see his eyes.\n You move dangerously close to see if he is awake and looking at you or if he's asleep\n")
guard_awake = True
if not guard_awake:
    outcome = "shadow: You sneak past the guard steathily as he sleeps. You move through the hall and come across a drawbridge."
else:
    outcome = "Doom: The guard spots you and yells. He sprints \ntowards you with his knife in hand, you engage in a fight with 'Bill: The Random Cave Guard'.\n You come out of the fight, Bill does not. Your clothes are bloody and red, pain flourishes through your body.\n"
print(outcome)
#you have to keep on creating events until the loop is over and you get the final answer
# #uses a loop to reset the players state and multiple "events" that must be solved to bne answer
import time
def start_day():
    print("\n--- A New Day Begins ---")
    print("You wake up in a strange room. A clock on the wall reads 8:00 AM.")
    print("You have a strange feeling that you have been there before.")
    print("---------------")

def event_breakfast(choice):
    print("\nYou head to the kitchen for breakfast.")
    if choice == "1":
        print ("You eat a piece of toast. It tastes . . . familiar")
        return True
    elif choice == "2":
        print("\nYou decide not to eat. Your stomach begins to growl.")
        return False
    else:
        print("\nYou wander aimlessly and trip over a chair")
        return False
    
def event_the_door(choice):
    print("nYou approach the heavy wooden door.")
    if choice == "1":
        print ("You try to open the door, but it is locked tight.")
        return "locked"
    elif choice == "2":
        print ("You look for a key on the side table.")
        return "key_found"
    else:
        print("You stare at the door until your eyes hurt.")
        return "nothing"
    
def main__game():
    loop_count = 0
    broken_loop = False
    print("WELCOME TO THE TIME LOOP SIMULATOR")
    print("Goal:Find the hidden key and unlock the door to break the cycle")
    #Resetting player state for the new loop
    has_key = False
    has_eaten = False

    # --- STEP 1: THE KITCHEN ---
    print ("\What do you wants first?")
    print("1. Eat breakfast")
    print("2. Skip breakfast")
    breakfast_choice = input("> ")
    if breakfast_choice == "1":
        has_eaten = True
        print("You feel energized.")
    else:
        print("You feel weak.")

    # --- STEP 2: THE SEARCH ---
    print("\nNow, where do you go?")
    print("1. Go to the door")
    print("2. Search the side table")
    search_choice = input("> ")
    if search_choice == "2":
        print("You found a small silver key!")
        has_key = True
    elif search_choice == "1":
        print("You walk straight to the door")
    else:
        print("You sit on the floor and wait")

    # --- STEP 3: THE CLIMAX ---
    print("\nYou are standing by the door. What is your move?")
    print("1. Try to open the door")
    print("2. Go back to the kitchen")
    door_choice = input("> ")
    if door_choice == "1":
        if has_key:
            print("\nYou insert the silver key into the lock . . .")
            time.sleep(1)
            print("CLICK. The door swings open!")
            print("Light floods the room. The loop is broken!")
            broken_loop = True
    else:
        print("\nThe door is locked. You need a key.")
        print("Suddenly, a loud chime sounds. Everything goes black.")
        time.sleep(2)
        print("\n[TIME RESSETING . . .]")
        
    
        print("\nYou walk back to the kitchen,but the room feels empty.")
        print("Suddenly, a loud chime sounds.Everything goes black.")
    time.sleep(2)
    print("\n[TIME RESSETING. . .]")
print("\nCONGRATULATIONS! You escaped the loop after {loop_count = 0} tries")
#Run the game
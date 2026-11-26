# Be Alive: One Bee's Life Cycle
# A choose-your-own-adventure game where you play a honeybee.
# Goal: bring Orchard Pollen back to the Queen's Chamber so the hive
# survives the winter.
#
# Each location in the game is its own function. A location function
# shows its description, asks which way to go, and then calls the
# function for the next location.
 
 
# ************************************
# My functions
# ************************************
 
def get_choice():
    """
    Parameter: none
    Return: string, either "left" or "right"
    What the function does: asks the player which way to go and keeps
    asking until they give a valid answer.
    """
    choice = input("Which way do you go, left or right? ").strip().lower()
    while choice != "left" and choice != "right":
        print("Please type left or right.")
        choice = input("Which way do you go, left or right? ").strip().lower()
    return choice
 
 
def choose_path(history, location_name):
    """
    Parameters: list of strings, the history so far; string, the name
    of the location the player is in
    Return: string, either "left" or "right"
    What the function does: asks the player which way to go and records
    the location and the choice in the history.
    """
    choice = get_choice()
    history.append(location_name)
    history.append("(" + choice + ")")
    print()
    return choice
 
 
def orchard_pollen(has_pollen):
    """
    Parameter: boolean, whether the player is already carrying pollen
    Return: boolean, whether the player is carrying pollen now
    What the function does: handles the player's interaction with the
    pollen in the Old Orchard, letting them pack some if they do not
    have any yet.
    """
    if has_pollen:
        print("Your legs are already full of pollen.")
        return True
 
    answer = input("Do you want to pack pollen onto your legs? "
                   "(yes/no) ").strip().lower()
    while answer != "yes" and answer != "no":
        print("Please type yes or no.")
        answer = input("Do you want to pack pollen onto your legs? "
                       "(yes/no) ").strip().lower()
 
    if answer == "yes":
        print("You pack your legs full of golden pollen.")
        return True
    print("You leave the pollen behind.")
    return False
 
 
def print_history(history):
    """
    Parameter: list of strings, the locations and choices in order
    Return: nothing
    What the function does: prints the path the player took through
    the game from start to finish.
    """
    print()
    print("Your journey:")
    print(" -> ".join(history))
 
 
def end_game(history, location_name, won):
    """
    Parameters: list of strings, the history so far; string, the name
    of the ending location; boolean, whether the player won
    Return: nothing
    What the function does: finishes the game by recording the ending
    in the history and printing the whole journey.
    """
    history.append(location_name)
    if won:
        print("YOU WIN!")
        history.append("YOU WIN!")
    else:
        print("YOU LOSE!")
        history.append("YOU LOSE!")
    print_history(history)
 
 
# ---------------------------------------------------------------
# Location functions
# ---------------------------------------------------------------
 
def larva_cell(history):
    """
    Parameter: list of strings, the history so far
    Return: nothing
    What the function does: runs the starting location, then sends the
    player to the Pupa Chamber or Tainted Pollen.
    """
    print("--- Larva Cell ---")
    print("You are a tiny white grub in a wax cell. "
          "Nurse bees are bringing food.")
    choice = choose_path(history, "Larva Cell")
    if choice == "left":
        pupa_chamber(history)
    else:
        tainted_pollen(history)
 
 
def pupa_chamber(history):
    """
    Parameter: list of strings, the history so far
    Return: nothing
    What the function does: runs the Pupa Chamber, then sends the
    player to the Hive Entrance or the Wasp Raid.
    """
    print("--- Pupa Chamber ---")
    print("You are sealed in wax, changing. Wings and legs are forming. "
          "Something rattles the comb.")
    choice = choose_path(history, "Pupa Chamber")
    if choice == "left":
        hive_entrance(history)
    else:
        wasp_raid(history)
 
 
def tainted_pollen(history):
    """
    Parameter: list of strings, the history so far
    Return: nothing
    What the function does: runs the pesticide ending, which is a loss.
    """
    print("--- Tainted Pollen ---")
    print("The pollen smells sweet but strange. It has been sprayed "
          "with pesticide. Your body shuts down.")
    end_game(history, "Tainted Pollen", False)
 
 
def hive_entrance(history):
    """
    Parameter: list of strings, the history so far
    Return: nothing
    What the function does: runs the Hive Entrance, then sends the
    player to the Wildflower Meadow (without pollen) or the Polluted
    Pond.
    """
    print("--- Hive Entrance ---")
    print("You chew out into the light. You are an adult now, and the "
          "world is huge and bright.")
    choice = choose_path(history, "Hive Entrance")
    if choice == "left":
        wildflower_meadow(history, False)
    else:
        polluted_pond(history)
 
 
def wildflower_meadow(history, has_pollen):
    """
    Parameters: list of strings, the history so far; boolean, whether
    the player is carrying pollen
    Return: nothing
    What the function does: runs the Wildflower Meadow, then sends the
    player to the Old Orchard or the Queen's Chamber.
    """
    print("--- Wildflower Meadow ---")
    print("Clover and lavender as far as you can see. "
          "The air hums with other bees.")
    choice = choose_path(history, "Wildflower Meadow")
    if choice == "left":
        old_orchard(history, has_pollen)
    else:
        queens_chamber(history, has_pollen)
 
 
def polluted_pond(history):
    """
    Parameter: list of strings, the history so far
    Return: nothing
    What the function does: runs the water contamination ending, which
    is a loss.
    """
    print("--- Polluted Pond ---")
    print("The water has a rainbow sheen. You take a sip. "
          "You are poisoned.")
    end_game(history, "Polluted Pond", False)
 
 
def old_orchard(history, has_pollen):
    """
    Parameters: list of strings, the history so far; boolean, whether
    the player is carrying pollen
    Return: nothing
    What the function does: runs the Old Orchard, where the player can
    pick up pollen, then sends them to the Mowed Lawn or back to the
    Wildflower Meadow.
    """
    print("--- Old Orchard ---")
    print("Apple blossoms hang heavy with pollen.")
    has_pollen = orchard_pollen(has_pollen)
    choice = choose_path(history, "Old Orchard")
    if choice == "left":
        mowed_lawn(history)
    else:
        wildflower_meadow(history, has_pollen)
 
 
def mowed_lawn(history):
    """
    Parameter: list of strings, the history so far
    Return: nothing
    What the function does: runs the habitat destruction ending, which
    is a loss.
    """
    print("--- Mowed Lawn ---")
    print("Flat green grass with no flowers in sight. There is nothing "
          "to eat, and you run out of energy.")
    end_game(history, "Mowed Lawn", False)
 
 
def wasp_raid(history):
    """
    Parameter: list of strings, the history so far
    Return: nothing
    What the function does: runs the predator ending, which is a loss.
    """
    print("--- Wasp Raid ---")
    print("A wasp tears into the comb. You never emerge.")
    end_game(history, "Wasp Raid", False)
 
 
def queens_chamber(history, has_pollen):
    """
    Parameters: list of strings, the history so far; boolean, whether
    the player is carrying pollen
    Return: nothing
    What the function does: runs the final location, where the player
    wins if they brought pollen and loses if they did not.
    """
    print("--- Queen's Chamber ---")
    print("The hive is quiet and the Queen waits. Winter is coming.")
    if has_pollen:
        print("You deliver the pollen. The hive survives the winter!")
        end_game(history, "Queen's Chamber", True)
    else:
        print("You arrive empty-handed. The hive runs out of food.")
        end_game(history, "Queen's Chamber", False)
 
 
# *******************************
# Start the game
# *******************************
 
def play_game():
    """
    Parameter: none
    Return: nothing
    What the function does: shows the introduction and starts the game
    at the first location with an empty history.
    """
    print("=== BEE ALIVE: ONE BEE'S LIFE CYCLE ===")
    print("You are a honeybee. Bring pollen to the Queen so your hive")
    print("survives the winter. Choose your path carefully.")
    print()
    history = []
    larva_cell(history)



if __name__ == "__main__":
    play_game()
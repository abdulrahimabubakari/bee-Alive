
# Bee Alive: One Bee's Life Cycle

A text-based choose-your-own-adventure game built in Python where you play a honeybee navigating its life cycle and trying to help its hive survive the winter.

## Overview

You begin as a larva inside a honeycomb and make decisions that determine your journey. As you progress through different locations, your choices can lead to survival or environmental dangers such as pesticides, pollution, habitat destruction, and predators.

Your ultimate goal is to collect pollen from the Old Orchard and deliver it to the Queen's Chamber before winter.

## Gameplay

- Navigate the game by choosing between left and right paths.
- Explore different locations throughout a honeybee's life cycle.
- Collect pollen from the Old Orchard.
- Encounter multiple endings based on your decisions.
- Keep track of your journey and see the path you took at the end of the game.

## Locations

| Location | Description |
|---|---|
| Larva Cell | Begin your journey as a developing honeybee. |
| Pupa Chamber | Continue developing inside the hive. |
| Hive Entrance | Emerge as an adult bee and enter the outside world. |
| Wildflower Meadow | Explore a meadow filled with flowers. |
| Old Orchard | Collect pollen to help your hive survive. |
| Queen's Chamber | Deliver pollen to the Queen to win the game. |
| Tainted Pollen | Encounter pesticide-contaminated pollen. |
| Polluted Pond | Encounter contaminated water. |
| Mowed Lawn | Lose access to food after habitat destruction. |
| Wasp Raid | Encounter a predator inside the hive. |

## Winning the Game

To win, you must navigate through the hive, reach the Wildflower Meadow, visit the Old Orchard, collect pollen, return to the meadow, and make your way to the Queen's Chamber.

Arriving at the Queen's Chamber without pollen results in a loss.

## Technologies

- Python 3

## Concepts Practiced

- Functions and function calls
- Conditional statements
- While loops
- User input and input validation
- Boolean variables and state management
- Lists and list manipulation
- Passing arguments between functions
- Return values
- String formatting and output
- Branching program logic

## How to Run

1. Clone the repository:

   ```bash
   git clone https://github.com/abdulrahimabubakari/bee-alive.git
   ```

2. Navigate into the project directory:

   ```bash
   cd bee-alive
   ```

3. Run the game:

   ```bash
   python bee_alive.py
   ```

## What I Learned

This project gave me practice organizing a program into functions and using function calls to control the flow of a game. I worked with user input validation, conditional branching, and tracking the player's state as they moved between locations.

I also practiced passing information between functions, including maintaining a journey history and tracking whether the player had collected pollen.

## Future Improvements

- [ ] Add the ability to restart the game without rerunning the program.
- [ ] Expand the game with more locations and decision paths.
- [ ] Add a more detailed inventory system.
- [ ] Improve the game interface and storytelling.
- [ ] Add automated tests for different paths and endings.

---

Built as part of my Computer Science learning journey.
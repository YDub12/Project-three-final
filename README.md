# Battleships 
This Battleships game is a terminal-based implementation of the classic game on a 5x5 grid. The objective is to sink all of the opponent's ships before they sink yours. The game features a main menu for selecting between playing against the computer, local multiplayer (under development), or exiting.

[[View the live site here](https://battleshipping-a257fd2be3f9.herokuapp.com/)]
## Design
Initial design was built on hte absic game design
## Features 
* Play Against the Computer: The player battles an AI opponent. The player places ships manually, while the computer places ships randomly using "random" which has been imported at the top of the script.
* Interactive Game Board: The game shows a 5x5 grid where the player can strike at different coordinates to find and sink the opponent's ships.
* Validation for Inputs: Input prompts include error checking for ship placement, guesses, and menu selection.
* Replayability: After each game, you can return to the main menu to play again or exit. Due to the random creation of the board for the computer the game has increased replayability. 
### Features left to implement 
* Local Multiplayer: This feature is under development and will allow two players to play against each other locally.
* Enhanced AI: The computer’s strategy could be made more intelligent in future updates.
* Add a nation selector to add some variety, using historical names of ships to provide some additional flavour
## Testing 
Each step was checked and validated individually at each stage.

Validation for username field: 
![Username validation](https://raw.githubusercontent.com/YDub12/Project-three-final/refs/heads/main/assets/images/username%20validation.PNG)

Game type:

![Game type Validation](https://raw.githubusercontent.com/YDub12/Project-three-final/refs/heads/main/assets/images/Game%20type%20validation.PNG)

Row and columns checked:

![Row validation](https://raw.githubusercontent.com/YDub12/Project-three-final/refs/heads/main/assets/images/Corrected%20validation.PNG)

![Column validation](https://raw.githubusercontent.com/YDub12/Project-three-final/refs/heads/main/assets/images/Column%20validation.PNG)

User hit and miss and already guessed:

![User hit](https://raw.githubusercontent.com/YDub12/Project-three-final/refs/heads/main/assets/images/User%20guess%20hit.PNG)

![User miss](https://raw.githubusercontent.com/YDub12/Project-three-final/refs/heads/main/assets/images/User%20guess%20miss.PNG)

![User duplication](https://raw.githubusercontent.com/YDub12/Project-three-final/refs/heads/main/assets/images/Already%20guessed.PNG)


## Deployment 

## Credits 


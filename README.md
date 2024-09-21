# Battleships 
This Battleships game is a terminal-based implementation of the classic game on a 5x5 grid. The objective is to sink all of the opponent's ships before they sink yours. The game features a main menu for selecting between playing against the computer, local multiplayer (under development), or exiting.

[[View the live site here](https://battleshipping-a257fd2be3f9.herokuapp.com/)]
## Design
Initial design was built on hthe basic game design and mapped out roughly here 

![Process map](https://raw.githubusercontent.com/YDub12/Project-three-final/refs/heads/main/assets/images/Process%20map%20-%20version%201.PNG)

Each function was then built and tested against a main function
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

Victory messages:

![User win](https://raw.githubusercontent.com/YDub12/Project-three-final/refs/heads/main/assets/images/Victory%20message%20-%20player.PNG)

![Computer win](https://raw.githubusercontent.com/YDub12/Project-three-final/refs/heads/main/assets/images/Victory%20message%20-%20computer.PNG)
## Deployment 
1. Log in to Heroku
2. On the main page click "New" and select "Create new app"
3. Choose your unique app name and select your region
4. Click "Create app"
5. On the next page find "settings" and locate "Config Vars"
6. Scroll down, locate "Buildpack" and click "Add", select "Python"
7. Repeat step 6. only this time add "Node.js", make sure "Python" is first
8. Scroll to the top and select "Deploy" tab
9. Select GitHub as deployment method and search for your repository and link them together
10. Scroll down and select either "Enable Automatic Deploys" or "Manual Deploy"
11. Deployed site here [Battleshipping](https://raw.githubusercontent.com/YDub12/Project-three-final/refs/heads/main/assets/images/Process%20map%20-%20version%201.PNG)

## Credits

Milton Bradley's 1967 release of battleship the game 

The "Random" import in Python

## Content 
All code was written by the developer
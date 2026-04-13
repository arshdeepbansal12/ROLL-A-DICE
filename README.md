🎲 Game of Luck: Dice Simulator
A simple, interactive command-line interface (CLI) game built with Python. This project simulates a 6-sided dice roll, allowing users to test their luck repeatedly through a menu-driven interface.

📝 Description
The Game of Luck provides a digital way to roll a die. It features a continuous loop that keeps the game running until the user chooses to exit, handling basic input validation to ensure a smooth user experience.

📂 Project Structure
The project is organized into three main Python files to maintain clean code and separation of concerns:

main.py: The entry point of the application. It handles the user interface, input loops, and coordinates the game logic.

dice.py: Contains the logic for generating a random number between 1 and 6.

exit.py: Contains the closing sequence and credits for the game.

🚀 How to Run
Prerequisites: Ensure you have Python installed on your system.

Download: Save main.py, dice.py, and exit.py in the same folder.

Execute: Open your terminal or command prompt, navigate to the folder, and run:

Bash
python main.py
🎮 How to Play
Upon starting the game, you will be presented with a menu:

Press [1]: To roll the dice and see your lucky number.

Press [2]: To exit the game.

Invalid Input: If you press any other key, the game will notify you and prompt you to try again.

🛠️ Features
Modular Code: Logic is split across multiple files for better readability.

Randomization: Uses the random module to ensure unbiased dice rolls.

Infinite Loop: Allows for multiple rolls in a single session without restarting the script.

Input Validation: Prevents the program from crashing if an unrecognized number is entered.

👨‍💻 Author
Arshdeep Singh

# HANGMAN with interface in Python 3

## Game Overview

**HANGMAN** is a classic word-guessing game where a **host** provides a word and a hint, and a **player** attempts to guess the word by selecting letters. The game continues until the player either correctly guesses the word or makes too many incorrect guesses, leading to a loss.

## Game Objective

- The **host** inputs a secret word and a hint.
- The **player** must guess the word by selecting letters.
- If the player guesses all letters correctly before reaching six mistakes, they **win**.
- If the player makes six incorrect guesses, the **host wins**.

---

## How to Play

### 1. **Word Input (Host Role)**
   - The host enters a word (1-10 characters long).
   - A warning appears if the word length is invalid.
   - Clicking **"Proceed"** moves to the next phase.

### 2. **Hint Input (Host Role)**
   - The host provides a hint (1-40 characters long) to help the player.
   - Clicking **"Proceed"** moves to the verification phase.

### 3. **Verification Phase**
   - The host reviews the chosen word and hint.
   - Clicking **"Proceed"** starts the game.
   - Clicking **"Edit"** returns to the word entry phase.

### 4. **Gameplay (Player Role)**
   - The player clicks on letters to guess the word.
   - Correct guesses reveal letters.
   - Incorrect guesses increase the **hangman drawing**.
   - The game ends when:
     - The word is fully guessed (**Player wins**).
     - The hangman is fully drawn (**Host wins**).

---

## Controls & Interaction

### **Keyboard Inputs**
- **Backspace:** Remove the last character during word/hint entry.
- **Any Letter Key:** Add a letter to the input during word/hint entry.

### **Mouse Inputs**
- **Click "Proceed" Button:** Move to the next phase.
- **Click "Edit" Button:** Return to word entry for modifications.
- **Click a Letter (During Gameplay):** Make a guess.

---

## Winning & Losing Conditions

### **Player Win Condition**
- The player correctly guesses **all letters in the word**.
- A **"PLAYER WON!"** message is displayed.

### **Host Win Condition**
- The player makes **six incorrect guesses**.
- A **"HOST WON!"** message is displayed along with the correct word.

## Code Explanation

### Constants & Initialization
- The game screen is set to **1000x700 pixels**.
- Fonts, colors, and button properties are initialized.
- **Hangman images** are loaded from `man1.png` to `man7.png`.

### Main Functions

#### `init_game()`
- Resets the game state, initializing word, hint, guessed letters, and hangman progress.

#### `draw_buttons()`
- Renders the **Proceed** and **Edit** buttons.

#### `draw()`
- Updates the screen based on the current phase (word entry, hint entry, verification, or gameplay).
- Displays text input fields, buttons, and the hangman image.

#### **Event Handling**
- Captures **mouse clicks** for button interactions.
- Captures **keyboard inputs** for text entry.

---

## Dependencies

This project requires **Python 3** and **Pygame**.

### Installing Dependencies

Ensure you have **Python** installed. If Pygame is missing, install it using:

```bash
pip install pygame
```

### Files Used

- `main.py` → The core game script.
- `man1.png` to `man7.png` → Hangman images for different incorrect attempts.

---

## Code Flow Overview

1. **Game Initialization (`init_game`)**
   - Sets up variables like `word`, `hint`, `guessed`, and `hangman` counter.
   - Defines letter positions on the screen.

2. **Game Loop (`while run`)**
   - Calls `draw()` every frame to update the screen.
   - Handles **keyboard inputs** for text entry.
   - Handles **mouse clicks** for guessing letters or proceeding through phases.

3. **Drawing Functions**
   - `draw_buttons()`: Renders interactive buttons.
   - `draw()`: Updates game UI depending on phase.

4. **Win/Loss Handling**
   - **Player wins** when all letters are correctly guessed.
   - **Host wins** if six incorrect guesses are made (full hangman drawn).


---

## Screenshots

1. Starting interface
   ![Image](https://github.com/user-attachments/assets/b99b28f3-640e-40d6-b1a0-b594b2f869d6)
2. The host writes a word and proceed
   ![Image](https://github.com/user-attachments/assets/5fbd1495-5a08-4817-8cfa-a1938ebe72a4)
3. The host then writes a hint and proceeds
   ![Image](https://github.com/user-attachments/assets/a80d57ff-a303-4e6b-ba43-02d11f9a1e98)
4. The host is then asked to verify if the word and hint is right. Host can either edit by clicking edit or just proceed
   ![Image](https://github.com/user-attachments/assets/61a276b2-9c11-4437-89e3-a1c131d85ad1)
5. Now it's the player's turn to guess the word
   ![Image](https://github.com/user-attachments/assets/0a82da44-2890-4618-b064-ced50cffe3cf)
6. Either the player looses and host wins
   ![Image](https://github.com/user-attachments/assets/157f95eb-843f-47f3-a2de-7f790a978bb4)
   ![Image](https://github.com/user-attachments/assets/b6e1b181-98c5-4033-b5af-49c627a9c8d1)
7. Or the player wins by guessing all letters correctly:
   ![Image](https://github.com/user-attachments/assets/b272d90c-679e-4e6a-831b-15e973f2cf2f)

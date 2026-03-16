# 🎮 Game Glitch Investigator: The Impossible Guesser

## 🚨 The Situation

You asked an AI to build a simple "Number Guessing Game" using Streamlit.
It wrote the code, ran away, and now the game is unplayable. 

- You can't win.
- The hints lie to you.
- The secret number seems to have commitment issues.

## 🛠️ Setup

1. Install dependencies: `pip install -r requirements.txt`
2. Run the broken app: `python -m streamlit run app.py`

## 🕵️‍♂️ Your Mission

1. **Play the game.** Open the "Developer Debug Info" tab in the app to see the secret number. Try to win.
2. **Find the State Bug.** Why does the secret number change every time you click "Submit"? Ask ChatGPT: *"How do I keep a variable from resetting in Streamlit when I click a button?"*
3. **Fix the Logic.** The hints ("Higher/Lower") are wrong. Fix them.
4. **Refactor & Test.** - Move the logic into `logic_utils.py`.
   - Run `pytest` in your terminal.
   - Keep fixing until all tests pass!

## 📝 Document Your Experience

- [ The Purpose of the game is for the User to guess the number the computer generated from a range given by the difficulty] Describe the game's purpose.
- [Bugs I found include hint system not working properly, secret being stored as a string sometimes, and the range of secret not changing when difficulty changes] Detail which bugs you found.
- [ Firstly, we changed the wording using AI so that hint system is no longer misleading. Then we changed a specific line that changed the secret from containing default range to the range given by difficulty. Finally, we typecasted the secret in all cases so that it is always an int, so no comparison errors occur] Explain what fixes you applied.

## 📸 Demo

- [ ![alt text](image.png)] [Insert a screenshot of your fixed, winning game here]

## 🚀 Stretch Features

- [ ] [If you choose to complete Challenge 4, insert a screenshot of your Enhanced Game UI here]
![alt text](image-1.png) For Challenge 1: Advanced Edge-Case Testing
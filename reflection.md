# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the secret number kept changing" or "the hints were backwards").

When I first ran the game with the intent as a player following the proper rules, the game itself worked. However, the hint logic system is Horrible! 90% of the time, it kept on saying go lower, even when the guess was under the target. Another bug was that we users could input any number(even decimals!) into the guess, there was no range restriction at all. This in turn caused some huge issues toward the attempts, where we bleeded into the negatives whenevers the user spams the guess button or puts in wrongs values. Sometimes the secret is stored as a string, which leads to weird comparisons and its range never changes from 1 to 100.
---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

I mainly used Copliot for this project and I was pleasently surprised. One correct example of AI suggestion was the logic behind why the range of secret was fixed between 0 and 100. The issue was a line which used the default range instead of the updated range which the AI suggested to fix. I verified by running the app and spamming new game in each section to see if the range is proper, and it was! One example AI failed on its own was the hints logic of the words which said to go higher or lower, it mixed them up, maybe because they were strings, but I give it some more clarificaton and it finally fixed the issue. I also ran the pytests for this method and ran the app itself and the method once again worked.
---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

I decided how a bug was fixed by looking at both pytest and manually looking through the app itself. One test using pytest was to check if the hints and the operators works as intended. When I ran pytest, I actually got a terminal error which with the help of copilot I fixed and when I ran the pytest, it came back as all passed! This showed that my code has the right logic for the game and that I was done fixing the bug. The AI helped me design test cases by checking each possible outcome(which in this case there were 3 for hints) and writing tests for each scenario. As such, I got full coverage of the method's scope.
---

## 4. What did you learn about Streamlit and state?

- In your own words, explain why the secret number kept changing in the original app.
- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
- What change did you make that finally gave the game a stable secret number?

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.

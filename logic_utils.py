
# FIX: Refactored logic into logic_utils.py using Copilot Agent mode
def get_range_for_difficulty(difficulty: str):
    """Return (low, high) inclusive range for a given difficulty."""
    if difficulty == "Easy":
        return 1, 20
    if difficulty == "Normal":
        return 1, 100
    # FIXME: For "Hard", hard difficulty is easier than normal difficulty.
    # FIX: For "Hard", we intentionally return a wider range to increase difficulty.
    if difficulty == "Hard":
        return 1, 1000
    return 1, 100


def parse_guess(raw: str):
    """
    Parse user input into an int guess.

    Returns: (ok: bool, guess_int: int | None, error_message: str | None)
    """
    if raw is None:
        return False, None, "Enter a guess."

    if raw == "":
        return False, None, "Enter a guess."

    try:
        if "." in raw:
            value = int(float(raw))
        else:
            value = int(raw)
    except Exception:
        return False, None, "That is not a number."

    return True, value, None


def check_guess(guess, secret):
    """
    Compare guess to secret and return (outcome, message).

    outcome examples: "Win", "Too High", "Too Low"
    """
    if guess == secret:
        return "Win", "🎉 Correct!"
        # FIXME: Hint is misleading saying too high and to go higher/too low and to go lower
    try:  # FIX: If Guess is higher than secret then the hint must be lower and vice versa, but if they are of different types we will just compare them as strings and ignore the glitchy behavior for hints
        if guess > secret:
            return "Too High", " 📉Go LOWER!"
        else:
            return "Too Low", " 📈Go HIGHER!"
    # FIXME: If types are different, we should compare as Ints
    # FIX: Changed both guess and secret to ints to ensure that we are comparing the actual values and not just the string representations, which can lead to incorrect hints.
    except TypeError:
        g = int(guess)
        if g == int(secret):
            return "Win", "🎉 Correct!"
        if g > int(secret):
            return "Too High", "📉 Go LOWER!"
        return "Too Low", "📈 Go HIGHER!"


def update_score(current_score: int, outcome: str, attempt_number: int):
    """Update score based on outcome and attempt number."""
    if outcome == "Win":
        points = 100 - 10 * (attempt_number + 1)
        if points < 10:
            points = 10
        return current_score + points

    if outcome == "Too High":
        if attempt_number % 2 == 0:
            return current_score + 5
        return current_score - 5

    if outcome == "Too Low":
        return current_score - 5

    return current_score

from logic_utils import check_guess

# FIX: Refactored logic into logic_utils.py using Copilot Agent mode, so we can now directly import and test the check_guess function without needing to run the full Streamlit app.


def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win and message should indicate correctness
    outcome, message = check_guess(50, 50)
    assert outcome == "Win"
    assert "correct" in message.lower()


def test_guess_too_high():
    # If secret is 50 and guess is 60, outcome should be "Too High" and hint should tell player to go lower
    outcome, message = check_guess(60, 50)
    assert outcome == "Too High"
    assert "lower" in message.lower() or "go lower" in message.lower()


def test_guess_too_low():
    # If secret is 50 and guess is 40, outcome should be "Too Low" and hint should tell player to go higher
    outcome, message = check_guess(40, 50)
    assert outcome == "Too Low"
    assert "higher" in message.lower() or "go higher" in message.lower()

def rock_paper_scissors(number):
    if number < 0  or number > 2:
        raise ValueError("Must be between 0 and 2")
    if number == 0:
        return "rock"
    if number == 1:
        return "paper"
    if number == 2:
        return "scissors"
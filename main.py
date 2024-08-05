# Defining scenarios
scenarios = [
    {
        "scenario": "You are lost in a forest and come across a fork in the path. Which way do you go?",
        "choices": [
            {"choice": "Left", "outcome": "You find a hidden treasure! You win!"},
            {
                "choice": "Right",
                "outcome": "You encounter a group of wolves. Game over.",
            },
        ],
    },
    {
        "scenario": "You are stranded on a desert island and find a boat. Do you try to repair it or build a raft?",
        "choices": [
            {
                "choice": "Repair the boat",
                "outcome": "You successfully repair the boat and escape the island. You win!",
            },
            {
                "choice": "Build a raft",
                "outcome": "The raft collapses during construction. Game over.",
            },
        ],
    },
    {
        "scenario": "You are in a haunted house and hear a noise. Do you investigate or run away?",
        "choices": [
            {
                "choice": "Investigate",
                "outcome": "You find a valuable artifact. You win!",
            },
            {"choice": "Run away", "outcome": "You are caught by a ghost. Game over."},
        ],
    },
    {
        "scenario": "You are in a room with two doors. One is labeled 'Danger' and the other is labeled 'Safety'. Which door do you choose?",
        "choices": [
            {
                "choice": "Danger",
                "outcome": "You find a treasure chest full of gold. You win!",
            },
            {"choice": "Safety", "outcome": "The room was a trap. Game over."},
        ],
    },
]

import random


def get_scenario():
    return random.choice(scenarios)


def present_choices(scenario):
    print(scenario["scenario"])
    for i, choice in enumerate(scenario["choices"], start=1):
        print(f"{i}. {choice['choice']}")


def get_player_choice(scenario):
    while True:
        try:
            choice = int(input("Enter the number of your choice: "))
            if choice < 1 or choice > len(scenario["choices"]):
                raise ValueError
            return choice
        except ValueError:
            print(
                "Invalid input. Please enter a number corresponding to one of the choices."
            )


def get_outcome(scenario, choice):
    outcome = scenario["choices"][choice - 1]["outcome"]
    if "You win!" in outcome:
        score = 1
    elif "Game over." in outcome:
        score = -1
    else:
        score = 0
    return outcome, score


def main():
    score = 0
    while True:
        scenario = get_scenario()
        present_choices(scenario)
        choice = get_player_choice(scenario)
        outcome, outcome_score = get_outcome(scenario, choice)
        score += outcome_score
        print(outcome)
        print(f"Your current score is: {score}")
        play_again = input("Play again? (y/n) ")
        if play_again.lower() != "y":
            break

        import json


def save_game(scenario, choice, score):
    game_state = {"scenario": scenario, "choice": choice, "score": score}
    with open("game_save.json", "w") as f:
        json.dump(game_state, f)


if __name__ == "__main__":
    main()

# The problem is that we have two functions named get_outcome. The second one overwrites the first one.

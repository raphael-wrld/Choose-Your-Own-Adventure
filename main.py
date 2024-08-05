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
]
import random


def get_scenario():
    return random.choice(scenarios)


def present_choices(scenario):
    print(scenario["scenario"])
    for i, choice in enumerate(scenario["choices"]):
        print(f"{i+1}. {choice['choice']}")


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
    return scenario["choices"][choice - 1]["outcome"]


def main():
    while True:
        scenario = get_scenario()
        present_choices(scenario)
        choice = get_player_choice(scenario)
        outcome = get_outcome(scenario, choice)
        print(outcome)
        play_again = input("Play again? (y/n) ")
        if play_again.lower() != "y":
            break

import random
import time


def get_range(difficulty):
    if difficulty == "easy":
        return 1, 50, 10
    elif difficulty == "medium":
        return 1, 100, 15
    elif difficulty == "hard":
        return 1, 200, 20
    else:
        return 1, 100, 15  # Default to medium difficulty if input is invalid


def calculate_score(max_guesses, guesses_taken):
    # Calculate the player's score based on guesses and time
    max_score = 1000
    min_score = 100
    time_penalty = 5  # Deduct 5 points for each second taken

    # Calculate the time taken for the current game
    end_time = time.time()
    time_taken = int(end_time - start_time)

    if guesses_taken <= max_guesses:
        score = max_score - (guesses_taken * 10) - (time_penalty * time_taken)
        return max(min_score, score)  # Ensure score is at least min_score
    else:
        return min_score  # Player exceeded max_guesses, earning minimum score


def play_game(min_number, max_number, max_guesses):
    # Generate a random number within the specified range
    random_number = random.randint(min_number, max_number)

    # Initialize the number of guesses for the current game
    guesses = 0

    # Start a timer
    global start_time  # Define start_time as a global variable
    start_time = time.time()

    # Start the game loop
    while guesses < max_guesses:
        # Prompt the player to enter a guess
        player_input = input(f"Guess the number between {min_number} and {max_number} "
                             f"(You have {max_guesses - guesses} guesses left): ")

        # Input validation
        if not player_input.isdigit():
            print("Invalid input. Please enter a valid number.")
            continue

        player_guess = int(player_input)

        # Check if the player's guess is within the valid range
        if player_guess < min_number or player_guess > max_number:
            print(f"Your guess should be between {min_number} and {max_number}. Try again.")
            continue

        # Increment the number of guesses for the current game
        guesses += 1

        # Check if the player's guess is correct
        if player_guess == random_number:
            end_time = time.time()
            time_taken = int(end_time - start_time)
            print(f"Congratulations! You guessed the correct number in {guesses} guesses "
                  f"and {time_taken} seconds.")

            # Calculate and display the player's score
            score = calculate_score(max_guesses, guesses)
            print(f"Your score: {score}")
            return True, score  # Player wins the game and earns a score
        elif player_guess < random_number:
            print("Your guess is too low. Try again.")
        else:
            print("Your guess is too high. Try again.")

    # Player ran out of guesses
    print(f"Sorry, you've run out of guesses. The correct number was {random_number}.")
    return False, 0  # Player loses the game and earns a score of 0


# Main game loop
total_games = 0
total_wins = 0
highest_scores = {"easy": 0, "medium": 0, "hard": 0}  # Dictionary to store highest scores

print("Welcome to the Number Guessing Game!")
print("Instructions:")
print("- You will choose a difficulty level: easy, medium, or hard.")
print("- You will have a limited number of guesses to guess the correct number.")
print("- Try to guess the correct number as quickly as possible to earn a higher score.")
print("- You can view your highest scores, reset them, or quit the game at any time.")

while True:
    print("\nOptions:")
    print("1. Play a game")
    print("2. View highest scores")
    print("3. Reset highest scores")
    print("4. Quit")

    option = input("Enter your choice (1/2/3/4): ")

    if option == "1":
        difficulty = input("Choose a difficulty level (easy/medium/hard): ")

        min_number, max_number, max_guesses = get_range(
            difficulty)  # Get range and max guesses for the chosen difficulty

        won, score = play_game(min_number, max_number, max_guesses)

        if won:
            total_wins += 1

            # Check if the current score is higher than the highest score for this difficulty level
            if score > highest_scores[difficulty]:
                highest_scores[difficulty] = score

        total_games += 1

        # Calculate and display win percentage
        win_percentage = (total_wins / total_games) * 100
        print(f"Win Percentage: {win_percentage:.2f}%")

    elif option == "2":
        # Display the highest scores for each difficulty level
        print("Highest Scores:")
        for level, high_score in highest_scores.items():
            print(f"{level.capitalize()}: {high_score}")

    elif option == "3":
        # Reset highest scores for each difficulty level
        highest_scores = {"easy": 0, "medium": 0, "hard": 0}
        print("Highest scores have been reset.")

    elif option == "4":
        print("Thank you for playing! Goodbye.")
        break

    else:
        print("Invalid choice. Please select a valid option (1/2/3/4).")

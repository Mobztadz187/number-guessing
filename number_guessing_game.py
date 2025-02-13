import time
import random

def welcome():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    print("You will be given a number of chances to guess the correct number based on the difficulty level.")

def difficulty():
    print("1. Easy (5 chances)")
    print("2. Medium (3 chances)")
    print("3. Hard (1 chances)")

    
    
    while True:
        try:
            choice = input("Choose the difficulty level (1/2/3): ")
            if choice == "1":
                return 5
            elif choice == "2":
                return 3
            elif choice == "3":
                return 1
        except ValueError:
            print("Invalid choice! Please enter 1, 2, or 3.") 
            break     

def guess_game():
     return random.randint(1, 10)

def play():
    chances = difficulty()
    number = guess_game()
    attempts = 0
    start_time = time.time()

    print(f"\nGreat! You have selected the difficulty level with {chances} chances.")
    print("Let's start the game!")

    while attempts < chances:
        try:
            guess = int(input("Enter your guess: "))
        except ValueError:
            message = ["Invalid input!", "Please enter a number between 1 to 10."]
            print(message[0])
            print(message[1])
            continue

        attempts += 1

        if guess < number:
            message = [f"Incorrect!", "Your guess is greater than {guess}"]
            print(message[0])
            print(message[1])
            continue
        elif guess > number:
            message = [f"Incorrect!", "Your guess is less than{guess}"]
            print(message[0])
            print(message[1])
            continue
        else:
            end_time = time.time()
            elapsed_time = end_time - start_time
            message = [f"Congratulations! You guessed the number in {attempts} attempts.", f"Elapsed time: {elapsed_time:.2f} seconds."]
            print(message[0])
            print(message[1])
            return attempts
        
    message = [f"Sorry, you've run out of chances. The correct number was {number}."]
    print(message)
    return attempts
    
def main():
    score = { 'easy': float('inf') ,  'medium': float('inf'), 'hard': float('inf')}

    while True:
        welcome()
        attempts = play()

        if attempts <= score['easy']:               
            message = ["New high score for easy level!"]
            print(message)
            score['easy'] = attempts
        elif attempts < score['medium']:
            message = ["New high score for medium level!"]
            print(message)
            score['medium'] = attempts
        elif attempts < score['hard']:
            message = ["New high score for hard level!"]
            print(message)
            score['hard'] = attempts

        message = [f"Easy: {score['easy']} attempts", f"Medium: {score['medium']} attempts", f"Hard: {score['hard']} attempts"]
        print(message)

        play_again = input("\nDo you want to play again? (y/n): ").strip().lower()
        if play_again == "n":
            print("Thank you for playing! Goodbye!")
            break
        elif play_again == "y":
            return main()
        else:
            print("Incorrect! Choose y/n")
            break


if __name__ == "__main__":
    main()
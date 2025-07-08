import ramdom
attempts_list = []
def show_score():
    if len (attempts_list)  <=0:
        print("There is currently no high score, it yours for the taking!")
    else:
        print("The current high score is {}attempts".format(min(attempts_list)))
        def start_game():
            ramdom_number = int (random.randint(1, 10))
            print("hey there welcome to the number guessing game!")
            player_name = input("enter your name!")
            wanna_play = input("hi{} would you like to play the guessing? (enter yes/no)".format(player_name))
            attempts = 0
            while wanna_play.lower() == "yes":
                try:
                    guess = input("pick a number between 1 and 10")
                    if int(guess) <1 or int (guess)> 10:
                       raise ValueError("please guess a number within the given range")
                    if int (guess)== ramdom_number:
                        print("congarts! you guessed it right!")
                        attempts += 1
                        attempts_list.append(attempts)
                        print("it took you {} attempts".format(attempts))
                        play_again = input("would you like to play again? (enter yes/no)")
                        

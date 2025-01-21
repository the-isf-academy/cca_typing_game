from prompts import prompt_list                                 # imports prompt list from prompts.py 
from random import choice
from helpers import print_slow, calculate_wpm, calculate_accuracy, generate_prompt
from time import time

print("-"*50)
print("Welcome to the ISF Typing Game")                         # print welcome to the game
print("-"*50)

input("> Input any key to view the rules.")                     # user input any key to view rules                          

print("     1. You will see the prompt")                        # print rules
print("     2. The timer will start")
print("     3. Type the prompt as fast as you can")
print("     4. Click 'enter/return' when you are done.\n")

input("> Input any key to start the game! ")                    # user input any key to start game

print("-"*30)
print("The game will start in...")
print_slow("3...2...1!", .2)
print("-"*30,"\n")


#### 💻 COMPLETE THE TO DO ITEMS BELOW 💻 ####

# create the variable chosen_prompt and store a random prompt from  prompt_list 
chosen_prompt = choice(prompt_list)

# 💻 TO DO: print chosen_prompt


# create the variable start_time and store the current time 
start_time = time()



# create the variable user_input_prompt and store user input prompt typing attempt 
user_input_prompt = input("> ")


# 💻 TO DO :create the variable end_time and store the current time 


# create the variable total_wpm and store the return value of calculated_wpm() 
# 💻 TO DO : remove the # from the line below when you have created the end_time variable
#total_wpm = calculate_wpm(user_input_prompt, start_time, end_time)


# 💻 TO DO : create the variable total_accuracy and store the return value of calculate_accuracy() 

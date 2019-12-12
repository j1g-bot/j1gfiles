##This project is a chatbot game based solely on luck.##
##The game faces you up against a random monster, and its up to your own luck to decide whether you escape alive or not.##

character_start()
##This function asks for your name. This name is later used in the battle results.##

game_start()
## This function starts the game up and sets up the enemy to fight.##

battle()
## This function asks whether you want to fight the monster or flee from it.##
##Attacking the monster and slaying it will grant you a point.##
##Fleeing from it will give you a chance to save your points for a higher chance or survival##

player_choice()
##This function performs the random calculation whether or not you will survive or not.##
## If you surive, you earn a point. If you are slain, you lose all your points.##

try_again()
##This function allows you to try again after being slain by a monster##

cont()
##This function allows you to continue while keeping your points after slaying a monster to test your luck once more.
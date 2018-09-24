
#Menu creation and coding to call each option
import create_attributes
import player_actions
import game_actions

ca=create_attributes
pa=player_actions
ga=game_actions

main_menu={": :":"MAIN MENU : : :",1:"New Game",2:"Resume Game",3:"View Character Attributes",4:"View Class Attributes",5:"View Species Attributes",6:"Exit"}
game_menu={": :":"GAME MENU : : :",1:"Move",2:"Attack",3:"Talk",4:"Take",5:"Give",6:"Save Game",7:"Main Menu"}
hidden_menu={": :":"Congrats! Welcome to the HIDDEN MENU : : :",1:"Create Species",2:"Create Class",3:"Update Species",4:"Update Class",5:"Delete Species",6:"Delete Class",7:"Create Map",8:"Update Monster Spots"}

#Displays specified menu 
def display_menu(menu):
	for key in menu:
	    print(str(key),":",menu[key])
	print("\n")

display_menu(main_menu)
display_menu(hidden_menu)
display_menu(game_menu)

def menu_action(menu,option):
	print(menu,option)
#	ga.new_game()
#	ga.resume_game()
#	ga.view_atts()
#	pa.move_player()
#	pa.attack()
#	pa.talk()
#	pa.take()
#	pa.give()
#	ca.savelog()
#	ga.return_main()
#handles options 1&2 of hidden menu
	if menu.upper()=="HIDDEN":
		if option==1:
			ca.create_log("Species")
		elif option==2:
			ca.create_log("Classes")	
	
	
	




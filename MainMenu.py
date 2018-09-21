#Main Menu creation and coding to call each option
main_menu={1:"New Game",2:"Resume Game",3:"View Character Attributes",4:"View Class Attributes",5:"View Species Attributes",6:"Exit"}
game_menu={1:"Move",2:"Attack"3:"Talk",4:"Take",5:"Give",6:"Save Game",7:"Main Menu"}
hidden_menu={1:"Create Species",2:"Create Class",3:"Update Species",4:"Update Class",5:"Delete Species",6:"Delete Class",7:"Create Map",8:"Update Monster Spots"}
for key in main_menu:
    print(str(key),":",main_menu[key])


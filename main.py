from datetime import datetime
import time
import sys
import platform
from colorama import init
from termcolor import colored
import os
import subprocess
from __core__ import version
from __core__ import commands








idx = 0



init()

#//////////////////////////////////////////////////////////////////////
#Fore: BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE, RESET.
#Back: BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE, RESET.
#Style: DIM, NORMAL, BRIGHT, RESET_ALL
#//////////////////////////////////////////////////////////////////////


#=====================================
machine = str(platform.machine())
versione = str(platform.version())
plat = str(platform.platform())
nome = str(platform.uname())
sistema = str(platform.system())
processore = str(platform.processor())
#=====================================
        

data = str(datetime.now())
print(
"Session started at: "+data+"\n")
print("@System: "+sistema+" "+versione+"_@Platform: "+plat+"_@Processor: "+processore+"_@Machine: "+machine)
print(colored(
"Created by:\n"
      
" \n _____        _____       _ "
"\n |  __ \      / ____|     | |"
"\n | |__) |   _| (___   __ _| |"
"\n |  ___/ | | |\___ \ / _` | |"
"\n | |   | |_| |____) | (_| | |"
"\n |_|    \__, |_____/ \__,_|_|"
 "\n        __/ |               "
"\n        |___/                "
,"green"))

print(colored("Program version: "+str(version.uver),"blue"))
















#Don't touch!!

#=============
#=============
while True:
    argument = ""
    arg = ""
    #Don't touch!!

    posizione = os.getcwd()
    

    #determinare il tipo di comando
    
    command = str(input(str(posizione)+">#"))
    arg  = command.split() #dividere il comando dato in una lista da n elementi
    if command == "help":
       commands.System.one_row[arg[0]]()
        
    try:
        argument = arg[2]
        argument = ""
        if "make" in arg:
            for m in range(2,len(arg)):
                argument = argument+arg[m]+" "
        elif "go" in command:
            argument = arg[2]
            argument = ""   
            for n in range(2,len(arg)):
                argument = argument+arg[n]+" "
            
    except:
        argument = ""
    if "exe" in arg:
        commands.System.one_row[arg[0]](arg[1])
    else:
    
        try:
            commands.System.modes[arg[0]].functions[arg[1]]()
            
        #tipi di errore
            
        
        
        except IndexError:
            print(colored("ArgError: "+str(arg[0])+" commands required two arguments,"+str(len(arg))+" date","red"))

        except KeyError:
            if arg[0] in commands.System.modes:
                print(colored("InputError: not a valid argument date for "+ str(arg[0])+" type help, for the list of commands.","yellow"))
            else:
                if command == "!/":
                    print(colored("InputError: "+str(arg[0])+" is not a command. Type help for all commands avabile.","yellow"))

        except:
            commands.System.modes[arg[0]].functions[arg[1]](argument)
            
    
            
            
  

















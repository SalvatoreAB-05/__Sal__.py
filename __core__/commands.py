import subprocess
import os
from colorama import init
from termcolor import colored
init()


class System:

    def helps():

        


        
        print(colored("to return to the console insert: !/ \nWelcome to the help section, please insert here the command that you can't use:","green"))
        def system():
            print("The system command can be used for system rebooting or system shutdown. Here all of the commands avabile:")

        def direc():
            print("ij")

        def exe():
            print("ij")

        celp = {
            "system":system,"direc":direc,"exe":exe
            }
        
        while True:
            argomento = str(input("H: "))
            if argomento == "!/":
                break
            celp[argomento]()


        
    def execute(file):
        subprocess.Popen([file], shell = True)
            

    







    

    class Shutdown:
        def spegni():
            subprocess.run("shutdown /s" ,shell=True)
            print("Done!")
        def disconnetti():
            subprocess.run("shutdown /l" ,shell=True)

        functions = {
            "turnoff":spegni,"disc":disconnetti
            }

    class Dir:
        def make(name):
            os.mkdir(name)

        def delete():
            print("ciao")
        def go_to(route):
            try:
                os.chdir(route)
            except:
                print(colored("SearchError: No file or directory found","red"))
        def exite():
            os.chdir("..")

        functions = {
            "make":make, "go":go_to,"ex":exite
        }

    
    
    
    modes = {
    "system": Shutdown, "direc": Dir
    
        }
    one_row = {
        "exe": execute, "help":helps
        }



            
        

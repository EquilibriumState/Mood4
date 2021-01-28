import os
import sys
import pickle
import webbrowser

class mood: #class for moods
    def __init__(self,name): #given string, while creating will be name of the mood
        self.name = name
        self.webpages = []
        self.files = []

    def name_mood(self, new_name):
        self.name = new_name

    def add_web(self, link):
        self.webpages.append(link)

    def add_files(self, file):
        self.files.append(file)

    def run_os(self): #run in macOS, check if the path and websites are correct
        for i in self.webpages:
            try:
                webbrowser.open(i)
            except:
                print(i, "is not valid webpage")
        for i in self.files:
            try:
                os.system("open " + i)
            except:
                print(i, "is not valid path")

def welcom_and_choose():
    '''
    Main function, which let us navigate in the program
    :return:
    '''
    print(r'''Hello.
    This program prepare your computer for work, relax or whatever you like.
    If you want to start 
    1. Write number or mood from list below (if you already created it)
    2. Or you can [C]reate new mood, [E]dit, [I]nfo (showing which mood what contains), [R]emove one or [Q]uit
    If you want to go back just input empty line''')

    if "moodslist.picle" not in os.listdir('.'): #check if we already have saved moods
        moods_list = []
        with open("moodslist.picle", "wb") as create_file: #if not creating empty list and pickle it
            pickle.dump(moods_list, create_file)
    else:
        with open("moodslist.picle", "rb") as open_file: #if yes is reading saved moods to the list
            moods_list = pickle.load(open_file)

    name_list = [i.name for i in moods_list]

    for n, i in enumerate(moods_list):
        print(n,i.name)

    while True:
        word = input("Enter input:\t")

        if word in ("q", "Q"): #decide to quit program
            sys.exit()
        elif word in ("r", "R"): #decide to remove mood
            name = input("What's the name of the mood you want to remove?\t")
            if name in name_list:
                moods_list.remove(moods_list[name_list.index(name)]) #remove mood from our list and save it
                with open("moodslist.picle", "wb") as create_file:
                    pickle.dump(moods_list, create_file)
                break

        elif word in ("c", "C"): #decide to create new mood
            name = input ("What's the name of the mood?\t")
            if name: #chceck if mood with that name already exists
                if name in name_list:
                    print("That mood already exist")
                    continue
                else:
                    create_mood(name, moods_list)
            else:
                continue

        elif word in ("e", "E"): #decide to edit mood
            name = input("What's the name of the mood you want to edit?\t")
            if name in name_list:
                edit_mood(name, moods_list, name_list)
                break
            else:
                print("Wrong name")

        elif word in ("i", "I"): #decide to print info about moods
            for i in moods_list:
                print(i.name)
                print("\tFiles:", "\n\t\t".join(i.files))
                print("\tWebpages:", "\n\t\t".join(i.webpages))

        elif word in [str(i) for i in range(0,len(moods_list))]: #run mood chosen from number
            moods_list[int(word)].run_os()
            sys.exit()

        elif word in [i.name for i in moods_list]: #run mood chosen from name
            moods_list[[i.name for i in moods_list].index(word)].run()
            sys.exit()
        else:
            print("Unknown input")
    welcom_and_choose() #if we break a loop without quiting or executeting mood, we start this function from the start

def create_mood(name, moods_list):
    new_mood = mood(name) #create class with given name
    print("Do you want to add [F]ile, [W]ebpage, [R]estart (If you finished click R) or [Q]uit?")
    while True:
        word = input("Enter input:\t")

        if word in ("q", "Q"):
            sys.exit()

        elif word in ("f", "F"): #decide to add files
            print("Add full path to files. After each approve by enter, if you finished approve empty line\t")
            while True:
                name = input ()
                if name:
                    if os.path.exists(name):
                        new_mood.add_files(name)
                    else:
                        print("That path doesn't exists. Insert correct one:")
                        continue
                else:
                    break

        elif word in ("w", "W"): #decide to add websites
            print("Add full address to webpage. After each approve by enter, if you finished approve empty line\t")
            while True:
                name = input ()
                if name:
                    new_mood.add_web(name)
                else:
                    break

        elif word in ("r", "R"): #decide to finish
            break

    moods_list.append(new_mood) #we add mood to our list and save it
    with open("moodslist.picle", "wb") as create_file:
        pickle.dump(moods_list, create_file)

def edit_mood(var, moods_list, name_list):
    edit_mood = moods_list[name_list.index(var)] #choose which mood we edit
    print("Do you want to edit [F]iles, [W]ebpages, change [N]ame, [R]estart (If you finished click R) or [Q]uit?")
    while True:
        word = input("Enter input:\t")

        if word in ("q", "Q"):
            sys.exit()

        elif word in ("f", "F"): #decide to edit files
            while True:
                ar = input("[A]dd or [R]emove")
                if ar in ("A","a"):
                    print("Add full path to files. After each approve by enter, if you finished approve empty line")
                    while True:
                        name = input()
                        if name:
                            if os.path.exists(name):
                                edit_mood.add_files(name)
                            else:
                                print("That path doesn't exists. Insert correct one:")
                                continue
                        else:
                            ar = 0
                            break
                elif ar in ("R","r"):
                    for n, i in enumerate(edit_mood.files):
                        print(n,i)
                    print("Which of the following files would you like to remove? \
                    (number, leave empty line if you wanna cancel)")
                    while True:
                        name = input()
                        if name:
                            try:
                                name = int(name)
                                if name not in range(len(edit_mood.files)+1): #cheking if we have file with that number
                                    print("This number is not in the list")
                                    continue
                                else:
                                    edit_mood.files.remove(edit_mood.files[name])
                                    break
                            except ValueError:
                                print("Input is not a number.")
                        else:
                            ar = 0
                            break
                if not ar:
                    break

        elif word in ("w", "W"): #decided to manage websites
            print("[A]dd or [R]emove")
            while True:
                ar = input()
                if ar in ("A", "a"):
                    print("Add full path to webpage. After each approve by enter, if you finished approve empty line")
                    while True:
                        name = input()
                        if name:
                            edit_mood.add_web(name)
                        else:
                            ar = 0
                            break
                elif ar in ("R", "r"):
                    for n, i in enumerate(edit_mood.webpages):
                        print(n, i)
                    print("Which of the following webpages would you like to remove? \
                    (number, leave empty line if you wanna cancel)")
                    while True:
                        name = input()
                        if name:
                            try:
                                name = int(name)
                                if name not in range(len(edit_mood.files)+1):
                                    print("This number is not in the list")
                                    continue
                                else:
                                    edit_mood.webpages.remove(edit_mood.webpages[name])
                                    break
                            except ValueError:
                                print("Input is not a number.")
                        else:
                            ar = 0
                            break
                if not ar:
                    break

        elif word in ("n", "N"): #decided to change name
            while True:
                name = input("Insert new name:\t")
                if name not in name_list:
                    edit_mood.name_mood(name)
                    break
                else:
                    print("You already have mood with that name")

        elif word in ("r", "R"):
            break

    moods_list[name_list.index(var)] = edit_mood #replicing changed mood with orginal and save it

    with open("moodslist.picle", "wb") as create_file:
        pickle.dump(moods_list, create_file)

if __name__ == '__main__':
    welcom_and_choose()



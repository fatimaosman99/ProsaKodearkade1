from ast import Call
import random
from dvaerge import Dwarf
import dwarfs 

#TODO Fetch reactions, integrate it here, 
def FetchReactions(dwarf):
    if dwarf == "Doc":
        #3 reactions
        return ["Hello", "Hi", "Namaste"]

    elif dwarf == "Grumpy":
        return ["wonderwoman", "gta", "greece"]

    elif dwarf == "Happy":
        return ["am happy", "am happy", "fries"]

    elif dwarf == "Sneezy":
        return ["Achoo", "haticho", "cho"]

def CallDwarfs():
    dwarfs = list()
    doc = Dwarf("Doc")
    dwarfs.append(doc.name)
    grumpy = Dwarf("Grumpy")
    dwarfs.append(grumpy.name)
    happy = Dwarf("Happy")
    dwarfs.append(happy.name)
    sneezy = Dwarf("Sneezy")
    dwarfs.append(sneezy.name)
    return dwarfs

def StartReactionChain():
    
    dwarfs = CallDwarfs()
    live_dwarfs = list()
    dwarf_1 = random.choice(dwarfs)
    live_dwarfs.append(dwarf_1)
    dwarfs.remove(dwarf_1)
    dwarf_2 = random.choice(dwarfs)
    live_dwarfs.append(dwarf_2)
    
    


    return [dwarf_1, dwarf_2]

def CallCharacters():
    live_dwarfs = StartReactionChain()
    dwarfs = CallDwarfs()
    #dwarfs minus live_dwarfs
    dwarfs.remove(live_dwarfs[0])
    dwarfs.remove(live_dwarfs[1])
    dwarf_1 = random.choice(dwarfs)
    live_dwarfs.append(dwarf_1)
    return dwarf_1


def io():
    #recieve input to get going
    i = 0
    while(i < 3):
        button_pressed = input("Welcome. Tab on x to call the dwarfs!")
        if button_pressed == "x" and i == 0:
            print(StartReactionChain())
            
        else: 
            print(CallCharacters())
        i = i+1
        

       
io()
#TODO tilføj elementerne til en list så du kan have styr på reaktioner
#TODO kom med reaktioner



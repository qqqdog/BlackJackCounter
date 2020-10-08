# -*- coding: utf-8 -*-
"""
Created on Thu Oct  8 12:16:15 2020

@author: Quinn
"""

import tkinter as tk

window = tk.Tk()

number_of_decks = 1
init_count = 4*number_of_decks
init_count_str = str(init_count)

index_to_card = {0:"2",
                 1:init_count_str,
                 2:"3",
                 3:init_count_str,
                 4:"4",
                 5:init_count_str,
                 6:"5",
                 7:init_count_str,
                 8:"6",
                 9:init_count_str,
                 10:"7",
                 11:init_count_str,
                 12:"8",
                 13:init_count_str,
                 14:"9",
                 15:init_count_str,
                 16:"10",
                 17:str(init_count*4),
                 18:"A",
                 19:init_count_str,
                 20:"COUNT",
                 21:"0",
                 22:"CARDS LEFT",
                 23:"52"}
                 


def click2():
    if(decrementLabelAndCount(0)):
        countPlusOne()
        
def click3():
    if(decrementLabelAndCount(1)):
        countPlusOne()

def click4():
    if(decrementLabelAndCount(2)):
        countPlusOne()

def click5():
    if(decrementLabelAndCount(3)):
        countPlusOne()

def click6():
    if(decrementLabelAndCount(4)):
        countPlusOne()

def click7():
    decrementLabelAndCount(5)
        
def click8():
    decrementLabelAndCount(6)
        
def click9():
    decrementLabelAndCount(7)
        
def click10():
    if(decrementLabelAndCount(8)):
        countMinusOne()
        
def click11():
    if(decrementLabelAndCount(9)):
        countMinusOne()
        
def decrementLabelAndCount(index):
    value = int(labels[index]["text"])
    if(value>0):
        labels[index]["text"] = str(value-1)
        labels[13]["text"] = int(labels[13]["text"])-1
        return True
    return False
        
def countPlusOne():
    value = int(labels[11]["text"])
    labels[11]["text"] = str(value+1)

def countMinusOne():
    value = int(labels[11]["text"])
    labels[11]["text"] = str(value-1)
        
buttons = []
labels = []
handlers = [click2, click3, click4, click5, click6, click7, click8, click9, click10, click11]

index = 0
for i in range(12):
    window.columnconfigure(i, weight=1, minsize=75)
    window.rowconfigure(i, weight=1, minsize=50)

    for j in range(0, 2):
        frame = tk.Frame(
            master=window,
            relief=tk.RAISED,
            borderwidth=1
        )
        frame.grid(row=i, column=j, padx=5, pady=5)
        
        if(index>19):
            label = label = tk.Label(master=frame, text=index_to_card[index])
            label.pack()
            labels.append(label)
        elif(index%2==0):
            button = tk.Button(master=frame, text=index_to_card[index], command=handlers[len(buttons)])
            button.pack()
            buttons.append(button)
        else:
            label = tk.Label(master=frame, text=index_to_card[index])
            label.pack()
            labels.append(label)
        index = index + 1



window.mainloop()
#main python script file
#Transcalc version 0.9 by: Jake Goodwin

#importing libary for gui
import tkinter as tk

#functions 

#Takes the values out of the text boxes
def grab_values(event):
    print("values taken!")
    test = tk.Label(root, text = "Calculated values:")
    test.grid(row = 3, column = 1, sticky = tk.W)

def retrieve_input(event):
    input_vp = vp_input.get()
    print(input_vp)
#root for gui window
root = tk.Tk()

#name in title bar at the top.
root.title("Transcalc ver 0.9")

#add labels
volts_pinchoff = tk.Label(root, text = "Vp:")
volts_pinchoff.grid(row = 0, column = 0, sticky = tk.E)

current_drain = tk.Label(root, text = "Idss(mA):")
current_drain.grid(row = 1, column = 0, sticky = tk.E)

#add input boxes
vp_input = tk.Entry(root)
vp_input.grid(row = 0, column = 1)

Idss_input = tk.Entry(root)
Idss_input.grid(row = 1, column = 1)

#Add calculate button
calc_button = tk.Button(root, text = "Calc")
calc_button.bind("<Button-1>", retrieve_input)
calc_button.grid(row = 0, column = 3)

root.mainloop()

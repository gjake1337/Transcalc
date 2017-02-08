#main python script file
#Transcalc version 0.9 by: Jake Goodwin

#importing libary for gui
import tkinter as tk

#global vars
output_list = []

#functions 

#Takes the values out of the text boxes and calls formula function.
def retrieve_input(event):
    input_vp = float(vp_input.get())
    input_idss = float(Idss_input.get())
    apply_trans_formula(input_vp, input_idss)

#uses the values and runs them through the formula.
def apply_trans_formula(vp, idss):
    idss = idss/1000
    for index in range(0, 6, 1):
        num = format((1000*(idss * ((1-(index / vp))** 2))), '10.6f')
        line = str('Amperage at: '+ str(index) + ' v : '+ str(num) + 'mA')
        x = index + 2
        new = tk.Label(root, text = line)
        new.grid(row = x, column = 0, sticky = tk.W)
        #output_list.append(line)
    #output_data = tk.Label(root, str(output_list))
    #output_data.grid(row = 2, column = 0, sticky = tk.W)
        
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
#vp_input.delete(0, tk.END)

Idss_input = tk.Entry(root)
Idss_input.grid(row = 1, column = 1)

#Add calculate button
calc_button = tk.Button(root, text = "Calc")
calc_button.bind("<Button-1>", retrieve_input)
calc_button.grid(row = 0, column = 3)

root.mainloop()

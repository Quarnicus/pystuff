from Tkinter import * #Python 2.X
#from tkinter import * #Python 3.x

selection_list = ('Fahrenheit to Celsius','Fahrenheit to Kelvin', 'Celsius to Fahrenheit','Celsius to Kelvin','Kelvin to Celsius','Kelvin to Fahrenheit')

def Convert_temp():
	x=0
	entry = float(temp_entry.get())
	for i in selection_list:
		if (i == selection.get()):
			break		
		x += 1
	if (x==0):
		result =str(format( (entry -32) * 5/9,'0.2f') + "C")
	elif (x==1):
		result = str(format( (entry -32) * 5/9 + 273.15,'0.2f')+"K")
	elif (x==2):
		result = str(format( (entry * 9/5) + 32,'0.2f') + "F")
	elif (x==3):
		result = str(format(entry + 273.15,'0.2f')+"K")
	elif (x==4):
		result = str(format(entry - 273.15,'0.2f')+"C")
	elif (x==5):
		result = str(format((entry - 273.15) * 9/5 + 32,'0.2f')+"F")
	else:
		result = "out of range!"
	result_label.config(text=result ,width=len())

root = Tk()
root.title('Temperature Converter')

screen_width = root.winfo_screenwidth()
screen_height= root.winfo_screenheight()

temp_entry= Entry(root,width='5')
temp_entry.grid(row='0',column='0',pady='6',padx='6')
temp_entry.focus()

selection = StringVar(root)
selection.set(selection_list[0])
select_menu = OptionMenu(root, selection, *selection_list)
select_menu.grid(row='0',column='1',padx='6',pady='6')

result_label= Label(root,text='0 C',bg='green',width='6')
result_label.grid(row='0',column='2',padx='6',pady='6')


convert_button = Button(root,text='convert',command=Convert_temp)
convert_button.grid(row='3',column='1',padx='6',pady='8')

root.mainloop()

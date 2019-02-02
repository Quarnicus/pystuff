from Tkinter import *
from webcolors import *
bg_color = 'white'
def Generate_RGB_Hex(self):
	red = red_slider.get()
	green = green_slider.get()
	blue = blue_slider.get()
	result = rgb_to_hex((red,green,blue))
	Set_Color_Hex_Labels(CSS3_HEX_TO_NAMES.get(result),result)
	
def CSS3_Name_To_Hex(self):
	selection = color_list_box.curselection()
	result = color_list_box.get(selection[0])
	res_hex = CSS3_NAMES_TO_HEX.get(result)
	color_frame.config(bg=res_hex)
	x=hex_to_rgb(CSS3_NAMES_TO_HEX.get(result))
	red_slider.set(x.red)
	green_slider.set(x.green)
	blue_slider.set(x.blue)
	Set_Color_Hex_Labels(result,CSS3_NAMES_TO_HEX.get(result))

def Set_Color_Hex_Labels(color,hex_):
	color_frame.config(bg=hex_)
	hex_label.config(text=hex_)
	if color != None :	
		name_label.config(text=color)
	else:
		name_label.config(text='None')

def Copy_Hex_To_Clipboard():
	copy_hex_button.clipboard_clear()
	copy_hex_button.clipboard_append(hex_label['text'])
	
def Copy_Name_To_Clipboard():
	copy_color_button.clipboard_clear()
	copy_color_button.clipboard_append(name_label['text'])
	
#-----------------------------------------------------------------------------
root = Tk()
root.title('CSS3 Colors')
#--------------------
color_frame = Frame(root,bg="green",borderwidth='4',width='292',height='142')
color_frame.grid(row='0',column='0',padx='4',pady='4')

color_list_frame = Frame(root,borderwidth='4',width='292',height='142')
color_list_frame.grid(row='2',column='0',padx='4',pady='4',sticky=W)

color_list_box = Listbox(color_list_frame,width='14',height='6')
color_list_box.grid(row='0',column='0',padx='4',pady='4')
color_list_box.bind('<ButtonRelease-1>',CSS3_Name_To_Hex)
selection_list = CSS3_HEX_TO_NAMES.values()

for x in selection_list:
	color_list_box.insert(END,x)
		
#---------------------
red_slider= Scale(root,from_='0',to='255',bg='red',orient=HORIZONTAL,command=Generate_RGB_Hex)
red_slider.grid(row='1',column='0',padx='4',pady='4',	sticky=W)

green_slider= Scale(root,from_='0',to='255',bg='green',orient=HORIZONTAL,command=Generate_RGB_Hex)
green_slider.grid(row='1',column='0',padx='4',pady='4',	sticky=E)

blue_slider= Scale(root,from_='0',to='255',bg='blue',orient=HORIZONTAL,command=Generate_RGB_Hex)
blue_slider.grid(row='1',column='0',padx='4',pady='4',	sticky=N)
#----------------------------

hex_label = Label(color_list_frame,text='dummy text' ,width='16',height='1',padx=4,pady=6 )
hex_label.grid(row='0',column='1',padx='2',pady='4',sticky=N)
copy_hex_button = Button(color_list_frame,text='Copy',command=Copy_Hex_To_Clipboard)
copy_hex_button.grid(row='0',column='2',padx='2',pady='4',sticky=N+E)

name_label = Label(color_list_frame,text='mo dummy text' ,width='16',height='1',padx=4,pady=6 )
name_label.grid(row='0',column='1',padx='2',pady='4',sticky=W)
copy_color_button = Button(color_list_frame,text='Copy',command=Copy_Name_To_Clipboard)
copy_color_button.grid(row='0',column='2',padx='2',pady='4',sticky=E)

Set_Color_Hex_Labels('black','#000000')

root.mainloop()

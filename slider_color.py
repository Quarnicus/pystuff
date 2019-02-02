#python 2.7
from Tkinter import *
from webcolors import *
bg_color = 'white'
def Generate_RGB_Hex(self):
	red = red_slider.get()
	green = green_slider.get()
	blue = blue_slider.get()
	result = rgb_to_hex((red,green,blue))
	Set_Color_Hex_Labels(HTML4_HEX_TO_NAMES.get(result),result)
	
def Copy_To_Clipboard():
	hex_button.clipboard_clear()
	hex_button.clipboard_append(hex_label['text'])
	

def Set_Fields(self):
	res = name_selection.get()
	Set_Color_Hex_Labels(res,HTML4_NAMES_TO_HEX.get(res))
	x=hex_to_rgb(HTML4_NAMES_TO_HEX.get(res))
	red_slider.set(x.red)
	green_slider.set(x.green)
	blue_slider.set(x.blue)

def Set_Color_Hex_Labels(color,hex_):
	color_label.config(bg=hex_)
	hex_label.config(text=hex_)
	name_label.config(text=color)
def Quit():
	root.destroy()
	
root = Tk()
root.title('RGB Sliders')

selection_list = HTML4_HEX_TO_NAMES.values()
name_selection = StringVar(root)
name_selection.set(selection_list[0])

left_frame= Frame(root)
left_frame.grid(row='0',column='0')

color_label = Label(left_frame,bg=bg_color ,width='20',height='5',padx=4,pady=6 )
color_label.pack(side=LEFT)

red_slider= Scale(left_frame,from_='0',to='255',bg='red',command=Generate_RGB_Hex)
red_slider.pack(side=LEFT,padx=2,pady=6)

green_slider= Scale(left_frame,from_='0',to='255',bg='green',command=Generate_RGB_Hex)
green_slider.pack(side=LEFT,padx=2,pady=6)

blue_slider= Scale(left_frame,from_='0',to='255',bg='blue',command=Generate_RGB_Hex)
blue_slider.pack(side=LEFT,padx=2,pady=6)

right_frame= Frame(root)
right_frame.grid(row='0',column='1')

select_menu = OptionMenu(right_frame, name_selection, *selection_list, command=Set_Fields)
select_menu.grid(row='2',column='2',padx='2',pady='4')


name_label = Label(right_frame,text='',bg=bg_color ,width='10',height='1',padx=4,pady=6 )
name_label.grid(row='2',column='1',padx='2',pady='4')

quit_button = Button(right_frame,text='Quit',command=Quit)
quit_button.grid(row='3',column='3',padx='2',pady='4')

hex_label = Label(right_frame,text='',bg=bg_color ,width='7',height='1',padx=4,pady=6 )
hex_label.grid(row='1',column='1',padx='2',pady='4')

hex_button = Button(right_frame,text='Copy',command=Copy_To_Clipboard)
hex_button.grid(row='1',column='2',padx='2',pady='4')



Set_Color_Hex_Labels('black','#000000')















root.mainloop()

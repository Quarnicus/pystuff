import random
from colors import *

#------------------------------------------------------------
#   role_dice(num_of_dice,num_of_sides)
#   num_of_dice = Number of Die to role_dice
#   num_of_sides = Number of sides the die have
#   returns result[] = a list of roles
def role_dice(num_of_dice,num_of_sides):
    result=[]
    for x in range(num_of_dice):
        result.append(random.randrange(1,num_of_sides+1))
    return(result)

directions = ('North','South','East','West')
class Item_Object():
    def __init__(self,title=None,current_location=None,keywords=None):
        self.title = title
        self.current_location = current_location
        self.keywords = keywords

class Animal(Item_Object):
    def __init__(self,title=None,current_location=None,keywords=None):
        Item_Object.__init__(self,title,current_location,keywords)
        self.items = []

    def find_item_character(self,noun):
        for x in self.items:
            if noun in x.keywords:
                return(x)
        return(None)

class Room:
    def __init__(self,title=None,desc=None):
        self.title = title
        self.desc  = desc
        self.exits = {}
        self.items = []

    def print_room(self):
        x=''
        print("%s\n%s" %(self.title,self.desc))
        for key in self.exits.keys():
            x = x +" " + key
        print("Exits: ",x)

        for y in self.items:
            print(y.title)

def find_item_room(noun,curr_room):
    for x in curr_room.items:
        if noun in x.keywords:
            return(x)
    return(None)

def do_stuff(verb,noun,character):

    if verb == 'get' or verb == 'take':
        x = find_item_room(noun,character.current_location)
        if (x != None):
            character.items.append(x)
            character.current_location.items.remove(x)
            return('You {} the {}.'.format(verb,noun))
        else:
            return("You don't see a %s here."% (noun))

    elif verb == 'drop':
        x= character.find_item_character(noun)
        if (x != None):
            character.current_location.items.append(x)
            character.items.remove(x)
            return('You {} the {}.'.format(verb,noun))
        else:
            return("You don't have a %s."% (noun))

    elif verb == 'look':
        character.current_location.print_room()

    elif verb == 'i' or verb == 'inventory' or verb == 'inv':
        result ='You are carrying:\n'
        if len(character.items)== 0:
            return(result + 'Nothing')
        for i in character.items:
            result = result + i.title + '\n'
        return(result)
    elif verb == 'n' or verb =='north':
            verb = 'North'
            for key in character.current_location.exits.keys():
                if verb == key:
                    character.current_location = character.current_location.exits.get(key)
                    do_stuff('look',' ',character)
                    return('you head off to the %s '%(verb))
            return("You can't go %s from here"%(verb))
    elif verb == 's' or verb =='south':
            verb = 'South'
            for key in character.current_location.exits.keys():
                if verb == key:
                    character.current_location = character.current_location.exits.get(key)
                    do_stuff('look',' ',character)
                    return('you head off to the %s '%(verb))
            return("You can't go %s from here"%(verb))
    elif verb == 'e' or verb =='east':
            verb = 'East'
            for key in character.current_location.exits.keys():
                if verb == key:
                    character.current_location = character.current_location.exits.get(key)
                    do_stuff('look',' ',character)
                    return('you head off to the %s '%(verb))
            return("You can't go %s from here"%(verb))
    elif verb == 'w' or verb =='west':
            verb = 'West'
            for key in character.current_location.exits.keys():
                print('keys;',key)
                if verb == key:
                    character.current_location = character.current_location.exits.get(key)
                    do_stuff('look',' ',character)
                    return('you head off to the %s '%(verb))
            return("You can't go %s from here"%(verb))


    else:
	       return("You can't do that to a %s."% (noun))



room = Room(title='A Dusty Old Room')
room.desc = '''This old dusty room in the corner of the house has very poor lighting.
Nothing much here of great value. just a few small fixtures like the desk'''
room2 = Room(title='A Second Dusty Old Room')
room2.desc = '''This is the second old dusty room in the corner of the house has very poor lighting.
Nothing much here of great value.'''
room3 = Room(title='A Third Dusty Room')
room3.desc = '''This is the third old dusty room. It is a lot like the other rooms.
Nothing much here of great value.'''
room4 = Room(title='A Fourth Dusty Room')
room4.desc = '''This is the Fourth old dusty room. It is a lot like the other rooms.
Nothing much here of great value. It is the last of the Dusty Rooms'''

item = Item_Object(title='A Dull Looking Sword',keywords=['sword','dull'])
item2 = Item_Object(title='A Dusty Cluttered Desk',keywords=['desk','dust','clutter'])

room.exits.update({directions[0]:room2})
room.exits.update({directions[3]:room4})

room2.exits.update({directions[1]:room,directions[3]:room3})
room3.exits.update({directions[1]:room4,directions[2]:room2})
room4.exits.update({directions[0]:room3,directions[2]:room})

room.items.append(item)
room.items.append(item2)
player = Animal(title='you')
player.current_location = room
player2 = Animal(title='A Tiny Mouse Sits In the Corner',keywords=['mouse','rodent'])
player2.current_location = room3
room3.items.append(player2)
print('room3 items :',player2.title)
player.current_location.print_room()
print('\n')

while(1):
        result = input('0==||>>>>>>>> ')
        if result == 'q':
            break
        vn = result.split()
        if len(vn) == 1:
            vn.append(' ')
        print(do_stuff(vn[0],vn[1],player))

# print(do_stuff('get','sword',player))
# print('\nthe player inventory',player.items,'\n')
# player.current_location.print_room()
# print('\n')
# print(do_stuff('drop','sword',player))
# print('\nthe player inventory',player.items,'\n')
# player.current_location.print_room()

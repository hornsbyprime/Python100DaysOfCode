print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

way = input('While traversing a forrest you come to a fork in the road. Do you go left or right?').lower()
if way == 'left':
  cross = input('You follow the left path and after several hours arrive at a large river. Next to the path is a dock for mooring boats. how do you attemt to cross swim or wait?').lower()
  if cross == 'wait':
    door = input('You sit on a bench and close your eyes listening to the beautiful meolodies of the local songbirds. Before long between the breaks in the songs of birds,the sounds of oars breaking the surface of the water can be heard. The boat captain pulls up to the dock and offers to ferry you across the mighty river. Once across the river you follow along the path until a clearing opens. In the middle of the clearing stands a building containing three doors. Which door do you choose to enter. Red, Yellow, or BLue?').lower()
    if door == 'red':
      print('You spring a booby trap and are engulfed in flame, burning to a crisp. You lose.')
    elif door == 'blue':
      print('You are eaten by zombies. You lose.') 
    elif door == 'yellow':
      print('You have chosen correctly, avoiding certain death. You ascend the tower and win the fair maidens heart. Unfortunatly the maiden is from Frankston and imediatly sends you out for some VB and winnie blues. While completing this quest you die or something, I don\'t know.')
    else:
      print('You wait to long making your choice and a dragon comes and eats you. You lose.')
  else:
    print('The river looks calm and you wade in thinking yourself to cool to wait for the likes of a lowly boat captain. However your hubris will be your undoing as the calm looking river has a deadly under current. Shortly after entering the current pulls you deeper and deeper into the murky depths. You struggle valiantly to reach the surface but the river cares not for your will to live. The river and the boat captain are actually good friends, and the river does not take kindly to your disrespect. Your body is never found and no one really care because most people thought you were a douche anyway. You lose.')
else:
  print('Your walk down the right path for a few hours when out of nowhere an arrow comes flying and strikes you in the knee. Your adventuring career is over. You lose.')  
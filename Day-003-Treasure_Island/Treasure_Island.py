print(r'''
 .       .
                                                    \     /
                                                 ._  '   '  _.
                                                   '  o@o  '
                                                     o@@@o
                                                 .-'  o@o  '-.
                                                     .   .
                                                    /     \
                                                   .       .

                             'Xx  xX*,
                          ,*xXXx_xXx
                            _xXXXXXxx*,
                          ,*XXx@x@Xx
                            X @|@@ `x
                            '  ||    '
                               ||
                               ||
                               ||
                               ||
                            /ssssssss.
                      /sssssssSSSSssssssssss.
        /\         /sssssSSSSSSSSSSSSSSSssssssssssss.              Dani
~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~
 ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ 
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
direction = input('You\'re at the cross road. Where do you want to go?\n '
                  'Type "left" or "right":').capitalize()
if direction == "Left":
   choice_1 = input('You\'ve come to a lake. There\'s an island in the middle of the lake.\n '
                    'Type "wait" to wait for a boat. '
                    'Type "swim" to swim across.').capitalize()
   if choice_1 == "Wait":
        door = input('You arrive at the island unharmed. '
                     'There is a house in front of you with three doors that are red, yellow and black. '
                     'Which do you pick?\n').capitalize()
        if door == "Yellow":
            print("You found the treasure!!")
        elif door == "Red":
            print("Oh no! Fire! Game over")
        elif door == "Black":
            print("It's haunted! You can never leave...")
        else:
            print("That's not a choice. Game over.")
   else:
       print("You got attacked by an angry trout. Game Over.")
else:
    print("Sorry, you fell into a hole and game over :(")

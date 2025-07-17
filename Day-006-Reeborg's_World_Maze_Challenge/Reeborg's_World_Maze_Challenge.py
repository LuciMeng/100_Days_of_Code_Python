# Reeborg's World: https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=problem_world.json&url=user_world%3Aproblem_world.json

def turn_right():
    turn_left()
    turn_left()
    turn_left()

while front_is_clear():
    move()
turn_left()

while not at_goal():
    if wall_in_front() and wall_on_right():
        turn_left()
    elif wall_on_right():
        move()
    else:
        turn_right()
        move()

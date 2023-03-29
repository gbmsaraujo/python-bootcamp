def turn_right():
    turn_left()
    turn_left()
    turn_left()


while at_goal() != True:
    if wall_in_front():
        turn_left()
        while front_is_clear() and not right_is_clear():
            if at_goal() == True:
                break
            move()
            if right_is_clear():
                turn_right()
    elif front_is_clear() and not wall_on_right():
        move()
        turn_right()
        move()
    else:
        move()

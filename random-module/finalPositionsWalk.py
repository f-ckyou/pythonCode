import random

def walk(steps):
    x, y = 0, 0
    for _ in range(steps): # _ is used when the iterating variable is not used inside the loop
        step = random.choice(['north', 'south', 'east', 'west']) # randomly selecting from the list
        if step == 'north':
            y += 1
        elif step == 'south':
            y -= 1
        elif step == 'east':
            x -= 1
        else:
            x += 1
    return x,y

step = 2400
final_position = walk(step) # last coordinates of the position wrt (0, 0)

print(f"Final position after {step} steps: {final_position}")
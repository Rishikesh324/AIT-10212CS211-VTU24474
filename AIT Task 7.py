# Operators
def move(subject, x1, x2):
    return f"Move {subject} from {x1} to {x2}"

def push_box(x1, x2):
    return f"Push box from {x1} to {x2}"

def climb_box(x, direction):
    return f"Climb box at {x} {direction}"

def have_banana(x):
    return f"Have banana at {x}"


# Initial State
initial_state = {
    'monkeyAt0': True,
    'monkeyLevel': 'Down',
    'bananaAt5': True,
    'boxAt3': True
}

# Goal State
goal_state = {
    'GetBanana': True,
    'at': 3
}


# Planning Algorithm
def plan_actions(initial_state, goal_state):
    actions = []
    # Example planning algorithm to achieve the goal state
    if initial_state['monkeyAt0'] and initial_state['bananaAt5']:
        actions.append(move('Monkey', 0, 5))
        actions.append(climb_box(3, 'Up'))
        actions.append(have_banana(3))
    return actions


# Execute the planning algorithm
actions = plan_actions(initial_state, goal_state)

# Print the actions in the plan
print("Plan:")
for action in actions:
    print(action)

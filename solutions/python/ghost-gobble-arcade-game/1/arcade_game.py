"""Functions for implementing the rules of the classic arcade game Pac-Man."""
def eat_ghost(power_pellet, touching_ghost):
    return power_pellet and touching_ghost

def score(power_pellet, touching_ghost):
    return power_pellet or touching_ghost

def lose(power_pellet, touching_ghost):
    return (not power_pellet) and touching_ghost

def win(has_eaten_all_dots, has_power_pellet, touching_ghost):
    return (has_eaten_all_dots and not touching_ghost) or (has_eaten_all_dots and has_power_pellet and touching_ghost)
"""

Visual Debugger

- Put Breakpoint
- Put breakpoint with condition inside loop
- Interactive Debug Console
- Evaluate Expression action

"""

from time import sleep

my_name = "Earth"
planets_list = ["Mercury", "Venus", "Earth",
                "Mars", "Jupiter", "Saturn",
                "Uranus", "Neptune"]

print(f"My name is {my_name}")


def greet_neighbors(neighbors):
    for n in neighbors:
        print(f"Hi my friend {n}")
    return len(neighbors)


def get_current_neighbors(num, planets, i):
    my_neighbors = []
    if i != 0:
        my_neighbors.append(planets[i - 1])
    if i != num - 1:
        my_neighbors.append(planets[i + 1])
    return my_neighbors


def greet_planets(planets):
    num = len(planets)
    for i in range(num):
        planet_name = planets[i]
        print(f"Hi I'm {planet_name}!")
        l = greet_neighbors(get_current_neighbors(num, planets, i))
        print(f"We have {l} neighbors")
        sleep(1)


if __name__ == "__main__":
    greet_planets(planets_list)

"""
Song generator function
Example for teaching about Functions
author: Argyriou Thanasis, email: argythana@gmail.com
date: Dec 2023
"""

def who_heart_broken():
    broken_heart = input("Enter name of heart broken person: ")
    return broken_heart


def who_heart_breaker():
    breaker = input("Enter name of heart breaker person: ")
    breaker = breaker + " "
    return breaker


def heart_damage():
    damage = abs(int(input("Enter integer number, how much it hurts, 1-10: ")))
    if 1 <= damage < 6:
        repeat = 2
    elif 6 <= damage <= 10:
        repeat = 6
    else:
        repeat = 12  # when too much heart damage
    return repeat


def lyrics_version():
    version = int(input("Enter 1 for clean version and 2 for explicit: "))
    if version == 1:
        lyrics = "\nBecause you are so beautiful"
    elif version == 2:
        lyrics = "\nBecause you are such a bad person"
    return lyrics


def generate_song(who="name1", for_whom="name2", lyrics="whatever", repeat=2):
    """Song generator. Enter names who, for whom, numbers for mood and damage."""
    who = who_heart_broken()
    for_whom = who_heart_breaker()
    lyrics = lyrics_version()
    repeat = heart_damage()
    for i in range(repeat):
        print(f"\nThis is {who} singing for you {for_whom}")
    print(f"{lyrics} {for_whom*repeat}")
    print(f"{lyrics} ...")


if __name__ == "__main__":  # syntax to make file executable
    generate_song()

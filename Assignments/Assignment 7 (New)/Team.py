from random import randint
from Characters import *


# return a random member in the team that is alive
# But we assume that someone must be alive in the team
def rand_alive(team):
    n = len(team)
    r = randint(0, n-1)
    return r if team[r].alive else rand_alive(team)


# return a random member in the team that is dead
# But we assume that someone must be dead in the team
def rand_death(team):
    n = len(team)
    r = randint(0, n-1)
    return r if not team[r].alive else rand_death(team)


# Check if everyone in the team is dead
def all_dead(team):
    for i in team:
        if i.alive:
            return False
    return True


# Check if everyone in the team is alive
def all_alive(team):
    for i in team:
        if not i.alive:
            return False
    return True


# The length of the longest name. Just for the printing format
len_longest_name = 11


# Print a team in a nice format
def print_stat(team):
    if team == []:
        print("(Currently no member in the team now)")
        return

    names = 'Members:   '
    hp = 'Hitpoints: '
    sth = 'Strength:  '
    maxm = 'Max. Mana: '
    mana = 'Current M: '

    for i in team:
        nspace = len_longest_name - len(i.name)
        names += '|' + ' '*nspace + i.name
        nspace = len_longest_name - len(str(i.hp))
        hp += '|' + ' '*nspace + str(i.hp)
        if i.str:
            nspace = len_longest_name - len(str(i.str))
            sth += '|' + ' '*nspace + str(i.str)
        else:
            sth += '|' + ' '*len_longest_name
        if i.maxmana:
            nspace = len_longest_name - len(str(i.maxmana))
            maxm += '|' + ' '*nspace + str(i.maxmana)
        else:
            maxm += '|' + ' '*len_longest_name

        if i.mana:
            nspace = len_longest_name - len(str(i.mana))
            mana += '|' + ' '*nspace + str(i.mana)
        else:
            mana += '|' + ' '*len_longest_name

    print(names)
    print(hp)
    print(sth)
    print(maxm)
    print(mana)

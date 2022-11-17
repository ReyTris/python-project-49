#!/usr/bin/env python3
from brain_games.games.engine_game import engine

from brain_games.games import even_game
from brain_games.games import calc_game
from brain_games.games import gcd_game
from brain_games.games import progression_game


def brain_even():
    engine(even_game)

def brain_calc():
    engine(calc_game)

def brain_gcd():
    engine(gcd_game)

def brain_progression():
    engine(progression_game)

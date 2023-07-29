"""keyboard_agents.py
 -----------------
 Licensing Information:  You are free to use or extend these projects for
 educational purposes provided that (1) you do not distribute or publish
 solutions, (2) you retain this notice, and (3) you provide clear
 attribution to UC Berkeley, including a link to http://ai.berkeley.edu.

Attribution Information: The Pacman AI projects were
developed at UC Berkeley.
The core projects and autograders were primarily created by John DeNero
(denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
Student side autograding was added by Brad Miller, Nick Hay, and
 Pieter Abbeel (pabbeel@cs.berkeley.edu)."""

import random
from game import Agent
from game import Directions
from graphics_utils import keys_waiting
from graphics_utils import keys_pressed


class KeyboardAgent(Agent):
    """
    An agent controlled by the keyboard.
    """
    # NOTE: Arrow keys also work.
    WEST_KEY = 'a'
    EAST_KEY = 'd'
    NORTH_KEY = 'w'
    SOUTH_KEY = 's'
    STOP_KEY = 'q'

    def __init__(self, index=0):
        super().__init__()
        self.last_move = Directions.STOP
        self.index = index
        self.keys = []

    def get_action(self, state):
        keys = keys_waiting() + keys_pressed()
        if keys:
            self.keys = keys

        legal = state.getLegalActions(self.index)
        move = self.get_move(legal)

        if move == Directions.STOP:
            # Try to move in the same direction as before
            if self.last_move in legal:
                move = self.last_move

        if (self.STOP_KEY in self.keys) and Directions.STOP in legal:
            move = Directions.STOP

        if move not in legal:
            move = random.choice(legal)

        self.last_move = move
        return move

    def get_move(self, legal):
        """Get the move for the pac"""
        north = Directions.NORTH in legal
        south = Directions.SOUTH in legal
        west = Directions.WEST in legal
        east = Directions.EAST in legal
        move = Directions.STOP
        if (self.WEST_KEY in self.keys or 'Left' in self.keys) and west:
            move = Directions.WEST
        if (self.EAST_KEY in self.keys or 'Right' in self.keys) and east:
            move = Directions.EAST
        if (self.NORTH_KEY in self.keys or 'Up' in self.keys) and north:
            move = Directions.NORTH
        if (self.SOUTH_KEY in self.keys or 'Down' in self.keys) and south:
            move = Directions.SOUTH
        return move


class KeyboardAgent2(KeyboardAgent):
    """
    A second agent controlled by the keyboard.
    """
    # NOTE: Arrow keys also work.
    WEST_KEY = 'j'
    EAST_KEY = "l"
    NORTH_KEY = 'i'
    SOUTH_KEY = 'k'
    STOP_KEY = 'u'

    def get_move(self, legal):
        move = Directions.STOP
        if (self.WEST_KEY in self.keys) and Directions.WEST in legal:
            move = Directions.WEST
        if (self.EAST_KEY in self.keys) and Directions.EAST in legal:
            move = Directions.EAST
        if (self.NORTH_KEY in self.keys) and Directions.NORTH in legal:
            move = Directions.NORTH
        if (self.SOUTH_KEY in self.keys) and Directions.SOUTH in legal:
            move = Directions.SOUTH
        return move


def remap_arrows(event):
    " TURN ARROW PRESSES INTO LETTERS (SHOULD BE IN KEYBOARD AGENT) "
    if event.char in ['a', 's', 'd', 'w']:
        return
    if event.keycode in [37, 101]:  # LEFT ARROW (win / _x)
        event.char = 'a'
    if event.keycode in [38, 99]:  # UP ARROW
        event.char = 'w'
    if event.keycode in [39, 102]:  # RIGHT ARROW
        event.char = 'd'
    if event.keycode in [40, 104]:  # DOWN ARROW
        event.char = 's'

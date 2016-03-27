import abc

from random import choice
from game import Rules

class Agent(object):
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_action(self, state):
        """ returns an action from a state according to a procedure defined in the subclass. """
        return

''' Agent that picks a random move from a list of avaliable moves. '''
class RandomAgent(Agent):

    def get_action(self, state):
        if state is None: raise ValueError("RandomAgent - get_state: state should not be None!")

        aval_moves = Rules.avaliable_moves(state)

        if len(aval_moves) != 0: return choice(aval_moves)
        else: return 0

''' Agent that picks the move that maximizes utility assuming the opponent is playing to minimize utility. '''
class MiniMaxAgent(Agent):

    def get_action(self, state):
        if state is None: raise ValueError("MiniMaxAgent - get_state: state should not be None!")
        return 0 # Do nothing for now.

    #TODO: implement this.
    def __mini_max(self, state, max):
        if Rules.is_terminal_state(state):
            pass

        if max:
            pass
        else: # min
            pass
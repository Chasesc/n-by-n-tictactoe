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

# TODO: Implement Alpha–beta pruning for improved performance
''' Agent that picks the move that maximizes utility assuming the opponent is playing to minimize utility. '''
class MiniMaxAgent(Agent):

    debug = False # TODO: Remove this once complete

    def get_action(self, state):
        if state is None: raise ValueError("MiniMaxAgent - get_state: state should not be None!")
        utility, action = self.max_value(state, 4)
        return action

    def max_value(self, state, depth):
        if Rules.is_terminal_state(state) or depth == 0: # terminal-test
            return (self.utility(state, Rules.ai_piece), 0)

        avaliable_actions = Rules.avaliable_moves(state)
        maximum = -float('inf')
        best_action = None        

        for action in avaliable_actions:
            new_state = self.result(state, action, Rules.ai_piece)
            new_max = self.min_value(new_state, depth - 1)[0]
            if maximum <= new_max:
                maximum, best_action = new_max, action

        if self.debug:
            print "max: (1/2) ", avaliable_actions, " ", state
            print "max: (2/2) ", (maximum, best_action), " ", depth
            raw_input()

        return (maximum, best_action)

    def min_value(self, state, depth):
        if Rules.is_terminal_state(state) or depth == 0: # terminal-test
            return (self.utility(state, Rules.player_piece), 0)

        avaliable_actions = Rules.avaliable_moves(state)
        minimum = float('inf')
        best_action = None

        for action in avaliable_actions:
            new_state = self.result(state, action, Rules.player_piece)
            new_min = self.max_value(new_state, depth - 1)[0]
            if minimum >= new_min:
                minimum, best_action = new_min, action

        if self.debug:
            print "min: (1/2) ", avaliable_actions, " ", state
            print "min: (2/2) ", (minimum, best_action), " ", depth
            raw_input()
       
        return (minimum, best_action)

    # returns a new state which is the result of a given action and piece
    def result(self, state, action, piece):
        # make a new copy instead of using the reference and changing the actual gameboard
        new_state = [p for p in state] 
        new_state[action] = piece
        return new_state


    # returns the utility of a state of a given state
    def utility(self, state, piece):
        other_piece = 'X' if piece == 'O' else 'O'

        if Rules.has_won(state, piece):
            return 1
        elif Rules.has_won(state, other_piece):
            return -1
        else:
            return 0
#!/usr/bin/env python3
"""Part of 'adventure_game'. Tiles file."""
__author__ = "Matt Bingham"
__email__ = "mattbingham@outlook.com"


import items


class MapTile:
	"""Movement grid"""
	def __init__(self, x, y):
		self.x = x
		self.y = y

def intro_text(self):
    raise NotImplementedError()
 
def modify_player(self, player):
    raise NotImplementedError()

class StartingRoom(MapTile):
    def intro_text(self):
        return """
        You find yourself on a beach, with a wrecked boat and a flickering lamp.
        You have no clear strategy, but can make out four paths.
        """
 
    def modify_player(self, player):
        #Room has no action on player
        pass
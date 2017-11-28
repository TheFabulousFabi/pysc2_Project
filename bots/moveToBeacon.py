###python -m pysc2.bin.agent --map MoveToBeacon --agent moveToBeacon.MoveToBeacon


from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import time
import numpy

from pysc2.agents import base_agent
from pysc2.lib import actions
from pysc2.lib import features

_PLAYER_RELATIVE = features.SCREEN_FEATURES.player_relative.index
_PLAYER_NEUTRAL = 3  # beacon ID
_NO_OP = actions.FUNCTIONS.no_op.id
_MOVE_SCREEN = actions.FUNCTIONS.Move_screen.id

_SELECT_ARMY = actions.FUNCTIONS.select_army.id
_NOT_QUEUED = [0]
_SELECT_ALL = [0]


class MoveToBeacon(base_agent.BaseAgent):

  def step(self, obs):
    super(MoveToBeacon, self).step(obs)
    if _MOVE_SCREEN in obs.observation["available_actions"]:

      #time.sleep(0.5)
      player_relative = obs.observation["screen"][_PLAYER_RELATIVE]
      neutral_y, neutral_x = (player_relative == _PLAYER_NEUTRAL).nonzero()
      
      if not neutral_y.any():
        return actions.FunctionCall(_NO_OP, [])

      target = [int(neutral_x.mean()), int(neutral_y.mean())]
      return actions.FunctionCall(_MOVE_SCREEN, [_NOT_QUEUED, target])

    else:
      return actions.FunctionCall(_SELECT_ARMY, [_SELECT_ALL])

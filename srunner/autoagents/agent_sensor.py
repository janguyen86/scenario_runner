from __future__ import print_function

import carla

from srunner.autoagents.sensor_interface import SensorInterface
from srunner.scenariomanager.timer import GameTime
from srunner.tools.route_manipulation import downsample_route

from srunner.autoagents.autonomous_agent import AutonomousAgent

class AgentSensor(AutonomousAgent):

    def __init__(self, width, height): 
        self._width = width 
        self._height = height 
        self._surface = None 
    
    def run_step(self, input_data, timestamp):
        #TODO: output agent's sensor data 
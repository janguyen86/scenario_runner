from __future__ import print_function

import carla

from srunner.autoagents.sensor_interface import SensorInterface
from srunner.scenariomanager.timer import GameTime
from srunner.tools.route_manipulation import downsample_route
from agent_wrapper import setup_sensors
from srunner.autoagents.autonomous_agent import AutonomousAgent

class AgentSensor(AutonomousAgent):
    _sensors = None 

    def __init__(self,
                 vehicle,
                 agent_config,
                 debug_mode=False):
        self.agent_id = agent_config.name
        self.sensor_interface = SensorInterface()
        self.vehicle = vehicle
        self.debug_mode = debug_mode
    
    @staticmethod
    def get_sensors():
        return AgentSensor._sensors
    
    def run_step(self, agent):
        #TODO: output agent's sensor data 
        sensor_data = self.sensor_interface.get_data()
        agent.setup_sensors(self.vehicle)
        return sensor_data
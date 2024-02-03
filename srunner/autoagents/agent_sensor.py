from __future__ import print_function

import carla

from srunner.autoagents.sensor_interface import SensorInterface
from agent_wrapper import AgentWrapper
from srunner.autoagents.autonomous_agent import AutonomousAgent
from srunner.scenariomanager.carla_data_provider import CarlaDataProvider

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
        self.data_provider = None 

    @staticmethod
    def get_sensors():
        """
        Get agent's sensors. 
        """
        return AgentSensor._sensors
    
    #TODO: Create local CarlaDataProvider 
    def get_data_provider(self): 
        """
        Create local CarlaDataProvider
        """
        self.data_provider = CarlaDataProvider() 

    #TODO: Create local setup_sensor called once at beginning of scenario 
    def setup_sensors(self, agent):
        agent.AgentWrapper.setup_sensors_local()

    #TODO: Execute run_step at every step
    def run_step(self):
        """
        Take sensor and output action. 
        """
        sensor_data = self.sensor_interface.get_data()
        return sensor_data
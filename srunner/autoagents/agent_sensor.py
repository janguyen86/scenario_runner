from __future__ import print_function

import carla

from srunner.autoagents.sensor_interface import SensorInterface
# from srunner.autoagents.agent_wrapper import AgentWrapper
from srunner.autoagents.autonomous_agent import AutonomousAgent
from srunner.scenariomanager.carla_data_provider import CarlaDataProvider
from srunner.autoagents.sensor_interface import CallBack

class AgentSensor(AutonomousAgent):
    _agent = None 
    _sensors_list = [] 

    def __init__(self,
                 debug_mode=False):
        self._agent = None 
        self._sensors = None
        self._vehicle = None 
        self.sensor_interface = SensorInterface()
        self.debug_mode = debug_mode
        self.data_provider = None 
    

    # @staticmethod
    def get_sensors(self):
        """
        Get agent's sensors. 
        """
        self._sensors = self._agent._sensors


    def get_data_provider(self): 
        """
        Create local CarlaDataProvider
        """
        self.data_provider = CarlaDataProvider() 


    def setup_sensors_local(self, vehicle, agent, debug_mode=False):
        """
        Create the sensors defined by the user and attach them to the ego-vehicle
        :param vehicle: ego vehicle
        :return:
        """
        self.get_sensors()
        bp_library = self.data_provider.get_world().get_blueprint_library()
        print(self._agent)
        for sensor_spec in self.sensors():
            # These are the sensors spawned on the carla world
            bp = bp_library.find(str(sensor_spec['type']))
            if sensor_spec['type'].startswith('sensor.camera'):
                bp.set_attribute('image_size_x', str(sensor_spec['width']))
                bp.set_attribute('image_size_y', str(sensor_spec['height']))
                bp.set_attribute('fov', str(sensor_spec['fov']))
                sensor_location = carla.Location(x=sensor_spec['x'], y=sensor_spec['y'],
                                                 z=sensor_spec['z'])
                sensor_rotation = carla.Rotation(pitch=sensor_spec['pitch'],
                                                 roll=sensor_spec['roll'],
                                                 yaw=sensor_spec['yaw'])
            elif sensor_spec['type'].startswith('sensor.lidar'):
                bp.set_attribute('range', str(sensor_spec['range']))
                bp.set_attribute('rotation_frequency', str(sensor_spec['rotation_frequency']))
                bp.set_attribute('channels', str(sensor_spec['channels']))
                bp.set_attribute('upper_fov', str(sensor_spec['upper_fov']))
                bp.set_attribute('lower_fov', str(sensor_spec['lower_fov']))
                bp.set_attribute('points_per_second', str(sensor_spec['points_per_second']))
                sensor_location = carla.Location(x=sensor_spec['x'], y=sensor_spec['y'],
                                                 z=sensor_spec['z'])
                sensor_rotation = carla.Rotation(pitch=sensor_spec['pitch'],
                                                 roll=sensor_spec['roll'],
                                                 yaw=sensor_spec['yaw'])
            elif sensor_spec['type'].startswith('sensor.other.gnss'):
                sensor_location = carla.Location(x=sensor_spec['x'], y=sensor_spec['y'],
                                                 z=sensor_spec['z'])
                sensor_rotation = carla.Rotation()

            # create sensor
            sensor_transform = carla.Transform(sensor_location, sensor_rotation)
            sensor = self.data_provider.get_world().spawn_actor(bp, sensor_transform, vehicle)
            # setup callback
            sensor.listen(CallBack(sensor_spec['id'], sensor, agent.sensor_interface))
            self._sensors_list.append(sensor)


    def setup_sensors(self, vehicle, agent):
        self.get_data_provider()
        self._agent = agent 
        self._vehicle = vehicle
        self.setup_sensors_local(vehicle, agent)


    #TODO: Execute run_step at every step
    def run_step(self, input_data, timestamp):
        """
        Take sensor and output action. 
        """
        control = carla.VehicleControl()
        sensor_data = self.sensor_interface.get_data()
        return control
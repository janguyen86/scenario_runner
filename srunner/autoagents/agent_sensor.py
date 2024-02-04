from __future__ import print_function

import carla

from srunner.autoagents.sensor_interface import SensorInterface
from agent_wrapper import AgentWrapper
from srunner.autoagents.autonomous_agent import AutonomousAgent
from srunner.scenariomanager.carla_data_provider import CarlaDataProvider
from srunner.autoagents.sensor_interface import CallBack

class AgentSensor(AutonomousAgent):
    _sensors = None 
    _agent = None 
    
    def __init__(self,
                 vehicle,
                 debug_mode=False):
        # self.agent_id = agent_config.name
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
        bp_library = self.data_provider .get_world().get_blueprint_library()
        for sensor_spec in self._agent.sensors():
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
            sensor = self.data_provider .get_world().spawn_actor(bp, sensor_transform, vehicle)
            # setup callback
            sensor.listen(CallBack(sensor_spec['id'], sensor, agent.sensor_interface))
            self._sensors_list.append(sensor)
        
        # Tick once to spawn the sensors
        self.data_provider .get_world().tick()
    
    def setup_sensors(self, agent):
        agent.setup_sensors_local()

    #TODO: Execute run_step at every step
    def run_step(self, input_data, timestamp):
        """
        Take sensor and output action. 
        """
        control = carla.VehicleControl()
        sensor_data = self.sensor_interface.get_data()
        return control
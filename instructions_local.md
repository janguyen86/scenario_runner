# Instructions to Run Scenario Runner with Local Carla Data Provider 

## Build the Carla docker image
```commandline 
sudo docker pull carlasim/carla:0.9.15 
```

## Install Correct Verision of Python Packages

```commandline 
python3 -m pip install -r requirements.txt
```

## Run Carla server on Docker 
```commandline
sudo docker run --privileged --gpus all --net=host -e DISPLAY=$DISPLAY carlasim/carla:0.9.15 /bin/bash ./CarlaUE4.sh
```

## Run Route Scenario 

### Example Route Scenario 
Run route scenario
```commandline 
python scenario_runner.py --route /home/janice/scenario_runner/srunner/data/routes_town10.xml --route-id 0 --agent srunner/autoagents/npc_agent.py
```

Start manual control agent 
```commandline 
python3 manual_control.py 
```

Debug mode 
```commandline 
--route /home/janice/scenario_runner/srunner/data/routes_town10.xml --route-id 0 --agent srunner/autoagents/npc_agent.py
```

### Single Sensor Agent 
Run route scenario
```commandline 
python scenario_runner.py --route /home/janice/scenario_runner/srunner/data/routes_town10.xml --route-id 0 --agent srunner/autoagents/human_agent.py
```

Start manual control agent 
```commandline 
python3 manual_control.py 
```

### Multiple Sensor Agent 
Run route scenario
```commandline 
python scenario_runner.py --route /home/janice/scenario_runner/srunner/examples/RouteOb.xml --route-id 0 --agent srunner/autoagents/npc_agent.py
```

Start manual control agent for each ego vehicle 
```commandline 
python3 manual_control.py --rolename hero
```

```commandline 
python3 manual_control.py --rolename hero2
```

## Debugging Mode 
 Run carla server 

 ```commandline 
 sudo docker run --privileged --gpus all --net=host -e DISPLAY=$DISPLAY carlasim/carla:0.9.15 /bin/bash ./CarlaUE4.sh
 ```

 Run debug mode with Arguements 
 ```commandline
 --route /home/janice/scenario_runner/srunner/examples/AgentSensor.xml 
 ```


## Multi_agent Type Scenario Runner 
Run route scenario
```commandline 
python scenario_runner_local.py --route /home/janice/scenario_runner/srunner/examples/AgentSensor.xml
```

Start manual control agent for each ego vehicle 
```commandline 
python3 manual_control.py --rolename hero
```

```commandline 
python3 manual_control.py --rolename hero2
```

# New Files added 

/srunner/autoagents/agent_sensor.py 

/srunner/examples/agent_sensor.xml (incomplete)

/scenariomanager/scenario_manager_local.py 

/scenario_runner_local.py 

/sruuner/scenarios/route_scenario_local.py 

/srunner/tools/route_parser_local.py

/srunner/scenarioconfigs/route_scenario_configuration_local.py
# Instructions to Run Scenario Runner with Local Carla Data Provider 

## Build the Carla docker image
```commandline 
sudo docker pull carlasim/carla:0.9.15 
```

## Run Carla server on Docker 
```commandline
sudo docker run --privileged --gpus all --net=host -e DISPLAY=$DISPLAY carlasim/carla:0.9.15 /bin/bash ./CarlaUE4.sh
```
## Install Correct Verision of Python Packages

```commandline 
python3 -m pip install -r requirements.txt
```

## Run Multi-Ego Vehicle Scenario Runner natively

Run a scenario
```commandline
python3 scenario_runner_local.py /scenario_runner/srunner/routes_debug.xml scenario_runner/srunner/data/all_towns_traffic_scenarios1_3_4.json 0 --agent srunner/autoagents/agent_sensor.py
```

Ex Route Scenario 
```commandline 
python scenario_runner.py --route /scenario_runner/srunner/routes_debug.xml /scenario_runner/srunner/data/all_towns_traffic_scenarios1_3_4.json 0 --agent srunner/autoagents/npc_agent.py
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

/srunner/examples/agent_sensor.xml

/scenariomanager/scenario_manager_local.py 

/scenario_runner_local.py 
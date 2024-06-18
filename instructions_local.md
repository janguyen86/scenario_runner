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

## Run Original Route Scenario 

### Single Agent
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

### Multiple Agent 
Run route scenario
```commandline 
python scenario_runner.py --route /home/janice/scenario_runner/srunner/data/routes_town10.xml --route-id 0 --agent srunner/autoagents/npc_agent.py
```

Start manual control agent for each ego vehicle 
```commandline 
python3 manual_control.py --rolename hero
```

```commandline 
python3 manual_control.py --rolename hero2
```

## Run Local Files  
 Run carla server 

 ```commandline 
 sudo docker run --privileged --gpus all --net=host -e DISPLAY=$DISPLAY carlasim/carla:0.9.15 /bin/bash ./CarlaUE4.sh
 ```

Run route scenario using `scenario_runner_local.py`
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
 Run debug mode for `scenario_runner_local.py` with Arguments 
 ```commandline
 --route /home/janice/scenario_runner/srunner/examples/AgentSensor.xml 
 ```

## Debug Files  
 Run carla server 

 ```commandline 
 sudo docker run --privileged --gpus all --net=host -e DISPLAY=$DISPLAY carlasim/carla:0.9.15 /bin/bash ./CarlaUE4.sh
 ```

Run route scenario using `scenario_runner_debug.py`
```commandline 
python scenario_runner_debug.py --route /home/janice/scenario_runner/srunner/examples/AgentSensorDebug.xml --agent srunner/autoagents/human_agent.py
```

Start manual control agent 
```commandline 
python3 manual_control.py 
```

 Run debug mode for `scenario_runner_debug.py` with Arguments 
 ```commandline
 --route /home/janice/scenario_runner/srunner/examples/AgentSensorDebug.xml --agent srunner/autoagents/human_agent.py
 ```

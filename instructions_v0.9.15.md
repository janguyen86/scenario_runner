# Instructions to Run Scenario Runner v0.9.15 Natively 

## Build the Carla docker image
```commandline 
sudo docker pull carlasim/carla:0.9.15 
```

## Run Carla server on Docker 
```commandline
sudo docker run --privileged --gpus all --net=host -e DISPLAY=$DISPLAY carlasim/carla:0.9.15 /bin/bash ./CarlaUE4.sh
```
## Install Correct Verision 

```commandline 
python3 -m pip install -r requirements.txt
```

## Run Multi-Ego Vehicle Scenario Runner natively

Run a scenario
```commandline
python3 scenario_runner.py --scenario MultiEgo_1 --reloadWorld
```

Start manual control agent for each ego vehicle
```commandline 
python3 manual_control.py --rolename hero
```

```commandline 
python3 manual_control.py --rolename hero2
```

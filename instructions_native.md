# Instructions to Run v0.9.15 Natively 

Run server on Docker 
```commandline
sudo docker run --privileged --gpus all --net=host -e DISPLAY=$DISPLAY carlasim/carla:0.9.15 /bin/bash ./CarlaUE4.sh
```

Run Scenario Runner native;y
```commandline
python3 scenario_runner.py --scenario FollowLeadingVehicle_11_multi --reloadWorld
```
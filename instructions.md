## Carla Docker Image 

```commandline
sudo docker pull hangqiu/carla:0.9.13
```

## Scenario Docker Image 

```commandline
sudo docker build -t hangqiu/srunner:0.9.13 --file ./srunner.Dockerfile .
```

## Run Scenario Runner 

Start the carla server
```commandline
sudo docker run --privileged --gpus all --net=host -e DISPLAY=$DISPLAY \
    -v /usr/share/vulkan/icd.d:/usr/share/vulkan/icd.d \
    hangqiu/carla:0.9.13 \
    /bin/bash /opt/carla-simulator/CarlaUE4.sh
```

Run multi-ego vehicle scenario runner 
```commandline
sudo docker run -it --privileged --gpus all --net=host -e DISPLAY=$DISPLAY \
    -v /usr/share/vulkan/icd.d:/usr/share/vulkan/icd.d  \
    janice/srunner:0.9.13  \
    /bin/python3 scenario_runner.py --scenario FollowLeadingVehicle_11_multi --reloadWorld
```
Starting manual control agent for each ego vehicle 

Hero0
 ```commandline 
 sudo docker run -it --privileged --gpus all --net=host -e DISPLAY=$DISPLAY \
    -v /usr/share/vulkan/icd.d:/usr/share/vulkan/icd.d \
    hangqiu/srunner:0.9.13 \
    /bin/python3 manual_control.py --rolename hero0
 ```

 Hero1
 ```commandline 
 sudo docker run -it --privileged --gpus all --net=host -e DISPLAY=$DISPLAY \
    -v /usr/share/vulkan/icd.d:/usr/share/vulkan/icd.d \
    hangqiu/srunner:0.9.13 \
    /bin/python3 manual_control.py --rolename hero1
 ```
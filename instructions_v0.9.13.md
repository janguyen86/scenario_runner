# Scenario Runner v0.9.13

## Carla Docker Image (v0.9.13)

```commandline
sudo docker pull hangqiu/srunner:0.9.13
```

## Scenario Docker Image (v0.9.13)

```commandline
sudo docker build -t janice/srunner:0.9.13 --file ./srunner13.Dockerfile . --no-cache
```

## Run Scenario Runner for Multiple Ego Vehicles (v0.9.13)

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
    /bin/python3 scenario_runner.py --scenario MultiEgo_1 --reloadWorld
```

Starting manual control agent for each ego vehicle 

Hero
 ```commandline 
 sudo docker run -it --privileged --gpus all --net=host -e DISPLAY=$DISPLAY \
    -v /usr/share/vulkan/icd.d:/usr/share/vulkan/icd.d \
    hangqiu/srunner:0.9.13 \
    /bin/python3 manual_control.py --rolename hero
 ```

 Hero2
 ```commandline 
 sudo docker run -it --privileged --gpus all --net=host -e DISPLAY=$DISPLAY \
    -v /usr/share/vulkan/icd.d:/usr/share/vulkan/icd.d \
    hangqiu/srunner:0.9.13 \
    /bin/python3 manual_control.py --rolename hero2
 ```
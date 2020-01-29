This ros2 project implements the example ament_x build-type described in ros2cli/ros2pkg/build-type/README.md.

*Note - at the time of this writing, pluggable build-types have not been merged to ros2cli. This README will be updates when build-types are generally available in the ros2 cli.*

To include the ament_x build-type into your ros2 environment do the following:

### Clone this repo
```
git clone https://github.com/wayneparrott/ament_x_buildtype
```

### Build the project using ros2 colcon
```
cd ament_x_buildtype
colcon build
```

### Add ament_x build-type to your ros2 environment
DON"T SKIP THIS STEP
```
source ament_x/install/local_setup.bash
```

### Confirm ament_x build-type is availble
List the ros2 package creation commandline args and confirm ament_x is included among the recognized build-types. 
```
> ros2 pkg create -h

usage: ros2 pkg create [-h] [--package-format {2,3}]
                       [--description DESCRIPTION] [--license LICENSE]
                       [--destination-directory DESTINATION_DIRECTORY]
                       [--build-type {ament_cmake,ament_python,ament_x,cmake}]
                       [--dependencies DEPENDENCIES [DEPENDENCIES ...]]
                       [--maintainer-email MAINTAINER_EMAIL]
                       [--maintainer-name MAINTAINER_NAME]
                       [--node-name NODE_NAME] [--library-name LIBRARY_NAME]
                       package_name
```

### Create ros package with ament_x build-type
```
ros2 pkg create --build-type ament_x my_x_project
```


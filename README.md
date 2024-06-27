# autonomous-systems

## CARLA Simulation
This component runs a simple CARLA simulation for an autonomous vehicle.

### Setup
1. Follow the [CARLA installation guide](https://carla.readthedocs.io/en/latest/start_quickstart/).
2. Set up the Python environment:
    ```sh
    source ../auto_systems_env/bin/activate
    ```

### Running the Simulation
```sh
./scripts/run_carla.sh
```

### Data Collection
```sh
python data_collection.py
```

## MuJoCo Simulation
This component runs a simple MuJoCo simulation for a robot model, with a C++ controller for performance-critical tasks.

### Setup
1. Follow the MuJoCo installation guide.
2. Set up the Python environment:
```sh
source ../auto_systems_env/bin/activate
```
3. Build the C++ controller:
```sh
cd mujoco_simulation
mkdir build
cd build
cmake ..
make
```
### Running the Simulation
```sh
./scripts/run_mujoco.sh
```

import carla
import random
import time

def main():
    client = carla.Client('localhost', 2000)
    client.set_timeout(10.0)

    world = client.get_world()
    blueprint_library = world.get_blueprint_library()
    vehicle_bp = blueprint_library.filter('vehicle.tesla.model3')[0]

    spawn_points = world.get_map().get_spawn_points()
    spawn_point = random.choice(spawn_points)

    vehicle = world.spawn_actor(vehicle_bp, spawn_point)
    vehicle.set_autopilot(True)

    time.sleep(10)

    vehicle.destroy()

if __name__ == '__main__':
    main()

import carla
import cv2
import numpy as np

client = carla.Client('localhost', 2000)
client.set_timeout(10.0)

world = client.get_world()
blueprint_library = world.get_blueprint_library()
vehicle_bp = blueprint_library.filter('vehicle.tesla.model3')[0]
spawn_points = world.get_map().get_spawn_points()
spawn_point = random.choice(spawn_points)

vehicle = world.spawn_actor(vehicle_bp, spawn_point)
camera_bp = blueprint_library.find('sensor.camera.rgb')
camera_bp.set_attribute('image_size_x', '800')
camera_bp.set_attribute('image_size_y', '600')
camera_bp.set_attribute('fov', '90')
camera_transform = carla.Transform(carla.Location(x=1.5, z=2.4))
camera = world.spawn_actor(camera_bp, camera_transform, attach_to=vehicle)

def process_image(image):
    array = np.frombuffer(image.raw_data, dtype=np.dtype("uint8"))
    array = np.reshape(array, (image.height, image.width, 4))
    array = array[:, :, :3]  # Remove alpha channel
    cv2.imshow("Camera", array)
    cv2.waitKey(1)

camera.listen(lambda image: process_image(image))
vehicle.set_autopilot(True)

time.sleep(10)

camera.stop()
vehicle.destroy()


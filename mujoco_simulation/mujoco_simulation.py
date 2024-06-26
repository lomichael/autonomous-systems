import mujoco_py
import numpy as np
from mujoco_py import load_model_from_path, MjSim, MjViewer

model = load_model_from_path("path_to_your_mujoco_model.xml")
sim = MjSim(model)
viewer = MjViewer(sim)

while True:
    sim.step()
    viewer.render()


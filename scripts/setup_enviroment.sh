#!/bin/bash
python3 -m venv auto_systems_env
source auto_systems_env/bin/activate
pip install torch torchvision gym opencv-python-headless carla mujoco-py

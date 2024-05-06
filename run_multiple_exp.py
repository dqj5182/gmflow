import os
import subprocess


target_dir = 'data/CLOIT/crop_images'
target_folders = os.listdir(target_dir)

output_dir = 'output'


for each_folder in target_folders:
    each_dir = os.path.join(target_dir, each_folder)
    each_out_dir = os.path.join(output_dir, each_folder)
    subprocess.call(["python", "main.py",  "--inference_dir", each_dir, "--output_path", each_out_dir, "--resume", "pretrained/gmflow_sintel-0c07dcb3.pth"])
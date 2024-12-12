import os
import sys

script_directory = os.path.dirname(os.path.abspath(sys.argv[0]))
instances_directory = os.path.join(script_directory, "instances")

os.makedirs(instances_directory, exist_ok=True)

for i in range(10, 160, 10):
    print(f"Creating instance {i:04d}")
    instance_path = os.path.join(instances_directory, f"bomb_{i:04d}.lp")
    with open(instance_path, "w") as f:
        f.write(f"input_length({i}).\n")

instances_directory = os.path.join(script_directory, "instances_many")

os.makedirs(instances_directory, exist_ok=True)

for i in range(10, 160, 10):
    for t in range(1, 5):
        print(f"Creating instance {i:04d}_{t:02d}")
        instance_path = os.path.join(instances_directory, f"bomb_{i:04d}_{t:02d}.lp")
        with open(instance_path, "w") as f:
            f.write(f"input_length({i}).\n")
            f.write(f"input_toilets({t}).\n")

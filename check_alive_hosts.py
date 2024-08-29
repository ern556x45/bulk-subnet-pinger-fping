import subprocess
import time
import os
import sys

input_file = 'subnets.txt'

output_file = 'alive_hosts.txt'

if os.path.exists(output_file):
    os.remove(output_file)
    print(f"{output_file} has been deleted.")

with open(input_file, 'r') as file:
    subnets = file.readlines()

total_subnets = len(subnets)
current_progress = 0

for subnet in subnets:
    subnet = subnet.strip()
    if not subnet:
        continue

    print(f"\nProcessing subnet: {subnet}")
    
    try:
        result = subprocess.run(['fping', '-g', subnet], capture_output=True, text=True)
        print("2s Delay to avoid ISP blocking")
        time.sleep(2)
        
        alive_hosts = [line for line in result.stdout.splitlines() if "alive" in line]
        
        if not alive_hosts:
            print(f"No IPs were reachable in subnet {subnet}.")

        with open(output_file, 'a') as f:
            for host in alive_hosts:
                f.write(host + '\n')
    
    except subprocess.CalledProcessError as e:
        print(f"Error processing subnet {subnet}. Please check the syntax: {e}")
    except FileNotFoundError:
        print(f"Error: The command 'fping' was not found. Make sure it is installed and accessible.")

    current_progress += 1
    progress_percentage = (current_progress / total_subnets) * 100
    progress_bar_length = 50
    filled_length = int(progress_bar_length * current_progress // total_subnets)
    bar = '=' * filled_length + '-' * (progress_bar_length - filled_length)
    sys.stdout.write(f'\rProgress: [{bar}] {progress_percentage:.2f}%')
    sys.stdout.flush()
    print("\n")

print(f"\n\nResults saved to {output_file}")
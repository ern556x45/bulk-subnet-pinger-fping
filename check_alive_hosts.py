import subprocess
import time
import os
from tqdm import tqdm

def read_input_file(filename):
    with open(filename, 'r') as file:
        subnets = file.readlines()
    return subnets

def delete_file(filename):
    if os.path.exists(filename):
        os.remove(filename)
        print(f"{filename} has been deleted.")    
        
        
def print_above_bar(text, pbar):
    # Clear the progress bar line by moving up and clearing it
    pbar.clear(nolock=True)   
    #print text
    print(text)  
    # Reprint the progress bar after the print statement
    pbar.refresh()
    
def append_results(alive_hosts, output_file):  
    with open(output_file, 'a') as f:
        for host in alive_hosts:
            f.write(host + '\n')
            
def launch_fping(subnet, pbar):
    try:
        #do the fping to get active subnets
        result = subprocess.run(['fping', '-g', subnet], capture_output=True, text=True)
        print_above_bar("1s Delay to avoid ISP blocking", pbar)
        time.sleep(2)          
    except subprocess.CalledProcessError as e:
        print_above_bar(f"Error processing subnet {subnet}. Please check the syntax: {e}", pbar)
    except FileNotFoundError:
        print_above_bar(f"Error: The command 'fping' was not found. Make sure it is installed and accessible.", pbar)
    
    alive_hosts = [line for line in result.stdout.splitlines() if "alive" in line]
    
    if not alive_hosts:
        print_above_bar(f"No IPs were reachable in subnet {subnet}.", pbar)
        
    return alive_hosts
    
    

def ping_subnets(subnets, output_file='alive_hosts.txt'):
    #delete old results file
    delete_file(output_file)
    
    # Initialize the progress bar
    pbar = tqdm(total=100, desc="Progress", ncols=100, leave=False)

    total_subnets = len(subnets)

    #loop subnets
    for subnet in subnets:
        subnet = subnet.strip()
        if not subnet:
            continue
        
        print_above_bar(f"\nProcessing subnet: {subnet}", pbar)
        
        #check for alive hosts
        alive_hosts = launch_fping(subnet, pbar)
        #save results
        append_results(alive_hosts, output_file)
        
        progress_percentage = round((1 / total_subnets) * 100,2)
        
        # Update the progress bar
        pbar.update(progress_percentage)

    print(f"\n\nResults saved to {output_file}")

if __name__ == "__main__":
    subnets = read_input_file("./subnets.txt")
    ping_subnets(subnets)
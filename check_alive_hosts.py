import subprocess

# Input file with subnets
input_file = 'subnets.txt'

# Output file to store the results
output_file = 'alive_hosts.txt'

# Clear the output file if it exists
with open(output_file, 'w') as f:
    pass  # Opening the file in 'w' mode clears it

# Read each subnet from the input file
with open(input_file, 'r') as file:
    subnets = file.readlines()

# Loop through each subnet and run the fping command
for subnet in subnets:
    subnet = subnet.strip()  # Remove any leading/trailing whitespace
    print(f"Processing subnet: {subnet}")
    
    try:
        # Run the fping command and capture the output
        result = subprocess.run(['fping', '-g', subnet], capture_output=True, text=True)
        
        # Filter the output for alive hosts
        alive_hosts = [line for line in result.stdout.splitlines() if "alive" in line]
        
        # Append the alive hosts to the output file
        with open(output_file, 'a') as f:
            for host in alive_hosts:
                f.write(host + '\n')
    
    except subprocess.CalledProcessError as e:
        print(f"Error processing subnet {subnet}: {e}")

print(f"Results saved to {output_file}")
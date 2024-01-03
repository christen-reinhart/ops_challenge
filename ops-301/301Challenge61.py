import subprocess

# Declare three variables
name = "John"
age = 25
city = "Ubuntu City"

# Print the values of the variables
print("Name:", name)
print("Age:", age)
print("City:", city)

# Execute the 'whoami' command using subprocess.run()
whoami_result = subprocess.run(['whoami'], capture_output=True, text=True)
print("\nResult of 'whoami' command:", whoami_result.stdout)

# Execute the 'ip a' command using subprocess.run()
ip_a_result = subprocess.run(['ip', 'a'], capture_output=True, text=True)
print("\nResult of 'ip a' command:\n", ip_a_result.stdout)

# Execute the 'lshw -short' command using subprocess.run()
lshw_result = subprocess.run(['lshw', '-short'], capture_output=True, text=True)
print("\nResult of 'lshw -short' command:\n", lshw_result.stdout)


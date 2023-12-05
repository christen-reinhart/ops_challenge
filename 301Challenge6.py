# Declare three variables

name = "John"
age = 25
city = "Ubuntu City"

# Print the values of the variables
print("Name:", name)
print("Age:", age)
print("City:", city)

# Execute the 'whoami' command using os.system()
whoami_result = os.popen('whoami').read()
print("\nResult of 'whoami' command:", whoami_result)

# Execute the 'ip a' command using os.system()
ip_a_result = os.popen('ip a').read()
print("\nResult of 'ip a' command:\n", ip_a_result)

# Execute the 'lshw -short' command using os.system()
lshw_result = os.popen('lshw -short').read()
print("\nResult of 'lshw -short' command:\n", lshw_result)
import requests

# Prompt user for URL
destination_url = input("Enter the destination URL: ")

# Display HTTP method options
print("Select an HTTP method:")
print("1. GET")
print("2. POST")
print("3. PUT")
print("4. DELETE")
print("5. HEAD")
print("6. PATCH")
print("7. OPTIONS")

# Get user's choice
method_choice = int(input("Enter your choice: "))

# Map user's choice to HTTP method
http_method = ""
if method_choice == 1:
    http_method = "GET"
elif method_choice == 2:
    http_method = "POST"
elif method_choice == 3:
    http_method = "PUT"
elif method_choice == 4:
    http_method = "DELETE"
elif method_choice == 5:
    http_method = "HEAD"
elif method_choice == 6:
    http_method = "PATCH"
elif method_choice == 7:
    http_method = "OPTIONS"
else:
    print("Invalid selection.")
    exit()

# Prepare confirmation message
confirmation_message = f"Sending {http_method} request to {destination_url}\nContinue? (y/n)"

# Get user confirmation
user_confirmation = input(confirmation_message).lower()

if user_confirmation != "y":
    print("Request cancelled.")
    exit()

# Send HTTP request
response = requests.request(http_method, destination_url)

# Translate status code to plain terms
status_code = response.status_code
status_message = {
    200: "OK",
    201: "Created",
    202: "Accepted",
    204: "No Content",
    301: "Moved Permanently",
    302: "Found",
    400: "Bad Request",
    401: "Unauthorized",
    403: "Forbidden",
    404: "Not Found",

    
405: "Method Not Allowed",
    500: "Internal Server Error",
    502: "Bad Gateway",
    503: "Service Unavailable",
}.get(status_code, "Unknown")

# Print response header information
print(f"\nResponse Status: {status_code} ({status_message})")
print(f"\nResponse Headers:")
for header, value in response.headers.items():
    print(f"{header}: {value}")

# Print request body (if applicable)
if http_method in ("POST", "PUT"):
    print(f"\nRequest Body: {response.request.body}")
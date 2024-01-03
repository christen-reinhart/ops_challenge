import requests

def translate_status_code(status_code):
    status_codes = {
        100: 'Continue',
        101: 'Switching Protocols',
        200: 'OK',
        201: 'Created',
        202: 'Accepted',
        203: 'Non-Authoritative Information',
        204: 'No Content',
        205: 'Reset Content',
        206: 'Partial Content',
        300: 'Multiple Choices',
        301: 'Moved Permanently',
        302: 'Found',
        303: 'See Other',
        304: 'Not Modified',
        305: 'Use Proxy',
        307: 'Temporary Redirect',
        400: 'Bad Request',
        401: 'Unauthorized',
        402: 'Payment Required',
        403: 'Forbidden',
        404: 'Not Found',
        405: 'Method Not Allowed',
        406: 'Not Acceptable',
        407: 'Proxy Authentication Required',
        408: 'Request Timeout',
        409: 'Conflict',
        410: 'Gone',
        411: 'Length Required',
        412: 'Precondition Failed',
        413: 'Payload Too Large',
        414: 'URI Too Long',
        415: 'Unsupported Media Type',
        416: 'Range Not Satisfiable',
        417: 'Expectation Failed',
        418: 'I\'m a teapot',
        500: 'Internal Server Error',
        501: 'Not Implemented',
        502: 'Bad Gateway',
        503: 'Service Unavailable',
        504: 'Gateway Timeout',
        505: 'HTTP Version Not Supported',
    }

    return status_codes.get(status_code, 'Unknown Status Code')

def main():
    # Prompt user for destination URL
    url = input("Enter the destination URL: ")

    # Prompt user to select HTTP Method
    http_method = input("Select HTTP Method (GET, POST, PUT, DELETE, HEAD, PATCH, OPTIONS): ").upper()

    # Print the entire request information and ask for confirmation
    print(f"\nSending {http_method} request to: {url}")
    confirmation = input("Do you want to proceed? (y/n): ").lower()

    if confirmation != 'y':
        print("Request aborted.")
        return

    # Perform the request
    response = requests.request(http_method, url)

    # Print translated status code
    print(f"\nResponse Status: {response.status_code} - {translate_status_code(response.status_code)}")

    # Print response header information
    print("\nResponse Headers:")
    for key, value in response.headers.items():
        print(f"{key}: {value}")

    # Print response content if available
    if response.content:
        print("\nResponse Content:")
        print(response.text)

if __name__ == "__main__":
    main()
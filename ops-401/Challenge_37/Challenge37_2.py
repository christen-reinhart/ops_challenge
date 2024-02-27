#!/usr/bin/env python3

# Script name: Cookie Monster's Cookie Fetcher
# Author: [Your Name]
# Date of Latest Revision: [Date]
# Sources: [List sources]
# Purpose: This script fetches a cookie from a website and sends it back to the site, capturing the response in an HTML file and opening it in Firefox.

import requests
import webbrowser

def fetch_cookie(target_site):
    """
    Fetches a cookie from the specified target site.
    
    Args:
    - target_site (str): The URL of the target site.
    
    Returns:
    - requests.cookies.RequestsCookieJar: The fetched cookie.
    """
    response = requests.get(target_site)
    return response.cookies

def send_cookie(cookie, target_site):
    """
    Sends the provided cookie back to the target site.
    
    Args:
    - cookie (requests.cookies.RequestsCookieJar): The cookie to be sent.
    - target_site (str): The URL of the target site.
    
    Returns:
    - str: The HTTP response text.
    """
    response = requests.get(target_site, cookies=cookie)
    return response.text

def generate_html_file(content):
    """
    Generates an HTML file with the provided content.
    
    Args:
    - content (str): The content to be written to the HTML file.
    """
    with open("response.html", "w") as file:
        file.write(content)
    print("HTML file generated successfully.")

def open_in_firefox():
    """
    Opens the generated HTML file in Firefox.
    """
    webbrowser.get("firefox").open("response.html")

def main():
    # Target site URL
    target_site = "http://www.whatarecookies.com/cookietest.asp"
    
    # Fetching cookie
    cookie = fetch_cookie(target_site)
    
    # Sending cookie back and capturing response
    http_response = send_cookie(cookie, target_site)
    
    # Generating HTML file
    generate_html_file(http_response)
    
    # Opening HTML file in Firefox
    open_in_firefox()

if __name__ == "__main__":
    main()

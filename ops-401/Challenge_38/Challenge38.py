#!/usr/bin/env python3

# Script name: Challenge: 401 Challenge 37
# Author: Christen Reinhart
# Date of Latest Revision: 02/27/2024
# Sources: https://chat.openai.com/share/a7aa2f2d-866b-4951-be1f-a62732fa5e85
# Purpose: Python script that detects for SQL vulnerability in the target web app.


# Import libraries
import requests
from pprint import pprint
from bs4 import BeautifulSoup as bs
from urllib.parse import urljoin

# Declare functions

# Function to get all forms from a given URL
def get_all_forms(url):
    soup = bs(requests.get(url).content, "html.parser")
    return soup.find_all("form")

# Function to get details of a form
def get_form_details(form):
    details = {}
    action = form.attrs.get("action").lower()
    method = form.attrs.get("method", "get").lower()
    inputs = []
    for input_tag in form.find_all("input"):
        input_type = input_tag.attrs.get("type", "text")
        input_name = input_tag.attrs.get("name")
        inputs.append({"type": input_type, "name": input_name})
    details["action"] = action
    details["method"] = method
    details["inputs"] = inputs
    return details

# Function to submit a form
def submit_form(form_details, url, value):
    target_url = urljoin(url, form_details["action"])
    inputs = form_details["inputs"]
    data = {}
    for input in inputs:
        if input["type"] == "text" or input["type"] == "search":
            input["value"] = value
        input_name = input.get("name")
        input_value = input.get("value")
        if input_name and input_value:
            data[input_name] = input_value

    if form_details["method"] == "post":
        return requests.post(target_url, data=data)
    else:
        return requests.get(target_url, params=data)

# Function to scan for XSS vulnerabilities
def scan_xss(url):
    forms = get_all_forms(url)
    print(f"[+] Detected {len(forms)} forms on {url}.")
    js_script = "<script>alert('XSS')</script>"  # HTTP and JS code to create an alert prompt with some text.
    is_vulnerable = False
    for form in forms:
        form_details = get_form_details(form)
        content = submit_form(form_details, url, js_script).content.decode()
        if js_script in content:
            print(f"[+] XSS Detected on {url}")  # Positive detection
            print(f"[*] Form details:")
            pprint(form_details)
            is_vulnerable = True
    return is_vulnerable

# Main function
if __name__ == "__main__":
    # Test with XSS-positive target URL
    positive_url = "https://xss-game.appspot.com/level1/frame"
    print("Testing positive URL:", positive_url)
    print(scan_xss(positive_url))

    # Test with XSS-negative target URL
    negative_url = "http://dvwa.local/login.php"
    print("Testing negative URL:", negative_url)
    print(scan_xss(negative_url))

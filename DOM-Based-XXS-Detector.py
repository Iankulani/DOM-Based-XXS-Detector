# -*- coding: utf-8 -*-
"""
Created on Fri Feb  21 03:345:47 2025

@author: IAN CARTER KULANI

"""

from colorama import Fore
import pyfiglet
import os
font=pyfiglet.figlet_format("DOM BASED XXS DETECTOR")
print(Fore.GREEN+font)

import requests
from urllib.parse import urljoin
import time

# Function to detect DOM-Based XSS by injecting payloads
def detect_dom_based_xss(ip_address):
    print(f"Checking for potential DOM-Based XSS on {ip_address}...\n")

    # List of common XSS payloads
    payloads = [
        "<script>alert('XSS')</script>",  # Basic script payload
        "<img src=x onerror=alert('XSS')>",  # Image with onerror event
        "<svg onload=alert('XSS')></svg>",  # SVG with onload event
        "<a href='javascript:alert(1)'>Click me</a>",  # JavaScript URL payload
    ]

    # URL for testing (e.g., adjust to test specific pages like login, search, etc.)
    url = f"http://{ip_address}/"  # Basic URL (modify as needed for your target)

    for payload in payloads:
        # Simulate GET request with payload
        test_url = urljoin(url, f"?q={payload}")  # Append payload to query string (or modify as needed)
        
        try:
            # Send the GET request
            response = requests.get(test_url)
            
            # Check if the response contains the payload or triggers a script
            if payload in response.text:
                print(f"[!] Potential DOM-Based XSS detected with payload: {payload}")
                print(f"Response contains injected payload: {payload}")
            else:
                print(f"[+] No DOM-Based XSS detected with payload: {payload}")
        
        except requests.exceptions.RequestException as e:
            print(f"[!] Error making request: {e}")

# Main function to prompt the user and start the detection process
def main():
    
    # Prompt the user for an IP address to test for DOM-Based XSS
    ip_address = input("Enter the target IP address:")

    # Start detecting DOM-Based XSS
    detect_dom_based_xss(ip_address)

if __name__ == "__main__":
    main()

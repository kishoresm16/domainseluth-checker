import argparse
import socket
import requests
import time
import sys

# Function to check if domain is up
def check_domain(domain):
    try:
        # Try to resolve the domain to an IP address
        ip = socket.gethostbyname(domain)
        
        # Try to send a request to the domain to check if it's reachable
        response = requests.get(f"http://{domain}", timeout=5)
        
        if response.status_code == 200:
            return f"[🟢 UP] {domain} - IP: {ip} is accessible (HTTP Status: {response.status_code})", True
        else:
            return f"[🔴 DOWN] {domain} - IP: {ip} returned Status Code: {response.status_code}", False
    
    except socket.gaierror:
        return f"[🔴 DOWN] {domain} - DNS Resolution Failed", False
    except requests.exceptions.RequestException:
        return f"[🔴 DOWN] {domain} - Network Request Failed", False

# Banner display with emojis
def display_banner():
    banner = """
    ================================================
    🕵♂ [ DomainSleuth ] - Domain Status Checker 🕵♀
    ================================================
         Created by: Kishore 🚀
    ================================================
    """
    print(banner)

# Read domains from a file
def read_domains_from_file(file_path):
    try:
        with open(file_path, 'r') as file:
            domains = [line.strip() for line in file.readlines()]
        return domains
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
        sys.exit(1)
    except Exception as e:
        print(f"Error: {str(e)}")
        sys.exit(1)

# Write results to files
def write_results(active_domains, inactive_domains):
    with open('active-domains.txt', 'w') as active_file:
        for domain in active_domains:
            active_file.write(f"{domain}\n")
    
    with open('inactive-domains.txt', 'w') as inactive_file:
        for domain in inactive_domains:
            inactive_file.write(f"{domain}\n")
    
    print("\nResults saved to 'active-domains.txt' and 'inactive-domains.txt'")

# Main function to process the list of domains
def main():
    # Display the banner
    display_banner()

    # Parse arguments using argparse
    parser = argparse.ArgumentParser(description='DomainSleuth: Check if a domain is up or down.')
    
    # Define command-line arguments
    parser.add_argument(
        'input', 
        metavar='input',
        type=str,
        help='File containing domains (e.g., urls.txt) or domains as a space-separated list'
    )
    parser.add_argument(
        '-v', '--version',
        action='version',
        version='DomainSleuth 1.0',
        help='Display the version of DomainSleuth.'
    )
    
    # Parse the arguments
    args = parser.parse_args()

    # If the input is a file, read domains from the file
    if args.input.endswith('.txt'):
        domains = read_domains_from_file(args.input)
    else:
        # Otherwise, assume it's a list of domains provided as arguments
        domains = args.input.split()
    
    # Lists to store active and inactive domains
    active_domains = []
    inactive_domains = []
    
    # Process each domain
    for domain in domains:
        print(f"Checking domain: {domain}...")
        result, is_active = check_domain(domain)
        print(result)
        
        if is_active:
            active_domains.append(domain)
        else:
            inactive_domains.append(domain)
        
        time.sleep(1)  # Adding a delay between requests
    
    # Write results to files
    write_results(active_domains, inactive_domains)

if __name__ == "__main__":
    main()

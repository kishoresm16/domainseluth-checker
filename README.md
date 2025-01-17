# DomainSleuth - Domain Status Checker

**DomainSleuth** is a tool that allows users to check whether a domain is "up" (active) or "down" (inactive). It resolves the domain's DNS and checks if the website is accessible via HTTP. The tool supports checking multiple domains at once and saves the results into separate files for active and inactive domains.

Built by **Kishore SM**, a Cyber Security Analyst.

## Features

- **DNS Resolution**: Checks whether the domain can be resolved into an IP address.
- **HTTP Status Check**: Verifies whether the domain is accessible by checking its HTTP response.
- **Batch Processing**: Supports checking a list of domains from a file or from command-line input.
- **Result Logging**: Saves results into two separate files: `active-domains.txt` and `inactive-domains.txt`.
- **Command-line friendly**: Easy to integrate into your workflow via simple commands.

## Installation

To run this tool, ensure you have Python 3 installed. This script requires the `requests` module, which you can install via `pip`.

1. Clone this repository:

   
   git clone https://github.com/your-username/domain-sleuth.git
   cd domain-sleuth

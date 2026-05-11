# Final-Project-Secret-Scanner

## Description
This Python CLI tool scans files and directories for hardcoded secrets using regex patterns.

The scanner checks for:
- AWS Access Keys
- Google API Keys
- Generic API Keys
- Passwords
- JWT Tokens
- Private Keys

## Features
- Scans individual files or entire directories
- Uses regex pattern matching
- Displays filename, line number, and matched string
- Includes logging
- Simple command-line interface using argparse

## Installation

bash
pip install -r requirements.txt
Usage

Scan a single file:

python scanner.py test.py

Scan a directory:

python scanner.py ./project-folder
Detection Logic

The application uses regular expressions to identify patterns commonly associated with secrets and credentials.

Examples:

AWS keys start with AKIA
Google API keys begin with AIza
JWT tokens contain three Base64 sections separated by periods
Private keys contain standard PEM headers
Log File

Scan activity and errors are stored in:

scanner.log


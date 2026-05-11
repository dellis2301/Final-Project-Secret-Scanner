import os 
import re 
import argparse 
import logging 

# Configure logging 
logging.basicConfig( filename='scanner.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s' )

# Regex patterns for secrets PATTERNS = { 
"AWS Access Key": r"AKIA[0-9A-Z]{16}", 
"Google API Key": r"AIza[0-9A-Za-z\\-_]{35}",
"Generic API Key": r"api[_-]?key\\s*=\\s*['\\\"][A-Za-z0-9\\-_]{16,}['\\\"]", 
"Password": r"password\\s*=\\s*['\\\"].+['\\\"]",
"Private Key": r"-----BEGIN PRIVATE KEY-----",
"JWT Token": r"eyJ[A-Za-z0-9-_]+\\.[A-Za-z0-9-_]+\\.[A-Za-z0-9-_]+" }
def scan_file(filepath):
  findings = []
  
  try: 
  with open(filepath, 'r', encoding='utf-8', errors='ignore') as file:
    for line_num, line in enumerate(file, start=1): 
    for secret_type, pattern in PATTERNS.items(): 
      matches = re.findall(pattern, line) 
      
      for match in matches: 
        findings.append({
          "file": filepath, 
          "line": line_num, 
          "type": secret_type, 
          "match": match 
        })
except Exception as e: 
logging.error(f"Error scanning file {filepath}: {e}") 
return findings 

def scan_directory(directory):
  all_findings = [] for root, _, files in os.walk(directory): 
 
  for file in files:
    filepath = os.path.join(root, file) 
    results = scan_file(filepath) 
    all_findings.extend(results) 
    
    return all_findings 
    
    def print_report(findings): 
    
    if not findings: 
      print("No secrets found.") 
      return print("\\n=== Secret Scan Report ===\\n") 
      
      for finding in findings: 
        print(f"File: {finding['file']}") 
        print(f"Line: {finding['line']}") 
        print(f"Type: {finding['type']}") 
        print(f"Match: {finding['match']}") 
        print("-" * 40)
        
        def main(): 
          parser = argparse.ArgumentParser(description="Secret Scanner CLI Tool") 
          parser.add_argument("path", help="File or directory to scan") 
          
          args = parser.parse_args() 
          
          path = args.path 
          
          if os.path.isfile(path): 
            findings = scan_file(path) 
          
          elif os.path.isdir(path): 
            findings = scan_directory(path) 
          
          else: print("Invalid path.") 
            return logging.info(f"Scan completed for: {path}") 
          print_report(findings) 
          
          if __name__ == "__main__": main()

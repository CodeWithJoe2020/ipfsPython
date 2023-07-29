import requests
import json

# IPFS gateway and API endpoints
gateway_url = 'http://localhost:8080'
api_url = 'http://localhost:5001/api/v0'

# Add a file to IPFS
def add_file(filename):
    with open(filename, 'rb') as f:
        files = {'file': f}
        response = requests.post(f'{api_url}/add', files=files)
        file_hash = json.loads(response.text)['Hash']
        print(f'Added file to IPFS with CID: {file_hash}')
        return file_hash

# Retrieve a file from IPFS
def get_file(file_hash, output_file):
    response = requests.get(f'{gateway_url}/ipfs/{file_hash}')
    with open(output_file, 'wb') as f:
        f.write(response.content)
    print(f'File retrieved from IPFS and saved as {output_file}')

# Test the functions
file_hash = add_file('myfile.txt')
get_file(file_hash, 'output.txt')

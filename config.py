import os
import json

def get_config():
    file_name = 'key.json'
    if os.path.isfile(file_name):
        try:
            # Open and read the JSON file
            with open(file_name, 'r') as file:
                data = json.load(file)
                return {
                'api_key': data['key'],
                'server': 'https://www.hybrid-analysis.com'
                }

        except FileNotFoundError:
            print(f"Error: The file '{file_name}' does not exist.")
        except json.JSONDecodeError:
            print("Error: The file is not a valid JSON file.")

    

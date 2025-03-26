import sys
import subprocess
import argparse
import json


def read_file(file):
    with open(file, "r") as f:
        lines = f.readlines()
    lines = [line.strip() for line in lines]
    return lines
def apikey(key):
    file_path = 'key.json'
    # Read the existing data from the JSON file
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)  # Load the current data from the file
    except FileNotFoundError:
        print(f"The file '{file_path}' does not exist.")
        data = {}

    data['key'] = key  # Updating an existing field

    # Write the modified data back to the file
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)

def main(argv=None):
    argv = sys.argv
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--file", action="store", help="hashes file")
    parser.add_argument("-k", "--apikey", action="store", help="Api key")
    args = parser.parse_args(argv[1:])
    hashes = read_file(args.file)
    apikey(args.apikey)
    for h in hashes:
        args = ['search_hash', h]
        subprocess.run(['python', 'vxapi.py'] + args)

if __name__ == "__main__":
    main(argv=sys.argv)
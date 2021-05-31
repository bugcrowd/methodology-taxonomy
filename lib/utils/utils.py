import json
import git

SCHEMA_FILENAME = 'schema.json'
METHODOLOGIES_DIR = 'methodologies'

def get_json(filename):
    with open(filename) as f:
        return json.loads(f.read())
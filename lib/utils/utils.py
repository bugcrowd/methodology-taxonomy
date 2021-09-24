import json
import git

SCHEMA_FILENAME = 'schema.json'
METHODOLOGIES_DIR = 'methodologies'
MAPPING_DIR = 'mappings'
TEMPLATE_FILENAME = 'templates.json'
TEMPLATE_SCHEMA = 'templates.schema.json'
TEMPLATE_BASE_URL = 'https://github.com/bugcrowd/templates/tree/master/'


def get_json(filename):
    with open(filename) as f:
        return json.loads(f.read())
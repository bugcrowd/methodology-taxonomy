from utils import utils
from tests.test_ import TestMethodologies
import os
import unittest
import requests

class TestTemplateMapping(unittest.TestCase):
  def setUp(self):
    self.template_schema = os.path.join(
        utils.MAPPING_DIR,
        utils.TEMPLATE_SCHEMA
    )
    self.template_filename = os.path.join(
        utils.MAPPING_DIR,
        utils.TEMPLATE_FILENAME
    )

  def test_mapping_schemas(self):
    """
    Validate the mapping templates using template.schema.json
    get the mapping data from templates.json
    and validating the templates data
    """
    TestMethodologies.validate_schema(
        TestMethodologies,
        self.template_schema,
        self.template_filename
    )

    mapping = utils.get_json(self.template_filename)

    self.validate_mapping_data(mapping['content'])

  def validate_mapping_data(self, mapping):
      for methodologyData in mapping:
          self.check_template_exists(methodologyData['methodology'], methodologyData['children'])

  def check_template_exists(self, methodology, steps):
      """
      Check a template mapping path from templates.json file
      and check methodology template exists (or not) in template repository
      if the template is not found, it will give an error for template missing
      """
      print("validating methodology : %s" % methodology)

      for step in steps:
        template_path = os.path.join('methodology', step['attribute'], methodology, step['template'])
        template_url = utils.TEMPLATE_BASE_URL + template_path
        response = requests.request("GET", template_url)
        print("validating methodology step : %s" % step['key'])

        self.assertEqual(response.status_code, 200, 'Missing template file for %s mapping' % methodology)

if __name__ == "__main__":
    unittest.main()

import unittest
import json

class TestNumber(unittest.TestCase):
    source = 'LearningObjectives (1145220_LO9)'
    expected_link_names = ["isabletoAnalyzeProblemOf", 
                           "isabletoApplyKnowledgeOf",
                           "isabletoUnderstandKnowledgeOf"]
    
    @classmethod
    def setUpClass(cls):
        with open('data/output.json', 'r') as json_file:
            cls.data = json.load(json_file)

    def test_number_of_LearningObjectives(self):
        # Count the number of source
        count = sum(1 for entry in self.data["links"] if entry["source"] == self.source)
        # Ensure the count matches the expected value
        self.assertEqual(3, count)

    def test_match_LinkNames(self):
        for entry in self.data["links"]:
            if entry["source"] == self.source:
                # Check if the link name is in the expected list
                self.assertIn(entry["name"], self.expected_link_names)
  
if __name__ == '__main__':
    unittest.main()

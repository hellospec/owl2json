import unittest
from owlready2 import get_ontology
from app import extract_nodes_and_links

class TestExtractNodesAndLinks(unittest.TestCase):
    source = 'LearningObjectives (1145220_LO9)'
    expected_link_names = ["isabletoAnalyzeProblemOf", 
                           "isabletoApplyKnowledgeOf",
                           "isabletoUnderstandKnowledgeOf"]

    @classmethod
    def setUpClass(cls):
        cls.ontology = get_ontology("file://data/example.owl").load()
        cls.nodes, cls.links = extract_nodes_and_links(cls.ontology)

    def test_number_of_LearningObjectives(self):
        count = sum(1 for entry in self.links if entry["source"] == self.source)     
        # Ensure the count matches the expected value 
        self.assertEqual(count, 3) 

    def test_match_LinkNames(self):
        for entry in self.links:
            if entry["source"] == self.source:
                # Check if the link name is in the expected list
                self.assertIn(entry["name"], self.expected_link_names) 

if __name__ == '__main__':
    unittest.main()

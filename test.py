import unittest
from owlready2 import get_ontology
from app import extract_nodes_and_links, load_ontology

class TestExtractNodesAndLinks(unittest.TestCase):
    def test_match_convert_1141001_cource(self):
        expected_json = {
            "nodes": [
                { "id": "1141001", "data": { "type": "courses" }},
                { "id": "1141001_LO4", "data": { "type": "learning_objectives" }},
                { "id": "1141001_LO3", "data": { "type": "learning_objectives" }},
                { "id": "1141001_LO2", "data": { "type": "learning_objectives" }},
                { "id": "1141001_LO1", "data": { "type": "learning_objectives" }},
                { "id": "ระเบียบวิธีการทางสถิติ", "data": { "type": "topics" }},
                { "id": "การสุ่มตัวอย่าง", "data": { "type": "topics" }},
                { "id": "การทดสอบสมมติฐาน", "data": { "type": "topics" }},
                { "id": "การประมาณค่าพารามิเตอร์", "data": { "type": "topics" }},
                { "id": "การวิเคราะห์การถดถอยเชิงเส้นแบบง่ายและการวิเคราะห์สหสัมพันธ์", "data": { "type": "topics" }},
                { "id": "ระบบสมการเชิงเส้น", "data": { "type": "topics" }},
                { "id": "รูปแบบมาร์คอฟ", "data": { "type": "topics" }}],
            "edges": [
                { "source": "1141001_LO1", "target": "ระเบียบวิธีการทางสถิติ", "data": { "name": "isabletoUnderstandKnowledgeOf", "title": "can_understand" }},
                { "source": "1141001_LO1", "target": "การสุ่มตัวอย่าง", "data": { "name": "isabletoUnderstandKnowledgeOf", "title": "can_understand" }},
                { "source": "1141001_LO1", "target": "การทดสอบสมมติฐาน", "data": { "name": "isabletoUnderstandKnowledgeOf", "title": "can_understand" }},
                { "source": "1141001_LO1", "target": "การประมาณค่าพารามิเตอร์", "data": { "name": "isabletoUnderstandKnowledgeOf", "title": "can_understand" }},
                { "source": "1141001_LO1", "target": "ระเบียบวิธีการทางสถิติ", "data": { "name": "isabletoApplyKnowledgeOf", "title": "can_apply" }},
                { "source": "1141001_LO1", "target": "การสุ่มตัวอย่าง", "data": { "name": "isabletoApplyKnowledgeOf", "title": "can_apply" }},
                { "source": "1141001_LO1", "target": "การทดสอบสมมติฐาน", "data": { "name": "isabletoApplyKnowledgeOf", "title": "can_apply" }},
                { "source": "1141001_LO1", "target": "การประมาณค่าพารามิเตอร์", "data": { "name": "isabletoApplyKnowledgeOf", "title": "can_apply" }},
                { "source": "1141001_LO1", "target": "ระเบียบวิธีการทางสถิติ", "data": { "name": "isabletoAnalyzeProblemOf", "title": "can_analyze" }},
                { "source": "1141001_LO1", "target": "การสุ่มตัวอย่าง", "data": { "name": "isabletoAnalyzeProblemOf", "title": "can_analyze" }},
                { "source": "1141001_LO1", "target": "การทดสอบสมมติฐาน", "data": { "name": "isabletoAnalyzeProblemOf", "title": "can_analyze" }},
                { "source": "1141001_LO1", "target": "การประมาณค่าพารามิเตอร์", "data": { "name": "isabletoAnalyzeProblemOf", "title": "can_analyze" }},
                { "source": "1141001_LO2", "target": "การวิเคราะห์การถดถอยเชิงเส้นแบบง่ายและการวิเคราะห์สหสัมพันธ์", "data": { "name": "isabletoUnderstandKnowledgeOf", "title": "can_understand" }},
                { "source": "1141001_LO2", "target": "การวิเคราะห์การถดถอยเชิงเส้นแบบง่ายและการวิเคราะห์สหสัมพันธ์", "data": { "name": "isabletoApplyKnowledgeOf", "title": "can_apply" }},
                { "source": "1141001_LO2", "target": "การวิเคราะห์การถดถอยเชิงเส้นแบบง่ายและการวิเคราะห์สหสัมพันธ์", "data": { "name": "isabletoAnalyzeProblemOf", "title": "can_analyze" }},
                { "source": "1141001_LO3", "target": "ระบบสมการเชิงเส้น", "data": { "name": "isabletoUnderstandKnowledgeOf", "title": "can_understand" }},
                { "source": "1141001_LO3", "target": "ระบบสมการเชิงเส้น", "data": { "name": "isabletoApplyKnowledgeOf", "title": "can_apply" }},
                { "source": "1141001_LO3", "target": "ระบบสมการเชิงเส้น", "data": { "name": "isabletoAnalyzeProblemOf", "title": "can_analyze" }},
                { "source": "1141001_LO4", "target": "รูปแบบมาร์คอฟ", "data": { "name": "isabletoUnderstandKnowledgeOf", "title": "can_understand" }},
                { "source": "1141001_LO4", "target": "รูปแบบมาร์คอฟ", "data": { "name": "isabletoApplyKnowledgeOf", "title": "can_apply" }},
                { "source": "1141001_LO4", "target": "รูปแบบมาร์คอฟ", "data": { "name": "isabletoAnalyzeProblemOf", "title": "can_analyze" }},
                { "source": "การวิเคราะห์การถดถอยเชิงเส้นแบบง่ายและการวิเคราะห์สหสัมพันธ์", "target": "การประมาณค่าพารามิเตอร์", "data": { "name": "continueFrom", "title": "continue_from" }},
                { "source": "การวิเคราะห์การถดถอยเชิงเส้นแบบง่ายและการวิเคราะห์สหสัมพันธ์", "target": "การทดสอบสมมติฐาน", "data": { "name": "continueFrom", "title": "continue_from" }},
                { "source": "การวิเคราะห์การถดถอยเชิงเส้นแบบง่ายและการวิเคราะห์สหสัมพันธ์", "target": "การสุ่มตัวอย่าง", "data": { "name": "continueFrom", "title": "continue_from" }},
                { "source": "การวิเคราะห์การถดถอยเชิงเส้นแบบง่ายและการวิเคราะห์สหสัมพันธ์", "target": "ระเบียบวิธีการทางสถิติ", "data": { "name": "continueFrom", "title": "continue_from" }},
                { "source": "ระบบสมการเชิงเส้น", "target": "การวิเคราะห์การถดถอยเชิงเส้นแบบง่ายและการวิเคราะห์สหสัมพันธ์", "data": { "name": "continueFrom", "title": "continue_from" }},
                { "source": "รูปแบบมาร์คอฟ", "target": "ระบบสมการเชิงเส้น", "data": { "name": "continueFrom", "title": "continue_from" }},
                { "source": "1141001", "target": "1141001_LO4", "data": { "name": "hasLearningOf", "title": "has_learning_of" }},
                { "source": "1141001", "target": "1141001_LO3", "data": { "name": "hasLearningOf", "title": "has_learning_of" }},
                { "source": "1141001", "target": "1141001_LO2", "data": { "name": "hasLearningOf", "title": "has_learning_of" }},
                { "source": "1141001", "target": "1141001_LO1", "data": { "name": "hasLearningOf", "title": "has_learning_of" }}]}
        expected_nodes = expected_json["nodes"]
        expected_edges = expected_json["edges"]


        owl_file = load_ontology("file://ambc2/test/data/testCurrOntology.owl")
        course_id = "1141001"
        actual_result = extract_nodes_and_links(owl_file, course_id)
        actual_nodes = actual_result["nodes"]
        actual_edges = actual_result["edges"]

        self.assertEqual(len(actual_nodes), len(expected_nodes))
        self.assertEqual(len(actual_edges), len(expected_edges))

        for node in expected_nodes:
            self.assertIn(node, actual_nodes)
        
        for edge in expected_edges:
            self.assertIn(edge, actual_edges)

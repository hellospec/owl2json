from owlready2 import *
import json

ontology_file = "file://data/testCurrOntology.owl"
output_file = "data/output.json"

def create_relationship(source, target, on_property_name):
    return {
        "source": source,
        "target": target,
        "name": on_property_name
    }

def load_ontology(file_path):
    return get_ontology(file_path).load()

def is_has_child_node(restriction):
    return isinstance(restriction, owlready2.Restriction)

def extract_learning_objective_name(restriction):
    return str(restriction).split(".")[-1][:-1]

def get_node_type(node_type):
    match node_type:
        case "LearningObjectives":
            return "learning_objectives"
        case "Topics":
            return "topics"
        case "Courses":
            return "courses"

def get_edge_title(edge_name):
    match edge_name:
        case "isabletoUnderstandKnowledgeOf":
            return "can_understand"
        case "isabletoApplyKnowledgeOf":
            return "can_apply"
        case "isabletoAnalyzeProblemOf":
            return "can_analyze"
        case "isabletoUnderstandKnowledgeOf":
            return "can_understand"
        case "continueFrom":
            return "continue_from"
        case "hasLearningOf":
            return "has_learning_of"
        case "hasLearningContentOf":
            return "has_learning_content_of"

def create_node(class_name, nodes):
    for restriction in ontology[class_name].is_a:
        if is_has_child_node(restriction):
            learning_objective = str(restriction).split(".")[-1][:-1]
            for obj in ontology[learning_objective].is_a:
                if not isinstance(obj, owlready2.Restriction):
                    data_type = str(obj).split(".")[-1]
                    node_type = get_node_type(data_type)
                    node = {'id': learning_objective,
                            'data': {'type': node_type }
                            }
                    if node not in nodes:
                        nodes.append(node)
        else :
            data_type = str(restriction).split(".")[1]
            node_type = get_node_type(data_type)
            node = {'id': class_name, 
                    'data': {'type': node_type}
                    }
            if node not in nodes:
                nodes.append(node)
    return nodes


def create_edge(ontology, course_id):
    course = ontology[course_id].is_a

    learning_objective_edges, topic_name = create_learning_objective_edges(course)
    course_edge = create_course_edge(course, course_id)
    topic_edge = create_topic_edge(ontology, topic_name)

    edges = learning_objective_edges + course_edge + topic_edge

    return edges

def create_topic_edge(ontology, topic_name):
    edges = []
    for source in topic_name:
        for restriction in ontology[source].is_a:
            if is_has_child_node(restriction):
                target = str(restriction).split(".")[-1][:-1]
                name = str(restriction).split(".")[1]
                title = get_edge_title(name)
                edge = { "source": source,
                         "target": target,
                         "data": { "name": name, "title": title } }
                if edge not in edges:
                    edges.append(edge)
    return edges
    

def create_course_edge(course, course_id):
    edges = []
    for restriction in course[1:]:
        target = extract_learning_objective_name(restriction)
        name = str(restriction).split(".")[1]
        title = get_edge_title(name)
        edge = { "source": course_id,
                 "target": target,
                 "data": { "name": name, "title": title } }
        if edge not in edges:
            edges.append(edge)
    return edges

def create_learning_objective_edges(course):
    edges = []
    topics = []
    for restriction in course:
        source = extract_learning_objective_name(restriction)
        if is_has_child_node(restriction):
            learning_objective_edge = ontology[source]
            for topic_obj in learning_objective_edge.is_a[1:]:
                name = str(topic_obj).split(".")[1]
                title = get_edge_title(name)
                name = str(topic_obj).split(".")[-1][:-1]
                edge = { "source": source, 
                         "traget": name,
                         "data": { "name": name, "title": title } }
                if name not in topics:
                    topics.append(name)
                if edge not in edges:
                    edges.append(edge)
    return edges, topics



def extract_nodes_and_links(ontology, course_id):
    nodes = []
    course = ontology[course_id].is_a
    edges = create_edge(ontology, course_id)

    for cls in ontology.classes():
        class_name = cls.name

        if course_id not in class_name:
            continue
        create_node(class_name, nodes)
    return nodes, edges 

def save_json_data(output_file, nodes, links):
    json_data = {
        "nodes": nodes,
        "edges": links
    }

    with open(output_file, "w", encoding="utf-8") as outfile:
        json.dump(json_data, outfile, indent=4, ensure_ascii=False)

    print(f"JSON data saved to {output_file}")

ontology = load_ontology(ontology_file)
course_id = "1141001"
extract_nodes_and_links(ontology, course_id)
nodes, edges = extract_nodes_and_links(ontology, course_id)
save_json_data(output_file, nodes, edges)

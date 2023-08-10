from owlready2 import *
import json

ontology_file = "file://data/example.owl"
output_file = "data/output.json"

def create_relationship(source, target, on_property_name):
    return {
        "source": source,
        "target": target,
        "name": on_property_name
    }

def load_ontology(file_path):
    return get_ontology(file_path).load()

def extract_nodes_and_links(ontology):
    nodes = []
    links_set = set()
    val_counter = 1

    for cls in ontology.classes():
        class_name = cls.name

        for subclass in cls.subclasses():
            subclass_name = subclass.name

            if class_name == subclass_name:
                continue

            class_id = f"{class_name} ({subclass_name})"
            nodes.append({
                "id": class_id,
                "name": subclass_name,
                "val": val_counter
            })
            val_counter += 1

            for restriction in subclass.is_a:
                if isinstance(restriction, owlready2.Restriction):
                    on_property_name = restriction.property.name
                    relationship = create_relationship(class_id, subclass_name, on_property_name)
                    links_set.add(json.dumps(relationship))

    links = [json.loads(link_str) for link_str in links_set]
    return nodes, links

def save_json_data(output_file, nodes, links):
    json_data = {
        "nodes": nodes,
        "links": links
    }

    with open(output_file, "w", encoding="utf-8") as outfile:
        json.dump(json_data, outfile, indent=4, ensure_ascii=False)

    print(f"JSON data saved to {output_file}")

ontology = load_ontology(ontology_file)
nodes, links = extract_nodes_and_links(ontology)
save_json_data(output_file, nodes, links)

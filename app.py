from owlready2 import *
import json

onto = get_ontology("file://data/example.owl").load()

nodes = []
links = []
val_counter = 1

for cls in onto.classes():
    class_name = cls.name
    class_id = f"{class_name} ({class_name})"
    nodes.append({
        "id": class_id,
        "name": class_name,
        "val": val_counter
    })
    val_counter += 1
    
    for subclass in cls.subclasses():
        subclass_name = subclass.name
        subclass_id = f"{class_name} ({subclass_name})"
        nodes.append({
            "id": subclass_id,
            "name": subclass_name,
            "val": val_counter
        })
        val_counter += 1
        
        for restriction in subclass.is_a:
            if isinstance(restriction, owlready2.Restriction):
                on_property_name = restriction.property.name
                links.append({
                    "source": class_id,
                    "target": subclass_id,
                    "name": on_property_name
                })

json_data = {
    "nodes": nodes,
    "links": links
}

output_file = "data/output.json"
with open(output_file, "w", encoding="utf-8") as outfile:
    json.dump(json_data, outfile, indent=4, ensure_ascii=False)

print(f"JSON data saved to {output_file}")

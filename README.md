# owl2json

This project aim to convert the owl file from specific domain (course/learning objective) to json object.

## Run
```
$ python3 app.py
```

## Output json
The output json object will be compliant to the [force-graph](https://github.com/vasturiano/force-graph) library. That said you should be able to use force-graph to display the graph from input owl file.

```json
{
    "nodes": [
        {
          "id": "learning objective (1145001_LO1)",
          "name": "1145001_LO1",
          "val": 1
        },
        {
          "id": "topic (การทดสอบสมมติฐาน)",
          "name": "การทดสอบสมมติฐาน",
          "val": 10
        },
        ...
    ],
    "links": [
        {
            "source": "course (11450001)",
            "target": "learning_objective (11450001_LO2)",
            "name": "hasLearningOf"
        },
        {
            "source": "learning_objective (11450001_LO2)",
            "target": "topic (การทดสอบสมมติฐาน)",
            "name": "isabletoAnalyzeProblemOf"
        },
        {
            "source": "learning_objective (11450001_LO2)",
            "target": "topic (การทดสอบสมมติฐาน)",
            "name": "isabletoApplyKnowledgeOf"
        },
        ...
    ]
}
```

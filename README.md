# owl2json

This project aim to convert the owl file from specific domain (course/learning objective) to json object.

## Output json
The output json object will be compliant to the [force-graph](https://github.com/vasturiano/force-graph) library. That said you should be able to use force-graph to display the graph from input owl file.

```json
{
    "nodes": [
        {
          "id": "id1",
          "name": "name1",
          "val": 1
        },
        {
          "id": "id2",
          "name": "name2",
          "val": 10
        },
        ...
    ],
    "links": [
        {
            "source": "id1",
            "target": "id2"
        },
        ...
    ]
}
```

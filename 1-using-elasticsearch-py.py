#!/usr/bin/env python3

from datetime import datetime
from elasticsearch import Elasticsearch

client = Elasticsearch()

#client.index(index="meetup", doc_type="test-type", id=42, body={"any": "data", "timestamp": datetime.now()})

response = client.search(
    index="meetup",
    doc_type="member",
    body={
      "query": {
        "query_string": {
          "query": "maciel"
        }
      }
    }
)

print(response)

for hit in response['hits']['hits']:
    print(hit['_score'], hit['_source']['name'], hit['_source']['age'])

#for tag in response['aggregations']['per_tag']['buckets']:
#    print(tag['key'], tag['max_lines']['value'])

#!/usr/bin/env python3

from elasticsearch import Elasticsearch
from elasticsearch_dsl import Search, Q
from elasticsearch_dsl.query import QueryString

client = Elasticsearch()

s = Search(using=client, index="meetup") \
    .query(QueryString(query="maciel")) \
    .sort("age")

#s = Search(using=client, index="meetup") \
    #.query(Q({"query_string": {"query": "maciel"}}))

#s = Search(using=client, index="meetup") \
    #.query(Q("query_string", query="maciel"))

#s = Search(using=client, index="meetup") \
    #.query("query_string", query="maciel")

response = s.execute()

for member in response:
    print(member.name)
    #print(member)

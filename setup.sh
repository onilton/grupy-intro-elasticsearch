#!/bin/bash

echo "Downloading elasticsearch"

wget -nc "https://download.elastic.co/elasticsearch/release/org/elasticsearch/distribution/tar/elasticsearch/2.3.3/elasticsearch-2.3.3.tar.gz"

echo "Unzipping elasticsearch"
tar -vzxf elasticsearch-2.3.3.tar.gz

echo "sudo pip install -r requirements.txt" 
#sudo pip install -r requirements.txt 

# maybe you will have to change to make it work for you
#sudo pip3 install -r requirements.txt 

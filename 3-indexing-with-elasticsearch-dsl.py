#!/usr/bin/env python3

from elasticsearch_dsl import DocType, String, Long
from elasticsearch_dsl.connections import connections
import random


technologies = ["javascript", "java", "c#", "php", "android", "jquery", "python", "html", "c++", "ios", "mysql", "css", "sql", "asp.net", "objective-c", "ruby-on-rails", ".net", "c", "iphone", "arrays", "angularjs", "sql-server", "ruby", "json", "ajax", "regex", "r", "xml", "asp.net-mvc", "linux", "node.js", "django", "wpf", "database", "xcode", "vb.net", "eclipse", "string", "swift", "windows", "excel", "wordpress", "html5", "spring", "multithreading", "facebook", "image", "forms", "git", "oracle", "bash", "osx", "winforms", "algorithm", "twitter-bootstrap", "mongodb", "apache", "vba", "performance", "matlab", "swing", "entity-framework", "linq", "visual-studio", "hibernate", "ruby-on-rails-3", "postgresql", "list", "css3", "scala", "perl", "web-services", "qt", "python-2.7", ".htaccess", "function", "sqlite", "file", "sql-server-2008", "visual-studio-2010", "shell", "excel-vba", "uitableview", "codeigniter", "wcf", "api", "cordova", "rest", "google-maps", "maven", "validation", "class", "unit-testing", "sockets", "jsp", "symfony2", "google-chrome", "actionscript-3", "laravel", "xaml", "tsql", "asp.net-mvc-3", "loops", "email", "sorting", "android-layout", "security", "asp.net-mvc-4"]


def random_techs():
    return " ".join([random.choice(technologies) for i in range(0, 3)])


# Define a default Elasticsearch client
connections.create_connection(hosts=['localhost'])


class Member(DocType):
    name = String()
    age = Long()
    techs = String()

    class Meta:
        index = 'meetup'

    def save(self, ** kwargs):
        self.age = random.randint(15, 40)
        self.techs = random_techs()
        return super(Member, self).save(** kwargs)

    #def is_published(self):
        #return datetime.now() < self.published_from

# create the mappings in elasticsearch
Member.init()

with open('users.txt', 'r') as f:
    for i, line in enumerate(f):
        member_name = line.rstrip('\n')
        print("Indexing", i, member_name)

        # create and save and member
        member = Member(meta={'id': i}, name=member_name)
        member.save()

# create and save and member
#member = Member(meta={'id': 42}, name='Eric Hideki')
#member.save()

member = Member.get(id=42)
print(member)

# Display cluster health
#print(connections.get_connection().cluster.health())

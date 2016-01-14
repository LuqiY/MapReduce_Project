"""
Study Groups
We might want to help students form study groups. But first we want to see if
there are already students on forums that communicate a lot between themselves.
As the first step for this analysis we have been tasked with writing a
mapreduce program that for each forum thread (that is a question node with all
it's answers and comments) would give us a list of students that have posted
there - either asked the question, answered a question or added a comment. If
a student posted to that thread several times, they should be added to that
list several times as well, to indicate intensity of communication.
"""

import sys
import csv

def mapper(stdin):
    reader = csv.reader(stdin, delimiter='\t')
    writer = csv.writer(sys.stdout, delimiter='\t', quotechar='"', quoting=csv.QUOTE_ALL)
    reader.next()
    
    for line in reader:
        if len(line) == 19:
            Q_id = line[0]
            node_type = line[5]
            author_id = line[3]
            if node_type == "question":
                writer.writerow([Q_id, author_id])
            else:
                parent_id = line[6]
                writer.writerow([parent_id, author_id])

if __name__ == "__main__":
    mapper(sys.stdin)
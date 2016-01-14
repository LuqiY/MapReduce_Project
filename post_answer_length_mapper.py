"""
We are interested to see if there is a correlation between the length of a post
and the length of answers.
Write a mapreduce program that would process the forum_node data and output the
length of the post and the average answer (just answer, not comment) length for
each post. You will have to decide how to write both the mapper and the reducer
to get the required result.
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
            body = line[4]
            node_type = line[5]
            parent_id = line[6]
            if node_type == "question":
                writer.writerow([Q_id, "0", len(body)])
            elif node_type == "answer":  
                writer.writerow([parent_id, "1", len(body)])

if __name__ == "__main__":
    mapper(sys.stdin)
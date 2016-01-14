
"""
Students and Posting Time on Forums

For each student what is the hour during
which the student has posted the most posts. Output from reducers should be:
    author_id    hour

For example:
    13431511\t13
    54525254141\t21
    
If there is a tie: there are multiple hours during which a student has posted a
maximum number of posts, please print the student-hour pairs on separate lines.
You can ignore the time-zone offset for all times - for example in the following
line:
    "2012-02-25 08:11:01.623548+00"
- you can ignore the +00 offset.
"""

import sys
import csv

def mapper(stdin):
    # read forums data
    reader = csv.reader(stdin, delimiter='\t')
    # skip header
    reader.next()
    
    for line in reader:
        if len(line) == 19:
            author_id = line[3]
            added_at = line[8]
            added_at = added_at.strip()
            # get the hour from added_at
            hour = added_at[11:13]
            print '{0}\t{1}' % (author_id, hour)

if __name__ == "__main__":
    mapper(sys.stdin)
import sys
import csv

def reducer():
    reader = csv.reader(sys.stdin, delimiter='\t')
    writer = csv.writer(sys.stdout, delimiter='\t', quotechar='"', quoting=csv.QUOTE_ALL)

    last_author = None
    this_author = None
    this_hour = None
    posts_hour = {}

    for line in reader:
        if(len(line) == 2):
            this_author, this_hour = line

            if(not posts_hour.has_key(this_hour)):
                posts_hour[this_hour] = 0

            posts_hour[this_hour]= posts_hour[this_hour]+1

        if last_author and last_author != this_author:
            max_post_count = max(posts_hour.values())
            max_post_hours = [this_hour for this_hour, count in posts_hour.items() if count == max_post_count]
            for post_hour in sorted(max_post_hours):
                print "{0}\t{1}".format(last_author, post_hour)

            posts_hour = {}

        last_author = this_author

    if last_author != None and posts_hour.values():
            max_post_count = max(posts_hour.values())
            max_post_hours = [this_hour for this_hour, count in posts_hour.items() if count == max_post_count]
            for post_hour in sorted(max_post_hours):
                 print "{0}\t{1}".format(last_author, post_hour)

if __name__ == "__main__":
    reducer()
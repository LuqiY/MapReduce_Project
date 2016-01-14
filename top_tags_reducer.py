import sys
import csv

def reducer():
    reader = csv.reader(sys.stdin, delimiter='\t')
    writer = csv.writer(sys.stdout, delimiter='\t', quotechar='"', quoting=csv.QUOTE_ALL)
    
    count = 0
    this_tag = None
    top_10 = []
    
    for line in reader:
        if len(line) == 2:
            tag = line[0]
            
            if this_tag is None or tag != this_tag:
                if not this_tag is None:
                    top_10 = add_record(this_tag, count, top_10)
                count = 0
                this_tag = tag

            count += 1
    
    if len(top_10) < 10 or count > top_10[9][1]:
        top_10.append([tag, count])
        top_10.sort(key=lambda tup: tup[1], reverse=True)
        top_10 = top_10[:10]
    
    for tag, count in top_10:
        writer.writerow([tag, count])

if __name__ == "__main__":
    reducer()
import sys
import csv

def reducer():
    reader = csv.reader(sys.stdin, delimiter='\t')
    writer = csv.writer(sys.stdout, delimiter='\t', quotechar='"', quoting=csv.QUOTE_ALL)
    
    current_id = None
    past_id = None
    authors = []
    
    for line in reader:
        if len(line) == 2:
            current_id, author = line
            
            if past_id is None or past_id != current_id:
        
                write_record([past_id, ','.join(authors)])
                
                authors = []
                
            past_id = current_id
            authors.append(author)

           
    if past_id != None:
        writer.writerow([past_id, ','.join(authors)])

if __name__ == "__main__":
    reducer()
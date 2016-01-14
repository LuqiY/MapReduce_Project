import sys
import csv

def reducer():
    reader = csv.reader(sys.stdin, delimiter='\t')
    writer = csv.writer(sys.stdout, delimiter='\t', quotechar='"', quoting=csv.QUOTE_ALL)

    last_Q = None
    this_Q = None
    node_type = None
    length = questionLength = answerCount = totalAnswerLength = 0

    for line in reader:
        if(len(line) == 3):
            this_Q, node_type, length = line

            if(node_type == '0'):
                questionLength = length
            else:
                answerCount = answerCount + 1
                totalAnswerLength = totalAnswerLength + int(length)

        if last_Q and last_Q != this_Q:
            if answerCount > 0:
                averageAnswerLength = totalAnswerLength / answerCount
            else:
                averageAnswerLength = 0

            print "{0}\t{1}\t{2}".format(last_Q, questionLength, averageAnswerLength)
            
            questionLength = answerCount = totalAnswerLength = 0

        last_Q = this_Q

    if last_Q != None:
            if answerCount > 0:
                averageAnswerLength = totalAnswerLength / answerCount
            else:
                averageAnswerLength = 0

            print "{0}\t{1}\t{2}".format(last_Q, questionLength, averageAnswerLength)

if __name__ == "__main__":
    reducer()
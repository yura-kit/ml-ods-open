import os
from tqdm import tqdm
import sys

TOTAL_LINES=10000000
TAGS_LIST={'javascript', 'java', 'python', 'ruby', 'php', 'c++', 'c#', 'go', 'scala', 'swift'}

if len(sys.argv) != 3:
    print ('Invalid command line arguments.')
    sys.exit()

in_filename = sys.argv[1]
out_filename = sys.argv[2]

with open(in_filename, 'r') as infile,open(out_filename, 'a') as outfile:
    for line in tqdm(infile, total=TOTAL_LINES, mininterval=10):
        pair = line.strip().split('\t')
        if len(pair) != 2:
            continue
        question, tags = pair
        line_tags = set(tags.split(' '))
        itsct=TAGS_LIST.intersection(line_tags)
        if len(itsct)==1:
            outfile.write(str(list(TAGS_LIST).index(''.join(itsct))+1)+' | '+question.replace(":", "").replace("|", " ")+'\n')
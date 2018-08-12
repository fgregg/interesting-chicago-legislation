import re
import sys

with open(sys.argv[1]) as f:
    summary = f.read()

for match in re.findall(r'\bO\d{4}-\d+\b', summary):
    print(match)

for match in re.findall(r'\bA\d{4}-\d+\b', summary):
    print(match)

for match in re.findall(r'\bR\d{4}-\d+\b', summary):
    print(match)

for match in re.findall(r'\bOr\d{4}-\d+\b', summary):
    print(match)
    


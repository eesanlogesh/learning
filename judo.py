import json
import sys

with open(sys.argv[1],'r') as contents:
 names=contents.read()
 val=names.split()
 del val[-1]
 love={"names":(val)}
print(love)
o_f=open("open.json","w")
json.dump(love,o_f)
o_f.close()
 
 
 
 

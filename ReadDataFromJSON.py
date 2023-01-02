import json

myjsonfile=open('jsonfolder\pos_0.png.json','r')

#jsondata=json.load(myjsonfile)
jsondata=myjsonfile.read()
print(jsondata)


simple_dict=json.loads(myjsonfile)
print(simple_dict)
print(type(simple_dict))

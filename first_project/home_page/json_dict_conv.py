import json


dict_data={'name': 'Khurshed', 'education': [{'SSC': 'First', 'marks': 808, 'Scholarship': True},
 {'HSC': 'First', 'marks': 806}], 'age': 51, 
 'instituion': ['CZS', 'DC', 'BUET', {'UIU': [{'deg': 'MBA', 'grade': 4.9}]}],
  'nested_object': {'obj1': {'obj2-1': 1, 'obj2-2': 80, 'obj2-3': 60},
   'float': 50.76}}
# step-01 =>  Serializing json / convert python data to json string 
json_object = json.dumps(dict_data) 
print("JSON STRING :",json_object)


# Step-2 : save json string data to json file 
with open("c:/Users/USER/django_project/first_project/home_page/data2.json", "w") as outfile:
   json_data= json.dump(dict_data, outfile)
   
   #print("DATA : ",json_data) => dump does not print data but save in a file
# Step-3 : view the stored data in json file

#step-4 : Now again convert json data from json file to python data
#import simplejson
# js = "{\"description\":\"fdsafsa\",\"order\":\"1\",\"place\":\"22 Plainsman Rd, Mississauga, ON, Canada\",\"lat\":43.5969175,\"lng\":-79.7248744,\"locationDate\":\"03/24/2010\"},{\"description\":\"sadfdsa\",\"order\":\"2\",\"place\":\"50 Dawnridge Trail, Brampton, ON, Canada\",\"lat\":43.7304774,\"lng\":-79.8055435,\"locationDate\":\"03/26/2010\"},"
#simplejson.loads('[%s]' % js[:-1])

with open("c:/Users/USER/django_project/first_project/home_page/data.json") as f :
  python_data=json.load( f) 
  print("json to python data :",python_data)
  


# Python JSON string  to Python Dictionary
jsonString = '{"a":54, "b": {"c":87}}'
aDict = json.loads(jsonString)
print(aDict)
print(aDict['b'])
print(aDict['b']['c'])   

json_string=json.dumps(['foo', {'bar': ('baz', None, 1.0, 2)}])
print("python_data to json_string :",json_string)
# output : '["foo", {"bar": ["baz", null, 1.0, 2]}]'

python_data=json.loads('["foo", {"bar":["baz", null, 1.0, 2]}]')
print ("json_string to python data :",python_data )
# output : ['foo', {'bar': ['baz', None, 1.0, 2]}]


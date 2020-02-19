import requests
import json
import sys



header = {
		"User-Agent": "GraphQL Map Viewer/1.0"
	}


def getSchema(endpoint):
	query = {
		"query":"{__schema{ types{ kind name fields { type { name kind description } description name args { description defaultValue name defaultValue } } ofType { name description } interfaces { name description } enumValues { description deprecationReason } description inputFields { description defaultValue } } queryType { name description kind fields{ name args { description defaultValue name type { name description } } type { name description } description } description } mutationType { name description kind fields{ name args { description defaultValue name type { name description } } type { name description } description } description } } }"
		}

	url = endpoint 
	r = requests.post(url, json=query, headers=header)

	data = json.loads(r.text)

	return data['data']['__schema']


def getTypes(name = ""):
	for x in range(len(schema['types'])):
		if name == '':
			displayType(name,x)
		if name == schema['types'][x]['name']:
			displayType(name,x)


def displayType(name = "",idx = 0):
	print "==========================================================================================================="
	print "       ---------------------------------------- TYPE INFO ----------------------------------------"
	print "==========================================================================================================="
	print "[+] Type Name: " +schema['types'][idx]['name']
	print "[+] Description: " +str(schema['types'][idx]['description'])
	print "[+] Kind: " +str(schema['types'][idx]['kind'])
	if schema['types'][idx]['fields'] != None:
		print "[+] Fields: "
		for idy in range(len(schema['types'][idx]['fields'])):
			print "   ["+ str(idy+1) +"]"
			print "   - name: " + str(schema['types'][idx]['fields'][idy]['name'])
			print "   - description: " + str(schema['types'][idx]['fields'][idy]['description']) 
			print "   - args: " + str(schema['types'][idx]['fields'][idy]['args'])
			print "   - type: " + str(schema['types'][idx]['fields'][idy]['type']['name'])
			print "   	> description: " + str(schema['types'][idx]['fields'][idy]['type']['description'])
			print "   	> kind: " + str(schema['types'][idx]['fields'][idy]['type']['kind'])
			print ""
	else:
		print "[+] Fields: None"

def displayQueryMutation(dType = "",name = "",idx = 0):
	if dType == "mutationType":
		displayType = dType
		print "==========================================================================================================="
		print "   ---------------------------------------- MUTATION TYPE INFO ----------------------------------------"
		print "==========================================================================================================="
		
		print "[+] Mutation Name: " +schema[displayType]['fields'][idx]['name']

	if dType == "queryType":
		displayType = dType
		print "==========================================================================================================="
		print "     ---------------------------------------- QUERY TYPE INFO ----------------------------------------"
		print "==========================================================================================================="
		
		print "[+] Query Name: " +schema[displayType]['fields'][idx]['name']

	
	print "[+] Description: " + str(schema[displayType]['fields'][idx]['description'])
	print "[+] Type: "
	print "   - name: " + str(schema[displayType]['fields'][idx]['type']['name'])
	print "   - description: " + str(schema[displayType]['fields'][idx]['type']['description'])
	print "[+] Args: "
	for idy in range(len(schema[displayType]['fields'][idx]['args'])):
		print "   ["+ str(idy+1) +"]"
		print "   - name: " + str(schema[displayType]['fields'][idx]['args'][idy]['name'])
		print "   - default value: " + str(schema[displayType]['fields'][idx]['args'][idy]['defaultValue'])
		print "   - type: "
		print "   	> name: " + str(schema[displayType]['fields'][idx]['args'][idy]['type']['name'])
		print "   	> description: " + str(schema[displayType]['fields'][idx]['args'][idy]['type']['description'])
		print "   - description: " + str(schema[displayType]['fields'][idx]['args'][idy]['description']) 
		print ""

	print "[+] Generated GQL Query: Soon" 


def getMutationType(name = ""):
	for x in range(len(schema['mutationType']['fields'])):
		if name == '':
			displayQueryMutation("mutationType",name,x)

		if name == schema['mutationType']['fields'][x]['name']:
			displayQueryMutation("mutationType",name,x)


def getQueryType(name = ""):
	for x in range(len(schema['queryType']['fields'])):
		if name == '':
			displayQueryMutation("queryType",name,x)

		if name == schema['queryType']['fields'][x]['name']:
			displayQueryMutation("queryType",name,x)


def menu():
	print "USAGE: "
	print "    -url [gql endpoit]	Target Domain"
	print "    -T			View All GraphQL Types Schema"
	print "    -t [name]		View GraphQL Schema Types"
	print "    -Q 			View All GraphQL Schema Query"
	print "    -q [name]		View GraphQL Schema Query"
	print "    -M 			View All GraphQL Schema Mutation"
	print "    -m [name]		View GraphQL Schema Mutation"	


def main():
	if len(sys.argv) <= 3:
		menu()

	if len(sys.argv) > 3:
		if sys.argv[3] == '-t':
			if len(sys.argv) == 5:
				print getTypes(sys.argv[4])
			else:
				print "Invalid argument count"

		if sys.argv[3] == '-T':
			print getTypes()
		
		if sys.argv[3] == '-q':
			if len(sys.argv) == 5:
				print getQueryType(sys.argv[4])
			else:
				print "Invalid argument count"

		if sys.argv[3] == '-Q':
			print getQueryType()

		if sys.argv[3] == '-m':
			if len(sys.argv) == 5:
				print getMutationType(sys.argv[4])
			else:
				print "Invalid argument count"

		if sys.argv[3] == '-M':
			print getMutationType()		

	


if len(sys.argv) >= 4: 
	schema = getSchema(sys.argv[2])
	
main()























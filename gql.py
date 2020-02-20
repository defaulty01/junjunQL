import requests
import json
import sys

header = {
		"User-Agent": "GraphQL Map Viewer/1.0"
	}


def getSchema(endpoint):
	query = {
		"query":"{__schema{ types{ possibleTypes{ name kind } kind name fields { type { name kind description } description name args { description defaultValue name defaultValue } } ofType { name description } interfaces { name description } enumValues { description deprecationReason } description inputFields { description defaultValue } } queryType { name description kind fields{ name args { description defaultValue name type { name description } } type { name description } description } description } mutationType { name description kind fields{ name args { description defaultValue name type { name description } } type { name description } description } description } } }"
		}

	url = endpoint 
	r = requests.post(url, json=query, headers=header)

	data = json.loads(r.text)

	return data['data']['__schema']




def genQuery(dType = "", name = ""):
	#schema = getSchema(sys.argv[2])
	data = schema[dType]['fields']
	param = ""
	res = ""
	for x in range(len(data)):
		if name == data[x]['name']:
			for y in range(len(data[x]['args'])):
				if (y+1) == len(data[x]['args']):
					param = param + str(data[x]['args'][y]['name'])+": \\\"\\\""
				else:
					param = param + str(data[x]['args'][y]['name'])+": \\\"\\\", "

			nType = data[x]['type']['name']

			if nType == None:
				res = ""
			else:
				res = getTypeField(nType)

			
			if dType == "mutationType":
				return "mutation { " + str(data[x]['name']) + "(" + param + "){ "+ res +" } }"
					
			if dType == "queryType":
				return "query { " + str(data[x]['name']) + "(" + param + "){ "+ res +" } }"



def getTypeField(name = ""):
	#schema = getSchema(sys.argv[2])
	res = schema['types']
	tmp = ""
	param = ""

	for a in range(len(res)):
		if name == res[a]['name']:
			if res[a]['fields'] != None:
				for b in range(len(res[a]['fields'])):
					if str(res[a]['fields'][b]['type']['kind']) == "OBJECT":
						if ((b+1) == len(res[a]['fields'])):
						 	tmp = getTypeField(res[a]['fields'][b]['type']['name'])
						 	tmp = str(res[a]['fields'][b]['name']) + "{" + tmp + "}"
						else:
						 	tmp = getTypeField(res[a]['fields'][b]['type']['name'])
						 	tmp = str(res[a]['fields'][b]['name']) + "{" + tmp + "}, "

						param = param + tmp
					else:
						if ((b+1) == len(res[a]['fields'])):
							tmp = tmp + str(res[a]['fields'][b]['name'])
						else:
							tmp = tmp + str(res[a]['fields'][b]['name'])+", "
						
						param = tmp
		
	return param


def getTypes(name = ""):
	for x in range(len(schema['types'])):
		if name == '':
			displayType(name,x)
		if name == schema['types'][x]['name']:
			displayType(name,x)


def displayType(name = "",idx = 0):
	data = schema['types']

	print "==========================================================================================================="
	print "       ---------------------------------------- TYPE INFO ----------------------------------------"
	print "==========================================================================================================="
	print "[+] Type Name: " +data[idx]['name']
	print "[+] Description: " +str(data[idx]['description'])
	print "[+] Kind: " +str(data[idx]['kind'])
	if data[idx]['fields'] != None:
		print "[+] Fields: "
		for idy in range(len(data[idx]['fields'])):
			print "   ["+ str(idy+1) +"]"
			print "   - name: " + str(data[idx]['fields'][idy]['name'])
			print "   - description: " + str(data[idx]['fields'][idy]['description']) 
			print "   - args: " + str(data[idx]['fields'][idy]['args'])
			print "   - type: " + str(data[idx]['fields'][idy]['type']['name'])
			print "   	> description: " + str(data[idx]['fields'][idy]['type']['description'])
			print "   	> kind: " + str(data[idx]['fields'][idy]['type']['kind'])
			print ""
	else:
		print "[+] Fields: None"
	if data[idx]['possibleTypes'] != None:
		print "[+] Possible Types: " 
		for idz in range(len(data[idx]['possibleTypes'])):
			print "   - name: " + str(data[idx]['possibleTypes'][idz]['name'])
	else:
		print "[+] Possible Types: None" 

def displayQueryMutation(dType = "",name = "",idx = 0):
	data = schema[dType]['fields']

	if dType == "mutationType":
		print "==========================================================================================================="
		print "   ---------------------------------------- MUTATION TYPE INFO ----------------------------------------"
		print "==========================================================================================================="
		
		print "[+] Mutation Name: " +data[idx]['name']

	if dType == "queryType":
		print "==========================================================================================================="
		print "     ---------------------------------------- QUERY TYPE INFO ----------------------------------------"
		print "==========================================================================================================="
		
		print "[+] Query Name: " +data[idx]['name']
	
	print "[+] Description: " + str(data[idx]['description'])
	print "[+] Type: "
	print "   - name: " + str(data[idx]['type']['name'])
	print "   - description: " + str(data[idx]['type']['description'])
	print "[+] Args: "
	for idy in range(len(data[idx]['args'])):
		print "   ["+ str(idy+1) +"]"
		print "   - name: " + str(data[idx]['args'][idy]['name'])
		print "   - default value: " + str(data[idx]['args'][idy]['defaultValue'])
		print "   - type: "
		print "   	> name: " + str(data[idx]['args'][idy]['type']['name'])
		print "   	> description: " + str(data[idx]['args'][idy]['type']['description'])
		print "   - description: " + str(data[idx]['args'][idy]['description']) 
		print ""
	print "[+] Generated GQL Query: Soon"  
	print "   " + str(genQuery(dType, data[idx]['name']))


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





			

















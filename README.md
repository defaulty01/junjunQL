Description:
	A simple recon script for graphql query and mutation. What this tool does is, it seeks all hidden queries and mutations on a graphQL endpoint on a target domain.

  This is still under develop...

  Please don't judge my coding skills :(

  Hope this will help hunters to find more bugs on GraphQL endpoints



Bug:
  Still have issues on terminating the dept of recursion during enumerating all returned types



Usage:
``` 
    -url [gql endpoit]	Target Domain
    -T			View All GraphQL Types Schema
    -t [name]		View GraphQL Schema Types
    -Q 			View All GraphQL Schema Query
    -q [name]		View GraphQL Schema Query
    -M 			View All GraphQL Schema Mutation
    -m [name]		View GraphQL Schema Mutation
```

Example:
```
terminal$ python gql.py 
	USAGE: 
    -url [gql endpoit]	Target Domain
    -T			View All GraphQL Types Schema
    -t [name]		View GraphQL Schema Types
    -Q 			View All GraphQL Schema Query
    -q [name]		View GraphQL Schema Query
    -M 			View All GraphQL Schema Mutation
    -m [name]		View GraphQL Schema Mutation

terminal$ $ python gql.py -url https://hackerone.com/graphql? -t BankTransferReference
===========================================================================================================
       ---------------------------------------- TYPE INFO ----------------------------------------
===========================================================================================================
[+] Type Name: BankTransferReference
[+] Description: Resources for setting up the Bank Transfer payment method
[+] Kind: OBJECT
[+] Fields: 
   [1]
   - name: beneficiary_required_details
   - description: None
   - args: [{u'defaultValue': None, u'description': None, u'name': u'currency'}, {u'defaultValue': None, u'description': None, u'name': u'bank_account_country'}, {u'defaultValue': None, u'description': None, u'name': u'beneficiary_country'}]
   - type: BeneficiaryRequiredDetail
    > description: A specification of information needed to create a bank transfer payment preference
    > kind: OBJECT

   [2]
   - name: countries
   - description: None
   - args: []
   - type: None
    > description: None
    > kind: LIST

   [3]
   - name: currencies
   - description: None
   - args: []
   - type: None
    > description: None
    > kind: LIST

   [4]
   - name: id
   - description: None
   - args: []
   - type: None
    > description: None
    > kind: NON_NULL

[+] Possible Types: None

terminal$  python gql.py -url https://hackerone.com/graphql? -q bank_transfer_reference
===========================================================================================================
     ---------------------------------------- QUERY TYPE INFO ----------------------------------------
===========================================================================================================
[+] Query Name: bank_transfer_reference
[+] Description: None
[+] Type: 
   - name: BankTransferReference
   - description: Resources for setting up the Bank Transfer payment method
[+] Args: 
[+] Generated GQL Query: Soon
   query { webhook_event_types(){ beneficiary_required_details{beneficiary_required_details{edges, nodes, pageInfo}, currency, id}, countries, currencies, id } }

```


Description:
	This is a GraphQL Schema Map Viewer. Please don't judge my coding skills

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

terminal$ python gql.py --url https://hackerone.com/graphql? -Q
===========================================================================================================
     ---------------------------------------- QUERY TYPE INFO ----------------------------------------
===========================================================================================================
[+] Query Name: application
[+] Description: None
[+] Type: 
   - name: None
   - description: None
[+] Args: 
[+] Generated GQL Query: Soon
===========================================================================================================
     ---------------------------------------- QUERY TYPE INFO ----------------------------------------
===========================================================================================================
[+] Query Name: assignable_teams
[+] Description: None
[+] Type: 
   - name: TeamConnection
   - description: The connection type for Team.
[+] Args: 
   [1]
   - name: after
   - default value: None
   - type: 
   	> name: String
   	> description: Represents textual data as UTF-8 character sequences. This type is most often used by GraphQL to represent free-form human-readable text.
   - description: Returns the elements in the list that come after the specified cursor.

   [2]
   - name: before
   - default value: None
   - type: 
   	> name: String
   	> description: Represents textual data as UTF-8 character sequences. This type is most often used by GraphQL to represent free-form human-readable text.
   - description: Returns the elements in the list that come before the specified cursor.

   [3]
   - name: first
   - default value: None
   - type: 
   	> name: Int
   	> description: Represents non-fractional signed whole numeric values. Int can represent values between -(2^31) and 2^31 - 1.
   - description: Returns the first _n_ elements from the list.

   [4]
   - name: last
   - default value: None
   - type: 
   	> name: Int
   	> description: Represents non-fractional signed whole numeric values. Int can represent values between -(2^31) and 2^31 - 1.

   	.
   	.
   	.
   	.
   	.

   	
```


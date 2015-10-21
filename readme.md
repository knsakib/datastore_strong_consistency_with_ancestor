For Datastore:
The way to get this Strong Consistency feature is to make the entities children of a parent key and use that parent key for an Ancestor Query.
In that case, what it does is that it looks in the event logs that needs to be processed. If waits until its finished and then it makes its query.  
Our Strong Consistency solution might not scale to millions of users (blocking isn't always great), but it'll work just fine for our needs today. :)
# RestFul API Design, Microservices, Microservice frameworks and microservice engineering practices

## A bit of history
 - HTTP - protocol that powers the web
    Basic operations when interacting with web sites:
      - Navigating to URL throug address bar (GET request)
      - Following links / redirects
      - Submitting FORMS (can be GET, but mostly POST)
    Sample form syntax:
        ```<html>
        <body>
             <form action="https://website.com/load_data" method="post" enctype="multipart/form-data">
                 <input type="file" name="datafile" />
                 <input type="text" name="comment" />
                 <input type="submit" />
             </form>
        </body>     
        </html>
    - POST is for MODIFYING data, GET is for retrieving data
    - Example of GET request:  curl -v https://en.wikipedia.org/wiki/Representational_state_transfer
    - Example of POST request: curl -v https://www.google.com -F comment=test

 -  Old-style webserver
    - Giving away fully-generated HTML as complete page (through use of templating engines)
    - have a concept of  *user session* (logging in and out, session is tracked on server by leveraging COOKIES)

**and then happened:
 - AJAX (Asynchronous web requests from inside javascript on the web page)
 - Frontend frameworks
 - Server doesnt need to generate complete HTML anymore. In fact it is needed only for DATA retrieval / saving operations.
 - Concept of microservices appear
    
## Introducing RestFul API design (2000, Roy Fielding, as a "HTTP Object model")

Initial concepts: Uniform interface, Cacheability, Layered System, Client-server architecture, Statelessness, Code-on-Demand
Central concepts devolved to: 
   - uniformity (with focus on simplicity)
   - statelessness 
   - state of objects are modified through representation (that's why it's REST - REpresentational State Transfer)
   
  Basic elements that could be accessed through specific URI:
   - RESOURCES
      GET /apples/1
   - RESOURCE COLLECTIONS
      GET /apples
      GET /apples?color=green
   - ACTIONS
      POST /apples/1/make_juice

 Examples of API calls:
    List items in the resource collection: GET to /apples  (HTTP 200 OK)
    Fetch particular resource item : GET to /apples/1 (HTTP 200 OK)
    Add new resource item: POST to /apples (HTTP 201 Created)
    Update existing item: PUT to /apples/1 (HTTP 200  OK or 204 - No Payload)
    Delete existing item: DELETE to /apples/1 (HTTP 200 OK or 204 - No Payload)

 HTTP Methods: GET, POST, PUT, DELETE    
 POST is not idempotent, all other are idempotent.
 
 HTTP Error mappings:
  - 200 OK - request completed successfully
  - 201 Created - New resource created
  - 204 No content - Existing resource was successfully created or updated
  - 400 Bad request - Invalid request
  - 401 Unauthorized - Authentication required
  - 403 Forbidden - User is not allowed to perform action
  - 404 Not found - Resource not found / not exists
  - 500 Internal Server Error
  
 HATEOAS - hyperlinking of resources.

Example of restful api: https://developer.zendesk.com/rest_api/docs/chat/chats

Authorization is usually done through 
  - Basic HTTP
  - Bearer token: Authorization: Bearer <TOKEN> 
  - API keys in headers, query string or cookies
    
Content negotiation: 
  - Headers Accept and Content-Type.   
  - postfixes for data retrieval URIs, e.g. GET /apples/1.json or /apples/1.xml
   

# PROBLEMS, PROBLEMS!!!   
## Data Validation
  - django-rest
    Detected from model.
     ``` 
         class UserSerializer(serializers.ModelSerializer):
             class Meta:
                 model = User
          
     ```
     Serialization is attached to resource handler in declarative manner:
     ```
        class UserViewSet(viewsets.ModelViewSet):
            queryset = User.objects.all().order_by('-date_joined')
            serializer_class = UserSerializer
            permission_classes = [permissions.IsAuthenticated]         
     ```

  
  - marshmallow
    ```
        class UserSchema(marshmallow.schema):
            class Meta:
                unknown = RAISE
            username = fields.String(required=True, validators=[Length(min=1, max=30)])
            password = fields.String(required=True, validators=[Length(min=1, max=30)])
        UserSchema().loads('{"username":"test","password":"123"}')
    ```
  - jsonschema https://json-schema.org/learn/miscellaneous-examples.html
  - cerberus (eve framework)
  
## API Documentation and API explorer
  - jsonschema
  - swagger / openapi : defines COMPLETE API SPECIFICATION: https://github.com/OAI/OpenAPI-Specification/blob/master/examples/v3.0/petstore.yaml
    object definitions based on jsonschema
  - django-rest api explorer
  - flaskapi

# RestFul frameworks

Actually, all of them are RESTful in some degree

## Django-rest (all in one)
## Flask-restful (plain restful router)
## Flask-restless (with sqlalchemy)
## eve  (document-based (mongo), validation through cerberus)
## Fastapi (recommended for async stuff)

# Ok, what's next?
   - OPENAPI 3.0
   - JSONAPI - essentially dead
   - GRAPHQL 
   - gRPC
   - Other fast RPC things (capnproto, flatbuffers, etc)

# MICROSERVICES (This is the fun part)

Evolution of a web system:
  - MONOLITH
  - microservices wrong way: monolith split to its parts, still tied with each other throuh RPC calls
  - micromonolith concept: separate domain of responsibility
 
Benefits of microservice design:
  - better scalability
  - smaller pieces to maintain

Cons of microservice design:
  - A lot of boilerplate dictated by operational ecosystem 
      In epam: accelerator projects
  - GREATLY increased system complexity, sometimes with performance issues
  - Distributed transactions are a pain

Best practices:
  - Meticulous documentation
  - Versioned API
  - No shared databases or interdependent data
   
 Operational:
  - Centralized configuration and secret management
  - Error management
  - Request tracing
  - SSO (single authorization framework)
  - Distributed logging
  - Monitoring
 
Tooling:
  - Relational DBs
  - Analytical DBs
  - Document-based DBs
  - Cache and transient storage
  - Queues
  - pubsub (notification) channels
  - Feed and stream processing

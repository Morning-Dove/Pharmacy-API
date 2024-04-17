Small FastAPI app with endpoints for serving up basic pharmacy information.

**Pharmacy API**

Attributes:

* first_name (string)
* last_name (string)
* address (string)
* age (integer)


## REST Endpoints

Name                           | Method | Path
-------------------------------|--------|------------------
Retrieve patients collection   | GET    | /patients
Create patients member         | POST   | /patients
Update patients member         | PUT    | /patients/*\<first_name\>*
Delete patients member         | DELETE | /patients/*\<first_name\>*

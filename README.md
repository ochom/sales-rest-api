
  <h3>
    <u>Supplier-Client api for building custom applications for the supply chain</u></h3>
		<h4>Instroduction</h4>
		<p>This restful api is build with django rest framework and provides simplicity in creating a supply application using webapps and or mobile applications
    <br>The hosted api is available at <a href="ochom.pythoneverywhere.com/api1/">This LINK</a>    
		<h5>You can download the zip file available <strong>SAMPLE</strong> and run it from your local machine</h5>
    <b>Models are:<b><br>
	<ul>
		<!-- <li>Sales Agents</li> -->
		<li>Clients</li>
		<li>Products</li>
		<li>Client Orders</li>
	</ul>

## To get all clients

	### Request

	`GET /clients/`

    curl -i -H 'Accept: application/json' http://ochom.pythoneverywhere.com/api1/clients/

    ### Response

	    HTTP/1.1 200 OK
	    Date: Thu, 24 Feb 2011 12:36:30 GMT
	    Status: 200 OK
	    Connection: close
	    Content-Type: application/json
	    Content-Length: 2

	    []


## Create a new client

	### Request

	`POST /thing/`

    curl -i -H 'Accept: application/json' -d 'Your JSON DATA' http://ochom.pythoneverywhere.com/api1/clients/


	### Response

	    HTTP/1.1 201 Created
	    Date: Thu, 24 Feb 2011 12:36:30 GMT
	    Status: 201 Created
	    Connection: close
	    Content-Type: application/json
	    Location: /clients/1

	    {
			"id": 1,
	        "username": "odhiambo",
	        "name": "Steven Adhiambo",
	        "address": "Nairobi",
	        "email": "adhiambo@mail.com",
	        "location": "0,0"
	    }

## Get a specific Client

	### Request

	`GET /client/id`

	    curl -i -H 'Accept: application/json' http://ochom.pythoneverywhere.com/api1/client/1

	### Response

	    HTTP/1.1 200 OK
	    Date: Thu, 24 Feb 2011 12:36:30 GMT
	    Status: 200 OK
	    Connection: close
	    Content-Type: application/json

	    {
			"id": 1,
	        "username": "odhiambo",
	        "name": "Steven Adhiambo",
	        "address": "Nairobi",
	        "email": "adhiambo@mail.com",
	        "location": "0,0"
	    }





## Products
	### Requests

		curl -i -H 'Accept: application/json' http://ochom.pythoneverywhere.com/api1/products/
		curl -i -H 'Accept: application/json' http://ochom.pythoneverywhere.com/api1/product/1


		{
	        "id": 1,
	        "product_name": "Hometheatre System",
	        "description": "Full set Hometheatre system for you",
	        "price": 45000,
	        "photo_url": "http://127.0.0.1:8000/media/images/products/154dabfb-e7a3-4dc7-be9b-546a89a600df.jpg",
	        "units": "boxes"
	    }



## Orders
	### Get Requests

		curl -i -H 'Accept: application/json' http://ochom.pythoneverywhere.com/api1/orders/
		curl -i -H 'Accept: application/json' http://ochom.pythoneverywhere.com/api1/order/1

		also 

		curl -i -H 'Accept: application/json'  http://ochom.pythoneverywhere.com/api1/orders/client=1
		curl -i -H 'Accept: application/json'  http://ochom.pythoneverywhere.com/api1/orders/product=1

		{
	        "id": 2,
	        "client_id": 1,
	        "agent_id": 3,
	        "product_id": 5,
	        "quantity": 5,
	        "total_cost": 56000,
	        "status": "devlivered"
	    }

# SOA_2026
Materials and Lab exercises for SOA 2026

**LAB --**

**Exercise 1**: Overview of Service-Oriented Architecture
**Goal:**
Understand basic SOA concepts by creating a simple service.
**What you do:**
Create a REST web service (e.g., /products, /users)
Use GET / POST methods
Run it locally
Consume the service using a client (browser / Postman / Curl)

**Key concepts:**
What a service is
Service exposure
Loose coupling
Service consumption


For windows if curl fails --

GET – Verify
Invoke-RestMethod http://127.0.0.1:5000/products

POST – Create a Product
Invoke-RestMethod `
  -Uri http://127.0.0.1:5000/products `
  -Method POST `
  -ContentType "application/json" `
  -Body '{"name":"Laptop","price":60000}'

PUT – Update the SAME Product
Invoke-RestMethod `
  -Uri http://127.0.0.1:5000/products/1 `
  -Method PUT `
  -ContentType "application/json" `
  -Body '{"name":"Gaming Laptop","price":75000}'

Example (Partial Update)
Invoke-RestMethod `
  -Uri http://127.0.0.1:5000/products/1 `
  -Method PUT `
  -ContentType "application/json" `
  -Body '{"price":80000}'


DELETE-
Invoke-RestMethod `
  -Uri http://127.0.0.1:5000/products/1 `
  -Method DELETE

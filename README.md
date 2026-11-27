# Integration Tests and Demo

## Project Description

This project demonstrates integration testing of a REST API built using FastAPI and SQLAlchemy.

It includes customer CRUD endpoints, API key authentication, webhook signature verification, and automated integration tests using pytest and TestClient.

The tests use a separate SQLite test database so that test data does not affect the normal application database.

## Technologies Used

- Python
- FastAPI
- SQLAlchemy
- SQLite
- Pytest
- TestClient
- pytest-cov
- HMAC and SHA-256
- Git and GitHub

## Features

- Create, read, update, and delete customers
- API key authentication
- Duplicate email validation
- Webhook signature verification
- Separate test database
- Integration tests for API endpoints
- Error handling for 401, 404, 409, and 422 responses
- Code coverage report

## Installation

Clone the repository:

```bash
git clone <your-repository-url>
```

Navigate to the project folder:

```bash
cd Integration_Tests_Demo
```

Create a virtual environment:

```bash
python -m venv .venv
```

Activate the virtual environment on Windows:

```powershell
.venv\Scripts\Activate
```

Install the required packages:

```bash
pip install fastapi uvicorn sqlalchemy psycopg2-binary pytest httpx pytest-cov python-dotenv email-validator
```

## Run the Application

Start the FastAPI server:

```bash
uvicorn src.main:app --reload
```

Open the API documentation:

http://127.0.0.1:8000/docs

## API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | `/` | Home endpoint |
| GET | `/health` | Health check |
| POST | `/customers/` | Create a customer |
| GET | `/customers/` | Get all customers |
| GET | `/customers/{customer_id}` | Get a customer |
| PUT | `/customers/{customer_id}` | Update a customer |
| DELETE | `/customers/{customer_id}` | Delete a customer |
| POST | `/webhook` | Receive a webhook |

Customer endpoints require the `X-API-Key` header.

## Authentication

The default development API key is:

```text
my-secret-api-key
```

Example request header:

```text
X-API-Key: my-secret-api-key
```

## Webhook Signature

The webhook uses HMAC with SHA-256 to verify the request body.

The signature must be sent using the following header:

```text
X-Webhook-Signature
```

The API rejects missing or invalid signatures with a 401 response.

The default development webhook secret is:

```text
my-webhook-secret
```

## Run Integration Tests

Run all tests:

```bash
pytest
```

Run tests with code coverage:

```bash
pytest --cov=src --cov-report=term-missing
```

## Test Cases

The integration tests cover:

- Successful customer creation
- Getting all customers
- Getting a customer by ID
- Updating a customer
- Deleting a customer
- Invalid or missing API key
- Customer not found
- Duplicate email
- Invalid customer data
- Valid webhook signature
- Tampered webhook signature
- Missing webhook signature

## Test Coverage

The project achieved **93% code coverage** during testing.

The coverage report was generated using pytest-cov.

## Learning Outcome

This project helped me understand:

- Integration testing with pytest
- Testing FastAPI endpoints using TestClient
- Using a separate test database
- Testing API error responses
- Testing webhook signatures
- Measuring code coverage
- Preparing a project for GitHub submission


## GitHub Actions

This project uses GitHub Actions for automated testing.

- Runs tests automatically on pushes and pull requests.
- Uses a PostgreSQL 16 service container.
- Runs pytest with coverage reporting.
- Uses SQLite for local testing.

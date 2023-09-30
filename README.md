# Book App Application

Welcome to Book App! This application is designed for Making Science as an internship test.

## Table of Contents

- [Introduction](#introduction)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
- [API Documentation](#api-documentation)
- [Unit Tests](#unit-tests)
- [Docker](#docker)

## Introduction

    This application serves as a platform for managing authors, books, genres, and conditions. It provides a set of API endpoints for creating, retrieving, updating, and deleting data related to these entities. Additionally, the application includes unit tests, and Docker support for containerized deployment.

Explore this README to learn how to get started with the application and leverage its features.

## Getting Started

These instructions will help you set up and run the application locally.

### Prerequisites

Before you begin, ensure you have the following prerequisites installed:

- Python 3.x
- PostgreSQL (if applicable)

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/testuser/testrepo.git
   ```


2. Navigate to the project directory:

   ```bash
   cd your-flask-app
   ```

3. Create a virtual environment (recommended):

   ```bash
   python -m venv venv
   ```

4. Activate the virtual environment:

   - For Windows:

     ```bash
     venv\Scripts\activate
     ```

   - For macOS and Linux:

     ```bash
     source venv/bin/activate
     ```

5. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

6. Set up your configuration (if needed).

## Usage

To interact with your Flask application, you can use the following methods:

### API Endpoints

Your Flask application provides the following API endpoints:

- **Create a new author:**
  - URL: `http://localhost:5000/authors` (POST)
  - Example request body:
    ```json
    {
      "name": "John Doe"
    }
    ```
- **Get all authors:**
  - URL: `http://localhost:5000/authors` (GET)

- **Get a specific author by ID:**
  - URL: `http://localhost:5000/authors/{author_id}` (GET)

- **Update an author by ID:**
  - URL: `http://localhost:5000/authors/{author_id}` (PUT)
  - Example request body:
    ```json
    {
      "name": "Updated Author Name"
    }
    ```

- **Delete an author by ID:**
  - URL: `http://localhost:5000/authors/{author_id}` (DELETE)

- **Create a new book:**
  - URL: `http://localhost:5000/books` (POST)
  - Example request body:
    ```json
    {
      "title": "Book Title",
      "author_id": 1,  # Replace with an existing author_id
      "genre_id": 1,   # Replace with an existing genre_id
      "condition_id": 1   # Replace with an existing condition_id
    }
    ```

- **Get all books:**
  - URL: `http://localhost:5000/books` (GET)

- **Get a specific book by ID:**
  - URL: `http://localhost:5000/books/{book_id}` (GET)

- **Update a book by ID:**
  - URL: `http://localhost:5000/books/{book_id}` (PUT)
  - Example request body:
    ```json
    {
      "title": "Updated Book Title",
      "author_id": 1,  # Replace with an existing author_id
      "genre_id": 1,   # Replace with an existing genre_id
      "condition_id": 1   # Replace with an existing condition_id
    }
    ```

- **Delete a book by ID:**
  - URL: `http://localhost:5000/books/{book_id}` (DELETE)

- **Create a new condition:**
  - URL: `http://localhost:5000/conditions` (POST)
  - Example request body:
    ```json
    {
      "name": "New Condition"
    }
    ```

- **Get all conditions:**
  - URL: `http://localhost:5000/conditions` (GET)

- **Get a specific condition by ID:**
  - URL: `http://localhost:5000/conditions/{condition_id}` (GET)

- **Update a condition by ID:**
  - URL: `http://localhost:5000/conditions/{condition_id}` (PUT)
  - Example request body:
    ```json
    {
      "name": "Updated Condition Name"
    }
    ```

- **Delete a condition by ID:**
  - URL: `http://localhost:5000/conditions/{condition_id}` (DELETE)

- **Create a new genre:**
  - URL: `http://localhost:5000/genres` (POST)
  - Example request body:
    ```json
    {
      "name": "New Genre"
    }
    ```

- **Get all genres:**
  - URL: `http://localhost:5000/genres` (GET)

- **Get a specific genre by ID:**
  - URL: `http://localhost:5000/genres/{genre_id}` (GET)

- **Update a genre by ID:**
  - URL: `http://localhost:5000/genres/{genre_id}` (PUT)
  - Example request body:
    ```json
    {
      "name": "Updated Genre Name"
    }
    ```

- **Delete a genre by ID:**
  - URL: `http://localhost:5000/genres/{genre_id}` (DELETE)

### Unit Tests

To run unit tests for your application, use the following command:

```bash
pytest
```
## Unit Tests

To run unit tests for the application, follow these steps:

1. Ensure you have the necessary testing dependencies installed (e.g., `pytest`).

2. Run the tests using the following command:

   ```bash
   pytest
   ```

   This will execute the unit tests and provide you with test results and coverage information.

## Docker

If you prefer to run the application in a Docker container, you can do so with the following steps:

1. Build the Docker image:

   ```bash
   docker build -t your-flask-app .
   ```

2. Run the Docker container:

   ```bash
   docker run -p 5000:5000 your-flask-app
   ```

   The application will be accessible at `http://localhost:5000`.
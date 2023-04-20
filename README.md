# Python API TDD and CI/CD Pipeline Demo

This project demonstrates a full Test-Driven Development (TDD) and Continuous Integration/Continuous Deployment (CI/CD) pipeline with a simple API. The API has the following characteristics:

## Endpoints 

- `GET /tasks`: Retrieve a list of all tasks. 
- `GET /tasks/<task_id>`: Retrieve a specific task by its unique identifier. 
- `POST /tasks`: Create a new task. 
- `PUT /tasks/<task_id>`: Update an existing task by its unique identifier. 
- `DELETE /tasks/<task_id>`: Delete a task by its unique identifier.

## Data Models

The API has a single data model, `Task`, with the following fields: 
- `id` (integer): A unique identifier for the task. 
- `title` (string): A short description of the task. 
- `description` (string): A detailed description of the task (optional). 
- `due_date` (datetime): The date and time by which the task must be completed (optional). 
- `completed` (boolean): Whether the task has been completed or not. Defaults to False.

## Business Logic

The API implements the following business logic: 
1. **Create a task** : Validate the input, generate a unique identifier, and store the task. 
2. **List tasks** : Retrieve all tasks stored in the system. 
3. **Get a task** : Retrieve a task by its unique identifier. 
4. **Update a task** : Validate the input, update the task with new data, and store the updated task. 
5. **Delete a task** : Remove a task by its unique identifier.

## Usage

You can run the API locally by installing the required dependencies and running the application:

```bash

pip install -r requirements.txt
python app.py
```

To run the tests, use the following command:

```bash

pytest tests
```
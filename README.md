# Flask Project for People Management

This project implements a simple API using Flask to manage information about people. It allows basic operations such as obtaining the list of people, retrieving information about a person by their ID, adding a new person, updating a person's information, and deleting a person by their ID.

## Project Structure

- **app.py**: Contains the main code of the Flask application.
- **Dockerfile**: Defines the configuration to build the Docker image of the application.
- **requirements.txt**: Lists Python dependencies necessary for the application.

## Usage

### Prerequisites

- Docker installed on the system.

### Build and Run the Application

1. Build the Docker image:

   ```bash
   docker build -t project_name .
   ```

2. Run the container:

   ```bash
   docker run -p 5000:5000 project_name
   ```

The application will be available at [http://localhost:5000](http://localhost:5000).

## API Endpoints

### Get All People

- **URL**: `/personas`
- **Method**: `GET`
- **Description**: Returns the list of all registered people.

### Get Person by ID

- **URL**: `/personas/<int:id>`
- **Method**: `GET`
- **Description**: Returns information about a specific person based on their ID.

### Add New Person

- **URL**: `/personas`
- **Method**: `POST`
- **Description**: Adds a new person using the information provided in the request body.

### Update Person by ID

- **URL**: `/personas/<int:id>`
- **Method**: `PUT`
- **Description**: Updates the information of a specific person based on their ID, using the information provided in the request body.

### Delete Person by ID

- **URL**: `/personas/<int:id>`
- **Method**: `DELETE`
- **Description**: Deletes a person based on their ID.

## Dockerfile

The Dockerfile builds the Docker image for the application. It installs dependencies specified in the `requirements.txt` file and exposes port 5000, which is the default port Flask runs on.

## Notes

- The application runs in debug mode (`debug=True`) to facilitate development. In a production environment, this value should be set to `False`.
- The application listens on all interfaces (`host='0.0.0.0'`) to allow external connections to the Docker container.

Enjoy exploring and working with the People Management API!

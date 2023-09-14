# API Documentation

This documentation provides information on how to use the CRUD API for managing "persons."

## API Endpoints

## Usage

To use this Django REST API, follow these instructions:

1. **Installation:**
     - follow the instruction in the README.md file on how to install this in your local machine

2. **API Endpoints:**

   - **Create a Person:**
     - **Endpoint:** `/api/`
     - **Method:** POST
     - **Request Format:**
       ```json
       {
         "name": "John Doe",
       }
       ```
     - **Response Format (Success - 201 Created):**
       ```json
       {
         "id": 1,
         "name": "John Doe",
       }
       ```

   - **Retrieve a Person:**
     - **Endpoint:** `/api/{id}/`
     - **Method:** GET
     - **Response Format (Success - 200 OK):**
       ```json
       {
         "id": 1,
         "name": "John Doe",
       }
       ```

   - **Update a Person:**
     - **Endpoint:** `/api/{id}/`
     - **Method:** PUT
     - **Request Format:**
       ```json
       {
         "name": "Updated Name",
       }
       ```
     - **Response Format (Success - 200 OK):**
       ```json
       {
         "id": 1,
         "name": "Updated Name",
       }
       ```

   - **Delete a Person:**
     - **Endpoint:** `/api/{id}/`
     - **Method:** DELETE
     - **Response (Success - 204 No Content)**

3. **Sample Usage:**

   Here are some sample API requests using cURL:

   - **Creating a Person:**
     ```shell
     curl -X POST -H "Content-Type: application/json" -d '{"name": "John Doe", "age": 30}' http://localhost:8000/api/persons/
     ```

   - **Retrieving a Person:**
     ```shell
     curl http://localhost:8000/api/1/
     ```

   - **Updating a Person:**
     ```shell
     curl -X PUT -H "Content-Type: application/json" -d '{"name": "Updated Name", "age": 35}' http://localhost:8000/api/persons/1/
     ```

   - **Deleting a Person:**
     ```shell
     curl -X DELETE http://localhost:8000/api/1/
     ```

4. **Known Limitations and Assumptions:**

   - Assumes that all person names should be unique.
   - Age is assumed to be a positive integer.
   - No authentication or authorization mechanisms are implemented in this example.
   - Error handling for invalid requests is not detailed in this documentation.

5. **Setting Up and Deploying the API:**

   To set up the API locally, follow the installation steps mentioned above. For deployment on a server, refer to your hosting provider's guidelines.

6. **Contributing:**

   Contributions are welcome! If you'd like to contribute to this project, please follow these steps:

   1. Fork the repository.
   2. Create a new branch for your feature or bug fix.
   3. Make your changes and commit them.
   4. Create a pull request with a detailed description of your changes.


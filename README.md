# Project Name - Django REST API for Persons

## Overview

This project is a simple Django REST API that allows you to perform CRUD (Create, Read, Update, Delete) operations on "persons." You can use this API to add, retrieve, update, and delete information about individuals. The API is designed to be flexible and secure, handling dynamic input parameters for operations like searching for persons by name.

**Table of Contents:**

- [Project Name - Django REST API for Persons](#project-name---django-rest-api-for-persons)
  - [Overview](#overview)
  - [Getting Started](#getting-started)
    - [Prerequisites](#prerequisites)
    - [Installation](#installation)

## Getting Started

### Prerequisites

Before setting up and running the API, ensure you have the following prerequisites installed:

- Python (3.6 or higher)
- Django
- Django REST Framework

## Installation

To use this Django REST API, follow these instructions:

1. **Installation:**
   - Clone the repository to your local machine:
     ```bash
     git clone https://github.com/codynego/HNG_stage2.git
     cd your-repo
     ```

   - Install project dependencies using pip:
     ```bash
     pip install -r requirements.txt
     ```

   - Apply database migrations:
     ```bash
     python manage.py makemigrations
     python manage.py migrate
     ```

   - Start the development server:
     ```bash
     python manage.py runserver
     ```


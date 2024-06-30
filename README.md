# Blog Application

A simple blog application allowing users to add, edit, delete, and paginate posts.

![Main window of the aplication](image-1.png)
![Main window of the aplication](image-2.png)

## Table of Contents

- [Features](#features)
- [Technologies](#technologies)
- [Setup](#setup)
- [Usage](#usage)

## Features

- Add new blog posts with a title, content and date.
- Edit and delete existing posts.
- Display the current date.

## Technologies

- HTML
- CSS
- JavaScript
- FastAPI for server communication
- Python
- PostgreSQL Database

## Setup

This section provides instructions on setting up your blog application, which uses FastAPI for the backend and PostgreSQL for the database.

Prerequisites
Ensure you have the following installed on your system:

- Python (version 3.7 or higher)
- PostgreSQL

1. Clone the repository to your local machine:

```bash
git clone https://github.com/julss2/blog.git
cd blog
```

2. Set Up a Virtual Environment (Optional but Recommended)

```bash
python -m venv venv
source venv/bin/activate   # On Windows, use `venv\Scripts\activate`
```

3. Install required packages

```bash
pip install -r requirements.txt
```

4. Configure the Database

- Start PostgreSQL: Ensure your PostgreSQL server is running.
- Create a Database: Create a new PostgreSQL database for the project:

```bash
CREATE DATABASE blog_db;
```

- Set Up Environment Variables: Create a .env file in the root of your project directory to store your database connection details. Add the following lines to the .env file, replacing the placeholders with your actual database credentials:

```bash
DATABASE_URL=postgresql://username:password@localhost/blog_db
```

Ensure you replace username, password, localhost, and blog_db with your actual PostgreSQL username, password, host, and database name respectively.

5. Apply Database Migrations
   Use Alembic to set up the database schema. Run the following commands to apply the database migrations:

```bash
alembic upgrade head
```

6. Run the FastAPI Application
   Start the FastAPI server:

```bash
uvicorn main:app --reload
```

This command will start the server and the application will be available at http://127.0.0.1:8000.

You can also access the automatically generated API documentation at http://127.0.0.1:8000/docs.

## Usage

1. Fill in the form with a title and content, then click the "Dodaj" button to add a new post.
2. The post will appear below the form.
3. Click "Edytuj" to edit a post, "Usuń" to delete a post.
4. Click "Zapisz" to save changes after editing, or "Anuluj" to cancel the edit.

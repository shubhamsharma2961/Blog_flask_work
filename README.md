# Blogging Website

Welcome to the Blogging Website repository! This guide will help you set up and run the website locally on your machine.

## Prerequisites

### Database Setup
1. **Import Database:**
    - Import the `database.sql` file provided into your MySQL database using phpMyAdmin or any MySQL management tool.
    - This will create the necessary tables for the website.

### Environment
1. **PHP Installation:**
    - Ensure you have PHP installed on your local machine.

2. **Local Server Environment:**
    - Set up a local server environment such as [XAMPP](https://www.apachefriends.org/index.html), [WAMP](http://www.wampserver.com/en/), or [MAMP](https://www.mamp.info/en/).

## Steps to Set Up

### 1. Download the Source Code
- Download or clone the repository from [GitHub Repository URL].

    ```sh
    git clone [GitHub Repository URL]
    ```

### 2. Configure Database Connection
1. **Navigate to the Project Directory:**
    - Open your terminal or command prompt and navigate to the project directory.

    ```sh
    cd path-to-project
    ```

2. **Update Database Settings:**
    - Open `config.php` (or the equivalent configuration file) and update the database connection settings to match your local database configuration:

    ```php
    define('DB_HOST', 'your-database-host');
    define('DB_USERNAME', 'your-database-username');
    define('DB_PASSWORD', 'your-database-password');
    define('DB_NAME', 'your-database-name');
    ```

### 3. Run the Local Server
- Start your local server environment (e.g., XAMPP, WAMP).

### 4. Access the Website
- Open your web browser and navigate to:

    ```url
    http://localhost/path-to-project/index.html
    ```

    - Replace `path-to-project` with the actual path where the project is located in your local server's `htdocs` or equivalent directory.

### 5. Explore the Website
- You should now be able to access the home page, about page, view, and contact page from the navigation menu.

## License
Specify the license under which the project is distributed.

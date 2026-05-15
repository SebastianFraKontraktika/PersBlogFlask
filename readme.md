# Flask Blog App

A personal blog platform built with Flask and MariaDB, where you can publish posts and readers can engage through comments and user profiles.

## Getting Started

### Prerequisites

- Python 3.x
- MariaDB installed and running

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/SebastianFraKontraktika/PersBlogFlask.git
   cd PersBlogFlask
   ```

2. Create and activate a virtual environment (recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install flask
   pip install mysql-connector-python
   ```

4. Set up the database:
   - Create a MariaDB database for the project
   (if you have not downloaded mariadb before then do this, else skip to next step)
   ```bash
   sudo mariadb -u root
   ```
   then in mariadb do this
   ```sql
   CREATE USER 'USERNAME'@'localhost' IDENTIFIED BY 'PASSWORD';
   GRANT ALL PRIVILEGES ON *.* TO 'brukernavn'@'localhost';
   FLUSH PRIVILEGES;
   ```
   login to your mariadb
   ```bash
   mysql -u USERNAME -p
   ```
   (P.S you exit mariadb with EXIT; or QUIT;) 
   When logged in, make a database for the project
   ```sql
   CREATE DATABASE database_name;
   USE database_name;
   ```
   when in the database, create the table:
   ```sql
   CREATE TABLE users (
      id       INT(11)      NOT NULL AUTO_INCREMENT,
      username VARCHAR(100) NOT NULL UNIQUE,
      email    VARCHAR(250) NOT NULL UNIQUE,
      password VARCHAR(100) NOT NULL,
      PRIMARY KEY (id)
   );
   ```
   - Update the database connection by creating a .env file in the projects root directory.
   ```bash
   touch .env
   ```
   Go into the .env file and add the following in it:
   ```bash
   secret_key = secret_key
   db_password = mariadb_password
   db_name = database_name
   username = mariadb_username
   ```
   P.S you can make a secret key with python in the terminal by writing this:
   ```bash
   python3 -c "import secrets; print(secrets.token_hex(32))"
   ```

5. Run the app:
   ```bash
   flask run
   ```

   The app will be available at `http://127.0.0.1:5000`


## Features

- **Authentication system** — Register, log in, and manage your account securely
- **Post management** — Create, publish, and manage blog posts
- **Commenting** — Registered users can comment on posts
- **Personal profiles** — Users get their own profile page to save and manage their content

## Tech Stack

- **Backend:** Python / Flask
- **Database:** MariaDB (via `mysql-connector-python`)

## Contributing

This is a personal project, but feel free to open an issue or fork the repo if you find something useful.

## Troubleshooting

if you have any trouble, then you can open an issue, or you can contact me.

## License

This project is released into the public domain under the [Unlicense](https://unlicense.org). You are free to use, copy, modify, and distribute it without any restrictions.

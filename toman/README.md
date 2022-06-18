# Project Setup

## Step 1 – Installing the Components from the Ubuntu Repositories

First you will install the essential components. This includes pip, the Python package manager for installing and managing Python components, and also the database software with its associated libraries.

You will be using Python 3, which ships with Ubuntu 20.04. Start the installation by typing:

    ➜ ~ sudo apt update
    ➜ ~ sudo apt install python3-venv python3-pip python3-dev libpq-dev postgresql postgresql-contrib

With the installation out of the way, you can move on to the database.

## Step 2 – Creating a Database and Database User

By default, Postgres uses an authentication scheme called “peer authentication” for local connections. Basically, this means that if the user’s operating system username matches a valid Postgres username, that user can login with no further authentication.

During the Postgres installation, an operating system user named postgres was created to correspond to the postgres PostgreSQL administrative user. You need to use this user to perform administrative tasks. You can use sudo and pass in the username with the -u option.

Log into an interactive Postgres session by typing:

    ➜ ~ sudo -u postgres psql

First, you will create a database for the Django project. Each project should have its own isolated database for security reasons. We will call the database myproject in this guide, but it’s always better to select something more descriptive:

    postgres=# CREATE DATABASE toman_interview;



Note: Remember to end all commands at an SQL prompt with a semicolon.

Next, you will create a database user which you will use to connect to and interact with the database. Set the password to something strong and secure:

    postgres=# CREATE USER tomanuser WITH PASSWORD 'tomanpassword';

Afterwards, you will modify a few of the connection parameters for the user you just created. This will speed up database operations so that the correct values do not have to be queried and set each time a connection is established.

    postgres=# ALTER ROLE tomanuser SET client_encoding TO 'utf8';
    postgres=# ALTER ROLE tomanuser SET default_transaction_isolation TO 'read committed';
    postgres=# ALTER ROLE tomanuser SET timezone TO 'UTC';

You are setting the default encoding to UTF-8, which Django expects. You are also setting the default transaction isolation scheme to “read committed”, which blocks reads from uncommitted transactions. Lastly, you are setting the timezone. By default, your Django projects will be set to use UTC. These are all recommendations from the Django project itself.

Now, all you need to do is give your database user access rights to the database you created:

    postgres=# GRANT ALL PRIVILEGES ON DATABASE toman_interview TO tomanuser;

Exit the SQL prompt to get back to the postgres user’s shell session:

    postgres=# \q

## Step 3 - Install project requirements and running project

Now that your database is set up, you can install Django. For better flexibility, you will install Django and all of its dependencies within a Python virtual environment. The virtualenv package allows you to create these environments easily.

Clone and move into project directory :

    ➜ ~ git clone .git
    ➜ ~ cd interview-project

You can create a virtual environment to store the project’s Python requirements by typing:

    ➜ interview-project python3 -m venv .venv

This will install a local copy of Python and a local pip command into a directory called myprojectenv within your project directory.

Before you install applications within the virtual environment, you need to activate it. You can do so by typing:

    ➜ interview-project source venv/bin/activate

Your prompt will change to indicate that you are now operating within the virtual environment. It will look something like this 

    (venv) ➜ interview-project

Once your virtual environment is active, you can install the official release of Django with pip. You will also install the psycopg2 package that will allow us to use the Postgres database you configured:



Note: Regardless of which version of Python you are using, when the virtual environment is activated, you should use the pip command (not pip3).

    (venv) ➜ interview-project pip install -r requirements.txt

You can now start a Django project within the myproject directory. This will create a child directory of the same name to hold the code itself, and will create a management script within the current directory. Make sure to add the dot at the end of the command so that this is set up correctly:

    
Configure the Django Settingsz environment variables

Now that you have a project, you need to configure it to use the database you created.

Open the main Django project settings file located within the child project directory:

    (venv) ➜ interview-project cp .env-example interview-project/.env


When you are done, you're ready to migrate the Database and test the project.

Now that the Django settings are configured, you can migrate the data structures to your database and test out the server.

You can begin by creating and applying migrations to your database. Since you don’t have any actual data yet, this will simply set up the initial database structure:

    (venv) ➜ interview-project python manage.py makemigrations
    (venv) ➜ interview-project python manage.py migrate

After creating the database structure, you can create an administrative account by typing:

    (venv) ➜ interview-project python manage.py createsuperuser

You will be asked to select a username, provide an email address, and choose and confirm a password for the account.

If you followed the initial server setup guide, you should have a UFW firewall in place. Before you can access the Django development server to test your database, you need to open the port in your firewall.

Allow external connections to the port by typing:

    (venv) ➜ interview-project sudo ufw allow 8000

Once you have the port open, you can test that your database is performing correctly by starting up the Django development server:

    (venv) ➜ interview-project python manage.py runserver 0.0.0.0:8000

In your web browser, visit your server’s domain name or IP address followed by :8000 to reach default Django 400 error page and that means you run this project successfully:

    http://server_domain_or_IP:8000
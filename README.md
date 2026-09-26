🍎 PyShop — Fruit Shop Web Application
📖 About PyShop

PyShop is a fruit shop web application built with Python and Django. The project is designed to demonstrate how a real-world e-commerce-style website can be structured using Django's framework.

The main purpose of PyShop is to provide a simple platform where users can view available fruits and their information through a web interface. The project also serves as a practical learning project for understanding how Django connects different parts of a web application, including Python code, HTML templates, databases, URLs, models, views, and Django's management system.

Although PyShop is currently focused on a fruit shop, its structure can be expanded into a larger online shopping platform containing different categories of products.

🛒 What PyShop Does

PyShop provides the foundation for a fruit-shopping website.

A typical user can visit the website and see products available in the shop. Each product can contain information such as:

🍎 Product name
💰 Product price
📝 Product description
🖼️ Product image
📦 Product availability

The project separates the website's structure, business logic, and database information, making it easier to maintain and expand.

For example, instead of writing every fruit directly into an HTML page, the products can be stored in the database and then retrieved by Django and displayed dynamically.

This is one of the important concepts demonstrated by PyShop:

The website is not just a collection of HTML pages. It is a dynamic application where Python, Django, HTML, and a database work together.

🏗️ Project Structure

A simplified structure of PyShop may look like this:

PyShop/
│
├── manage.py
│
├── pyshop/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── product/
│   ├── migrations/
│   ├── templates/
│   │   └── product/
│   │       └── index.html
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   ├── views.py
│   └── urls.py
│
├── db.sqlite3
│
└── templates/
    └── ...

The exact structure can vary depending on how the project is organized, but the main components have specific responsibilities.

🍊 1. Product

The product folder is a Django application inside the PyShop project.

It is responsible for functionality related to the products sold by the fruit shop.

For example, the product app can handle:

Creating products
Storing product information
Retrieving products
Displaying products
Updating products
Deleting products
Managing product-related pages

The product app keeps product-related functionality organized instead of placing everything inside the main PyShop project.

Models

One of the most important files inside the product app is:

models.py

Models define the structure of the information that will be stored in the database.

For example, a product model could contain:

class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField()
    description = models.TextField()

This tells Django that a product has a name, price, and description.

Django can then use this model to create the appropriate database structure.

Views

Another important file is:

views.py

Views contain the Python logic that determines what happens when a user visits a particular page.

For example, a view could retrieve products from the database and send them to an HTML template:

def index(request):
    products = Product.objects.all()
    return render(request, 'product/index.html', {
        'products': products
    })

The view acts as a connection between the database and the HTML page.

🏪 2. PyShop

The pyshop folder is the main Django project configuration.

It is different from the product application.

This distinction is important.

pyshop = Main Project

The pyshop folder contains the configuration that controls the overall Django website.

product = Application

The product folder contains functionality for a particular part of the website—in this case, the fruit products.

A single Django project can contain multiple applications.

For example, PyShop could eventually contain:

pyshop/
│
├── product/
├── customers/
├── orders/
├── payments/
└── accounts/

The main pyshop project would coordinate these applications.

⚙️ Important PyShop Files
settings.py

The settings.py file contains the main configuration of the Django project.

It can contain settings for:

Installed applications
Database configuration
Templates
Static files
Media files
Security settings
Time zone
Middleware

For example, Django needs to know which applications belong to the project. The INSTALLED_APPS section is used for this.

The database configuration is also defined in this file.

urls.py

The main:

pyshop/urls.py

controls the URL routing for the project.

It determines which part of the application should handle a particular URL.

For example:

/products/

could be directed to the product application's URL configuration.

This creates a chain:

Browser
   ↓
pyshop/urls.py
   ↓
product/urls.py
   ↓
views.py
   ↓
Database
   ↓
HTML Template
   ↓
Browser

This is an important part of understanding how Django applications work.

asgi.py

asgi.py provides an entry point for Django applications that use ASGI, which supports asynchronous web applications.

It is useful when deploying Django applications with servers that support ASGI.

wsgi.py

wsgi.py provides an entry point for Django applications using WSGI.

It is commonly involved when deploying Django applications with traditional Python web servers.

For a beginner project, you generally do not need to modify these files frequently.

📄 3. Templates

The templates folder contains the HTML files used to display the website.

For example:

templates/
└── product/
    └── index.html

The HTML template controls what the user actually sees in the browser.

A template can contain normal HTML:

<h1>PyShop</h1>

But Django templates can also contain dynamic template syntax:

{% for product in products %}

    <h2>{{ product.name }}</h2>

{% endfor %}

This allows Django to take information retrieved from the database and insert it into the HTML page.

🔄 How Templates Work

Suppose the database contains:

Apple
Banana
Orange
Mango

The Django view retrieves those products.

The view then sends them to the template.

The template loops through them:

{% for product in products %}
    <h2>{{ product.name }}</h2>
{% endfor %}

The browser can then display:

Apple
Banana
Orange
Mango

This is much more powerful than manually writing every product into the HTML file.

🗄️ 4. db.sqlite3

db.sqlite3 is the database file used by PyShop.

Django can use different database systems, but SQLite is commonly used for development and beginner Django projects because it is simple to set up.

The database stores structured information used by the application.

For PyShop, this could include information such as:

Products
Customers
Orders
Prices
Descriptions

For example, the product table might contain:

ID	Name	Price
1	Apple	500
2	Banana	300
3	Orange	400
4	Mango	600

The exact structure depends on the models created in the project.

🔗 Django and SQLite

Django's ORM (Object-Relational Mapper) allows Python code to interact with the database.

Instead of writing SQL for every operation, you can use Python/Django code such as:

Product.objects.all()

to retrieve products.

You can also create a product using a model:

Product.objects.create(
    name="Apple",
    price=500
)

Django translates these operations into the appropriate database queries.

This makes working with databases much easier from Python.

🛠️ 5. manage.py

manage.py is one of the most important files in a Django project.

It is a command-line utility that allows you to interact with your Django project.

For example, you can start the development server with:

python manage.py runserver

Django will start a local development server, allowing you to open the website in your browser.

Important manage.py Commands
Start the Development Server
python manage.py runserver

This allows you to run PyShop locally.

Create Migrations
python manage.py makemigrations

This tells Django to create migration instructions based on changes made to your models.

Apply Migrations
python manage.py migrate

This applies the migrations to the database.

It helps Django create and update database tables.

Create an Admin User
python manage.py createsuperuser

This creates a user that can log into Django's administration interface.

Open the Django Shell
python manage.py shell

This allows you to interact with your Django project using Python.

For example, you can work with your models directly from the shell.

🔄 How All the Components Work Together

One of the most important things PyShop demonstrates is how the different components communicate.

Imagine a user visits:

http://127.0.0.1:8000/products/

The process can look like this:

Step 1 — Browser

The user requests the products page.

↓

Step 2 — URL Configuration

Django receives the URL and checks:

pyshop/urls.py

↓

Step 3 — Product Application

The request is directed to the product application.

↓

Step 4 — View

The view in:

product/views.py

handles the request.

↓

Step 5 — Database

The view retrieves product information from:

db.sqlite3

using Django's ORM.

↓

Step 6 — Template

The product information is sent to:

product/templates/product/index.html

↓

Step 7 — Browser

Django renders the HTML and sends the finished webpage back to the user.

The user sees the available fruits.

🧩 PyShop Architecture

The relationship can be represented as:

                  PYSHOP
                    │
          ┌─────────┴─────────┐
          │                   │
       Project              Product
          │                   │
     pyshop/              product/
          │                   │
     ┌────┴────┐        ┌─────┴─────┐
     │         │        │           │
 settings.py  urls.py  models.py  views.py
     │                    │           │
     │                    └─────┬─────┘
     │                          │
     │                     db.sqlite3
     │                          │
     └──────────────┬───────────┘
                    │
                Templates
                    │
                    ↓
                 Browser

This architecture separates different responsibilities.

The database stores information.

The models define the structure of that information.

The views process requests and retrieve information.

The URLs determine where requests should go.

The templates display information.

The main PyShop project brings the different parts together.

🌱 Future Improvements

PyShop can be expanded considerably as the project develops.

Possible future features include:

🔐 User registration and login
🛒 Shopping cart
💳 Payment system
📦 Order management
🔎 Product search
🏷️ Product categories
📊 Admin dashboard
❤️ Favourite products
⭐ Product reviews and ratings
📱 Responsive mobile design
🖼️ Product images
📧 Order confirmation emails
👤 Customer profiles
🚚 Delivery tracking

These features would turn PyShop from a simple learning project into a more complete e-commerce application.

🎯 What This Project Demonstrates

PyShop demonstrates several important web-development concepts:

Python programming
Django web development
Django project structure
Django applications
URL routing
Views
Models
Templates
Template inheritance
Databases
SQLite
Django ORM
Database migrations
Dynamic webpages
HTML integration
CRUD operations
Git and GitHub project management
💡 Learning Purpose

PyShop is more than just a fruit-shop website.

It is a practical project for learning how the different parts of a modern web application communicate with one another.

Instead of treating Python, HTML, databases, and web pages as separate technologies, PyShop demonstrates how they can be combined into one working application.

The project can therefore serve as a foundation for learning more advanced Django concepts and eventually building larger applications.

🚀 Running the Project

After cloning the project, navigate to the project directory:

cd PyShop

Activate your virtual environment if you have one configured, then run:

python manage.py migrate

Start the Django development server:

python manage.py runserver

Django will provide a local address that can be opened in a web browser.

📌 Conclusion

PyShop is a Django-based fruit shop application created to demonstrate the fundamentals of building a dynamic web application.

The project brings together:

Python + Django + HTML + Templates + SQLite + Database Models + Views + URLs

The product application manages product-related functionality, the pyshop project provides the main configuration, templates control the presentation layer, db.sqlite3 stores application data, and manage.py provides the commands needed to develop and manage the Django project.

Together, these components form the foundation of PyShop and provide a strong starting point for developing more advanced web applications.

👨‍💻 Project

Project Name: PyShop
Project Type: Fruit Shop Web Application
Framework: Django
Programming Language: Python
Database: SQLite
Frontend: HTML / CSS
Purpose: Django and full-stack web-development practice

# GreatKart - Django E-Commerce Application

A full-featured e-commerce platform built with **Django** and **Django REST Framework**. GreatKart provides a complete online shopping experience with user authentication, product management, shopping cart functionality, and order processing.

## 📋 Table of Contents

- [Project Overview](#project-overview)
- [Features](#features)
- [Technology Stack](#technology-stack)
- [Project Structure](#project-structure)
- [Prerequisites](#prerequisites)
- [Installation & Setup](#installation--setup)
- [Configuration](#configuration)
- [Database Models](#database-models)
- [Running the Application](#running-the-application)
- [API Endpoints](#api-endpoints)
- [Contributing](#contributing)
- [License](#license)

---

## 🎯 Project Overview

**GreatKart** is a comprehensive e-commerce web application designed to provide an intuitive shopping experience for customers while offering robust admin management tools. The application is built using Django, a powerful and versatile Python web framework, ensuring scalability, security, and maintainability.

The platform supports:
- **User Management**: Registration, login, profile management with custom user model
- **Product Catalog**: Browse products by category with detailed descriptions and images
- **Shopping Cart**: Add/remove products with quantity management
- **Order Management**: Place orders, track order status, and view order history
- **Reviews & Ratings**: Customers can rate and review products
- **Product Variations**: Support for different product options (colors, sizes, etc.)
- **Email Notifications**: Automated email communication for order confirmations and notifications

---

## ✨ Features

### User Features
- ✅ Custom user authentication system with email-based login
- ✅ User registration and account creation
- ✅ User profile management (address, phone, profile picture)
- ✅ Session timeout management (1-hour default session)
- ✅ Email verification and password reset functionality

### Product Features
- ✅ Product catalog with categories and subcategories
- ✅ Product search and filtering
- ✅ Product images and gallery
- ✅ Product variations (color, size options)
- ✅ Stock management and availability tracking
- ✅ Rich product descriptions

### Shopping Features
- ✅ Shopping cart functionality
- ✅ Add/remove items from cart
- ✅ Quantity adjustment
- ✅ Real-time cart counter
- ✅ Cart persistence

### Review & Rating System
- ✅ Product reviews and ratings (1-5 stars)
- ✅ Review moderation
- ✅ Average rating calculation
- ✅ Review count aggregation

### Order Management
- ✅ Order placement and confirmation
- ✅ Order tracking
- ✅ Order history
- ✅ Admin order management panel

### Security Features
- ✅ CSRF protection
- ✅ Session timeout middleware
- ✅ Admin honeypot for security
- ✅ Secure password hashing

---

## 🛠️ Technology Stack

### Backend
- **Python 3.x** - Programming language
- **Django 3.1+** - Web framework
- **SQLite3** (default) or **PostgreSQL** - Database
- **Pillow** - Image processing
- **Python Decouple** - Environment variable management

### Frontend
- **HTML5** - Structure
- **CSS3** - Styling
- **JavaScript** - Interactivity
- **Django Templates** - Server-side templating

### Additional Libraries
- **django-session-timeout** - Session management
- **django-admin-honeypot** - Security enhancement
- **Requests** - HTTP library (if applicable)

---

## 📁 Project Structure

```
GreatKart/
│
├── greatkart/                      # Main project configuration
│   ├── settings.py                # Django settings
│   ├── urls.py                    # URL routing
│   ├── wsgi.py                    # WSGI configuration
│   ├── asgi.py                    # ASGI configuration
│   └── static/                    # Project-level static files
│
├── accounts/                       # User management app
│   ├── models.py                  # Account and UserProfile models
│   ├── views.py                   # Authentication views
│   ├── urls.py                    # Account URL routes
│   ├── forms.py                   # Authentication forms
│   └── templates/                 # Account templates
│
├── store/                         # Product management app
│   ├── models.py                  # Product, Variation, Review models
│   ├── views.py                   # Product views
│   ├── urls.py                    # Store URL routes
│   ├── admin.py                   # Admin configuration
│   └── templates/                 # Product templates
│
├── category/                      # Category management app
│   ├── models.py                  # Category model
│   ├── views.py                   # Category views
│   └── context_processors.py      # Menu navigation processor
│
├── carts/                         # Shopping cart app
│   ├── models.py                  # Cart model
│   ├── views.py                   # Cart functionality
│   ├── context_processors.py      # Cart counter processor
│   └── templates/                 # Cart templates
│
├── orders/                        # Order management app
│   ├── models.py                  # Order models
│   ├── views.py                   # Order views
│   └── templates/                 # Order templates
│
├── templates/                     # Global templates
│   ├── base.html                  # Base template
│   ├── includes/                  # Reusable template includes
│   └── ...
│
├── static/                        # Static assets
│   ├── css/                       # Stylesheets
│   ├── js/                        # JavaScript files
│   └── images/                    # Images
│
├── media/                         # User-uploaded content
│   └── photos/                    # Product photos
│
├── manage.py                      # Django management script
├── .env-sample                    # Environment variables template
├── .gitignore                     # Git ignore file
└── README.md                      # This file
```

---

## 📋 Prerequisites

Before you begin, ensure you have the following installed:

- **Python 3.7+** - [Download Python](https://www.python.org/downloads/)
- **pip** - Python package installer (comes with Python)
- **Git** - Version control system
- **Virtual Environment** - Recommended for project isolation

---

## 🚀 Installation & Setup

### Step 1: Clone the Repository

```bash
git clone https://github.com/tushar75083/GreatKart.git
cd GreatKart
```

### Step 2: Create and Activate Virtual Environment

**On macOS/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

**On Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

If `requirements.txt` doesn't exist, install the necessary packages:

```bash
pip install django==3.1
pip install pillow
pip install python-decouple
pip install django-session-timeout
pip install django-admin-honeypot
pip install psycopg2-binary  # For PostgreSQL support (optional)
```

### Step 4: Configure Environment Variables

Copy the `.env-sample` file to `.env`:

```bash
cp .env-sample .env
```

Edit the `.env` file with your configuration:

```env
# Email Configuration (Gmail example)
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_HOST_USER=your_email@gmail.com
EMAIL_HOST_PASSWORD=your_app_password
EMAIL_USE_TLS=True

# Django Security
SECRET_KEY=your-secret-key-here
DEBUG=True
```

**Note:** To generate a SECRET_KEY, run:
```bash
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

### Step 5: Apply Database Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### Step 6: Create a Superuser (Admin Account)

```bash
python manage.py createsuperuser
```

Follow the prompts to create an admin account with:
- First Name
- Last Name
- Email
- Username
- Password

### Step 7: Collect Static Files

```bash
python manage.py collectstatic --noinput
```

---

## ⚙️ Configuration

### Database Configuration

**Default (SQLite):**
The project is configured to use SQLite by default, which is suitable for development.

**Using PostgreSQL (Production):**

Uncomment and modify the PostgreSQL configuration in `greatkart/settings.py`:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'greatkart_ecommerce_application',
        'USER': 'postgres',
        'PASSWORD': 'your_password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

### Email Configuration

Add your email credentials to `.env`:

```env
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_HOST_USER=your_email@gmail.com
EMAIL_HOST_PASSWORD=your_app_password
EMAIL_USE_TLS=True
```

For Gmail:
1. Enable "Less Secure App Access" or use an "App Password"
2. Generate an App Password from your Google Account settings

### Session Configuration

Default session timeout is set to **1 hour**. Modify in `settings.py`:

```python
SESSION_EXPIRE_SECONDS = 3600  # 1 hour in seconds
```

---

## 📊 Database Models

### Accounts App
- **Account**: Custom user model with email-based authentication
- **UserProfile**: Extended user profile with address and profile picture

### Store App
- **Product**: Core product model with pricing, stock, and category
- **Variation**: Product variations (colors, sizes)
- **ReviewRating**: Customer reviews and ratings
- **ProductGallery**: Multiple product images

### Category App
- **Category**: Product categories and subcategories

### Carts App
- **Cart**: Shopping cart model linking users to products

### Orders App
- **Order**: Order information and status
- **OrderProduct**: Individual items in an order

---

## ▶️ Running the Application

### Start the Development Server

```bash
python manage.py runserver
```

The application will be available at: `http://localhost:8000`

### Access Admin Panel

Navigate to: `http://localhost:8000/admin/`

Login with your superuser credentials created during setup.

### Stop the Server

Press `CTRL + C` in your terminal.

---

## 🔌 API Endpoints

### Authentication
- `POST /accounts/register/` - User registration
- `POST /accounts/login/` - User login
- `GET /accounts/logout/` - User logout
- `GET /accounts/profile/` - View user profile

### Products
- `GET /store/` - List all products
- `GET /store/product/<slug>/` - Product detail
- `GET /category/<category_slug>/` - Products by category
- `POST /store/<slug>/review/` - Submit product review

### Cart
- `GET /cart/` - View shopping cart
- `POST /cart/add/<product_id>/` - Add to cart
- `POST /cart/remove/<product_id>/` - Remove from cart

### Orders
- `POST /order/place_order/` - Place an order
- `GET /order/order_complete/` - Order confirmation
- `GET /orders/` - View order history

---

## 👨‍💻 Contributing

Contributions are welcome! Here's how to get started:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

---

## 📝 License

This project is open source and available under the MIT License.

---

## 📧 Support & Contact

For issues, questions, or suggestions:
- Open an issue on [GitHub Issues](https://github.com/tushar75083/GreatKart/issues)
- Contact: tushar75083@gmail.com

---

## 🙏 Acknowledgments

- Django documentation and community
- All contributors and supporters

---

**Happy coding! 🚀**

# Ecommerce Website

A simple Django-based Ecommerce Website for educational purposes.

## Features

- Product catalog with categories
- Shopping cart functionality
- User authentication (login/registration)
- Guest checkout option
- Admin interface for managing products, categories, and orders

## Quick Start

1. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

2. Run migrations:
   ```
   python manage.py migrate
   ```

3. Create a superuser:
   ```
   python manage.py createsuperuser
   ```

4. Run the development server:
   ```
   python manage.py runserver
   ```

5. Visit http://127.0.0.1:8000/ in your browser

## Usage

- Browse products by category
- Add products to your cart
- Register or login to make purchases
- Checkout as a guest or registered user
- Admin interface at http://127.0.0.1:8000/admin/

## Deployment Preparation

This project is NOT ready for production deployment. Before deploying to a production environment, you MUST make the following changes:

1. **Security Settings**:
   - Change `SECRET_KEY` in `demo/settings.py` to a new random value
   - Set `DEBUG = False` in `demo/settings.py`
   - Configure `ALLOWED_HOSTS` with your domain name(s)

2. **Database**:
   - Switch from SQLite to PostgreSQL or MySQL for production
   - Update database settings in `demo/settings.py`

3. **Static Files**:
   - Configure a CDN or proper static file serving
   - Run `python manage.py collectstatic` for production

4. **Environment Variables**:
   - Use environment variables for sensitive settings
   - Never commit secrets to version control

5. **Web Server**:
   - Use a production web server like Nginx or Apache
   - Configure SSL/HTTPS

For detailed deployment instructions, refer to the Django deployment documentation:
https://docs.djangoproject.com/en/5.2/howto/deployment/

## Project Structure

```
demo/
├── manage.py
├── demo/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── myapp/
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   ├── admin.py
│   └── cart.py
└── templates/
    └── (HTML templates)
```

## Contributing

This project was created for educational purposes. Feel free to fork and modify as needed.
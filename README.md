# 🛒 Django eCommerce API

A backend-only eCommerce platform built with Django and Django REST Framework. This project supports user authentication, product management, reviews, scraping, and Stripe-based checkout.

---
## admin access
## email and password
-admin@gmail.com
-123456
## Features

###  User & Auth
- Custom user model with email as username
- Email verification during registration
- Password reset via email
- Login with email and password
- Profile API for authenticated users

### Shop
- Category & Product models
- Image upload support (Cloudinary)
- Product listing with:
  - Filtering by category
  - Search functionality
  - Pagination
- Product CRUD via DRF
- Product Reviews (one user can review multiple products)

### External Integration
- Web scraper to fetch book titles from [books.toscrape.com](https://books.toscrape.com)

###  Payment (Stripe)
- Add to cart system (by session or user)
- Stripe integration for checkout
- Payment intent creation
- Stripe webhook handling ready (optional)


---

## Tech Stack

- Python 3.x
- Django 4.x
- Django REST Framework
-  SQLite (for development)
- Stripe API
- Cloudinary (for image/media upload)
- `requests + BeautifulSoup` (for scraping)
- `django-allauth` ( for email auth)

---

##  Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/yourname/django-ecommerce-api.git
cd django-ecommerce-api

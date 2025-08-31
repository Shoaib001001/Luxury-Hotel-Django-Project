Luxury Hotel Django Project

A complete hotel management web application built with Django featuring room booking, recipe sharing, user authentication, and contact management.

🌟 Features

User Authentication & Authorization - Secure login/registration system

Room Management - Browse and book luxurious rooms

Recipe Sharing - Users can share their favorite recipes

Contact System - Integrated contact form and management

Responsive Design - Beautiful UI that works on all devices

Admin Dashboard - Complete backend management system


🏗️ Project Structure


hotel_project/
├── hotel_project/          # Django project settings
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── home/                   # Home app - main pages
│   ├── templates/home/
│   ├── models.py
│   ├── views.py
│   └── urls.py
├── recipes/                # Recipes app - recipe sharing
│   ├── templates/recipes/
│   ├── models.py
│   ├── views.py
│   └── urls.py
├── authentication/         # Authentication app - user management
│   ├── templates/authentication/
│   ├── models.py
│   ├── views.py
│   └── urls.py
├── contact/                # Contact app - contact management
│   ├── templates/contact/
│   ├── models.py
│   ├── views.py
│   └── urls.py
├── static/                 # Static files
│   ├── css/
│   ├── js/
│   └── images/
├── templates/              # Base templates
│   └── base.html
├── manage.py
└── requirements.txt

📦 Django Apps Overview
🏠 Home App
Main landing page with hero section

Room listings and details

Booking functionality

Static pages (About, Services, etc.)

📝 Recipes App
Recipe sharing platform

User-generated content

Recipe categories and search

Rating and comment system

🔐 Authentication App
User registration and login

Password reset functionality

Profile management

Social authentication (optional)

📞 Contact App
Contact form with validation

Message management

Admin notification system

Contact information management

🗄️ Database Models
User Model (Extended)
Custom user profile with additional fields

Booking history

Recipe contributions

Room Model
Room types (Standard, Deluxe, Suite)

Pricing and availability

Amenities and features

Booking system

Recipe Model
Title, description, and ingredients

Cooking instructions

Categories and tags

User ratings and reviews

Contact Model
Visitor messages

Contact information

Response tracking

🎨 Frontend Features
Responsive Bootstrap 5 Design

Custom CSS with luxurious styling

Interactive JavaScript elements

Font Awesome icons

Smooth animations and transitions

Mobile-first approach
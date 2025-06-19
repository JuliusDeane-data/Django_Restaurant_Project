# My Restaurant App

This repository contains a simple web application built with **Django** and **Bootstrap 5**, designed to showcase basic restaurant menu functionality.

---

## 🚀 Project Overview

This project primarily serves as a **learning and practice exercise** for Django web development. It's built upon concepts taught in a Udemy course. Therefore, the application focuses on demonstrating core Django features and fundamental web development principles, rather than providing a comprehensive, production-ready solution. It's intended more as a **portfolio piece** to illustrate skills in Django, Python, HTML, CSS, and Bootstrap.

The application currently allows users to browse a menu of meals and add them to their cart (login required for adding meals).
They can also contact the restaurant via contact form.

---

## ✨ Key Features (Currently Implemented)

* **Meal Display:** View various meal items with their names, prices, and stock information.
* **User Login/Logout:** Users can register, log in, and log out to access certain features.
* **Order Functionality:** Authenticated users can "order" meals (simple click, no actual order processing yet).
* **Contact Form:** A basic contact form for users to send messages.
* **Responsive Design:** Basic responsiveness using Bootstrap 5.

---

## ⚙️ Technologies Used

* **Django:** Web framework for the backend logic.
* **Python:** Programming language.
* **HTML & CSS:** For structuring and styling the web pages.
* **Bootstrap 5:** For responsive design and UI components.

---

## 🔮 Future Enhancements

I plan to add the following features and improvements:

* **Shopping Cart Management:** Implement functionality to remove items from the shopping cart.
* **Order Submission:** Develop a full order submission process.
* **Bug Fixing & Refinements:** Address any existing display issues or bugs for a smoother user experience.
* **Contact Form Styling:** Visually enhance the contact form for better aesthetics and usability.

---

## 🏃 Getting Started

To run this project locally:

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/JuliusDeane-data/Django_Restaurant_Project.git](https://github.com/JuliusDeane-data/Django_Restaurant_Project.git)
    cd Django_Restaurant_Project
    ```
2.  **Create and activate a virtual environment:**
    ```bash
    python -m venv venv
    # On Windows
    .\venv\Scripts\activate
    # On macOS/Linux
    source venv/bin/activate
    ```
3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
4.  **Apply database migrations:**
    ```bash
    python manage.py migrate
    ```
5.  **Create a superuser (optional, for admin access):**
    ```bash
    python manage.py createsuperuser
    ```
6.  **Run the development server:**
    ```bash
    python manage.py runserver
    ```
7.  Open your browser and go to `http://127.0.0.1:8000/`.

---

## 📚 Learning Resource

This project's foundational concepts were derived from this comprehensive Django course on Udemy.

**Udemy Course Link:** [Django Mastery 2025: Build AI-Powered Apps Like a Pro](https://www.udemy.com/course/django-mastery-build-ai-powered-apps-like-a-pro/)
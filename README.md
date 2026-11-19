# Inventory Management System

## Project Overview

The Inventory Management System is a web-based application developed using Python and Django to manage products, suppliers, and categories in a small store.

It provides a simple interface to maintain inventory records, track product quantities, and organise supplier and category information.

## Features

- **Product Management:** Add, view, update and delete product records.
- **Supplier Management:** Maintain supplier details and contact information.
- **Category Management:** Organise products into categories.
- **Stock Management:** Track product prices and available quantities.
- **SKU Validation:** Prevent duplicate product SKU values.
- **Stock Validation:** Prevent negative stock quantities.
- **Django Admin Panel:** Manage inventory records through Django administration.
- **SQLite Database:** Store and manage application data.

## Technologies Used

- Python
- Django
- SQLite3
- HTML5
- CSS3
- Visual Studio Code

## Project Structure

```text
Inventory-Management-System/
│
├── app/
├── project/
├── manage.py
├── requirements.txt
└── README.md
```

## Installation and Setup

1. Clone the repository:

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

2. Navigate to the project directory:

```bash
cd Inventory-Management-System
```

3. Install the required dependencies:

```bash
pip install -r requirements.txt
```

4. Apply database migrations:

```bash
python manage.py migrate
```

5. Start the development server:

```bash
python manage.py runserver
```

6. Open the application in your browser:

```text
http://127.0.0.1:8000/
```

## Live Project

[Inventory Management System – View Live Website](https://haripriyadarshinim.pythonanywhere.com/)

## Future Enhancements

- Stock-in and stock-out tracking.
- Inventory reports and analytics.
- Low-stock notifications.
- Enhanced dashboard features.

## Author

**Haripriyadarshini M**

GitHub: [HaripriyadarshiniM](https://github.com/HaripriyadarshiniM)

---

*An inventory management application built to practise core Django concepts and database operations.*

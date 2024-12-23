
```markdown:README.md
# Python Bookstore Management System

A simple bookstore management system built with Python that allows you to manage and search through a collection of books.

## Features

- Create and manage books with unique IDs
- Store book information including:
  - Title
  - Author
  - Description
  - Year of release
- Search functionality (coming soon)
- Input validation using Pydantic
- UUID-based book identification

## Requirements

- Python 3.12
- Pydantic

## Installation

1. Clone the repository:
```bash
git clone https://github.com/KelvinxG/bookstore.git
```

2. Install dependencies:
```bash
pip install pydantic
```

## Usage

```python
from bookstore import Bookstore

# Create a new bookstore instance
bookstore = Bookstore()

# Add a new book
book = bookstore.create_book(
    title="The Great Gatsby",
    author="F. Scott Fitzgerald",
    description="A story of decadence and excess",
    year_release=1925
)

# Get all books
all_books = bookstore.get_all()

# Get a specific book by ID
book = bookstore.get_book(book_id)
```

## Data Model

Books are stored with the following attributes:
- `id`: UUID (automatically generated)
- `name`: String
- `author`: String
- `description`: String
- `year_release`: Integer (between 1900 and 2100)

## Contributing

Feel free to submit issues and enhancement requests.


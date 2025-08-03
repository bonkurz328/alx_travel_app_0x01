# ALX Travel App

A property listing and booking platform.

## Setup

1. Clone the repository
2. Create and activate a virtual environment
3. Install dependencies: `pip install -r requirements.txt`
4. Run migrations: `python manage.py migrate`
5. Seed the database: `python manage.py seed`
6. Run the development server: `python manage.py runserver`

## API Endpoints

- `/api/listings/` - GET/POST property listings
- `/api/listings/{id}/` - GET/PUT/PATCH/DELETE specific listing
- `/api/bookings/` - GET/POST bookings
- `/api/bookings/{id}/` - GET/PUT/PATCH/DELETE specific booking
- `/api/reviews/` - GET/POST reviews
- `/api/reviews/{id}/` - GET/PUT/PATCH/DELETE specific review

## Database Seeding

To populate the database with sample data:

```bash
python manage.py seed


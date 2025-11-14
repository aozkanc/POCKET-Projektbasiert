# Python 3.12
FROM python:3.12

# DIRECTORY
WORKDIR /app

# REQUIREMENTS
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# COPY ALL BACKEND FILES IN CONTAINER
COPY . .

# Migration and static file collection will be done before running the Django application.
CMD ["sh", "-c", "python manage.py migrate && python manage.py collectstatic --noinput && python manage.py runserver 0.0.0.0:8000"]

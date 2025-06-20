# Stage 1: Use an official Python runtime as a parent image
FROM python:3.12.8-slim

# Set environment variables for Python
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

# Set the working directory in the container
WORKDIR /app

# Install dependencies
# We copy requirements.txt first to leverage Docker's layer caching.
# If requirements.txt doesn't change, Docker won't reinstall dependencies on every build.
COPY requirements.txt .
RUN pip install --upgrade pip
# We need gunicorn to run our app in production
RUN pip install -r requirements.txt gunicorn

# Copy the rest of the application's code into the container
COPY . .

# Run collectstatic to gather all static files into one directory
# This will be served by Nginx
RUN python manage.py collectstatic --noinput

# The port the container will listen on (for internal communication)
EXPOSE 8000

# The command to run the application using Gunicorn
# This is a production-grade WSGI server, unlike the Django development server.
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "--chdir", "django", "todo.wsgi:application"]
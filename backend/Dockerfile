FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Install PostgreSQL client for pg_isready
RUN apt-get update && apt-get install -y postgresql-client && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Create wait-for-db script
RUN echo '#!/bin/sh\n\
echo "Waiting for PostgreSQL..."\n\
while ! pg_isready -h "$DB_HOST" -p "$DB_PORT" -U "$DB_USER" > /dev/null 2>&1; do\n\
  sleep 1\n\
done\n\
echo "PostgreSQL is ready!"\n\
exec "$@"' > /wait-for-db.sh && chmod +x /wait-for-db.sh

CMD ["/wait-for-db.sh", "sh", "-c", "python manage.py migrate && python manage.py runserver 0.0.0.0:8000"]

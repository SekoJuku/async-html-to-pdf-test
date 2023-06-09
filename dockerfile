FROM python:3.9-slim-buster

# Install dependencies
RUN pip install --upgrade pip
RUN pip install pipenv

# Set working directory
WORKDIR /app

# Install wget
RUN apt-get update && apt-get install libssl-dev wkhtmltopdf -y

#RUN apt-get install -f ./wkhtmltox_0.12.6.1-2.buster_ppc64el.deb

# Copy Pipfile and Pipfile.lock
COPY requirements.txt .

# Install dependencies
RUN pip install -r requirements.txt

# Copy project
COPY . .

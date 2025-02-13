# Stage 1: Node.js environment for building Tailwind CSS
FROM node:23-alpine AS builder

WORKDIR /app

# Copy package.json and package-lock.json
COPY package.json package-lock.json ./
RUN npm install tailwindcss @tailwindcss/cli
RUN npm install

# Copy Tailwind configuration files
COPY static/styles.css ./static/styles.css
COPY templates templates


# Build Tailwind CSS
RUN npm run build:css
RUN npm run minify-html

# Stage 2: Python environment for running Flask
FROM python:3.10-slim

WORKDIR /app

# Install Flask and any other dependencies
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copy the Flask application
COPY . .
RUN rm -rf static/styles.css requirements.txt Dockerfile package.json package-lock.json tailwind.config.js

# Copy the built Tailwind CSS from the first stage
COPY --from=builder /app/static/tailwind.css ./static/tailwind.css
COPY --from=builder /app/templates-min/* ./templates/

# Expose port and run the Flask app
EXPOSE 8000

CMD ["gunicorn", "-b", "0.0.0.0:8000", "-w", "4", "app:app"]

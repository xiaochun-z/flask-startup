A starter template for launching a Flask web application, showcasing the use of Tailwind CSS and HTML template minification.

a few command tips for you to start the sample.

```bash
docker build -t flask-startup .
docker run --rm -p 8000:8000 flask-startup

# or go into the container first and launch gunicorn manually.
docker run --rm -it -p 8000:8000 flask-startup /bin/bash
gunicorn -b 0.0.0.0:8000 -w 4 app:app

```

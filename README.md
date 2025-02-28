A starter template for launching a Flask web application(hosted in docker), showcasing the use of Tailwind CSS and HTML template minification.

This can be useful if you're focusing on the python and need some pre-configuration for GUI, or maybe you know python but are not quite familiar with flask. 

The example demonstrates how to use HTML templates, sessions, forms, Tailwind CSS, and HTML minification. It's a starting point for your Flask app.

Here are a few command tips for you to start the sample.


```bash
docker build -t flask-startup .
docker run --rm -p 8000:8000 flask-startup

# or go into the container first and launch gunicorn manually.
docker run --rm -it -p 8000:8000 flask-startup /bin/bash
gunicorn -b 0.0.0.0:8000 -w 4 app:app

```

mount with volume configuration so you can copy your files to your host, some people need this.
```bash
docker run --rm -it -p 8000:8000 -v "$(pwd)/build/out":/out flask-startup /bin/sh
# now you're in the container, copy everything out to your host machine
# so your can review all the final output files in your host machine
cp -r /app /out
```
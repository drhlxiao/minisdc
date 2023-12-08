# Interactive Website Template - minisdc

Welcome to minisdc, a Flask project template designed to help you create interactive websites with ease.

## How to Run

### Install Dependencies
```bash
pip install -r requirements.txt
```

### Run
Download the source code.

```bash
cd minisdc/
python wsgi.py
```

## Preview in Your Browser
Visit [http://localhost:5000](http://localhost:5000) in your browser.

## File Structure

- **routes.py** and modules in **blueprints/**
  - Define URL routes for your application.

- **wsgi.py**
  - Portal file for running the application.

- **blueprint/examples.py**
  - Add your code to query the database here. A dummy function is included as a placeholder.

- **templates/**
  - HTML templates for your web pages.

- **core/stix_bundle.py**
  - Module that bundles CSS and JS files when running Flask.

- **static/js/**
  - User JS files.

- **static/css/**
  - User CSS files.

- **static/vendor/css & js/**
  - Third-party CSS and JS files.

- **static/images/**
  - Static images for your project.

Feel free to customize and extend the functionality based on your project requirements. Happy coding!

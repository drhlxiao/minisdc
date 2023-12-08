#!/usr/bin/python3
"""
    This module compiles js and css files 
"""
from flask_assets import Bundle, Environment
def set_bundles(app):
    bundles = {
        'base_js':
        Bundle('vendor/js/jquery-3.4.1.min.js',
               'vendor/js/bootstrap.min.js',
               'vendor/js/daterangepicker.min.js',
               'vendor/js/flatpickr.js',
               'js/layout.js',
               'js/datetime-picker.js',
               output='gen/base.js',
               filters='jsmin'),
        'base_css':
        Bundle('vendor/css/bootstrap.min.css',
               'vendor/css/daterangepicker.css',
                'vendor/css/flatpickr.min.css',
               'css/layout.css',
               output='gen/base.css',
               filters='cssmin'
               ),
       'example_js':
        Bundle(
               'js/example.js',
               output='gen/example.js',
               filters='jsmin'
               ),
        'example_css':
        Bundle(
               'css/example.css',
               output='gen/example.css',
               filters='cssmin'),

    }

    assets = Environment(app)
    assets.register(bundles)
    return assets

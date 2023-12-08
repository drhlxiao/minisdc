#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
#  Author: Hualin Xiao (hualin.xiao@fhnw.ch)
#TODO:

import os
from flask import Flask
app = Flask(__name__)
from core import stix_bundle

app = Flask(__name__)
app.secret_key = b'\xe4Y\xd2\x079O\xde\x0f\x10\x1a\xf1\x02\xd5Cj?\xc4\xa3M_\xe2\xccg\xf9'

bundles=stix_bundle.set_bundles(app)


#include blueprints below
from blueprints.example import example
app.register_blueprint(example)

#include more below
#from blueprints.example2 import example2
#app.register_blueprint(ior_manager)


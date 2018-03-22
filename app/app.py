import os

from flask import Flask, request, render_template
from config import Config

APP = Flask(__name__)
APP.config.from_object(Config)

from models import *

import featureRequestManager, featureRequestService, routes

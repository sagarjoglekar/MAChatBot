import os
import sys
sys.path.insert(0,'../')
from flask import Flask, render_template, request, redirect, session
import json
from flask_cors import CORS
import datetime
from storage.data_models import connect_to_mongo, Vendor, Brand, JSONEncoder, Brief, Solution

from flask import Flask, request, jsonify, render_template, redirect, url_for, session, Response, make_response
import sys, json, datetime
import urllib2

from teammaker import app
from teammaker import firebase

# *********************** ROUTES ***********************

@app.route('/')
def index():
	result = firebase.get('/requests', None)
	print result
	return 'index'

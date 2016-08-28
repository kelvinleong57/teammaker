from flask import Flask, request, jsonify, render_template, redirect, url_for, session, Response, make_response
import sys, json, datetime
import urllib2

from teammaker_flask import app

from file_upload import upload_file

# *********************** ROUTES ***********************

@app.route('/')
def index():
	# result = firebase.get('/requests', None)
	# print result
	return render_template('index.html')

@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        success = upload_file(request)
        if success:
        	return 'success upload'
        else:
        	return 'invalid'
    return render_template('upload.html')
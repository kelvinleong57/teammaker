from flask import Flask, request, jsonify, render_template, redirect, url_for, session, Response, make_response
import sys, json, datetime
import urllib2

from teammaker import app

# *********************** ROUTES ***********************

@app.route('/')
def index():
	return 'index'

from nose.tools import *
from gothonweb import app
from flask import Flask

#passing to the Flask object, (from flask docs)"The config is actually a subclass of a dictionary and can be modified just like any dictionary:..."
app = Flask(__name__)
web = app.test_client()

def test_index():
    rv = web.get('/', follow_redirects=True)
    assert_equal(rv.status_code, 404)

    rv = web.get('/hello', follow_redirects=True)
    assert_equal(rv.status_code, 200)
    assert_in(b"Fill Out This Form", rv.data)

    data = {'name': 'jake', 'greet': 'yo'}
    rv = web.post('/hello', follow_redirects=True, data=data)
    assert_in(b"jake", rv.data)
    assert_in(b"yo", rv.data)
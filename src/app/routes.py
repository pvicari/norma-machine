from flask import render_template, request, jsonify
from .norma_machine import NormaMachine

from app import app

nm = NormaMachine()


@app.route('/', methods=['GET'])
@app.route('/index', methods=['GET'])
def index():
    return render_template('index.html')


@app.route('/set-0-to-reg', methods=['POST'])
def set_0_to_reg():
    assert request.path == '/set-0-to-reg'
    assert request.method == 'POST'

    nm.clear_response()
    response = nm.set_0_to_reg(request.form['reg'])

    return jsonify({'response': response})


@app.route('/set-n-to-reg', methods=['POST'])
def set_n_to_reg():
    assert request.path == '/set-n-to-reg'
    assert request.method == 'POST'

    nm.clear_response()
    response = nm.set_n_to_reg(request.form['reg'], int(request.form['val']))

    return jsonify({'response': response})


@app.route('/add-b-to-a', methods=['POST'])
@app.route('/add-b-to-a-with-c', methods=['POST'])
@app.route('/set-b-to-a-with-c', methods=['POST'])
@app.route('/mult-a-with-b', methods=['POST'])
@app.route('/test-a-lower-eq-than-b', methods=['POST'])
@app.route('/test-a-lower-than-b', methods=['POST'])
@app.route('/factorial', methods=['POST'])
@app.route('/power', methods=['POST'])
def todo():
    pass

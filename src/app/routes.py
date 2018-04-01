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
def add_b_to_a():
    assert request.path == '/add-b-to-a'
    assert request.method == 'POST'

    nm.clear_response()
    response = nm.add_b_to_a()

    return jsonify({'response': response})


@app.route('/add-b-to-a-with-c', methods=['POST'])
def add_b_to_a_with_c():
    assert request.path == '/add-b-to-a-with-c'
    assert request.method == 'POST'

    nm.clear_response()
    response = nm.add_b_to_a_with_c()

    return jsonify({'response': response})


@app.route('/set-b-to-a', methods=['POST'])
def set_b_to_a():
    assert request.path == '/set-b-to-a'
    assert request.method == 'POST'

    nm.clear_response()
    response = nm.set_b_to_a_with_c()

    return jsonify({'response': response})


@app.route('/mult-a-with-b', methods=['POST'])
def mult_a_with_b():
    assert request.path == '/multi-a-with-b'
    assert request.method == 'POST'

    nm.clear_response()
    response = nm.mult_a_with_b_with_c_and_d()

    return jsonify({'response': response})


@app.route('/test-a-lower-eq-than-b', methods=['POST'])
@app.route('/test-a-lower-than-b', methods=['POST'])
@app.route('/push', methods=['POST'])
def push_to_stack():
    assert request.path == '/push'
    assert request.method == 'POST'

    nm.clear_response()
    response = nm.push_to_stack(request.form['val'])

    return jsonify({'response': response})


@app.route('/pop', methods=['POST'])
def pop_from_stack():
    assert request.path == '/pop'
    assert request.method == 'POST'

    nm.clear_response()
    response = nm.pop_from_stack()

    return jsonify({'response': response})


@app.route('/factorial', methods=['POST'])
def factorial():
    assert request.path == '/factorial'
    assert request.method == 'POST'

    nm.clear_response()
    response = nm.factorial(request.form['n'])

    return jsonify({'response': response})


@app.route('/power', methods=['POST'])
def power():
    assert request.path == '/power'
    assert request.method == 'POST'

    nm.clear_response()
    response = nm.power(request.form['base'], request.form['exp'])

    return jsonify({'response': response})

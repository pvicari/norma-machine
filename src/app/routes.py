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

    nm.set_0_to_reg(request.form['reg'])

    return jsonify({'val': nm.get_reg_magnitude("A")})


@app.route('/set-n-to-reg', methods=['POST'])
@app.route('/set-n-to-reg', methods=['POST'])
@app.route('/set-n-to-reg', methods=['POST'])
@app.route('/set-n-to-reg', methods=['POST'])
@app.route('/set-n-to-reg', methods=['POST'])
def set_n_to_reg():
    pass

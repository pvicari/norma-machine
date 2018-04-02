# norma-machine

norma-machine é um simulador de Máquina Norma feito em Flask.

## Instalação
Siga essas instruções para obter uma cópia do projeto rodando localmente.

### Requisitos
* Python 3.6+

### Passos para instalação

1. clone o projeto: 
    
```
$ git clone https://github.com/pvicari/norma-machine
```

2. Crie um `virtualenv` dentro da pasta do projeto: 

```
$ cd norma-machine
$ python3.6 -m venv venv
```

3. Ative o `virtualenv`:

```
$ source venv/bin/activate # Linux
$ venv\Scripts\activate # Windows
```

4. Instale os pacotes necessários:

```
$ pip install -r requirements.txt
```

5. Crie a variável de ambiente para o Flask:

```
$ export FLASK_APP=src/main.py # Linux, Mac
$ set FLASK_APP=src\main.py # Windows
```

6. Tudo pronto, agora basta executar a aplicação e navegar para [localhost:5000](http://127.0.0.1:5000)

```
$ flask run
 * Serving Flask app "main"
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
```

## Utilização

```python
import app

app.set_0_to_reg('A') # A := 0
app.set_n_to_reg('A', 3) # A := 3
```

## Desenvolvimento

É recomendado para desenvolvedores acrescentar o parâmetro `reload` na execução do projeto para recarregar o webserver no caso de mudanças no código-fonte (alterações no template necessitam de uma reexecução do projeto no momento).

```
$ flask run --reload
 * Serving Flask app "main"
 * Restarting with stat # reaload com mudaças no código-fonte
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
```

## Contribuindo
Pull requests são bem vindas, porém, abra um issue para discução primeiro.

Certifique-se de atualizar os testes de maneira apropriada.

## Licença
[MIT](https://choosealicense.com/licenses/mit/)
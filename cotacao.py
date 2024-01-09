from flask import Flask, json , render_template
import json, requests

cotacoes = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL")
cotacoes = cotacoes.json()
cotacao_dollar = cotacoes['USDBRL']['bid']
cotacao_euro = cotacoes['EURBRL']['bid']
cotacao_btc = cotacoes['BTCBRL']['bid']


app = Flask(__name__)

@app.route('/')
def paginainicial():
    return render_template("cotacao.html", titulo='COTAÇÃO DO DIA', dollar=cotacao_dollar, euro=cotacao_euro, bitcoin=cotacao_btc)


if __name__ ==  "__main__":
    app.run(debug=True)
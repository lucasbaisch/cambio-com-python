import requests
import jsons
import pandas as pd

def main():
    Dollar = valor_dolar()
    Euro = valor_euro()
    Argentino = valor_peso()
    Venezuelano = valor_vef()
    BitCoin = valor_btn()
    Uruguaio = valor_uyu()
    export_csv(Dollar, Euro, Argentino, Venezuelano, BitCoin, Uruguaio)

def valor_dolar(url = "http://data.fixer.io/api/latest?access_key=6fa03799424534abe4cc423280fbb2e8&format=1"):
    response = requests.get(url)
    if response.status_code == 200:
        print("A conexão foi estabelecida com sucesso")
        dados = response.json()
    taxa_usd = dados['rates']['USD']
    taxa_brl = dados['rates']['BRL']
    real_dolar = taxa_brl / taxa_usd
    print("O valor do Dólar Americano no dia é %.4f" % real_dolar)
    real_dolar = round(real_dolar, 2)
    return real_dolar

def valor_euro(url = "http://data.fixer.io/api/latest?access_key=6fa03799424534abe4cc423280fbb2e8&format=1"):
    global dados
    response = requests.get(url)
    if response.status_code == 200:
        print("A conexão foi estabelecida com sucesso")
        dados = response.json()
    taxa_euro = dados['rates']['EUR']
    taxa_brl = dados['rates']['BRL']
    real_euro = taxa_brl / taxa_euro
    print("O valor do Euro é %.4f" % real_euro)
    real_euro = round(real_euro, 2)
    return real_euro

def valor_peso(url = "http://data.fixer.io/api/latest?access_key=6fa03799424534abe4cc423280fbb2e8&format=1"):
    response = requests.get(url)
    if response.status_code == 200:
        print("A conexão foi estabelecida com sucesso")
        dados = response.json()
    taxa_ars = dados['rates']['ARS']
    taxa_brl = dados['rates']['BRL']
    real_ars = taxa_brl / taxa_ars
    print("O valor do Peso Argentino dia é %.4f" % real_ars)
    real_ars = round(real_ars, 2)
    return real_ars

def valor_vef(url = "http://data.fixer.io/api/latest?access_key=6fa03799424534abe4cc423280fbb2e8&format=1"):
    response = requests.get(url)
    if response.status_code == 200:
        print("A conexão foi estabelecida com sucesso")
        dados = response.json()
    taxa_vef = dados['rates']['VEF']
    taxa_brl = dados['rates']['BRL']
    real_vef = taxa_brl / taxa_vef
    print("O valor do Peso Venezuelano é %.4f" % real_vef)
    real_vef = round(real_vef, 2)
    return real_vef

def valor_btn(url = "http://data.fixer.io/api/latest?access_key=6fa03799424534abe4cc423280fbb2e8&format=1"):
    response = requests.get(url)
    if response.status_code == 200:
        print("A conexão foi estabelecida com sucesso")
        dados = response.json()
    taxa_btc = dados['rates']['BTC']
    taxa_brl = dados['rates']['BRL']
    real_btc = taxa_brl / taxa_btc
    print("O valor do BitCoin é %.4f" % real_btc)
    real_btc = round(real_btc, 2)
    return real_btc

def valor_uyu(url = "http://data.fixer.io/api/latest?access_key=6fa03799424534abe4cc423280fbb2e8&format=1"):
    response = requests.get(url)
    if response.status_code == 200:
        print("A conexão foi estabelecida com sucesso")
        dados = response.json()
    taxa_uyu = dados['rates']['UYU']
    taxa_brl = dados['rates']['BRL']
    real_uyu = taxa_brl / taxa_uyu
    print("O valor do Peso Uruguaio é %.4f" % real_uyu)
    real_uyu = round(real_uyu, 2)
    return real_uyu

def export_csv(dollar, euro, peso, venezuelano, bitcoin, uruguaio):
    #cria a linha na tabela do Excel
    linha = {'Dollar - USD':[dollar], 'Euro - EUR':[euro], 'Peso Argentino':[peso], 'Peso Venezuelano':[venezuelano], 'BitCoin':[bitcoin], 'Peso Uruguaio':[uruguaio]}
    frame = pd.DataFrame(linha, columns = ['Dollar - USD', 'Euro - EUR', 'Peso Argentino', 'Peso Venezuelano', 'BitCoin', 'Peso Uruguaio'])
    frame.to_csv('moeda.csv')
    print("Dados salvos na tabela!")

# função main deste arquivo
if __name__ == '__main__':
    main()
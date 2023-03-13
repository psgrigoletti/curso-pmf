import pandas as pd
import requests
import logging

class CarteiraGlobal:
    token = None
    headers = None
    
    def __init__(self):
        logging.log(logging.INFO, "Inicializando objeto da classe CarteiraGlobal")
    
    def setar_token(self, token):
        self.token = token
        self.headers = {'x-api-key': token}
        
    def retornar_lista_fiis(self):
        url = f"https://api.carteiraglobal.com/equity/fiis"
        req = requests.get(url, headers = self.headers)
        response = req.json()
        df = pd.DataFrame(response)
        return df
        
    def retonar_dados_fiis(self, ticker):
        url = f"https://api.carteiraglobal.com/equity/fiis/{ticker}"
        req = requests.get(url, headers = self.headers)
        response = req.json()
        df = pd.DataFrame(response)
        return df
    
    def retornar_cotacoes(self, ticker, data_inicial, data_final):
        url = f"https://api.carteiraglobal.com/equity/{ticker}/report?init_date={data_inicial}&end_date={data_final}"
        req = requests.get(url, headers = self.headers)
        response = req.json()
        cotacoes = pd.DataFrame(response)
        cotacoes = cotacoes[['date_report', 'open_quote_value', 'max_quote_value', 'min_quote_value', 'quote_value', 'volume']]
        cotacoes.columns = ['Date', 'Open', 'High', 'Low', 'Close', 'Volume']
        cotacoes['Date'] = pd.to_datetime(cotacoes['Date'])        
        cotacoes = cotacoes.set_index('Date', drop = False)
        cotacoes.dropna(inplace=True)
        return cotacoes    

    def retornar_dividendos(self, ticker, data_inicial, data_final, buscar_dy=True):
        url = f"https://api.carteiraglobal.com/equity/{ticker}/event?init_date={data_inicial}&end_date={data_final}"
        req = requests.get(url, headers = self.headers)
        response = req.json()
        dividendos = pd.DataFrame(response)
        dividendos = dividendos[(dividendos["event_type_name"] == "Dividendo") | 
                                (dividendos["event_type_name"] == "Juros sobre Capital Próprio")]
        dividendos = dividendos[['date_com', 'date_pmt', 'quote_value']]
        dividendos.columns = ['Data base', 'Data pagamento', 'Dividends']
        dividendos['Data base'] = pd.to_datetime(dividendos['Data base'])
        dividendos = dividendos.set_index('Data base', drop = False)
        if buscar_dy:
            dividendos['Close'] = self.retornar_cotacoes(ticker, data_inicial, data_final)['Close']
            dividendos['DY'] = (dividendos['Dividends']/dividendos['Close'])*100.0
        dividendos.dropna(inplace=True)
        return dividendos
    
# cg = CarteiraGlobal("jZscuLc4sN6dPO4FfOiSn7617Meab4B51GdL31ri")
# div = cg.retornar_dividendos('WEGE3', '2022-01-01', '2023-01-01')
# cot = cg.retornar_cotacoes('WEGE3', '2022-01-01', '2023-01-01')

# print(div.tail())
# print(cot.tail())
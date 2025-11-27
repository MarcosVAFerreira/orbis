import requests
from typing import Dict


API = "https://api.exchangerate.host/latest"




def fetch_rates(base: str = 'BRL') -> Dict[str, float]:
try:
r = requests.get(API, params={"base": base})
r.raise_for_status()
data = r.json()
return data.get('rates', {})
except Exception:
# fallback simples
return {
'USD': 0.20, # 1 BRL = 0.20 USD -> exemplo
'EUR': 0.18,
'GBP': 0.15,
'BRL': 1.0
}




def convert(amount: float, from_currency: str, to_currency: str, rates: Dict[str, float] = None) -> float:
from_currency = from_currency.upper()
to_currency = to_currency.upper()
if rates is None:
rates = fetch_rates(base=to_currency)
# Se a API devolve rates com base = to_currency, então rate[from_currency]
if from_currency == to_currency:
return amount
if from_currency in rates:
rate = rates[from_currency]
# rate é 1 TO = rate FROM -> amount_in_to = amount / rate
return amount / rate
# se não, tentar rota direta
raise ValueError('Currency not supported')
import tkinter as tk
def _deposit(self):
cid = self.tx_conta_entry.get().strip()
try:
amount = float(self.tx_amount_entry.get())
except Exception:
return
try:
t = self.transacao_service.deposit(cid, amount, 'BRL')
self.tx_log.insert('end', f'Deposit: {t.amount} {t.currency} -> {t.created_at}\n')
except Exception as e:
self.tx_log.insert('end', f'Erro: {e}\n')


def _withdraw(self):
cid = self.tx_conta_entry.get().strip()
try:
amount = float(self.tx_amount_entry.get())
except Exception:
return
try:
t = self.transacao_service.withdraw(cid, amount, 'BRL')
self.tx_log.insert('end', f'Withdraw: {t.amount} {t.currency} -> {t.created_at}\n')
except Exception as e:
self.tx_log.insert('end', f'Erro: {e}\n')


def _build_exchange_tab(self):
frm = self.frame_exchange
ttk.Label(frm, text='Conversão (ex: 100 USD -> BRL)').grid(row=0, column=0, columnspan=3)
self.ex_amount = ttk.Entry(frm)
self.ex_amount.grid(row=1, column=0)
self.ex_from = ttk.Entry(frm)
self.ex_from.insert(0, 'USD')
self.ex_from.grid(row=1, column=1)
self.ex_to = ttk.Entry(frm)
self.ex_to.insert(0, 'BRL')
self.ex_to.grid(row=1, column=2)
ttk.Button(frm, text='Converter (mock)', command=self._converter).grid(row=1, column=3)
self.ex_result = ttk.Label(frm, text='Resultado:')
self.ex_result.grid(row=2, column=0, columnspan=4)


def _converter(self):
try:
amount = float(self.ex_amount.get())
except Exception:
return
# uso direto do módulo cambio
from src import cambio
try:
val = cambio.convert(amount, self.ex_from.get(), self.ex_to.get())
self.ex_result.config(text=f'{amount} {self.ex_from.get().upper()} = {val:.2f} {self.ex_to.get().upper()}')
except Exception as e:
self.ex_result.config(text=f'Erro: {e}')




if __name__ == '__main__':
root = tk.Tk()
app = OrbisGUI(root)
root.mainloop()
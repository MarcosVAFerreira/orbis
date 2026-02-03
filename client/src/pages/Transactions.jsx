import { useState, useEffect } from 'react';
import { useParams, useNavigate } from 'react-router-dom';
import { getAccount, getTransactions, createTransaction } from '../services/api';

const currencySymbols = {
  BRL: 'R$',
  USD: '$',
  EUR: '€',
  GBP: '£',
  JPY: '¥',
};

function Transactions() {
  const { accountId } = useParams();
  const navigate = useNavigate();
  const [account, setAccount] = useState(null);
  const [transactions, setTransactions] = useState([]);
  const [loading, setLoading] = useState(true);
  const [showModal, setShowModal] = useState(false);
  const [newTransaction, setNewTransaction] = useState({
    type: 'DEPOSIT',
    amount: '',
    description: '',
  });

  useEffect(() => {
    loadData();
  }, [accountId]);

  const loadData = async () => {
    try {
      const [accountRes, transactionsRes] = await Promise.all([
        getAccount(accountId),
        getTransactions(accountId),
      ]);
      setAccount(accountRes.data);
      setTransactions(transactionsRes.data);
    } catch (error) {
      console.error('Erro ao carregar dados:', error);
      navigate('/accounts');
    } finally {
      setLoading(false);
    }
  };

  const handleCreateTransaction = async (e) => {
    e.preventDefault();
    try {
      await createTransaction({
        account_id: accountId,
        ...newTransaction,
        amount: parseFloat(newTransaction.amount),
      });
      setShowModal(false);
      setNewTransaction({ type: 'DEPOSIT', amount: '', description: '' });
      loadData();
    } catch (error) {
      console.error('Erro ao criar transação:', error);
      alert(error.response?.data?.detail || 'Erro ao criar transação');
    }
  };

  if (loading) {
    return <div className="text-center py-8">Carregando...</div>;
  }

  if (!account) {
    return <div className="text-center py-8">Conta não encontrada</div>;
  }

  return (
    <div className="space-y-8">
      <button
        onClick={() => navigate('/accounts')}
        className="text-primary hover:text-blue-600 flex items-center"
      >
        ← Voltar para contas
      </button>

      {/* Card da conta */}
      <div className="bg-gradient-to-r from-blue-500 to-blue-600 rounded-xl shadow-lg p-8 text-white">
        <h2 className="text-lg font-medium opacity-90">{account.label}</h2>
        <p className="text-4xl font-bold mt-2">
          {currencySymbols[account.currency]} {Number(account.balance).toLocaleString('pt-BR', { minimumFractionDigits: 2 })}
        </p>
        <p className="text-sm opacity-75 mt-2">{account.currency}</p>
      </div>

      {/* Ações */}
      <div className="flex space-x-4">
        <button
          onClick={() => {
            setNewTransaction({ ...newTransaction, type: 'DEPOSIT' });
            setShowModal(true);
          }}
          className="flex-1 bg-green-500 text-white px-6 py-3 rounded-lg hover:bg-green-600 font-medium"
        >
          + Depositar
        </button>
        <button
          onClick={() => {
            setNewTransaction({ ...newTransaction, type: 'WITHDRAWAL' });
            setShowModal(true);
          }}
          className="flex-1 bg-red-500 text-white px-6 py-3 rounded-lg hover:bg-red-600 font-medium"
        >
          - Sacar
        </button>
      </div>

      {/* Histórico */}
      <div>
        <h2 className="text-2xl font-bold text-gray-900 mb-4">Histórico de Transações</h2>
        <div className="bg-white rounded-lg shadow overflow-hidden">
          {transactions.length === 0 ? (
            <p className="p-6 text-gray-500 text-center">Nenhuma transação ainda</p>
          ) : (
            <div className="divide-y divide-gray-200">
              {transactions.map((tx) => (
                <div key={tx.id} className="p-6 hover:bg-gray-50">
                  <div className="flex justify-between items-start">
                    <div>
                      <p className="font-medium text-gray-900">{tx.description}</p>
                      <p className="text-sm text-gray-500">
                        {new Date(tx.created_at).toLocaleString('pt-BR')}
                      </p>
                    </div>
                    <div className="text-right">
                      <p className={`text-lg font-bold ${
                        tx.type === 'DEPOSIT' ? 'text-green-600' : 'text-red-600'
                      }`}>
                        {tx.type === 'DEPOSIT' ? '+' : '-'} {currencySymbols[tx.currency]} {Number(tx.amount).toLocaleString('pt-BR', { minimumFractionDigits: 2 })}
                      </p>
                      <p className="text-sm text-gray-500">
                        Saldo: {currencySymbols[tx.currency]} {Number(tx.balance_after).toLocaleString('pt-BR', { minimumFractionDigits: 2 })}
                      </p>
                    </div>
                  </div>
                </div>
              ))}
            </div>
          )}
        </div>
      </div>

      {/* Modal */}
      {showModal && (
        <div className="fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center z-50">
          <div className="bg-white rounded-lg p-8 max-w-md w-full mx-4">
            <h2 className="text-2xl font-bold text-gray-900 mb-4">
              {newTransaction.type === 'DEPOSIT' ? 'Depositar' : 'Sacar'}
            </h2>
            <form onSubmit={handleCreateTransaction} className="space-y-4">
              <div>
                <label className="block text-sm font-medium text-gray-700 mb-1">
                  Valor ({account.currency})
                </label>
                <input
                  type="number"
                  step="0.01"
                  min="0.01"
                  required
                  value={newTransaction.amount}
                  onChange={(e) => setNewTransaction({ ...newTransaction, amount: e.target.value })}
                  placeholder="0.00"
                  className="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-primary focus:border-primary"
                />
              </div>
              <div>
                <label className="block text-sm font-medium text-gray-700 mb-1">
                  Descrição (opcional)
                </label>
                <input
                  type="text"
                  value={newTransaction.description}
                  onChange={(e) => setNewTransaction({ ...newTransaction, description: e.target.value })}
                  placeholder={newTransaction.type === 'DEPOSIT' ? 'Depósito' : 'Saque'}
                  className="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-primary focus:border-primary"
                />
              </div>
              <div className="flex space-x-3">
                <button
                  type="button"
                  onClick={() => setShowModal(false)}
                  className="flex-1 px-4 py-2 border border-gray-300 rounded-lg hover:bg-gray-50"
                >
                  Cancelar
                </button>
                <button
                  type="submit"
                  className={`flex-1 px-4 py-2 text-white rounded-lg ${
                    newTransaction.type === 'DEPOSIT' 
                      ? 'bg-green-500 hover:bg-green-600' 
                      : 'bg-red-500 hover:bg-red-600'
                  }`}
                >
                  Confirmar
                </button>
              </div>
            </form>
          </div>
        </div>
      )}
    </div>
  );
}

export default Transactions;

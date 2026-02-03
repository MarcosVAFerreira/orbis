import { useState, useEffect } from 'react';
import { getDashboard } from '../services/api';

const currencySymbols = {
  BRL: 'R$',
  USD: '$',
  EUR: '€',
  GBP: '£',
  JPY: '¥',
};

function Dashboard() {
  const [data, setData] = useState(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    loadDashboard();
  }, []);

  const loadDashboard = async () => {
    try {
      const res = await getDashboard();
      setData(res.data);
    } catch (error) {
      console.error('Erro ao carregar dashboard:', error);
    } finally {
      setLoading(false);
    }
  };

  if (loading) {
    return <div className="text-center py-8">Carregando...</div>;
  }

  if (!data) {
    return <div className="text-center py-8">Erro ao carregar dados</div>;
  }

  return (
    <div className="space-y-8">
      <div>
        <h1 className="text-3xl font-bold text-gray-900">Dashboard</h1>
        <p className="text-gray-600">Bem-vindo, {data.user.name}!</p>
      </div>

      {/* Saldo consolidado */}
      <div className="bg-gradient-to-r from-blue-500 to-blue-600 rounded-xl shadow-lg p-8 text-white">
        <h2 className="text-lg font-medium opacity-90">Saldo Total Consolidado</h2>
        <p className="text-4xl font-bold mt-2">
          R$ {Number(data.consolidated_balance.total_brl).toLocaleString('pt-BR', { minimumFractionDigits: 2 })}
        </p>
        <p className="text-sm opacity-75 mt-2">
          Atualizado em {new Date(data.consolidated_balance.updated_at).toLocaleString('pt-BR')}
        </p>
      </div>

      {/* Contas */}
      <div>
        <h2 className="text-2xl font-bold text-gray-900 mb-4">Suas Contas</h2>
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
          {data.consolidated_balance.accounts.map((account, idx) => (
            <div key={idx} className="bg-white rounded-lg shadow p-6">
              <div className="flex justify-between items-start">
                <div>
                  <p className="text-sm text-gray-600">{account.currency}</p>
                  <p className="text-2xl font-bold text-gray-900">
                    {currencySymbols[account.currency]} {Number(account.balance).toLocaleString('pt-BR', { minimumFractionDigits: 2 })}
                  </p>
                </div>
                <div className="text-xs text-gray-500">
                  Taxa: {Number(account.rate).toFixed(2)}
                </div>
              </div>
              <div className="mt-3 pt-3 border-t border-gray-200">
                <p className="text-sm text-gray-600">Em BRL:</p>
                <p className="text-lg font-semibold text-green-600">
                  R$ {Number(account.balance_brl).toLocaleString('pt-BR', { minimumFractionDigits: 2 })}
                </p>
              </div>
            </div>
          ))}
        </div>
      </div>

      {/* Transações recentes */}
      <div>
        <h2 className="text-2xl font-bold text-gray-900 mb-4">Transações Recentes</h2>
        <div className="bg-white rounded-lg shadow overflow-hidden">
          {data.recent_transactions.length === 0 ? (
            <p className="p-6 text-gray-500 text-center">Nenhuma transação ainda</p>
          ) : (
            <div className="overflow-x-auto">
              <table className="min-w-full divide-y divide-gray-200">
                <thead className="bg-gray-50">
                  <tr>
                    <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                      Data
                    </th>
                    <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                      Descrição
                    </th>
                    <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                      Tipo
                    </th>
                    <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                      Valor
                    </th>
                  </tr>
                </thead>
                <tbody className="bg-white divide-y divide-gray-200">
                  {data.recent_transactions.map((tx) => (
                    <tr key={tx.id}>
                      <td className="px-6 py-4 whitespace-nowrap text-sm text-gray-500">
                        {new Date(tx.created_at).toLocaleDateString('pt-BR')}
                      </td>
                      <td className="px-6 py-4 whitespace-nowrap text-sm text-gray-900">
                        {tx.description}
                      </td>
                      <td className="px-6 py-4 whitespace-nowrap">
                        <span className={`px-2 py-1 text-xs rounded-full ${
                          tx.type === 'DEPOSIT' ? 'bg-green-100 text-green-800' : 'bg-red-100 text-red-800'
                        }`}>
                          {tx.type === 'DEPOSIT' ? 'Depósito' : 'Saque'}
                        </span>
                      </td>
                      <td className={`px-6 py-4 whitespace-nowrap text-sm font-medium ${
                        tx.type === 'DEPOSIT' ? 'text-green-600' : 'text-red-600'
                      }`}>
                        {tx.type === 'DEPOSIT' ? '+' : '-'} {currencySymbols[tx.currency]} {Number(tx.amount).toLocaleString('pt-BR', { minimumFractionDigits: 2 })}
                      </td>
                    </tr>
                  ))}
                </tbody>
              </table>
            </div>
          )}
        </div>
      </div>
    </div>
  );
}

export default Dashboard;

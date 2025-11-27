// Mock dos dados simulando API
const mockUser = {
    id: 1,
    nome: "Usuário Teste",
    saldo: 1250.75,
    extrato: [
        { tipo: "Entrada", valor: 500, data: "2025-10-20" },
        { tipo: "Saída", valor: 50, data: "2025-10-21" },
        { tipo: "Entrada", valor: 800, data: "2025-10-22" },
    ]
};

const mockMarket = {
    USD: { nome: "Dólar", valor: 5.62, variacao: +0.8 },
    EUR: { nome: "Euro", valor: 6.03, variacao: -0.3 },
    BRL: { nome: "Real", valor: 1.00, variacao: 0 }
};

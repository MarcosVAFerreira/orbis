// URL da API Flask
const API = "http://127.0.0.1:5000";

let userAtual = null;

async function login() {
    const user = document.getElementById("user").value;
    const password = document.getElementById("password").value;

    const resp = await fetch(`${API}/login`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ user, password })
    });

    const data = await resp.json();

    const msg = document.getElementById("login-msg");
    msg.textContent = data.message;

    if (resp.ok) {
        userAtual = user;
        document.getElementById("username").textContent = user;
        document.getElementById("dashboard").classList.remove("hidden");
        carregarSaldo();
        carregarExtrato();
    }
}

async function carregarSaldo() {
    const resp = await fetch(`${API}/saldo/${userAtual}`);
    const data = await resp.json();
    document.getElementById("saldo").textContent = `R$ ${data.saldo.toFixed(2)}`;
}

async function depositar() {
    const valor = Number(document.getElementById("valDeposito").value);

    const resp = await fetch(`${API}/depositar/${userAtual}`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ valor })
    });

    const data = await resp.json();
    document.getElementById("msg-dep").textContent = data.message;

    carregarSaldo();
    carregarExtrato();
}

async function sacar() {
    const valor = Number(document.getElementById("valSaque").value);

    const resp = await fetch(`${API}/sacar/${userAtual}`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ valor })
    });

    const data = await resp.json();
    document.getElementById("msg-saq").textContent = data.message;

    carregarSaldo();
    carregarExtrato();
}

async function carregarExtrato() {
    const resp = await fetch(`${API}/extrato/${userAtual}`);
    const data = await resp.json();

    document.getElementById("extrato").textContent = data.extrato.join("\n");
}

/* app.js
   Login / cadastro / sessão / operações (localStorage)
*/

const STORAGE_USERS = "orbis_users_v1";
const STORAGE_SESSION = "orbis_session_v1";

/* ---------- Helpers de storage ---------- */
function loadUsers() {
    return JSON.parse(localStorage.getItem(STORAGE_USERS) || "{}");
}
function saveUsers(users) {
    localStorage.setItem(STORAGE_USERS, JSON.stringify(users));
}
function setSession(username) {
    localStorage.setItem(STORAGE_SESSION, username);
}
function getSession() {
    return localStorage.getItem(STORAGE_SESSION);
}
function clearSession() {
    localStorage.removeItem(STORAGE_SESSION);
}

/* ---------- User model helpers ---------- */
function createUser(username, password) {
    const users = loadUsers();
    if (users[username]) throw new Error("Usuário já existe");
    users[username] = {
        username,
        password,
        saldo: 0,
        extrato: [] // {type, amount, date, desc}
    };
    saveUsers(users);
    return users[username];
}

function registerFromForm() {
    // optional small register modal can call this
    const user = prompt("Novo usuário - digite username:");
    if (!user) return;
    const pass = prompt("Senha:");
    try {
        createUser(user, pass || "");
        alert("Conta criada! Faça login.");
    } catch (e) {
        alert(e.message);
    }
}

/* ---------- Auth (called by page) ---------- */
function login() {
    const u = document.getElementById("user").value.trim();
    const p = document.getElementById("password").value;
    const users = loadUsers();
    const elmsg = document.getElementById("login-msg");
    if (!u) { elmsg.textContent = "Digite o usuário"; return; }
    if (!users[u]) { elmsg.textContent = "Usuário não encontrado"; return; }
    if (users[u].password !== p) { elmsg.textContent = "Senha incorreta"; return; }
    setSession(u);
    elmsg.textContent = "";
    loadDashboard();
}

/* ---------- Logout ---------- */
function logout() {
    clearSession();
    // reload to show login
    window.location.href = "index.html";
}

/* ---------- Core operations ---------- */
function getCurrentUser() {
    const u = getSession();
    if (!u) return null;
    const users = loadUsers();
    return users[u] || null;
}
function saveCurrentUser(userObj) {
    const users = loadUsers();
    users[userObj.username] = userObj;
    saveUsers(users);
}

/* depositar */
function depositar() {
    const v = Number(document.getElementById("valDeposito").value || 0);
    if (!(v > 0)) { document.getElementById("msg-dep").textContent = "Insira valor positivo"; return; }
    const user = getCurrentUser();
    if (!user) return alert("Faça login");
    user.saldo += v;
    user.extrato.unshift({ type: "Depósito", amount: v, date: new Date().toLocaleString(), desc: "Depósito via demo" });
    saveCurrentUser(user);
    document.getElementById("valDeposito").value = "";
    document.getElementById("msg-dep").textContent = "Depositado com sucesso!";
    refreshDashboardUI(user);
}

/* sacar */
function sacar() {
    const v = Number(document.getElementById("valSaque").value || 0);
    if (!(v > 0)) { document.getElementById("msg-saq").textContent = "Insira valor positivo"; return; }
    const user = getCurrentUser();
    if (!user) return alert("Faça login");
    if (user.saldo < v) { document.getElementById("msg-saq").textContent = "Saldo insuficiente"; return; }
    user.saldo -= v;
    user.extrato.unshift({ type: "Saque", amount: -v, date: new Date().toLocaleString(), desc: "Saque via demo" });
    saveCurrentUser(user);
    document.getElementById("valSaque").value = "";
    document.getElementById("msg-saq").textContent = "Saque concluído!";
    refreshDashboardUI(user);
}

/* extrato */
function renderExtrato(user) {
    const el = document.getElementById("extrato");
    if (!el) return;
    el.textContent = "";
    if (!user.extrato || user.extrato.length === 0) {
        el.textContent = "Sem transações ainda.";
        return;
    }
    user.extrato.slice(0,50).forEach(t => {
        const sign = t.amount >= 0 ? "+" : "";
        el.textContent += `${t.date} — ${t.type} — ${sign}${t.amount.toFixed(2)} — ${t.desc}\n`;
    });
}

/* refresh UI */
function refreshDashboardUI(user) {
    if (!user) return;
    document.getElementById("username").textContent = user.username;
    document.getElementById("saldo").textContent = user.saldo.toFixed(2);
    renderExtrato(user);
}

/* carregar dashboard quando logado */
function loadDashboard() {
    const user = getCurrentUser();
    if (!user) {
        // show login
        document.getElementById("login-section").classList.remove("hidden");
        document.getElementById("dashboard").classList.add("hidden");
        return;
    }
    document.getElementById("login-section").classList.add("hidden");
    document.getElementById("dashboard").classList.remove("hidden");
    refreshDashboardUI(user);
}

/* quick demo seed: create default user if no users */
function ensureDemoUser() {
    const users = loadUsers();
    if (Object.keys(users).length === 0) {
        const demo = { username: "demo", password: "1234", saldo: 1250.75, extrato: [
            { type: "Depósito", amount: 1250.75, date: new Date().toLocaleString(), desc: "Saldo inicial demo" }
        ]};
        users["demo"] = demo;
        saveUsers(users);
    }
}

/* convert simple: use exchange API (exchangerate.host) to convert between currencies */
async function convertCurrency(amount, from, to) {
    // if same
    if (from === to) return amount;
    try {
        const r = await fetch(`https://api.exchangerate.host/convert?from=${from}&to=${to}&amount=${amount}`);
        const j = await r.json();
        if (j && j.result !== undefined) return j.result;
    } catch (e) {
        console.warn("convert error", e);
    }
    throw new Error("Erro na conversão");
}

/* init on load */
document.addEventListener("DOMContentLoaded", () => {
    ensureDemoUser();
    loadDashboard();
});

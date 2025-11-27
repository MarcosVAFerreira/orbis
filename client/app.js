const API = "http://127.0.0.1:5000";

async function listarUsuarios() {
    const r = await fetch(API + "/usuarios");
    resposta.value = await r.text();
}

async function criarUsuario() {
    const r = await fetch(API + "/usuarios", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
            nome: nome.value,
            email: email.value
        })
    });
    resposta.value = await r.text();
}

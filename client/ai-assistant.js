/* ai-assistant.js — Orbinho assistant (pure client) */
(function(){
    // avoid duplication
    if (document.querySelector(".orbinho-assistant")) return;

    const ORB_SRC = "assets/mascot/orbinho.jpg"; // your file
    const assistant = document.createElement("div");
    assistant.className = "orbinho-assistant";

    assistant.innerHTML = `
        <img class="orbinho-img" src="${ORB_SRC}" alt="Orbinho">
        <div class="orbinho-bubble" style="display:none;">
            <div class="bubble-text">Olá! Eu sou o Orbinho. Clique e eu dou dicas rápidas.</div>
            <div style="margin-top:8px;display:flex;gap:6px;">
                <button class="orb-btn" data-cmd="balance">Ver saldo</button>
                <button class="orb-btn" data-cmd="market">Ver mercado</button>
                <button class="orb-btn" data-cmd="tip">Dica</button>
            </div>
        </div>
    `;
    // styles (minimal inline for reliability)
    Object.assign(assistant.style, {
        position: "fixed", right: "22px", bottom: "22px", zIndex: 9999, textAlign: "right"
    });
    document.body.appendChild(assistant);

    const img = assistant.querySelector(".orbinho-img");
    const bubble = assistant.querySelector(".orbinho-bubble");

    img.style.width = "84px";
    img.style.cursor = "pointer";
    img.style.borderRadius = "12px";
    img.style.boxShadow = "0 8px 18px rgba(0,0,0,0.18)";
    img.style.transition = "transform .25s";

    img.addEventListener("mouseenter", () => img.style.transform = "translateY(-6px)");
    img.addEventListener("mouseleave", () => img.style.transform = "translateY(0)");

    img.addEventListener("click", () => {
        bubble.style.display = bubble.style.display === "block" ? "none" : "block";
    });

    // buttons
    assistant.querySelectorAll(".orb-btn").forEach(btn => {
        btn.addEventListener("click", async (ev) => {
            const cmd = ev.target.dataset.cmd;
            if (cmd === "balance") {
                const cur = localStorage.getItem("orbis_session_v1");
                if (!cur) {
                    say("Faça login para eu ver seu saldo.");
                } else {
                    const users = JSON.parse(localStorage.getItem("orbis_users_v1") || "{}");
                    const u = users[cur];
                    say(`Seu saldo atual é R$ ${u ? u.saldo.toFixed(2) : "0.00"}`);
                }
            } else if (cmd === "market") {
                say("Buscando cotações...");
                try {
                    const res = await fetch("https://api.exchangerate.host/latest?base=BRL");
                    const j = await res.json();
                    // show three: USD, EUR, GBP
                    const usd = (1 / j.rates.USD).toFixed(4);
                    const eur = (1 / j.rates.EUR).toFixed(4);
                    const gbp = (1 / j.rates.GBP).toFixed(4);
                    say(`1 USD ≈ R$ ${usd}\n1 EUR ≈ R$ ${eur}\n1 GBP ≈ R$ ${gbp}`);
                } catch (e) {
                    say("Não consegui buscar o mercado agora.");
                }
            } else if (cmd === "tip") {
                const tips = [
                    "Reserve 10% do seu depósito para poupança.",
                    "Converter quando a moeda estiver em baixa tende a ser vantajoso.",
                    "Verifique o extrato semanalmente."
                ];
                say(tips[Math.floor(Math.random()*tips.length)]);
            }
        });
    });

    function say(text) {
        const t = assistant.querySelector(".bubble-text");
        t.innerText = text;
    }

})();

// Mascote Orbinho
document.addEventListener("DOMContentLoaded", () => {
    const orb = document.createElement("img");
    orb.src = "assets/mascot/orbinho.jpg";   // <-- CAMINHO CORRETO
    orb.className = "orbinho";
    document.body.appendChild(orb);

    const chat = document.createElement("div");
    chat.className = "chat-box";
    chat.innerHTML = `<p><b>Orbinho:</b> Precisa de ajuda?</p>`;
    document.body.appendChild(chat);

    orb.onclick = () => {
        chat.style.display =
            chat.style.display === "none" ? "block" : "none";
    };
});

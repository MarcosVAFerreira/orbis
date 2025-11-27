function converter() {
    const de = document.getElementById("moeda1").value;
    const para = document.getElementById("moeda2").value;
    const quantia = parseFloat(document.getElementById("valor").value);

    const taxa = mockMarket[para].valor / mockMarket[de].valor;
    const convertido = quantia * taxa;

    document.getElementById("resultado").innerText =
        `Resultado: ${convertido.toFixed(2)} ${para}`;
}

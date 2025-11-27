function carregarGrafico() {
    const ctx = document.getElementById("grafico").getContext("2d");

    new Chart(ctx, {
        type: "line",
        data: {
            labels: ["Seg", "Ter", "Qua", "Qui", "Sex"],
            datasets: [{
                label: "Variação USD",
                data: [5.58, 5.61, 5.63, 5.60, 5.62],
                borderWidth: 2
            }]
        }
    });
}

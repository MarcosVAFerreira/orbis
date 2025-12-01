function renderChart(labels, data) {
    const ctx = document.getElementById("chart").getContext("2d");
    // destroy previous if exists (helpful in dev)
    if (window._orbisChart) window._orbisChart.destroy();
    window._orbisChart = new Chart(ctx, {
        type: 'line',
        data: {
            labels,
            datasets: [{
                label: 'USD (R$)',
                data,
                borderColor: '#1b3b6f',
                backgroundColor: 'rgba(27,59,111,0.15)',
                tension: 0.25,
                pointRadius: 3,
                pointBackgroundColor: '#F4C542'
            }]
        },
        options: {
            scales: {
                y: { beginAtZero: false }
            },
            plugins: {
                legend: { display: false }
            }
        }
    });
}

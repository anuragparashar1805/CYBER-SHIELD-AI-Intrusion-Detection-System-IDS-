// Initialize Chart.js
const ctx = document.getElementById('threatChart').getContext('2d');
const threatChart = new Chart(ctx, {
    type: 'doughnut',
    data: {
        labels: ['Normal', 'DDoS', 'Port Scan'],
        datasets: [{
            data: [0, 0, 0],
            backgroundColor: ['#00ffcc', '#ff0055', '#ffcc00'],
            borderColor: '#0a0f1d'
        }]
    },
    options: { responsive: true, maintainAspectRatio: false }
});

// Loop execution to pull statistics from Flask API
setInterval(() => {
    // 1. Fetch Metrics
    fetch('/api/metrics')
        .then(response => response.json())
        .then(data => {
            document.getElementById('total-packets').innerText = data.total_packets;
            document.getElementById('threat-count').innerText = data.ddos + data.port_scan;

            // Update Chart
            threatChart.data.datasets[0].data = [data.normal, data.ddos, data.port_scan];
            threatChart.update();
        });

    // 2. Fetch Logs
    fetch('/api/logs')
        .then(response => response.json())
        .then(data => {
            const consoleBox = document.getElementById('log-console');
            consoleBox.innerHTML = ''; // Clear prior logs
            data.forEach(log => {
                const p = document.createElement('div');
                p.className = 'log-entry';
                p.innerText = `[${log.timestamp}] WARN: ${log.type} flagged from ${log.src} -> Severity: ${log.severity}`;
                consoleBox.appendChild(p);
            });
        });
}, 1000); // Refreshes every 1000ms (1 second)
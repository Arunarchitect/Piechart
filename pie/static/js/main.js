var costSplitLabel = {{ cost_split_label|safe }};
var costSplitData = {{ cost_split|safe }};

// Prefix the rupee symbol to Y-axis tick labels
function formatRupee(value) {
    return '\u20B9' + value;
}

var ctx = document.getElementById('costSplitChart').getContext('2d');
var myChart = new Chart(ctx, {
    type: 'pie',
    data: {
        labels: costSplitLabel,
        datasets: [{
            label: 'Cost Split',
            data: costSplitData,
            backgroundColor: [
                'rgba(255, 99, 132, 0.2)',
                'rgba(255, 159, 64, 0.2)',
                'rgba(255, 205, 86, 0.2)',
                'rgba(75, 192, 192, 0.2)',
                'rgba(54, 162, 235, 0.2)',
                'rgba(153, 102, 255, 0.2)'
              ],
            borderColor: [
                'rgb(255, 99, 132)',
                'rgb(255, 159, 64)',
                'rgb(255, 205, 86)',
                'rgb(75, 192, 192)',
                'rgb(54, 162, 235)',
                'rgb(153, 102, 255)'
              ],
            borderWidth: 1
        }]
    },
    options: {
        scales: {
            y: {
                beginAtZero: true,
                ticks: {
                    callback: function(value, index, values) {
                        return formatRupee(value);
                    }
                }
            }
        }
    }
});
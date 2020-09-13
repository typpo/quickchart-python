from quickchart import QuickChart

qc = QuickChart()
qc.config = '''{
  type: 'bar',
  data: {
    labels: ['Q1', 'Q2', 'Q3', 'Q4'],
    datasets: [{
      label: 'Users',
      data: [50, 60, 70, 180]
    }, {
      label: 'Revenue',
      data: [100, 200, 300, 400]
    }]
  },
  options: {
    scales: {
      yAxes: [{
        ticks: {
          callback: (val) => {
            return val + 'k';
          }
        }
      }]
    }
  }
}'''

print(qc.get_short_url())
#
# Example output (note that this shortened URL is now expired and will not display a chart):
#
# https://quickchart.io/chart/render/f-b4bf9221-0499-4bc6-b1ae-6f7c78be9d93
#

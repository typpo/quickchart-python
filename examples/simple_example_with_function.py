from quickchart import QuickChart

qc = QuickChart()
qc.width = 600
qc.height = 300
qc.device_pixel_ratio = 2.0
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

print(qc.get_url())

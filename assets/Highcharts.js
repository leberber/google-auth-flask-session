
window.dash_clientside = Object.assign({}, window.dash_clientside, {

    highcharts: {

        packedbubble: function (emissions, reset) {

          const packedbubbleChart = Highcharts.chart('highchartAreaChart',
           {
            chart: {
                type: 'packedbubble',
                height: '55%'
            },
            title: {
                text: 'Carbon emissions around the world (2014)',
                align: 'center'
            },
            tooltip: {
                useHTML: true,
                pointFormat: '<b>{point.name}:</b> {point.value}m CO<sub>2</sub>'
            },
            plotOptions: {
                packedbubble: {
                    minSize: '30%',
                    maxSize: '120%',
                    zMin: 0,
                    zMax: 1000,
                    layoutAlgorithm: {
                        splitSeries: false,
                        gravitationalConstant: 0.02
                    },
                    dataLabels: {
                        enabled: true,
                        format: '{point.name}',
                        filter: {
                            property: 'y',
                            operator: '>',
                            value: 250
                        },
                        style: {
                            color: 'black',
                            textOutline: 'none',
                            fontWeight: 'normal'
                        }
                    }
                }
            },
            series: emissions
        });

        document.getElementById('selectRegion').addEventListener('change', (e) => {

            let selectedSeries = emissions.map(a => a.name).indexOf(e.target.value);
            packedbubbleChart.series[selectedSeries].setData()
        });

        return window.dash_clientside.no_update
    },
    },
});
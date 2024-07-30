function retorna_total_gasto(url){
    fetch(url,{
        method: 'GET',
    }).then(function(result){
        return result.json()
    }).then(function(datacompra){
        document.getElementById('gasto_total').innerHTML = datacompra.total
    })
}


function gera_cor(qtd=1){
    var bg_color = []
    var border_color = []
    for(let i = 0; i < qtd; i++){
        let r = Math.random() * 255;
        let g = Math.random() * 255;
        let b = Math.random() * 255;
        bg_color.push(`rgba(${r}, ${g}, ${b}, ${0.2})`)
        border_color.push(`rgba(${r}, ${g}, ${b}, ${1})`)
    }

    return [bg_color, border_color];

}


function relatorio_gasto(url){
    fetch(url, {
        method: 'get',
    }).then(function(result){
        return result.json()
    }).then(function(data){

        const ctx = document.getElementById('gastos_mensal').getContext('2d');
        let cores_faturamento_mensal = gera_cor(qtd=12)
        const myChart = new Chart(ctx, {
            type: 'line',
            data: {
                labels:data.labels,
                datasets: [{
                    label:'Gastos Mensais' ,
                    data: data.datacompra,
                    backgroundColor: cores_faturamento_mensal[0],
                    borderColor: cores_faturamento_mensal[1],
                    borderWidth: 0.2
                }]
            },
            options: {
                scales: {
                    y: {
                        beginAtZero: true
                    }
                }
            }
        });


    })




}

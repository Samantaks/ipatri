
// Introdução

function gera_cor(qtd=1){
    var bg_color = []
    var border_color = []
    for(let i = 0; i < qtd; i++){
        let r = Math.random() * 255;
        let g = Math.random() * 255;
        let b = Math.random() * 255;
        bg_color.push(`rgba(${r}, ${g}, ${b}, ${0.5})`)
        border_color.push(`rgba(${r}, ${g}, ${b}, ${2})`)
    }

    return [bg_color, border_color];

}

async function gerarGrafico(url, elementoCanvasId, tipoGrafico, labelGrafico, qtdCores) {
    try {
        const response = await fetch(url);
        const data = await response.json();

        const ctx = document.getElementById(elementoCanvasId).getContext('2d');
        const cores = gera_cor(qtdCores);

        new Chart(ctx, {
            type: tipoGrafico,
            data: {
                labels: data.labels,
                datasets: [{
                    label: labelGrafico,
                    data: data.data,
                    backgroundColor: cores[0],
                    borderColor: cores[1],
                    borderWidth: 1
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
    } catch (error) {
        console.error(`Erro ao gerar o gráfico ${labelGrafico}:`, error);
    }
}



// Parte 1

function retorna_total_gasto(url){
    fetch(url,{
        method: 'GET',
    }).then(function(result){
        return result.json()
    }).then(function(datacompra){
        document.getElementById('gasto_total').innerHTML = datacompra.total
    })
}

 function retorna_quantidade_setores(url) {
    fetch(url, {
        method: 'GET',
    }).then(function(result) {
                return result.json()
            }).then(function(id_setor) {
                document.getElementById('setores_total').innerHTML = id_setor.quantidade
            })
        }




// Parte 2

async function relatorio_gasto(url) {
    try {
        const response = await fetch(url);
        const data = await response.json();

        const ctx = document.getElementById('gastos_mensal').getContext('2d');
        const coresFaturamentoMensal = gera_cor(12);

        new Chart(ctx, {
            type: 'line',
            data: {
                labels: data.labels,
                datasets: [{
                    label: 'Gastos Mensais',
                    data: data.datacompra,
                    backgroundColor: coresFaturamentoMensal[0],
                    borderColor: coresFaturamentoMensal[1],
                    borderWidth: 1
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
    } catch (error) {
        console.error("Erro ao gerar o gráfico de gastos mensais:", error);
    }
}

// Parte 3

function relatorio_marcas(url) {
    gerarGrafico(url, 'gastos_marca', 'bar', 'Gastos geral da Marca', 5);
}

function relatorio_setores(url) {
    gerarGrafico(url, 'gastos_setor', 'bar', 'Gastos geral do Setor', 3);
}


// Parte 4



async function relatorio_gasto_por_conta_contabil(url) {
    try {
        const response = await fetch(url);
        const data = await response.json();

        const ctx = document.getElementById('gastos_contacontabil').getContext('2d');
        const coresFaturamentoMensal = gera_cor(data.datasets.length); // Gerar cores suficientes para cada dataset

        const datasets = data.datasets.map((dataset, index) => ({
            label: dataset.label,  // Nome da conta contábil
            data: dataset.data,  // Dados dos gastos para essa conta
            backgroundColor: coresFaturamentoMensal[index],
            borderColor: coresFaturamentoMensal[index],
            borderWidth: 1
        }));

        new Chart(ctx, {
            type: 'line',
            data: {
                labels: data.labels,  // Meses no eixo x
                datasets: datasets  // Todos os datasets gerados
            },
            options: {
                scales: {
                    y: {
                        beginAtZero: true
                    }
                }
            }
        });
    } catch (error) {
        console.error("Erro ao gerar o gráfico de gastos mensais:", error);
    }
}
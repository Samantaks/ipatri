
// Introdução

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


// Função para gerar gráficos de barras em Chart.js
async function gerarRelatorio(url, ctxId, labelGrafico, qtdCores) {
    try {
        const data = await fetchDados(url);
        const ctx = document.getElementById(ctxId).getContext('2d');
        const cores = gera_cor(quantidade=qtdCores);

        criarGraficoBarra(ctx, data, labelGrafico, cores);
    } catch (error) {
        console.error(`Erro ao gerar o relatório: ${error}`);
    }
}


// Função para buscar os dados do humilde Djanguinho
async function fetchDados(url) {
    const response = await fetch(url, { method: 'GET' });
    if (!response.ok) {
        throw new Error(`Erro ao buscar dados: ${response.statusText}`);
    }
    return response.json();
}

// Geral pra Gráfico de barras
function criarGraficoBarra(ctx, data, labelGrafico, cores) {
    new Chart(ctx, {
        type: 'bar',
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
            type: 'radar',
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


// Chamando função de relatório para Marcas
function relatorio_marcas(url) {
    gerarRelatorio(url, 'gastos_marca', 'Gastos geral da Marca', qtdCores=5);
}

// Chamando função de relatório para Setores
function relatorio_setores(url) {
    gerarRelatorio(url, 'gastos_setor', 'Gastos geral do Setor', qtdCores=3);
}



// Parte 4

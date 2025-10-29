/**
 * Função para analisar o processo jurídico
 */
function analyzeProcess() {
    const processText = document.getElementById("processText").value;

    if (!processText.trim()) {
        alert("Por favor, insira o texto do processo para análise.");
        return;
    }

    // Mostrar loading
    document.getElementById("loading-analysis").style.display = "block";
    document.getElementById("analysis-result").style.display = "none";

    // Fazer requisição
    let xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
        if (this.readyState == 4) {
            // Esconder loading
            document.getElementById("loading-analysis").style.display = "none";

            if (this.status == 200) {
                // Mostrar resultado
                document.getElementById("analysis-content").innerHTML = xhttp.responseText;
                document.getElementById("analysis-result").style.display = "block";

                // Scroll para o resultado
                document.getElementById("analysis-result").scrollIntoView({
                    behavior: 'smooth',
                    block: 'start'
                });
            } else {
                alert("Erro ao analisar processo. Por favor, tente novamente.");
            }
        }
    };

    xhttp.open("GET", "analyzeProcess?processText=" + encodeURIComponent(processText), true);
    xhttp.send();
}

/**
 * Função para calcular liquidação
 */
function calculateSettlement() {
    const baseValue = document.getElementById("baseValue").value;
    const startDate = document.getElementById("startDate").value;
    const endDate = document.getElementById("endDate").value;
    const interestRate = document.getElementById("interestRate").value;
    const correctionIndex = document.getElementById("correctionIndex").value;

    if (!baseValue || !startDate || !endDate) {
        alert("Por favor, preencha todos os campos obrigatórios (Valor Base, Data Inicial e Data Final).");
        return;
    }

    // Mostrar loading
    document.getElementById("loading-calculation").style.display = "block";
    document.getElementById("calculation-result").style.display = "none";

    // Construir URL com parâmetros
    let url = "calculateSettlement?baseValue=" + encodeURIComponent(baseValue) +
              "&startDate=" + encodeURIComponent(startDate) +
              "&endDate=" + encodeURIComponent(endDate);

    if (interestRate) {
        url += "&interestRate=" + encodeURIComponent(interestRate);
    }

    if (correctionIndex) {
        url += "&correctionIndex=" + encodeURIComponent(correctionIndex);
    }

    // Fazer requisição
    let xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
        if (this.readyState == 4) {
            // Esconder loading
            document.getElementById("loading-calculation").style.display = "none";

            if (this.status == 200) {
                // Mostrar resultado
                document.getElementById("calculation-content").innerHTML = xhttp.responseText;
                document.getElementById("calculation-result").style.display = "block";

                // Scroll para o resultado
                document.getElementById("calculation-result").scrollIntoView({
                    behavior: 'smooth',
                    block: 'start'
                });
            } else {
                alert("Erro ao calcular liquidação. Por favor, verifique os dados e tente novamente.");
            }
        }
    };

    xhttp.open("GET", url, true);
    xhttp.send();
}

/**
 * Função para carregar exemplo de processo
 */
function loadExample() {
    const exampleText = `PROCESSO Nº 0001234-56.2023.5.02.0001
VARA DO TRABALHO DE SÃO PAULO

RECLAMANTE: João da Silva
RECLAMADO: Empresa XYZ Ltda

SENTENÇA

Vistos etc.

I - RELATÓRIO
Trata-se de Reclamação Trabalhista ajuizada por JOÃO DA SILVA em face de EMPRESA XYZ LTDA,
postulando o pagamento de verbas rescisórias, horas extras, adicional noturno e danos morais.

II - FUNDAMENTAÇÃO
O reclamante comprovou que laborou para a reclamada no período de 01/01/2020 a 31/12/2022,
sem o devido pagamento de horas extras e adicional noturno.

Restou comprovado que o reclamante trabalhou habitualmente além da jornada contratual,
fazendo jus ao pagamento de horas extras com adicional de 50%.

O pedido de danos morais também merece acolhimento, diante das condições degradantes
de trabalho comprovadas nos autos.

III - DISPOSITIVO
Pelo exposto, JULGO PROCEDENTE o pedido para condenar a reclamada ao pagamento de:

a) Horas extras no valor de R$ 45.000,00 (quarenta e cinco mil reais)
b) Adicional noturno no valor de R$ 15.000,00 (quinze mil reais)
c) Verbas rescisórias no valor de R$ 20.000,00 (vinte mil reais)
d) Danos morais no valor de R$ 50.000,00 (cinquenta mil reais)

Total da condenação: R$ 130.000,00 (cento e trinta mil reais)

Os valores deverão ser corrigidos monetariamente pelo IPCA-E e acrescidos de juros de mora
pela taxa SELIC, ambos a partir da data do ajuizamento da ação (01/03/2023) até o efetivo
pagamento.

Custas pela reclamada no valor de R$ 2.600,00 (dois mil e seiscentos reais).

São Paulo, 15 de setembro de 2023.

Juiz do Trabalho`;

    document.getElementById("processText").value = exampleText;

    // Scroll suave para o textarea
    document.getElementById("processText").scrollIntoView({
        behavior: 'smooth',
        block: 'center'
    });
}

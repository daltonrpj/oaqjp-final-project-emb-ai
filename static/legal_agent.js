// JavaScript para o Agente de IA de Teses Jurídicas

let currentThesis = null;

// Função para gerar tese jurídica
function generateThesis() {
    const topic = document.getElementById('thesisTopic').value;
    const area = document.getElementById('legalArea').value;
    const detailLevel = document.getElementById('detailLevel').value;

    if (!topic.trim()) {
        alert('Por favor, insira um tópico para a tese.');
        return;
    }

    // Mostrar loading
    $('#loadingModal').modal('show');

    // Fazer requisição ao servidor
    fetch('/generateThesis', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({
            topic: topic,
            area: area,
            detailLevel: detailLevel
        })
    })
    .then(response => response.json())
    .then(data => {
        $('#loadingModal').modal('hide');

        if (data.error) {
            alert('Erro: ' + data.error);
            return;
        }

        currentThesis = data.thesis;
        displayThesis(data.thesis);
    })
    .catch(error => {
        $('#loadingModal').modal('hide');
        alert('Erro ao gerar tese: ' + error);
    });
}

// Função para exibir a tese
function displayThesis(thesis) {
    const resultDiv = document.getElementById('thesisResult');
    const contentDiv = document.getElementById('thesisContent');

    let html = `
        <h3 class="text-primary">${thesis.title}</h3>
        <div class="alert alert-info">
            <strong>Área:</strong> ${thesis.metadata.area.charAt(0).toUpperCase() + thesis.metadata.area.slice(1)}<br>
            <strong>Nível de detalhamento:</strong> ${thesis.metadata.detail_level}<br>
            <strong>Gerado em:</strong> ${new Date(thesis.metadata.generated_at).toLocaleString('pt-BR')}
        </div>
    `;

    // Adicionar seções
    thesis.sections.forEach((section, index) => {
        html += `
            <div class="thesis-section mb-4">
                <h4 class="text-secondary">
                    <span class="badge badge-primary">${index + 1}</span> ${section.title}
                </h4>
                <div class="thesis-content p-3 bg-light rounded">
                    ${section.content.replace(/\n/g, '<br>')}
                </div>
            </div>
        `;
    });

    // Adicionar referências
    if (thesis.legal_references && thesis.legal_references.length > 0) {
        html += `
            <div class="references mt-4">
                <h4 class="text-secondary"><i class="fas fa-book"></i> Referências Jurídicas</h4>
                <ul class="list-group">
        `;
        thesis.legal_references.forEach(ref => {
            html += `<li class="list-group-item">${ref}</li>`;
        });
        html += `
                </ul>
            </div>
        `;
    }

    contentDiv.innerHTML = html;
    resultDiv.style.display = 'block';

    // Scroll suave até o resultado
    resultDiv.scrollIntoView({ behavior: 'smooth' });
}

// Função para analisar caso
function analyzeCase() {
    const caseDescription = document.getElementById('caseDescription').value;

    if (!caseDescription.trim()) {
        alert('Por favor, descreva o caso a ser analisado.');
        return;
    }

    $('#loadingModal').modal('show');

    fetch('/analyzeCase', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({
            caseDescription: caseDescription
        })
    })
    .then(response => response.json())
    .then(data => {
        $('#loadingModal').modal('hide');

        if (data.error) {
            alert('Erro: ' + data.error);
            return;
        }

        displayAnalysis(data.analysis);
    })
    .catch(error => {
        $('#loadingModal').modal('hide');
        alert('Erro ao analisar caso: ' + error);
    });
}

// Função para exibir análise
function displayAnalysis(analysis) {
    const resultDiv = document.getElementById('analysisResult');
    const contentDiv = document.getElementById('analysisContent');

    let html = `
        <div class="alert alert-info">
            <strong><i class="fas fa-tag"></i> Área Identificada:</strong>
            ${analysis.identified_area.charAt(0).toUpperCase() + analysis.identified_area.slice(1)}
        </div>

        <div class="mb-4">
            <h5><i class="fas fa-clipboard"></i> Resumo do Caso</h5>
            <p class="p-3 bg-light rounded">${analysis.summary}</p>
        </div>

        <div class="mb-4">
            <h5><i class="fas fa-exclamation-circle"></i> Questões Jurídicas Identificadas</h5>
            <ul class="list-group">
    `;

    analysis.legal_issues.forEach(issue => {
        html += `<li class="list-group-item">${issue}</li>`;
    });

    html += `
            </ul>
        </div>

        <div class="mb-4">
            <h5><i class="fas fa-balance-scale"></i> Princípios Aplicáveis</h5>
            <div class="row">
    `;

    analysis.applicable_principles.forEach(principle => {
        html += `
            <div class="col-md-6 mb-2">
                <div class="card">
                    <div class="card-body">
                        <i class="fas fa-check-circle text-success"></i> ${principle}
                    </div>
                </div>
            </div>
        `;
    });

    html += `
            </div>
        </div>

        <div class="mb-4">
            <h5><i class="fas fa-route"></i> Abordagem Sugerida</h5>
            <div class="p-3 bg-light rounded">
                ${analysis.suggested_approach.replace(/\n/g, '<br>')}
            </div>
        </div>

        <div class="mb-4">
            <h5><i class="fas fa-lightbulb"></i> Argumentos Potenciais</h5>
    `;

    analysis.potential_arguments.forEach((arg, index) => {
        html += `
            <div class="card mb-2">
                <div class="card-header bg-primary text-white">
                    ${arg.type}
                </div>
                <div class="card-body">
                    ${arg.content}
                </div>
            </div>
        `;
    });

    html += `</div>`;

    contentDiv.innerHTML = html;
    resultDiv.style.display = 'block';
    resultDiv.scrollIntoView({ behavior: 'smooth' });
}

// Função para sugerir argumentos
function suggestArguments() {
    const position = document.getElementById('position').value;
    const context = document.getElementById('context').value;

    if (!position.trim()) {
        alert('Por favor, informe a posição a ser defendida.');
        return;
    }

    $('#loadingModal').modal('show');

    fetch('/suggestArguments', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({
            position: position,
            context: context
        })
    })
    .then(response => response.json())
    .then(data => {
        $('#loadingModal').modal('hide');

        if (data.error) {
            alert('Erro: ' + data.error);
            return;
        }

        displayArguments(data.arguments);
    })
    .catch(error => {
        $('#loadingModal').modal('hide');
        alert('Erro ao sugerir argumentos: ' + error);
    });
}

// Função para exibir argumentos
function displayArguments(args) {
    const resultDiv = document.getElementById('argumentsResult');
    const contentDiv = document.getElementById('argumentsContent');

    let html = `
        <div class="alert alert-primary">
            <h5><i class="fas fa-bullseye"></i> Posição a Defender</h5>
            <p class="mb-0">${args.position}</p>
        </div>

        <div class="alert alert-info">
            <strong><i class="fas fa-tag"></i> Área do Direito:</strong>
            ${args.legal_area.charAt(0).toUpperCase() + args.legal_area.slice(1)}
        </div>

        <h5 class="mt-4"><i class="fas fa-list"></i> Argumentos Principais</h5>
    `;

    args.main_arguments.forEach((arg, index) => {
        const strengthClass = arg.strength === 'Alta' ? 'success' :
                            arg.strength === 'Média' ? 'warning' : 'info';
        html += `
            <div class="card mb-3">
                <div class="card-header bg-${strengthClass} text-white">
                    <strong>${index + 1}. ${arg.title}</strong>
                    <span class="badge badge-light float-right">Força: ${arg.strength}</span>
                </div>
                <div class="card-body">
                    <p>${arg.description}</p>
                    <small class="text-muted">
                        <i class="fas fa-bookmark"></i> Base: ${arg.basis}
                    </small>
                </div>
            </div>
        `;
    });

    html += `
        <h5 class="mt-4"><i class="fas fa-exchange-alt"></i> Contra-argumentos e Refutações</h5>
    `;

    args.counterarguments_and_rebuttals.forEach((item, index) => {
        html += `
            <div class="card mb-3">
                <div class="card-body">
                    <h6 class="text-danger"><i class="fas fa-times-circle"></i> Contra-argumento:</h6>
                    <p>${item.counterargument}</p>
                    <h6 class="text-success"><i class="fas fa-check-circle"></i> Refutação:</h6>
                    <p class="mb-0">${item.rebuttal}</p>
                </div>
            </div>
        `;
    });

    html += `
        <div class="card mt-4 bg-light">
            <div class="card-body">
                <h5><i class="fas fa-graduation-cap"></i> Elementos de Suporte</h5>

                <h6 class="mt-3">Princípios Fundamentais:</h6>
                <ul>
    `;

    args.supporting_elements.principles.forEach(principle => {
        html += `<li>${principle}</li>`;
    });

    html += `
                </ul>

                <h6 class="mt-3">Pesquisas Recomendadas:</h6>
                <ol>
    `;

    args.supporting_elements.recommended_research.forEach(research => {
        html += `<li>${research}</li>`;
    });

    html += `
                </ol>
            </div>
        </div>
    `;

    contentDiv.innerHTML = html;
    resultDiv.style.display = 'block';
    resultDiv.scrollIntoView({ behavior: 'smooth' });
}

// Função para baixar tese
function downloadThesis() {
    if (!currentThesis) return;

    let text = `${currentThesis.title}\n\n`;
    text += `Área: ${currentThesis.metadata.area}\n`;
    text += `Gerado em: ${new Date(currentThesis.metadata.generated_at).toLocaleString('pt-BR')}\n\n`;
    text += '='.repeat(80) + '\n\n';

    currentThesis.sections.forEach((section, index) => {
        text += `\n${index + 1}. ${section.title}\n`;
        text += '-'.repeat(80) + '\n';
        text += section.content + '\n\n';
    });

    if (currentThesis.legal_references) {
        text += '\n\nREFERÊNCIAS JURÍDICAS:\n';
        text += '-'.repeat(80) + '\n';
        currentThesis.legal_references.forEach(ref => {
            text += `- ${ref}\n`;
        });
    }

    const blob = new Blob([text], { type: 'text/plain' });
    const url = window.URL.createObjectURL(blob);
    const a = document.createElement('a');
    a.href = url;
    a.download = `tese_juridica_${Date.now()}.txt`;
    a.click();
    window.URL.revokeObjectURL(url);
}

// Função para copiar tese
function copyThesis() {
    if (!currentThesis) return;

    const contentDiv = document.getElementById('thesisContent');
    const text = contentDiv.innerText;

    navigator.clipboard.writeText(text).then(() => {
        alert('Tese copiada para a área de transferência!');
    }).catch(err => {
        alert('Erro ao copiar: ' + err);
    });
}

// ============= FUNÇÕES PARA SUBSÍDIOS JURÍDICOS =============

let currentContestacao = null;

// Função para gerar contestação
function gerarContestacao() {
    const peticaoInicial = document.getElementById('peticaoInicial').value;
    const subsidioTecnico = document.getElementById('subsidioTecnico').value;

    if (!peticaoInicial.trim() || !subsidioTecnico.trim()) {
        alert('Por favor, forneça tanto a petição inicial quanto o subsídio técnico.');
        return;
    }

    $('#loadingModal').modal('show');

    fetch('/gerarContestacao', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({
            peticaoInicial: peticaoInicial,
            subsidioTecnico: subsidioTecnico
        })
    })
    .then(response => response.json())
    .then(data => {
        $('#loadingModal').modal('hide');

        if (data.error) {
            alert('Erro: ' + data.error);
            return;
        }

        currentContestacao = data;
        displayAnalisePrevia(data);
        displayContestacao(data);
    })
    .catch(error => {
        $('#loadingModal').modal('hide');
        alert('Erro ao gerar contestação: ' + error);
    });
}

// Função para exibir análise prévia
function displayAnalisePrevia(data) {
    const analiseDiv = document.getElementById('analisePrevia');
    const peticaoInfoDiv = document.getElementById('peticaoInfoContent');
    const subsidioInfoDiv = document.getElementById('subsidioInfoContent');
    const tesesDiv = document.getElementById('tesesContent');

    // Informações da Petição
    let peticaoHtml = `
        <div class="alert alert-light">
            <p><strong>Autor:</strong> ${data.peticaoInfo.autor}</p>
            <p><strong>CPF:</strong> ${data.peticaoInfo.cpf}</p>
            <p><strong>Processo:</strong> ${data.peticaoInfo.processo}</p>
            <p><strong>Juízo:</strong> ${data.peticaoInfo.juizo}</p>
            <p><strong>Valor da Causa:</strong> R$ ${data.peticaoInfo.valor_causa}</p>
        </div>
    `;
    peticaoInfoDiv.innerHTML = peticaoHtml;

    // Informações do Subsídio
    let subsidioHtml = `
        <div class="alert alert-light">
            <p><strong>Cliente:</strong> ${data.subsidioInfo.cliente.nome}</p>
            <p><strong>Linha:</strong> ${data.subsidioInfo.linha}</p>
            <p><strong>Contrato:</strong> ${data.subsidioInfo.contrato}</p>
            <p><strong>Operadora:</strong> ${data.subsidioInfo.operadora_linha}</p>
            <p><strong>Conclusão:</strong> ${data.subsidioInfo.conclusao_tecnica.substring(0, 150)}...</p>
        </div>
    `;
    subsidioInfoDiv.innerHTML = subsidioHtml;

    // Teses Identificadas
    let tesesHtml = '<div class="row">';
    data.tesesDisponiveis.forEach(tese => {
        const badgeClass = tese.relevancia === 'alta' ? 'badge-danger' : 'badge-warning';
        const isSelecionada = data.tesesSelecionadas.some(t => t.tese === tese.tese);
        const border = isSelecionada ? 'border-success' : '';

        tesesHtml += `
            <div class="col-md-6 mb-2">
                <div class="card ${border}">
                    <div class="card-body">
                        <h6>
                            ${tese.detalhes.titulo}
                            <span class="badge ${badgeClass} float-right">${tese.relevancia}</span>
                            ${isSelecionada ? '<i class="fas fa-check-circle text-success float-right mr-2"></i>' : ''}
                        </h6>
                        <p class="small mb-0">${tese.fundamentacao}</p>
                    </div>
                </div>
            </div>
        `;
    });
    tesesHtml += '</div>';
    tesesDiv.innerHTML = tesesHtml;

    analiseDiv.style.display = 'block';
    analiseDiv.scrollIntoView({ behavior: 'smooth' });
}

// Função para exibir contestação
function displayContestacao(data) {
    const resultDiv = document.getElementById('contestacaoResult');
    const contentDiv = document.getElementById('contestacaoContent');

    let html = `
        <div class="alert alert-success">
            <h5><i class="fas fa-check"></i> Contestação Gerada com Sucesso!</h5>
            <p><strong>Processo:</strong> ${data.contestacao.metadata.processo}</p>
            <p><strong>Autor:</strong> ${data.contestacao.metadata.autor}</p>
            <p class="mb-0"><strong>Gerado em:</strong> ${new Date(data.contestacao.metadata.gerado_em).toLocaleString('pt-BR')}</p>
        </div>
    `;

    // Exibir cada seção da contestação
    data.contestacao.secoes.forEach((secao, index) => {
        html += `
            <div class="contestacao-secao mb-4">
                <h4 class="text-danger">
                    <span class="badge badge-danger">${index + 1}</span> ${secao.titulo}
                </h4>
                <div class="contestacao-content p-3 bg-light rounded">
                    ${secao.conteudo.replace(/\n/g, '<br>')}
                </div>
            </div>
        `;
    });

    contentDiv.innerHTML = html;
    resultDiv.style.display = 'block';
    resultDiv.scrollIntoView({ behavior: 'smooth' });
}

// Função para baixar contestação
function downloadContestacao() {
    if (!currentContestacao) return;

    const text = currentContestacao.textoFormatado;

    const blob = new Blob([text], { type: 'text/plain;charset=utf-8' });
    const url = window.URL.createObjectURL(blob);
    const a = document.createElement('a');
    a.href = url;
    a.download = `contestacao_${currentContestacao.peticaoInfo.processo.replace(/\D/g, '')}_${Date.now()}.txt`;
    a.click();
    window.URL.revokeObjectURL(url);

    alert('Contestação baixada com sucesso!');
}

// Função para copiar contestação
function copyContestacao() {
    if (!currentContestacao) return;

    const text = currentContestacao.textoFormatado;

    navigator.clipboard.writeText(text).then(() => {
        alert('Contestação copiada para a área de transferência!');
    }).catch(err => {
        alert('Erro ao copiar: ' + err);
    });
}

// Função para imprimir contestação
function printContestacao() {
    if (!currentContestacao) return;

    const contentDiv = document.getElementById('contestacaoContent');
    const printWindow = window.open('', '_blank');

    printWindow.document.write(`
        <!DOCTYPE html>
        <html>
        <head>
            <title>Contestação - Processo ${currentContestacao.peticaoInfo.processo}</title>
            <style>
                body {
                    font-family: Arial, sans-serif;
                    font-size: 12pt;
                    line-height: 1.6;
                    margin: 2cm;
                }
                h4 {
                    color: #000;
                    margin-top: 20px;
                }
                .badge {
                    display: none;
                }
                .contestacao-content {
                    text-align: justify;
                    margin-bottom: 20px;
                }
            </style>
        </head>
        <body>
            ${contentDiv.innerHTML}
        </body>
        </html>
    `);

    printWindow.document.close();
    printWindow.focus();
    printWindow.print();
    printWindow.close();
}

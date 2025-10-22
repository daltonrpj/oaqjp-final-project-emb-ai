# Agente de IA para Desenvolvimento de Teses Jurídicas

Um sistema inteligente desenvolvido em Python/Flask que utiliza técnicas de Inteligência Artificial para auxiliar na elaboração de teses jurídicas, análise de casos e sugestão de argumentos legais.

## Funcionalidades

### 1. Gerador de Teses Jurídicas
- Gera teses completas e estruturadas sobre qualquer tópico jurídico
- Identifica automaticamente a área do direito (Constitucional, Civil, Penal, Trabalhista, Administrativo)
- Três níveis de detalhamento: Básico, Médio e Detalhado
- Inclui fundamentação teórica, análise jurisprudencial e referências legais

### 2. Análise de Casos Jurídicos
- Analisa descrições de casos e identifica questões jurídicas relevantes
- Sugere princípios aplicáveis
- Propõe abordagem jurídica adequada
- Gera argumentos potenciais para o caso

### 3. Sugestão de Argumentos
- Cria argumentos jurídicos estruturados para defender uma posição
- Identifica contra-argumentos e fornece refutações
- Classifica argumentos por força (Alta, Média)
- Recomenda pesquisas complementares

## Estrutura do Projeto

```
oaqjp-final-project-emb-ai/
├── server.py                 # Servidor Flask principal
├── legal_thesis_agent.py     # Lógica do agente de IA
├── requirements.txt          # Dependências Python
├── templates/
│   └── index.html           # Interface web principal
├── static/
│   ├── legal_agent.js       # JavaScript do frontend
│   ├── styles.css           # Estilos CSS
│   └── mywebscript.js       # Script legado
└── README.md                # Esta documentação
```

## Tecnologias Utilizadas

- **Backend**: Python 3.x, Flask
- **Frontend**: HTML5, CSS3, JavaScript
- **UI Framework**: Bootstrap 4
- **Ícones**: Font Awesome 5

## Instalação

### Pré-requisitos
- Python 3.7 ou superior
- pip (gerenciador de pacotes Python)

### Passos para Instalação

1. Clone o repositório:
```bash
git clone https://github.com/daltonrpj/oaqjp-final-project-emb-ai.git
cd oaqjp-final-project-emb-ai
```

2. Instale as dependências:
```bash
pip install -r requirements.txt
```

3. Execute o servidor:
```bash
python server.py
```

4. Acesse a aplicação em seu navegador:
```
http://localhost:5000
```

## Como Usar

### Gerar uma Tese Jurídica

1. Acesse a aba "Gerar Tese"
2. Digite o tópico da tese (ex: "Responsabilidade civil no direito digital")
3. Selecione a área do direito (ou deixe em "Geral" para detecção automática)
4. Escolha o nível de detalhamento
5. Clique em "Gerar Tese Jurídica"
6. A tese será gerada com introdução, fundamentação, análise e conclusão
7. Você pode baixar ou copiar a tese gerada

### Analisar um Caso

1. Acesse a aba "Analisar Caso"
2. Descreva o caso jurídico que deseja analisar
3. Clique em "Analisar Caso"
4. O sistema identificará:
   - Área jurídica do caso
   - Questões jurídicas relevantes
   - Princípios aplicáveis
   - Abordagem sugerida
   - Argumentos potenciais

### Sugerir Argumentos

1. Acesse a aba "Sugerir Argumentos"
2. Digite a posição que deseja defender
3. Opcionalmente, forneça contexto adicional
4. Clique em "Sugerir Argumentos"
5. O sistema fornecerá:
   - Argumentos principais classificados por força
   - Contra-argumentos e refutações
   - Elementos de suporte e pesquisas recomendadas

## Arquitetura do Agente de IA

### LegalThesisAgent

O agente utiliza uma abordagem baseada em conhecimento estruturado:

1. **Base de Conhecimento**: Princípios jurídicos organizados por área do direito
2. **Identificação de Área**: Análise de palavras-chave para classificar o tema
3. **Geração Estruturada**: Templates dinâmicos que se adaptam ao contexto
4. **Argumentação Lógica**: Construção de argumentos baseados em princípios fundamentais

### Áreas do Direito Suportadas

- **Constitucional**: Direitos fundamentais, separação de poderes
- **Civil**: Contratos, responsabilidade civil, obrigações
- **Penal**: Crimes, penas, princípios penais
- **Trabalhista**: Relações de trabalho, direitos trabalhistas
- **Administrativo**: Atos administrativos, poder público
- **Geral**: Análise jurídica abrangente

### Princípios Jurídicos

Cada área possui seus princípios fundamentais que orientam a geração de teses:

- Constitucional: Dignidade da pessoa humana, Legalidade, Supremacia da Constituição
- Civil: Autonomia da vontade, Boa-fé objetiva, Função social
- Penal: Legalidade penal, Presunção de inocência, Individualização da pena
- Trabalhista: Proteção ao trabalhador, Primazia da realidade
- Administrativo: Legalidade, Impessoalidade, Moralidade, Publicidade, Eficiência

## API Endpoints

### POST /generateThesis
Gera uma tese jurídica completa.

**Request Body:**
```json
{
  "topic": "string",
  "area": "string",
  "detailLevel": "basic|medium|detailed"
}
```

**Response:**
```json
{
  "success": true,
  "thesis": {
    "title": "string",
    "metadata": {...},
    "sections": [...],
    "legal_references": [...]
  }
}
```

### POST /analyzeCase
Analisa um caso jurídico.

**Request Body:**
```json
{
  "caseDescription": "string"
}
```

**Response:**
```json
{
  "success": true,
  "analysis": {
    "identified_area": "string",
    "summary": "string",
    "legal_issues": [...],
    "applicable_principles": [...],
    "suggested_approach": "string",
    "potential_arguments": [...]
  }
}
```

### POST /suggestArguments
Sugere argumentos jurídicos.

**Request Body:**
```json
{
  "position": "string",
  "context": "string"
}
```

**Response:**
```json
{
  "success": true,
  "arguments": {
    "position": "string",
    "legal_area": "string",
    "main_arguments": [...],
    "counterarguments_and_rebuttals": [...],
    "supporting_elements": {...}
  }
}
```

## Limitações e Considerações

- Este é um sistema de auxílio educacional e não substitui a consulta jurídica profissional
- As teses geradas devem ser revisadas e adaptadas por profissionais do direito
- O sistema não tem acesso a bases de dados jurisprudenciais em tempo real
- As referências legais são genéricas e devem ser complementadas com pesquisa específica

## Contribuindo

Contribuições são bem-vindas! Para contribuir:

1. Faça um fork do projeto
2. Crie uma branch para sua feature (`git checkout -b feature/NovaFuncionalidade`)
3. Commit suas mudanças (`git commit -m 'Adiciona nova funcionalidade'`)
4. Push para a branch (`git push origin feature/NovaFuncionalidade`)
5. Abra um Pull Request

## Licença

Este projeto está sob a licença especificada no arquivo LICENSE.

## Autor

Desenvolvido como projeto final de IA aplicada ao direito.

## Próximos Passos

- [ ] Integração com APIs de jurisprudência
- [ ] Suporte a mais áreas do direito (Tributário, Internacional, etc.)
- [ ] Exportação para formatos PDF e DOCX
- [ ] Sistema de templates personalizáveis
- [ ] Integração com modelos de linguagem avançados (GPT, BERT)
- [ ] Histórico de teses geradas
- [ ] Sistema de usuários e autenticação

## Suporte

Para suporte, abra uma issue no repositório do GitHub.

# Sistema de Análise de Processos e Cálculo de Liquidação

Sistema web inteligente para análise automatizada de processos jurídicos e cálculo de liquidação judicial, utilizando Inteligência Artificial (DeepSeek) via OpenRouter API.

## Funcionalidades

### 1. Análise de Processos
- Extração automática de informações relevantes de processos jurídicos
- Identificação de partes, valores, decisões e datas
- Análise de juros e correção monetária aplicáveis
- Geração de resumo estruturado do processo

### 2. Cálculo de Liquidação
- Cálculo automatizado de valores de liquidação judicial
- Aplicação de correção monetária (IPCA-E, INPC, etc.)
- Cálculo de juros de mora (SELIC, etc.)
- Memória de cálculo detalhada
- Fundamentação legal

## Tecnologias Utilizadas

- **Backend**: Python 3 + Flask
- **Frontend**: HTML5, CSS3, JavaScript (Vanilla)
- **IA**: OpenRouter API com DeepSeek v3.1
- **UI**: Bootstrap 4 + Font Awesome
- **Ambiente**: dotenv para gerenciamento de variáveis

## Instalação

### Pré-requisitos
- Python 3.8 ou superior
- pip (gerenciador de pacotes Python)
- Chave API do OpenRouter

### Passo a Passo

1. **Clone o repositório**
```bash
git clone <url-do-repositorio>
cd oaqjp-final-project-emb-ai
```

2. **Crie um ambiente virtual (recomendado)**
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
# ou
venv\Scripts\activate  # Windows
```

3. **Instale as dependências**
```bash
pip install -r requirements.txt
```

4. **Configure as variáveis de ambiente**

O arquivo `.env` já deve estar configurado com sua chave API do OpenRouter:
```
OPENROUTER_API_KEY=sua-chave-api-aqui
OPENROUTER_BASE_URL=https://openrouter.ai/api/v1
OPENROUTER_MODEL=deepseek/deepseek-chat-v3.1:free
```

5. **Execute o servidor**
```bash
python server.py
```

6. **Acesse a aplicação**

Abra o navegador e acesse: `http://localhost:5000`

## Como Usar

### Análise de Processo

1. Na aba "Análise de Processo", cole o texto completo do processo judicial
2. Você pode clicar em "Carregar exemplo" para ver um exemplo prático
3. Clique em "Analisar Processo"
4. Aguarde alguns segundos enquanto a IA processa o documento
5. O resultado será exibido com todas as informações extraídas

### Cálculo de Liquidação

1. Vá para a aba "Cálculo de Liquidação"
2. Preencha os campos:
   - **Valor Base**: Valor principal da condenação (em reais)
   - **Data Inicial**: Data de início do cálculo
   - **Data Final**: Data final do cálculo (geralmente a data atual)
   - **Taxa de Juros** (opcional): Ex: SELIC, 1% a.m.
   - **Índice de Correção** (opcional): Ex: IPCA-E, INPC
3. Clique em "Calcular Liquidação"
4. O sistema retornará o cálculo completo com memória de cálculo

## Estrutura do Projeto

```
oaqjp-final-project-emb-ai/
│
├── .env                      # Variáveis de ambiente (não versionado)
├── .gitignore               # Arquivos ignorados pelo Git
├── requirements.txt         # Dependências Python
├── server.py               # Servidor Flask principal
├── settlement_calculator.py # Módulo de integração com IA
├── README.md               # Este arquivo
│
├── templates/
│   └── index.html          # Interface web principal
│
└── static/
    └── mywebscript.js      # Scripts JavaScript
```

## API Endpoints

### `GET /`
Retorna a página principal da aplicação

### `GET /analyzeProcess`
Analisa um processo jurídico

**Parâmetros:**
- `processText` (string): Texto completo do processo

**Resposta:** HTML com análise estruturada

### `GET /calculateSettlement`
Calcula valores de liquidação

**Parâmetros:**
- `baseValue` (float): Valor base em reais
- `startDate` (string): Data inicial (formato: YYYY-MM-DD)
- `endDate` (string): Data final (formato: YYYY-MM-DD)
- `interestRate` (string, opcional): Taxa de juros
- `correctionIndex` (string, opcional): Índice de correção

**Resposta:** HTML com cálculos detalhados

### `GET /health`
Health check do servidor

**Resposta:** JSON com status do serviço

## Segurança

- A chave API do OpenRouter está armazenada no arquivo `.env`
- O arquivo `.env` está incluído no `.gitignore` e não é versionado
- Nunca compartilhe sua chave API publicamente
- Em produção, use variáveis de ambiente do servidor

## Limitações e Considerações

- Os cálculos são gerados por IA e devem ser revisados por um profissional
- A precisão depende da qualidade do texto do processo fornecido
- O modelo gratuito do DeepSeek pode ter limitações de taxa
- Os valores calculados são estimativas e podem precisar de ajustes

## Solução de Problemas

### Erro: "OPENROUTER_API_KEY não encontrada"
- Verifique se o arquivo `.env` existe na raiz do projeto
- Confirme que a chave API está corretamente configurada

### Erro de conexão com OpenRouter
- Verifique sua conexão com a internet
- Confirme que a chave API está válida
- Verifique se não atingiu o limite de requisições

### Servidor não inicia
- Certifique-se de que todas as dependências estão instaladas
- Verifique se a porta 5000 não está em uso
- Confirme que o Python 3.8+ está instalado

## Desenvolvimento

Para contribuir com o projeto:

1. Faça um fork do repositório
2. Crie uma branch para sua feature (`git checkout -b feature/MinhaFeature`)
3. Commit suas mudanças (`git commit -m 'Adiciona MinhaFeature'`)
4. Push para a branch (`git push origin feature/MinhaFeature`)
5. Abra um Pull Request

## Licença

Este projeto está sob a licença especificada no arquivo `LICENSE`.

## Suporte

Para questões e suporte, abra uma issue no repositório do projeto.

---

**Desenvolvido com OpenRouter + DeepSeek AI**

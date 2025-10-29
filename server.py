"""
Servidor Flask para aplicação de análise de processos e cálculo de liquidação
"""

from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
from settlement_calculator import SettlementCalculator
import json

app = Flask(__name__)
CORS(app)

# Inicializar o calculador
calculator = SettlementCalculator()


@app.route('/')
def index():
    """Rota principal - renderiza a página inicial"""
    return render_template('index.html')


@app.route('/analyzeProcess', methods=['GET', 'POST'])
def analyze_process():
    """
    Endpoint para análise de processos jurídicos
    Aceita texto do processo e retorna análise detalhada
    """
    try:
        if request.method == 'GET':
            process_text = request.args.get('processText', '')
        else:
            data = request.get_json()
            process_text = data.get('processText', '')

        if not process_text:
            return jsonify({
                "success": False,
                "error": "Texto do processo não fornecido"
            }), 400

        # Analisar o processo
        result = calculator.analyze_process(process_text)

        if result['success']:
            # Formatar resultado para HTML
            data = result['data']

            if data.get('formato') == 'texto':
                html_output = f"""
                <div class="alert alert-success">
                    <h4>Análise Completa do Processo</h4>
                    <div style="white-space: pre-wrap;">{data['analise_completa']}</div>
                </div>
                """
            else:
                html_output = f"""
                <div class="alert alert-success">
                    <h4>Análise do Processo</h4>

                    <div class="mt-3">
                        <strong>Tipo de Ação:</strong> {data.get('tipo_acao', 'N/A')}
                    </div>

                    <div class="mt-2">
                        <strong>Autor:</strong> {data.get('autor', 'N/A')}
                    </div>

                    <div class="mt-2">
                        <strong>Réu:</strong> {data.get('reu', 'N/A')}
                    </div>

                    <div class="mt-3">
                        <strong>Valores:</strong>
                        <div class="ml-3">{format_field(data.get('valores', 'N/A'))}</div>
                    </div>

                    <div class="mt-3">
                        <strong>Decisões:</strong>
                        <div class="ml-3">{format_field(data.get('decisoes', 'N/A'))}</div>
                    </div>

                    <div class="mt-3">
                        <strong>Cálculos de Liquidação:</strong>
                        <div class="ml-3">{format_field(data.get('calculos_liquidacao', 'N/A'))}</div>
                    </div>

                    <div class="mt-3">
                        <strong>Datas Relevantes:</strong>
                        <div class="ml-3">{format_field(data.get('datas_relevantes', 'N/A'))}</div>
                    </div>

                    <div class="mt-3">
                        <strong>Juros e Correção:</strong>
                        <div class="ml-3">{format_field(data.get('juros_correcao', 'N/A'))}</div>
                    </div>

                    <div class="mt-3">
                        <strong>Resumo:</strong>
                        <div class="ml-3">{format_field(data.get('resumo', 'N/A'))}</div>
                    </div>
                </div>
                """

            return html_output
        else:
            return f"""
            <div class="alert alert-danger">
                <strong>Erro na análise:</strong> {result.get('error', 'Erro desconhecido')}
            </div>
            """, 500

    except Exception as e:
        return f"""
        <div class="alert alert-danger">
            <strong>Erro:</strong> {str(e)}
        </div>
        """, 500


@app.route('/calculateSettlement', methods=['GET', 'POST'])
def calculate_settlement():
    """
    Endpoint para cálculo de liquidação
    Aceita parâmetros de cálculo e retorna valores atualizados
    """
    try:
        if request.method == 'GET':
            base_value = float(request.args.get('baseValue', 0))
            start_date = request.args.get('startDate', '')
            end_date = request.args.get('endDate', '')
            interest_rate = request.args.get('interestRate')
            correction_index = request.args.get('correctionIndex')
        else:
            data = request.get_json()
            base_value = float(data.get('baseValue', 0))
            start_date = data.get('startDate', '')
            end_date = data.get('endDate', '')
            interest_rate = data.get('interestRate')
            correction_index = data.get('correctionIndex')

        if not base_value or not start_date or not end_date:
            return jsonify({
                "success": False,
                "error": "Parâmetros obrigatórios não fornecidos"
            }), 400

        # Calcular liquidação
        result = calculator.calculate_settlement(
            base_value,
            start_date,
            end_date,
            interest_rate,
            correction_index
        )

        if result['success']:
            html_output = f"""
            <div class="alert alert-info">
                <h4>Cálculo de Liquidação</h4>
                <div style="white-space: pre-wrap;">{result['calculation']}</div>
            </div>
            """
            return html_output
        else:
            return f"""
            <div class="alert alert-danger">
                <strong>Erro no cálculo:</strong> {result.get('error', 'Erro desconhecido')}
            </div>
            """, 500

    except ValueError as e:
        return f"""
        <div class="alert alert-danger">
            <strong>Erro:</strong> Valor inválido fornecido
        </div>
        """, 400
    except Exception as e:
        return f"""
        <div class="alert alert-danger">
            <strong>Erro:</strong> {str(e)}
        </div>
        """, 500


def format_field(field):
    """
    Formata campos para exibição HTML
    """
    if isinstance(field, list):
        return "<br>".join([f"• {item}" for item in field])
    elif isinstance(field, dict):
        return "<br>".join([f"• {k}: {v}" for k, v in field.items()])
    else:
        return str(field)


@app.route('/health')
def health():
    """Endpoint de health check"""
    return jsonify({
        "status": "healthy",
        "service": "Settlement Calculator API"
    })


if __name__ == '__main__':
    print("=" * 60)
    print("Servidor de Análise de Processos e Cálculo de Liquidação")
    print("=" * 60)
    print("Servidor rodando em: http://localhost:5000")
    print("=" * 60)
    app.run(host='0.0.0.0', port=5000, debug=True)

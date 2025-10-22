"""
Servidor Flask para o Agente de IA de Teses Jurídicas
"""
from flask import Flask, render_template, request, jsonify
from legal_thesis_agent import LegalThesisAgent
import json

app = Flask(__name__)

# Inicializar o agente de teses jurídicas
legal_agent = LegalThesisAgent()

@app.route('/')
def index():
    """Renderiza a página principal"""
    return render_template('index.html')

@app.route('/emotionDetector')
def emotion_detector():
    """Endpoint original para detecção de emoções (mantido para compatibilidade)"""
    text = request.args.get('textToAnalyze', '')
    if not text:
        return "Por favor, forneça um texto para análise."

    # Análise simples de emoção (pode ser expandida)
    emotions = {
        'anger': 0.1,
        'joy': 0.3,
        'sadness': 0.1,
        'fear': 0.05,
        'neutral': 0.45
    }

    return json.dumps(emotions)

@app.route('/generateThesis', methods=['POST'])
def generate_thesis():
    """Endpoint para gerar teses jurídicas"""
    try:
        data = request.get_json()
        topic = data.get('topic', '')
        area = data.get('area', 'geral')
        detail_level = data.get('detailLevel', 'medium')

        if not topic:
            return jsonify({
                'error': 'Por favor, forneça um tópico para a tese jurídica.'
            }), 400

        # Gerar a tese usando o agente
        thesis = legal_agent.generate_thesis(topic, area, detail_level)

        return jsonify({
            'success': True,
            'thesis': thesis
        })

    except Exception as e:
        return jsonify({
            'error': f'Erro ao gerar tese: {str(e)}'
        }), 500

@app.route('/analyzeCase', methods=['POST'])
def analyze_case():
    """Endpoint para análise de casos jurídicos"""
    try:
        data = request.get_json()
        case_description = data.get('caseDescription', '')

        if not case_description:
            return jsonify({
                'error': 'Por favor, forneça uma descrição do caso.'
            }), 400

        # Analisar o caso usando o agente
        analysis = legal_agent.analyze_case(case_description)

        return jsonify({
            'success': True,
            'analysis': analysis
        })

    except Exception as e:
        return jsonify({
            'error': f'Erro ao analisar caso: {str(e)}'
        }), 500

@app.route('/suggestArguments', methods=['POST'])
def suggest_arguments():
    """Endpoint para sugerir argumentos jurídicos"""
    try:
        data = request.get_json()
        position = data.get('position', '')
        context = data.get('context', '')

        if not position:
            return jsonify({
                'error': 'Por favor, forneça uma posição para argumentar.'
            }), 400

        # Sugerir argumentos usando o agente
        arguments = legal_agent.suggest_arguments(position, context)

        return jsonify({
            'success': True,
            'arguments': arguments
        })

    except Exception as e:
        return jsonify({
            'error': f'Erro ao sugerir argumentos: {str(e)}'
        }), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

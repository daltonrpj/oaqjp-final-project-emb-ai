"""
Módulo para análise de processos jurídicos e cálculo de liquidação
usando OpenRouter API com DeepSeek
"""

import os
from openai import OpenAI
from dotenv import load_dotenv
import json

# Carregar variáveis de ambiente
load_dotenv()

class SettlementCalculator:
    def __init__(self):
        """Inicializa o cliente OpenRouter"""
        self.api_key = os.getenv('OPENROUTER_API_KEY')
        self.base_url = os.getenv('OPENROUTER_BASE_URL')
        self.model = os.getenv('OPENROUTER_MODEL')

        if not self.api_key:
            raise ValueError("OPENROUTER_API_KEY não encontrada no arquivo .env")

        self.client = OpenAI(
            base_url=self.base_url,
            api_key=self.api_key,
        )

    def analyze_process(self, process_text):
        """
        Analisa o texto do processo jurídico e extrai informações relevantes

        Args:
            process_text (str): Texto completo do processo a ser analisado

        Returns:
            dict: Resultado da análise com informações extraídas
        """
        try:
            prompt = f"""
            Você é um assistente jurídico especializado em análise de processos e cálculos de liquidação.
            Analise o seguinte processo judicial e extraia as seguintes informações:

            1. Tipo de ação (trabalhista, cível, etc.)
            2. Partes envolvidas (autor e réu)
            3. Valores mencionados no processo
            4. Decisões judiciais e sentenças
            5. Cálculos de liquidação necessários
            6. Datas relevantes
            7. Juros e correção monetária aplicáveis
            8. Resumo da situação

            Processo:
            {process_text}

            Forneça uma resposta estruturada em formato JSON com as seguintes chaves:
            - tipo_acao
            - autor
            - reu
            - valores
            - decisoes
            - calculos_liquidacao
            - datas_relevantes
            - juros_correcao
            - resumo
            """

            completion = self.client.chat.completions.create(
                extra_headers={
                    "HTTP-Referer": "https://settlement-calculator.app",
                    "X-Title": "Settlement Calculator",
                },
                extra_body={},
                model=self.model,
                messages=[
                    {
                        "role": "system",
                        "content": "Você é um assistente jurídico especializado em análise de processos e cálculos de liquidação. Sempre forneça respostas estruturadas e detalhadas."
                    },
                    {
                        "role": "user",
                        "content": prompt
                    }
                ],
                temperature=0.3,  # Menor temperatura para respostas mais consistentes
            )

            response_text = completion.choices[0].message.content

            # Tentar extrair JSON da resposta
            try:
                # Procurar por blocos JSON na resposta
                start_idx = response_text.find('{')
                end_idx = response_text.rfind('}') + 1

                if start_idx != -1 and end_idx > start_idx:
                    json_text = response_text[start_idx:end_idx]
                    result = json.loads(json_text)
                else:
                    # Se não encontrar JSON, retornar resposta em texto
                    result = {
                        "analise_completa": response_text,
                        "formato": "texto"
                    }
            except json.JSONDecodeError:
                result = {
                    "analise_completa": response_text,
                    "formato": "texto"
                }

            return {
                "success": True,
                "data": result
            }

        except Exception as e:
            return {
                "success": False,
                "error": str(e)
            }

    def calculate_settlement(self, base_value, start_date, end_date, interest_rate=None, correction_index=None):
        """
        Calcula valores de liquidação com base nos parâmetros fornecidos

        Args:
            base_value (float): Valor base da condenação
            start_date (str): Data inicial para cálculo
            end_date (str): Data final para cálculo
            interest_rate (float): Taxa de juros (opcional)
            correction_index (str): Índice de correção monetária (opcional)

        Returns:
            dict: Cálculos detalhados de liquidação
        """
        try:
            prompt = f"""
            Como especialista em cálculos de liquidação judicial, calcule os valores devidos considerando:

            Valor Base: R$ {base_value}
            Data Inicial: {start_date}
            Data Final: {end_date}
            Taxa de Juros: {interest_rate if interest_rate else 'Taxa SELIC padrão'}
            Índice de Correção: {correction_index if correction_index else 'IPCA-E padrão'}

            Forneça:
            1. Valor atualizado com correção monetária
            2. Valor dos juros
            3. Valor total da liquidação
            4. Memória de cálculo detalhada
            5. Fundamentação legal aplicável

            Formate a resposta de forma clara e estruturada.
            """

            completion = self.client.chat.completions.create(
                extra_headers={
                    "HTTP-Referer": "https://settlement-calculator.app",
                    "X-Title": "Settlement Calculator",
                },
                extra_body={},
                model=self.model,
                messages=[
                    {
                        "role": "system",
                        "content": "Você é um especialista em cálculos de liquidação judicial e matemática financeira aplicada ao direito."
                    },
                    {
                        "role": "user",
                        "content": prompt
                    }
                ],
                temperature=0.1,  # Temperatura muito baixa para precisão matemática
            )

            result = completion.choices[0].message.content

            return {
                "success": True,
                "calculation": result
            }

        except Exception as e:
            return {
                "success": False,
                "error": str(e)
            }


def test_calculator():
    """Função de teste do calculador"""
    calc = SettlementCalculator()

    # Teste simples
    test_process = """
    PROCESSO Nº 0001234-56.2023.5.02.0001
    AUTOR: João da Silva
    RÉU: Empresa XYZ Ltda

    SENTENÇA: Julgo procedente o pedido para condenar a ré ao pagamento de R$ 50.000,00
    a título de indenização por danos morais, com juros e correção monetária desde a data
    do fato (01/01/2020) até o efetivo pagamento.
    """

    result = calc.analyze_process(test_process)
    print("Resultado da análise:", json.dumps(result, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    test_calculator()

"""
Módulo de Análise de Subsídios Técnicos e Criação de Contestações Jurídicas
Especializado em processos de telecomunicações (Claro S/A)
"""

import re
from datetime import datetime


class SubsidiosJuridicosAgent:
    """
    Agente especializado em análise de subsídios técnicos e criação de contestações
    jurídicas para processos de telecomunicações
    """

    def __init__(self):
        """Inicializa o agente com padrões de contestações"""
        self.teses_defesa = {
            'ilegitimidade_passiva': {
                'titulo': 'Ilegitimidade Passiva',
                'descricao': 'Linha pertence a outra operadora',
                'fundamento': 'Ausência de relação jurídica entre as partes'
            },
            'cobranca_legitima': {
                'titulo': 'Cobrança Legítima',
                'descricao': 'Serviços efetivamente prestados',
                'fundamento': 'Contrato válido e serviços utilizados'
            },
            'inexistencia_falha': {
                'titulo': 'Inexistência de Falha',
                'descricao': 'Rede operando normalmente, cobertura adequada',
                'fundamento': 'Ausência de defeito na prestação do serviço'
            },
            'necessidade_pericia': {
                'titulo': 'Necessidade de Perícia Técnica',
                'descricao': 'Casos técnicos complexos que requerem perícia',
                'fundamento': 'Impossibilidade de julgamento sem análise técnica especializada'
            },
            'ausencia_dano_moral': {
                'titulo': 'Ausência de Dano Moral',
                'descricao': 'Não houve negativação ou abalo moral',
                'fundamento': 'Mero dissabor não configura dano moral indenizável'
            },
            'autor_contumaz': {
                'titulo': 'Autor Contumaz',
                'descricao': 'Múltiplos processos contra a mesma operadora',
                'fundamento': 'Litigância habitual e má-fé processual'
            }
        }

        self.estrutura_contestacao = [
            'cabecalho',
            'publicacoes_intimacoes',
            'dos_fatos',
            'preliminar',
            'merito',
            'pedidos',
            'encerramento'
        ]

    def analisar_peticao_inicial(self, texto_peticao):
        """
        Analisa a petição inicial e extrai informações relevantes

        Args:
            texto_peticao: Texto da petição inicial

        Returns:
            Dict com informações extraídas
        """
        info = {
            'autor': self._extrair_autor(texto_peticao),
            'cpf': self._extrair_cpf(texto_peticao),
            'processo': self._extrair_numero_processo(texto_peticao),
            'juizo': self._extrair_juizo(texto_peticao),
            'causa_pedir': self._extrair_causa_pedir(texto_peticao),
            'pedidos': self._extrair_pedidos(texto_peticao),
            'valor_causa': self._extrair_valor_causa(texto_peticao)
        }

        return info

    def analisar_subsidio_tecnico(self, texto_subsidio):
        """
        Analisa o subsídio técnico fornecido

        Args:
            texto_subsidio: Texto do subsídio técnico

        Returns:
            Dict com análise do subsídio
        """
        analise = {
            'cliente': self._extrair_dados_cliente(texto_subsidio),
            'linha': self._extrair_linha(texto_subsidio),
            'contrato': self._extrair_contrato(texto_subsidio),
            'conclusao_tecnica': self._extrair_conclusao_tecnica(texto_subsidio),
            'telas_disponiveis': self._identificar_telas(texto_subsidio),
            'operadora_linha': self._identificar_operadora(texto_subsidio)
        }

        return analise

    def identificar_tese_defesa(self, peticao_info, subsidio_info):
        """
        Identifica a tese de defesa mais adequada com base nas informações

        Args:
            peticao_info: Informações da petição inicial
            subsidio_info: Informações do subsídio técnico

        Returns:
            Lista de teses aplicáveis ordenadas por relevância
        """
        teses_aplicaveis = []

        # Verificar ilegitimidade passiva
        if subsidio_info.get('operadora_linha') and subsidio_info['operadora_linha'].upper() != 'CLARO':
            teses_aplicaveis.append({
                'tese': 'ilegitimidade_passiva',
                'relevancia': 'alta',
                'detalhes': self.teses_defesa['ilegitimidade_passiva'],
                'fundamentacao': f"A linha pertence à operadora {subsidio_info['operadora_linha']}"
            })

        # Verificar cobrança legítima
        if 'serviços prestados' in subsidio_info.get('conclusao_tecnica', '').lower():
            teses_aplicaveis.append({
                'tese': 'cobranca_legitima',
                'relevancia': 'alta',
                'detalhes': self.teses_defesa['cobranca_legitima'],
                'fundamentacao': 'Serviços efetivamente prestados conforme subsídio técnico'
            })

        # Verificar inexistência de falha
        conclusao = subsidio_info.get('conclusao_tecnica', '').lower()
        if 'rede normal' in conclusao or 'cobertura adequada' in conclusao or 'sem problemas' in conclusao:
            teses_aplicaveis.append({
                'tese': 'inexistencia_falha',
                'relevancia': 'alta',
                'detalhes': self.teses_defesa['inexistencia_falha'],
                'fundamentacao': 'Análise técnica demonstra funcionamento normal dos serviços'
            })

        # Verificar necessidade de perícia
        if 'análise técnica necessária' in conclusao or 'perícia' in conclusao:
            teses_aplicaveis.append({
                'tese': 'necessidade_pericia',
                'relevancia': 'média',
                'detalhes': self.teses_defesa['necessidade_pericia'],
                'fundamentacao': 'Matéria técnica que demanda análise pericial especializada'
            })

        # Verificar ausência de dano moral
        if 'negativação' not in peticao_info.get('causa_pedir', '').lower():
            teses_aplicaveis.append({
                'tese': 'ausencia_dano_moral',
                'relevancia': 'média',
                'detalhes': self.teses_defesa['ausencia_dano_moral'],
                'fundamentacao': 'Não houve negativação ou dano concreto ao autor'
            })

        return teses_aplicaveis

    def gerar_contestacao(self, peticao_info, subsidio_info, teses_selecionadas):
        """
        Gera a contestação completa formatada

        Args:
            peticao_info: Informações da petição inicial
            subsidio_info: Informações do subsídio técnico
            teses_selecionadas: Lista de teses a serem utilizadas

        Returns:
            Dict com a contestação completa estruturada
        """
        contestacao = {
            'metadata': {
                'processo': peticao_info.get('processo', 'N/A'),
                'autor': peticao_info.get('autor', 'N/A'),
                'gerado_em': datetime.now().isoformat()
            },
            'secoes': []
        }

        # Gerar cada seção
        contestacao['secoes'].append(self._gerar_cabecalho(peticao_info))
        contestacao['secoes'].append(self._gerar_publicacoes())
        contestacao['secoes'].append(self._gerar_dos_fatos(peticao_info, subsidio_info))

        # Adicionar preliminares se aplicável
        if any(t.get('tese') == 'ilegitimidade_passiva' for t in teses_selecionadas):
            contestacao['secoes'].append(self._gerar_preliminar_ilegitimidade(subsidio_info))

        contestacao['secoes'].append(self._gerar_merito(peticao_info, subsidio_info, teses_selecionadas))
        contestacao['secoes'].append(self._gerar_pedidos(teses_selecionadas))
        contestacao['secoes'].append(self._gerar_encerramento())

        return contestacao

    # Métodos auxiliares de extração

    def _extrair_autor(self, texto):
        """Extrai o nome do autor da petição"""
        patterns = [
            r'(?:autor|requerente|cliente):\s*([A-ZÀÁÂÃÈÉÊÌÍÒÓÔÕÙÚÇ\s]+)',
            r'([A-ZÀÁÂÃÈÉÊÌÍÒÓÔÕÙÚÇ\s]{3,}),\s*(?:brasileiro|portador)',
        ]
        for pattern in patterns:
            match = re.search(pattern, texto, re.IGNORECASE)
            if match:
                return match.group(1).strip().title()
        return 'Não identificado'

    def _extrair_cpf(self, texto):
        """Extrai o CPF do texto"""
        pattern = r'CPF[:\s]*(\d{3}\.?\d{3}\.?\d{3}-?\d{2})'
        match = re.search(pattern, texto, re.IGNORECASE)
        return match.group(1) if match else 'Não identificado'

    def _extrair_numero_processo(self, texto):
        """Extrai o número do processo"""
        pattern = r'(\d{7}-\d{2}\.\d{4}\.\d{1}\.\d{2}\.\d{4})'
        match = re.search(pattern, texto)
        return match.group(1) if match else 'Não identificado'

    def _extrair_juizo(self, texto):
        """Extrai o juízo do processo"""
        pattern = r'(\d+º\s*Juizado\s*Especial\s*C[ií]vel[^\.]*)'
        match = re.search(pattern, texto, re.IGNORECASE)
        return match.group(1) if match else 'Não identificado'

    def _extrair_causa_pedir(self, texto):
        """Extrai a causa de pedir"""
        keywords = ['causa de pedir', 'dos fatos', 'fundamentação']
        for keyword in keywords:
            pattern = rf'{keyword}[:\s]+(.*?)(?=\n\n|pedidos|requer)'
            match = re.search(pattern, texto, re.IGNORECASE | re.DOTALL)
            if match:
                return match.group(1).strip()[:500] + '...'
        return 'Não identificado'

    def _extrair_pedidos(self, texto):
        """Extrai os pedidos da petição"""
        pattern = r'(?:pedidos?|requer)[:\s]+(.*?)(?=\n\n\w|valor da causa|termos em que)'
        match = re.search(pattern, texto, re.IGNORECASE | re.DOTALL)
        if match:
            pedidos_texto = match.group(1).strip()
            return [p.strip() for p in pedidos_texto.split('\n') if p.strip()]
        return []

    def _extrair_valor_causa(self, texto):
        """Extrai o valor da causa"""
        pattern = r'valor\s*da\s*causa[:\s]*R?\$?\s*([\d.,]+)'
        match = re.search(pattern, texto, re.IGNORECASE)
        return match.group(1) if match else 'Não identificado'

    def _extrair_dados_cliente(self, texto):
        """Extrai dados do cliente do subsídio"""
        return {
            'nome': self._extrair_autor(texto),
            'cpf': self._extrair_cpf(texto)
        }

    def _extrair_linha(self, texto):
        """Extrai o número da linha"""
        pattern = r'(?:linha|telefone|número)[:\s]*(\d{2}\s*\d{4,5}-?\d{4})'
        match = re.search(pattern, texto, re.IGNORECASE)
        return match.group(1) if match else 'Não identificado'

    def _extrair_contrato(self, texto):
        """Extrai o número do contrato"""
        pattern = r'(?:contrato|acordo)[:\s]*(\d+)'
        match = re.search(pattern, texto, re.IGNORECASE)
        return match.group(1) if match else 'Não identificado'

    def _extrair_conclusao_tecnica(self, texto):
        """Extrai a conclusão técnica do subsídio"""
        patterns = [
            r'conclusão[:\s]+(.*?)(?=\n\n|\Z)',
            r'análise\s*técnica[:\s]+(.*?)(?=\n\n|\Z)',
            r'parecer[:\s]+(.*?)(?=\n\n|\Z)'
        ]
        for pattern in patterns:
            match = re.search(pattern, texto, re.IGNORECASE | re.DOTALL)
            if match:
                return match.group(1).strip()
        return 'Não identificada'

    def _identificar_telas(self, texto):
        """Identifica menções a telas no subsídio"""
        telas_comuns = ['SIEBEL', 'CRM', 'BILLING', 'REDE', 'ATENDIMENTO', 'FATURAS']
        telas_encontradas = []

        for tela in telas_comuns:
            if tela.lower() in texto.lower():
                telas_encontradas.append(tela)

        return telas_encontradas

    def _identificar_operadora(self, texto):
        """Identifica a operadora da linha"""
        operadoras = ['CLARO', 'VIVO', 'TIM', 'OI', 'NEXTEL']

        for operadora in operadoras:
            if operadora.lower() in texto.lower():
                return operadora

        return 'CLARO'  # Default

    # Métodos de geração de seções da contestação

    def _gerar_cabecalho(self, peticao_info):
        """Gera o cabeçalho da contestação"""
        return {
            'titulo': 'CABEÇALHO',
            'conteudo': f"""EXCELENTÍSSIMO(A) SENHOR(A) DOUTOR(A) JUIZ(A) DE DIREITO DO {peticao_info.get('juizo', 'JUIZADO ESPECIAL CÍVEL')}

PROCESSO Nº {peticao_info.get('processo', 'N/A')}

CLARO S/A, pessoa jurídica de direito privado, inscrita no CNPJ sob o nº 40.432.544/0001-47, com sede na Rua Henri Dunant, 780, Santo Amaro, São Paulo/SP, CEP 04.709-110, vem, respeitosamente, à presença de Vossa Excelência, por meio de seus procuradores que esta subscrevem, apresentar

CONTESTAÇÃO

em face da ação proposta por {peticao_info.get('autor', 'AUTOR')}, CPF nº {peticao_info.get('cpf', 'N/A')}, pelos fundamentos de fato e de direito a seguir expostos."""
        }

    def _gerar_publicacoes(self):
        """Gera a seção de publicações e intimações"""
        return {
            'titulo': 'DAS PUBLICAÇÕES E INTIMAÇÕES',
            'conteudo': """A Contestante requer que todas as publicações e intimações sejam realizadas em nome de seus advogados, conforme procuração anexa, no endereço constante do rodapé desta peça."""
        }

    def _gerar_dos_fatos(self, peticao_info, subsidio_info):
        """Gera a seção dos fatos"""
        return {
            'titulo': 'DOS FATOS',
            'conteudo': f"""O Autor ajuizou a presente demanda alegando {peticao_info.get('causa_pedir', 'fatos descritos na petição inicial')}.

Contudo, conforme se demonstrará, a pretensão autoral não merece prosperar.

A análise técnica realizada pela Contestante demonstra que:

Cliente: {subsidio_info.get('cliente', {}).get('nome', 'N/A')}
CPF: {subsidio_info.get('cliente', {}).get('cpf', 'N/A')}
Linha: {subsidio_info.get('linha', 'N/A')}
Contrato: {subsidio_info.get('contrato', 'N/A')}

Conclusão Técnica: {subsidio_info.get('conclusao_tecnica', 'Análise técnica demonstra a inexistência de irregularidades.')}"""
        }

    def _gerar_preliminar_ilegitimidade(self, subsidio_info):
        """Gera preliminar de ilegitimidade passiva"""
        operadora = subsidio_info.get('operadora_linha', 'outra operadora')

        return {
            'titulo': 'PRELIMINAR - DA ILEGITIMIDADE PASSIVA',
            'conteudo': f"""A análise dos sistemas da Contestante demonstra que a linha objeto da demanda pertence à operadora {operadora}, e não à CLARO S/A.

Conforme se verifica nas telas sistêmicas anexas, não há qualquer relação contratual entre a Contestante e o Autor relativamente à linha em questão.

Nos termos do artigo 485, VI, do Código de Processo Civil, é caso de extinção do processo sem resolução do mérito por ilegitimidade passiva.

A jurisprudência é pacífica no sentido de que a operadora que não mantém relação jurídica com o consumidor é parte ilegítima para figurar no polo passivo da demanda:

"APELAÇÃO. TELEFONIA. FALHA NA PRESTAÇÃO DE SERVIÇOS. ILEGITIMIDADE PASSIVA. Linha pertencente a outra operadora. Ausência de relação jurídica. Sentença mantida. Recurso desprovido." (TJSP, Apelação nº...)

Assim, impõe-se o reconhecimento da ilegitimidade passiva da Contestante, com a consequente extinção do processo sem resolução do mérito."""
        }

    def _gerar_merito(self, peticao_info, subsidio_info, teses):
        """Gera a seção do mérito"""
        conteudo = "DO MÉRITO\n\n"

        for tese in teses:
            if tese.get('tese') == 'cobranca_legitima':
                conteudo += self._secao_cobranca_legitima()
            elif tese.get('tese') == 'inexistencia_falha':
                conteudo += self._secao_inexistencia_falha(subsidio_info)
            elif tese.get('tese') == 'ausencia_dano_moral':
                conteudo += self._secao_ausencia_dano_moral()
            elif tese.get('tese') == 'necessidade_pericia':
                conteudo += self._secao_necessidade_pericia()

        return {
            'titulo': 'DO MÉRITO',
            'conteudo': conteudo
        }

    def _secao_cobranca_legitima(self):
        """Gera seção sobre cobrança legítima"""
        return """1. DA COBRANÇA LEGÍTIMA - SERVIÇOS EFETIVAMENTE PRESTADOS

Os serviços foram efetivamente prestados pela Contestante, conforme demonstram as telas sistêmicas anexas.

A cobrança impugnada pelo Autor refere-se a serviços devidamente contratados e utilizados, não havendo qualquer irregularidade.

O contrato foi validamente celebrado, com observância de todas as formalidades legais, havendo plena ciência do consumidor quanto aos serviços contratados e respectivos valores.

Assim, a cobrança é legítima e encontra respaldo no contrato firmado entre as partes.\n\n"""

    def _secao_inexistencia_falha(self, subsidio_info):
        """Gera seção sobre inexistência de falha"""
        return f"""2. DA INEXISTÊNCIA DE FALHA NA PRESTAÇÃO DOS SERVIÇOS

A análise técnica realizada pela Contestante demonstra que não houve qualquer falha na prestação dos serviços.

Conclusão Técnica: {subsidio_info.get('conclusao_tecnica', 'Os serviços foram prestados de forma regular.')}

As telas sistêmicas anexas comprovam que a rede operou normalmente durante todo o período questionado, com cobertura adequada na região do Autor.

Não se verifica, portanto, qualquer irregularidade que possa ensejar o dever de indenizar.

Eventual insatisfação do consumidor, desacompanhada de prova de falha concreta na prestação do serviço, não é suficiente para caracterizar defeito na prestação do serviço.\n\n"""

    def _secao_ausencia_dano_moral(self):
        """Gera seção sobre ausência de dano moral"""
        return """3. DA AUSÊNCIA DE DANO MORAL

Ainda que se cogitasse de alguma irregularidade (o que se admite apenas para argumentar), não há que se falar em dano moral indenizável.

O Autor não teve seu nome negativado, não sofreu qualquer abalo concreto em sua honra ou dignidade, limitando-se a narrar mero dissabor.

A jurisprudência do STJ é firme no sentido de que o mero dissabor, aborrecimento ou contratempo não configura dano moral indenizável:

"O mero dissabor não pode ser alçado ao patamar do dano moral, mas somente aquela agressão que exacerba a naturalidade dos fatos da vida, causando fundadas aflições ou angústias no espírito de quem ela se dirige." (STJ, REsp...)

Assim, não há dano moral a ser indenizado.\n\n"""

    def _secao_necessidade_pericia(self):
        """Gera seção sobre necessidade de perícia"""
        return """4. DA NECESSIDADE DE PERÍCIA TÉCNICA

A matéria controvertida envolve questões técnicas complexas relacionadas à prestação de serviços de telecomunicações, que demandam conhecimento especializado.

A mera análise documental não é suficiente para esclarecer os fatos, sendo imprescindível a realização de perícia técnica por profissional habilitado.

Nos termos do artigo 464 do CPC, a prova pericial é necessária quando a comprovação do fato depender de conhecimento técnico ou científico.

Requer, portanto, a produção de prova pericial técnica.\n\n"""

    def _gerar_pedidos(self, teses):
        """Gera a seção de pedidos"""
        pedidos = []

        # Verificar se há preliminar
        tem_ilegitimidade = any(t.get('tese') == 'ilegitimidade_passiva' for t in teses)

        if tem_ilegitimidade:
            pedidos.append("a) Seja reconhecida a ILEGITIMIDADE PASSIVA da Contestante, com a consequente EXTINÇÃO DO PROCESSO SEM RESOLUÇÃO DO MÉRITO, nos termos do artigo 485, VI, do CPC;")

        pedidos.extend([
            "b) Alternativamente, caso não acolhida a preliminar, seja a presente ação JULGADA TOTALMENTE IMPROCEDENTE, com a condenação do Autor ao pagamento das custas processuais e honorários advocatícios;",
            "c) Seja deferida a produção de todos os meios de prova em direito admitidos, especialmente documental e pericial, se necessário."
        ])

        conteudo = "DOS PEDIDOS\n\nDiante do exposto, requer a Contestante:\n\n"
        conteudo += "\n".join(pedidos)

        return {
            'titulo': 'DOS PEDIDOS',
            'conteudo': conteudo
        }

    def _gerar_encerramento(self):
        """Gera o encerramento da contestação"""
        return {
            'titulo': 'ENCERRAMENTO',
            'conteudo': f"""Termos em que,
Pede deferimento.

São Paulo, {datetime.now().strftime('%d de %B de %Y')}.

[ADVOGADO]
OAB/SP nº [NÚMERO]"""
        }

    def formatar_contestacao_completa(self, contestacao):
        """
        Formata a contestação completa em texto

        Args:
            contestacao: Dict com a contestação estruturada

        Returns:
            String com a contestação formatada
        """
        texto = ""

        for secao in contestacao['secoes']:
            texto += f"\n{secao['titulo']}\n"
            texto += "=" * len(secao['titulo']) + "\n\n"
            texto += secao['conteudo'] + "\n\n"

        return texto

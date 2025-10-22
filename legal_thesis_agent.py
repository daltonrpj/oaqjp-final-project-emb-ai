"""
Agente de IA para Desenvolvimento de Teses Jurídicas
Este módulo implementa um agente inteligente que gera teses jurídicas,
analisa casos e sugere argumentos baseados em princípios do direito.
"""

import re
from datetime import datetime


class LegalThesisAgent:
    """
    Agente de IA especializado em desenvolver teses jurídicas
    """

    def __init__(self):
        """Inicializa o agente com bases de conhecimento jurídico"""
        self.legal_areas = {
            'constitucional': {
                'principles': ['Dignidade da pessoa humana', 'Separação dos poderes',
                              'Legalidade', 'Supremacia da Constituição'],
                'keywords': ['constitucional', 'fundamental', 'direitos humanos', 'constituição']
            },
            'civil': {
                'principles': ['Autonomia da vontade', 'Boa-fé objetiva',
                              'Função social dos contratos', 'Responsabilidade civil'],
                'keywords': ['contrato', 'responsabilidade', 'obrigação', 'patrimônio']
            },
            'penal': {
                'principles': ['Legalidade penal', 'Presunção de inocência',
                              'Individualização da pena', 'Dignidade do preso'],
                'keywords': ['crime', 'pena', 'culpabilidade', 'ilícito']
            },
            'trabalhista': {
                'principles': ['Proteção ao trabalhador', 'Irrenunciabilidade de direitos',
                              'Primazia da realidade', 'Continuidade da relação de emprego'],
                'keywords': ['trabalho', 'emprego', 'salário', 'jornada']
            },
            'administrativo': {
                'principles': ['Legalidade administrativa', 'Impessoalidade',
                              'Moralidade', 'Publicidade', 'Eficiência'],
                'keywords': ['administração pública', 'servidor', 'ato administrativo', 'poder público']
            },
            'geral': {
                'principles': ['Justiça', 'Equidade', 'Segurança jurídica', 'Razoabilidade'],
                'keywords': ['direito', 'lei', 'jurídico', 'norma']
            }
        }

        self.thesis_structures = {
            'basic': ['Introdução', 'Fundamentação', 'Conclusão'],
            'medium': ['Introdução', 'Contextualização', 'Fundamentação Jurídica',
                      'Análise Crítica', 'Conclusão'],
            'detailed': ['Introdução e Delimitação do Tema', 'Contextualização Histórica e Social',
                        'Fundamentação Teórica', 'Análise Jurisprudencial',
                        'Argumentação Jurídica', 'Contrapontos e Refutação',
                        'Conclusão e Proposições']
        }

    def identify_legal_area(self, text):
        """Identifica a área jurídica mais relevante para o texto"""
        text_lower = text.lower()
        area_scores = {}

        for area, data in self.legal_areas.items():
            score = sum(1 for keyword in data['keywords'] if keyword in text_lower)
            area_scores[area] = score

        # Retorna a área com maior pontuação, ou 'geral' se nenhuma for identificada
        max_area = max(area_scores, key=area_scores.get)
        return max_area if area_scores[max_area] > 0 else 'geral'

    def generate_thesis(self, topic, area='geral', detail_level='medium'):
        """
        Gera uma tese jurídica completa baseada no tópico fornecido

        Args:
            topic: Tópico da tese jurídica
            area: Área do direito (constitucional, civil, penal, etc.)
            detail_level: Nível de detalhamento (basic, medium, detailed)

        Returns:
            Dict com a estrutura completa da tese
        """
        # Se a área não for especificada ou for inválida, tenta identificar
        if area not in self.legal_areas or area == 'geral':
            area = self.identify_legal_area(topic)

        # Seleciona a estrutura apropriada
        structure_key = detail_level if detail_level in self.thesis_structures else 'medium'
        structure = self.thesis_structures[structure_key]

        # Gera cada seção da tese
        thesis = {
            'title': self._generate_title(topic, area),
            'metadata': {
                'area': area,
                'generated_at': datetime.now().isoformat(),
                'detail_level': detail_level
            },
            'sections': []
        }

        for section_title in structure:
            content = self._generate_section_content(section_title, topic, area)
            thesis['sections'].append({
                'title': section_title,
                'content': content
            })

        # Adiciona referências jurídicas
        thesis['legal_references'] = self._generate_legal_references(area)

        return thesis

    def _generate_title(self, topic, area):
        """Gera um título apropriado para a tese"""
        area_names = {
            'constitucional': 'Constitucional',
            'civil': 'Civil',
            'penal': 'Penal',
            'trabalhista': 'Trabalhista',
            'administrativo': 'Administrativo',
            'geral': 'Jurídica'
        }
        area_name = area_names.get(area, 'Jurídica')
        return f"{topic}: Uma Análise {area_name}"

    def _generate_section_content(self, section_title, topic, area):
        """Gera o conteúdo de uma seção específica da tese"""
        principles = self.legal_areas[area]['principles']

        content_templates = {
            'Introdução': f"""
A presente tese jurídica tem por objetivo analisar o tema "{topic}" sob a perspectiva do direito {area}.
Trata-se de matéria de grande relevância no cenário jurídico contemporâneo, demandando uma análise
criteriosa dos institutos jurídicos aplicáveis e dos princípios fundamentais que regem a matéria.

O estudo abordará os aspectos teóricos e práticos relacionados ao tema, buscando contribuir para
o debate jurídico e oferecer subsídios para a adequada compreensão e aplicação do direito.
""",
            'Introdução e Delimitação do Tema': f"""
A presente tese jurídica tem por objetivo analisar o tema "{topic}" sob a perspectiva do direito {area}.
Trata-se de matéria de grande relevância no cenário jurídico contemporâneo, demandando uma análise
criteriosa dos institutos jurídicos aplicáveis e dos princípios fundamentais que regem a matéria.

DELIMITAÇÃO: O presente estudo delimita-se à análise dos aspectos jurídicos relacionados a {topic},
considerando especialmente os princípios de {principles[0]} e {principles[1]}.
""",
            'Contextualização': f"""
O tema "{topic}" insere-se no contexto do direito {area}, área que se fundamenta em princípios
essenciais como {', '.join(principles[:3])}.

A compreensão adequada deste instituto jurídico requer a análise de sua evolução histórica,
bem como das transformações sociais e jurídicas que moldaram sua aplicação contemporânea.
""",
            'Contextualização Histórica e Social': f"""
EVOLUÇÃO HISTÓRICA:
O instituto jurídico relacionado a "{topic}" passou por significativas transformações ao longo
do desenvolvimento do direito {area}. Originalmente concebido sob paradigmas distintos dos atuais,
adaptou-se às mudanças sociais e aos novos valores constitucionais.

CONTEXTO SOCIAL:
Na sociedade contemporânea, o tema assume especial relevância, considerando as transformações
tecnológicas, econômicas e sociais que impactam diretamente a aplicação do direito. A análise
deve considerar não apenas os aspectos normativos, mas também a realidade fática subjacente.
""",
            'Fundamentação': f"""
A fundamentação jurídica do presente estudo baseia-se nos seguintes pilares:

1. PRINCÍPIO DA {principles[0].upper()}:
   Este princípio fundamental orienta toda a interpretação e aplicação do direito em relação ao
   tema "{topic}". Sua observância é imperativa para garantir a conformidade jurídica das soluções propostas.

2. PRINCÍPIO DA {principles[1].upper()}:
   Complementarmente, este princípio estabelece diretrizes essenciais que devem nortear a análise
   jurídica, assegurando a harmonia com o ordenamento jurídico vigente.

3. APLICAÇÃO NORMATIVA:
   A legislação pertinente deve ser interpretada à luz destes princípios, buscando a solução que
   melhor realize os valores constitucionais e atenda aos fins sociais do direito.
""",
            'Fundamentação Jurídica': f"""
BASE NORMATIVA:
A fundamentação jurídica do tema "{topic}" encontra respaldo em diversos diplomas normativos
do direito {area}. A interpretação sistemática e teleológica destas normas revela o alcance
e os limites do instituto jurídico em análise.

PRINCÍPIOS APLICÁVEIS:
Os princípios fundamentais que regem a matéria incluem:
- {principles[0]}: orienta a interpretação em conformidade com os valores fundamentais
- {principles[1]}: estabelece critérios objetivos de aplicação
- {principles[2]}: assegura a conformidade com os fins sociais do direito

DOUTRINA:
A doutrina especializada em direito {area} oferece importantes contribuições para a compreensão
do tema, destacando-se diferentes correntes interpretativas que enriquecem o debate jurídico.
""",
            'Fundamentação Teórica': f"""
MARCO TEÓRICO:
A análise do tema "{topic}" exige um sólido marco teórico fundado nas principais doutrinas
do direito {area}. As teorias clássicas e contemporâneas oferecem diferentes perspectivas
sobre o instituto jurídico em questão.

CORRENTES DOUTRINÁRIAS:
Primeira Corrente: Enfatiza a aplicação estrita do princípio da {principles[0]}, defendendo
uma interpretação que privilegie este fundamento.

Segunda Corrente: Propõe uma abordagem mais flexível, considerando a harmonização entre
{principles[1]} e as necessidades sociais contemporâneas.

Terceira Corrente: Advoga por uma síntese que contemple tanto os aspectos formais quanto
materiais do direito, buscando o equilíbrio entre segurança jurídica e justiça concreta.
""",
            'Análise Crítica': f"""
A análise crítica do tema "{topic}" revela aspectos que merecem especial atenção:

PONTOS POSITIVOS:
- A abordagem atual privilegia os princípios de {principles[0]} e {principles[1]}
- Há evolução jurisprudencial significativa na matéria
- O ordenamento jurídico oferece instrumentos adequados para a tutela dos direitos envolvidos

PONTOS CONTROVERSOS:
- Subsistem divergências interpretativas quanto à extensão de determinados conceitos
- A aplicação prática nem sempre corresponde aos ideais teóricos
- Há necessidade de maior harmonização entre as diferentes instâncias decisórias

PERSPECTIVAS DE APERFEIÇOAMENTO:
O direito {area} deve continuar evoluindo para melhor atender às demandas sociais,
mantendo-se fiel aos princípios fundamentais que o sustentam.
""",
            'Análise Jurisprudencial': f"""
PANORAMA JURISPRUDENCIAL:
A jurisprudência dos tribunais superiores tem se manifestado de forma consistente sobre
o tema "{topic}", estabelecendo importantes precedentes no âmbito do direito {area}.

PRINCIPAIS ORIENTAÇÕES:
1. Consolidou-se o entendimento de que o princípio da {principles[0]} deve prevalecer
   na interpretação das normas aplicáveis.

2. Os tribunais têm reconhecido a importância de harmonizar {principles[1]} com
   {principles[2]}, buscando soluções equilibradas.

3. A tendência jurisprudencial mais recente aponta para uma interpretação evolutiva
   que considera as transformações sociais e tecnológicas.

CASOS PARADIGMÁTICOS:
A análise de casos concretos demonstra como os tribunais têm aplicado estes princípios,
oferecendo valiosos subsídios para a compreensão do tema.
""",
            'Argumentação Jurídica': f"""
TESE PRINCIPAL:
Defende-se que "{topic}" deve ser compreendido à luz dos princípios fundamentais do
direito {area}, especialmente {principles[0]} e {principles[1]}.

ARGUMENTOS CENTRAIS:

Argumento 1 - Fundamento Constitucional:
O ordenamento jurídico pátrio, fundado na supremacia constitucional, exige que a interpretação
das normas infraconstitucionais observe os valores e princípios constitucionais fundamentais.

Argumento 2 - Interpretação Sistemática:
A análise sistemática do ordenamento revela a necessidade de harmonizar as diversas normas
aplicáveis, evitando contradições e privilegiando a coerência do sistema jurídico.

Argumento 3 - Finalidade Social:
O direito deve realizar seus fins sociais, promovendo a justiça concreta e atendendo aos
anseios legítimos da sociedade, sem descuidar da segurança jurídica.

Argumento 4 - Precedentes Jurisprudenciais:
A jurisprudência consolidada oferece importante orientação para a solução de casos concretos,
devendo ser considerada na fundamentação jurídica.
""",
            'Contrapontos e Refutação': f"""
CONTRAPONTOS POSSÍVEIS:
É importante considerar as objeções que podem ser levantadas contra a tese defendida:

Objeção 1: Pode-se argumentar que a interpretação proposta amplia excessivamente o
alcance das normas aplicáveis.

Refutação: A interpretação sistemática e teleológica não representa ampliação indevida,
mas sim a busca pela efetividade dos princípios constitucionais, especialmente {principles[0]}.

Objeção 2: Poderia haver alegação de insegurança jurídica decorrente de interpretação
mais flexível.

Refutação: A segurança jurídica não se confunde com rigidez interpretativa. O direito
deve evoluir para atender às transformações sociais, mantendo-se fiel aos princípios fundamentais.

Objeção 3: Questiona-se a aplicabilidade prática das soluções propostas.

Refutação: A jurisprudência demonstra que a aplicação dos princípios de {principles[1]}
e {principles[2]} tem produzido resultados concretos e efetivos na proteção dos direitos envolvidos.
""",
            'Conclusão': f"""
Diante do exposto, conclui-se que o tema "{topic}" no âmbito do direito {area} deve ser
compreendido à luz dos princípios fundamentais de {principles[0]} e {principles[1]}.

A análise realizada demonstra que o ordenamento jurídico oferece instrumentos adequados para
a tutela dos direitos envolvidos, sendo necessária uma interpretação que harmonize os diversos
valores em jogo.

Recomenda-se especial atenção à evolução jurisprudencial e doutrinária sobre a matéria,
bem como à necessidade de constante adequação do direito às transformações sociais,
sem perder de vista os princípios fundamentais que sustentam o Estado Democrático de Direito.
""",
            'Conclusão e Proposições': f"""
SÍNTESE CONCLUSIVA:
A presente análise sobre "{topic}" no contexto do direito {area} permite concluir que:

1. O tema possui relevância jurídica e social significativa, demandando tratamento adequado
   pelo ordenamento jurídico;

2. Os princípios de {principles[0]}, {principles[1]} e {principles[2]} constituem fundamentos
   essenciais para a adequada compreensão e aplicação do direito;

3. A jurisprudência tem evoluído no sentido de harmonizar os diversos valores em jogo,
   buscando soluções equilibradas e justas;

4. A doutrina oferece importantes contribuições teóricas que enriquecem o debate e orientam
   a aplicação prática do direito.

PROPOSIÇÕES:
Com base na análise realizada, propõe-se:

• A adoção de interpretação sistemática e teleológica que privilegie a efetividade dos
  princípios constitucionais;

• A harmonização entre segurança jurídica e justiça concreta, evitando formalismos excessivos
  que frustrem a realização do direito;

• O acompanhamento contínuo da evolução jurisprudencial e doutrinária, promovendo o
  aperfeiçoamento constante da aplicação do direito;

• A consideração das transformações sociais e tecnológicas na interpretação das normas,
  assegurando a atualidade e efetividade do ordenamento jurídico.

PERSPECTIVAS FUTURAS:
O direito {area} deve continuar evoluindo para melhor atender às demandas da sociedade
contemporânea, mantendo-se fiel aos valores fundamentais que sustentam o Estado Democrático
de Direito e promovendo a realização da justiça em sua dimensão concreta e efetiva.
"""
        }

        # Retorna o template correspondente ou um conteúdo genérico
        return content_templates.get(section_title,
            f"Análise detalhada sobre {topic} no contexto de {section_title}.")

    def _generate_legal_references(self, area):
        """Gera referências jurídicas relevantes"""
        references = {
            'constitucional': [
                'Constituição Federal de 1988',
                'Declaração Universal dos Direitos Humanos',
                'Pacto de San José da Costa Rica',
                'Lei 9.882/99 (ADPF)',
                'Lei 9.868/99 (ADI e ADC)'
            ],
            'civil': [
                'Código Civil (Lei 10.406/2002)',
                'Código de Defesa do Consumidor (Lei 8.078/90)',
                'Lei de Locações (Lei 8.245/91)',
                'Marco Civil da Internet (Lei 12.965/14)'
            ],
            'penal': [
                'Código Penal (Decreto-Lei 2.848/40)',
                'Código de Processo Penal (Decreto-Lei 3.689/41)',
                'Lei de Execução Penal (Lei 7.210/84)',
                'Lei de Crimes Hediondos (Lei 8.072/90)'
            ],
            'trabalhista': [
                'Consolidação das Leis do Trabalho (CLT)',
                'Constituição Federal (arts. 7º a 11)',
                'Lei 13.467/17 (Reforma Trabalhista)',
                'Súmulas do TST'
            ],
            'administrativo': [
                'Lei 8.429/92 (Improbidade Administrativa)',
                'Lei 9.784/99 (Processo Administrativo)',
                'Lei 8.666/93 (Licitações)',
                'Lei 14.133/21 (Nova Lei de Licitações)'
            ],
            'geral': [
                'Constituição Federal de 1988',
                'Lei de Introdução às Normas do Direito Brasileiro (LINDB)',
                'Código de Processo Civil (Lei 13.105/15)'
            ]
        }

        return references.get(area, references['geral'])

    def analyze_case(self, case_description):
        """
        Analisa um caso jurídico e fornece estrutura de análise

        Args:
            case_description: Descrição do caso a ser analisado

        Returns:
            Dict com análise estruturada do caso
        """
        area = self.identify_legal_area(case_description)
        principles = self.legal_areas[area]['principles']

        analysis = {
            'identified_area': area,
            'summary': self._generate_case_summary(case_description),
            'legal_issues': self._identify_legal_issues(case_description, area),
            'applicable_principles': principles,
            'suggested_approach': self._suggest_legal_approach(case_description, area),
            'potential_arguments': self._generate_case_arguments(case_description, area)
        }

        return analysis

    def _generate_case_summary(self, case_description):
        """Gera um resumo do caso"""
        words = case_description.split()
        if len(words) > 50:
            return ' '.join(words[:50]) + '...'
        return case_description

    def _identify_legal_issues(self, case_description, area):
        """Identifica questões jurídicas no caso"""
        issues = []

        # Análise baseada em palavras-chave
        issue_keywords = {
            'direito': 'Questão de direito subjetivo',
            'obrigação': 'Questão obrigacional',
            'responsabilidade': 'Questão de responsabilidade jurídica',
            'contrato': 'Questão contratual',
            'dano': 'Questão de reparação de danos',
            'ilícito': 'Questão de ilicitude',
            'constitucional': 'Questão constitucional'
        }

        case_lower = case_description.lower()
        for keyword, issue in issue_keywords.items():
            if keyword in case_lower:
                issues.append(issue)

        if not issues:
            issues.append(f'Questão central de direito {area}')

        return issues

    def _suggest_legal_approach(self, case_description, area):
        """Sugere abordagem jurídica para o caso"""
        principles = self.legal_areas[area]['principles']

        approach = f"""
ABORDAGEM SUGERIDA:

1. ANÁLISE PRELIMINAR:
   Examinar os fatos sob a ótica do direito {area}, identificando os elementos
   essenciais e as normas aplicáveis.

2. FUNDAMENTAÇÃO PRINCIPIOLÓGICA:
   Estruturar a argumentação com base nos princípios de {principles[0]} e {principles[1]},
   que orientam a matéria.

3. ANÁLISE NORMATIVA:
   Identificar e interpretar as normas jurídicas aplicáveis ao caso concreto,
   considerando a hierarquia normativa e a interpretação sistemática.

4. PESQUISA JURISPRUDENCIAL:
   Buscar precedentes relevantes que possam fundamentar ou orientar a solução do caso.

5. CONSTRUÇÃO ARGUMENTATIVA:
   Desenvolver argumentação sólida que articule fatos, normas, princípios e
   jurisprudência de forma coerente e persuasiva.
"""
        return approach

    def _generate_case_arguments(self, case_description, area):
        """Gera argumentos possíveis para o caso"""
        principles = self.legal_areas[area]['principles']

        arguments = [
            {
                'type': 'Argumento Principiológico',
                'content': f'Com base no princípio de {principles[0]}, pode-se argumentar que a solução deve privilegiar a proteção dos valores fundamentais envolvidos.'
            },
            {
                'type': 'Argumento Sistemático',
                'content': f'A interpretação sistemática do ordenamento jurídico, considerando o princípio de {principles[1]}, conduz a uma solução que harmoniza as diversas normas aplicáveis.'
            },
            {
                'type': 'Argumento Teleológico',
                'content': 'A finalidade da norma e os valores que busca proteger devem orientar sua interpretação e aplicação ao caso concreto.'
            },
            {
                'type': 'Argumento Consequencialista',
                'content': 'As consequências práticas da decisão devem ser consideradas, buscando a solução que melhor realize os fins sociais do direito.'
            }
        ]

        return arguments

    def suggest_arguments(self, position, context=''):
        """
        Sugere argumentos jurídicos para uma posição específica

        Args:
            position: Posição a ser defendida
            context: Contexto adicional (opcional)

        Returns:
            Lista de argumentos estruturados
        """
        combined_text = f"{position} {context}"
        area = self.identify_legal_area(combined_text)
        principles = self.legal_areas[area]['principles']

        arguments = {
            'position': position,
            'legal_area': area,
            'main_arguments': [
                {
                    'title': 'Argumento Constitucional',
                    'description': f'A posição defendida encontra respaldo nos princípios constitucionais, especialmente no princípio da {principles[0]}, que fundamenta a pretensão jurídica.',
                    'strength': 'Alta',
                    'basis': 'Constitucional'
                },
                {
                    'title': 'Argumento Legal',
                    'description': f'A legislação de direito {area} oferece suporte normativo à tese, devendo ser interpretada em conformidade com o princípio de {principles[1]}.',
                    'strength': 'Alta',
                    'basis': 'Legal'
                },
                {
                    'title': 'Argumento Doutrinário',
                    'description': f'A doutrina especializada em direito {area} sustenta posição alinhada com a tese defendida, reconhecendo a importância de {principles[2]}.',
                    'strength': 'Média',
                    'basis': 'Doutrinária'
                },
                {
                    'title': 'Argumento Jurisprudencial',
                    'description': 'Os tribunais superiores têm se manifestado favoravelmente em casos análogos, estabelecendo precedentes que fortalecem a argumentação.',
                    'strength': 'Alta',
                    'basis': 'Jurisprudencial'
                },
                {
                    'title': 'Argumento Sistemático',
                    'description': 'A interpretação sistemática do ordenamento jurídico conduz à conclusão pretendida, harmonizando as diversas normas aplicáveis.',
                    'strength': 'Média',
                    'basis': 'Sistemática'
                }
            ],
            'counterarguments_and_rebuttals': [
                {
                    'counterargument': 'Possível alegação de ausência de previsão legal expressa',
                    'rebuttal': 'A interpretação extensiva e analógica são instrumentos legítimos de integração do direito, autorizados pelo ordenamento jurídico.'
                },
                {
                    'counterargument': 'Questionamento sobre a aplicabilidade dos princípios invocados',
                    'rebuttal': f'Os princípios de {principles[0]} e {principles[1]} possuem aplicabilidade direta e imediata, conforme reconhecido pela jurisprudência.'
                }
            ],
            'supporting_elements': {
                'principles': principles[:3],
                'recommended_research': [
                    'Pesquisar jurisprudência dos tribunais superiores sobre o tema',
                    'Consultar doutrina especializada em direito ' + area,
                    'Analisar casos análogos e precedentes relevantes',
                    'Examinar a legislação comparada, se aplicável'
                ]
            }
        }

        return arguments

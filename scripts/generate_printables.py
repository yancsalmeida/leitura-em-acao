import os
import sys
from fpdf import FPDF, XPos, YPos

OUTPUT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


class MissionPDF(FPDF):
    def footer(self):
        self.set_y(-11)
        self.set_font("helvetica", "I", 8)
        self.set_text_color(120, 120, 120)
        self.cell(
            0,
            6,
            f"Projeto Leitura em Ação - Preparação 6º Ano (CMRJ / CP2 / CAp UERJ) | Página {self.page_no()}/2",
            align="C",
        )


def build_mission_sheet_pdf(filepath: str):
    pdf = MissionPDF(orientation="P", unit="mm", format="A4")
    pdf.set_auto_page_break(auto=False)

    # =========================================================================
    # PAGE 1: MISSÃO DE LEITURA + MAPA ANTI-FUGA (4 CAIXAS) + BANCO DE CONECTIVOS
    # =========================================================================
    pdf.add_page()

    # Header Banner
    pdf.set_fill_color(30, 58, 138)  # Deep Navy Blue
    pdf.rect(10, 10, 190, 20, "F")
    pdf.set_xy(14, 12)
    pdf.set_text_color(255, 255, 255)
    pdf.set_font("helvetica", "B", 14.5)
    pdf.cell(125, 8, "MISSÃO DE LEITURA E MAPA ANTI-FUGA", new_x=XPos.RIGHT, new_y=YPos.TOP)
    pdf.set_font("helvetica", "B", 10.5)
    pdf.cell(57, 8, "Missão #_____  Data: ___/___/___", new_x=XPos.LMARGIN, new_y=YPos.NEXT, align="R")

    pdf.set_xy(14, 21)
    pdf.set_font("helvetica", "", 9)
    pdf.set_text_color(219, 234, 254)
    pdf.cell(
        182,
        6,
        "Passo 1: Leia com atenção  |  Passo 2: Planeje nas 4 caixas (5 min)  |  Passo 3: Escreva a redação na Página 2",
        new_x=XPos.LMARGIN,
        new_y=YPos.NEXT,
    )

    # 1. Registro da Leitura
    y = 34
    pdf.set_fill_color(241, 245, 249)
    pdf.set_draw_color(148, 163, 184)
    pdf.rect(10, y, 190, 24, "DF")

    pdf.set_xy(14, y + 2.5)
    pdf.set_text_color(15, 23, 42)
    pdf.set_font("helvetica", "B", 10)
    pdf.cell(
        0,
        6,
        "1. O QUE EU LI HOJE (Título do Mangá, Gibi, Livro ou Conto + Capítulo):",
        new_x=XPos.LMARGIN,
        new_y=YPos.NEXT,
    )

    pdf.set_draw_color(100, 116, 139)
    pdf.line(14, y + 14.5, 196, y + 14.5)

    pdf.set_xy(14, y + 16.5)
    pdf.set_font("helvetica", "B", 8.5)
    pdf.set_text_color(51, 65, 85)
    pdf.cell(27, 5, "Nível da Leitura:", new_x=XPos.RIGHT, new_y=YPos.TOP)
    pdf.set_font("helvetica", "", 8.5)
    pdf.cell(48, 5, "[  ] Bronze (1 Gibi / 1 Cap. Mangá)", new_x=XPos.RIGHT, new_y=YPos.TOP)
    pdf.cell(52, 5, "[  ] Prata (2-3 Caps. Mangá / Livro)", new_x=XPos.RIGHT, new_y=YPos.TOP)
    pdf.cell(55, 5, "[  ] Ouro (+15 min: Conto/Livro s/ fig.)", new_x=XPos.LMARGIN, new_y=YPos.NEXT)

    # 2. A ÂNCORA (Caixa 0 - Tema + 3 Palavras-Chave)
    y = 62
    pdf.set_fill_color(254, 243, 199)  # Warm Amber background
    pdf.set_draw_color(217, 119, 6)
    pdf.set_line_width(0.5)
    pdf.rect(10, y, 190, 36, "DF")
    pdf.set_line_width(0.2)

    pdf.set_xy(14, y + 2.5)
    pdf.set_text_color(146, 64, 14)
    pdf.set_font("helvetica", "B", 10.5)
    pdf.cell(
        0,
        6,
        "2. A ÂNCORA DA MISSÃO (Regra de Ouro: Tudo no texto precisa ter relação com esta caixa!)",
        new_x=XPos.LMARGIN,
        new_y=YPos.NEXT,
    )

    pdf.set_xy(14, y + 9)
    pdf.set_text_color(30, 41, 59)
    pdf.set_font("helvetica", "B", 9)
    pdf.cell(35, 6, "Tipo de Missão:", new_x=XPos.RIGHT, new_y=YPos.TOP)
    pdf.set_font("helvetica", "", 8.5)
    pdf.cell(
        0,
        6,
        "[  ] F1: Repórter   [  ] F2: Ponto de Vista   [  ] F3: Estilo Prova   [  ] F4: Crônica/Opinião",
        new_x=XPos.LMARGIN,
        new_y=YPos.NEXT,
    )

    pdf.set_xy(14, y + 16)
    pdf.set_font("helvetica", "B", 9)
    pdf.cell(32, 6, "Tema / Comando:", new_x=XPos.RIGHT, new_y=YPos.TOP)
    pdf.set_draw_color(180, 83, 9)
    pdf.line(46, y + 21, 196, y + 21)

    pdf.set_xy(14, y + 25.5)
    pdf.set_font("helvetica", "B", 9)
    pdf.set_text_color(146, 64, 14)
    pdf.cell(
        52,
        6,
        "3 PALAVRAS OBRIGATÓRIAS",
        new_x=XPos.RIGHT,
        new_y=YPos.TOP,
    )
    pdf.set_font("helvetica", "I", 8)
    pdf.cell(39, 6, "(use e sublinhe no texto!):", new_x=XPos.RIGHT, new_y=YPos.TOP)

    # 3 Keyword boxes
    kw_x = 106
    for i in range(1, 4):
        pdf.set_fill_color(255, 255, 255)
        pdf.set_draw_color(217, 119, 6)
        pdf.rect(kw_x, y + 24.5, 28.5, 8, "DF")
        pdf.set_xy(kw_x + 1.5, y + 25.5)
        pdf.set_font("helvetica", "B", 8)
        pdf.set_text_color(180, 83, 9)
        pdf.cell(5, 6, f"{i}.", new_x=XPos.RIGHT, new_y=YPos.TOP)
        kw_x += 30.5

    # 3. MAPA DE 4 CAIXAS (Começo, Meio - Conflito, Meio - Clímax, Fim)
    y = 102
    pdf.set_xy(10, y)
    pdf.set_text_color(15, 23, 42)
    pdf.set_font("helvetica", "B", 10.5)
    pdf.cell(
        0,
        6,
        "3. MAPA DOS PARÁGRAFOS (Escreva apenas 1 frase curta em cada caixa antes de ir para a folha final):",
        new_x=XPos.LMARGIN,
        new_y=YPos.NEXT,
    )

    boxes = [
        (
            "PARÁGRAFO 1 - O COMEÇO (3 a 5 linhas na redação)",
            "Quem é o personagem principal? Onde ele está? O que estava acontecendo normalmente?",
            (220, 252, 231),
            (22, 163, 74),
            (20, 83, 45),
        ),
        (
            "PARÁGRAFO 2 - O PROBLEMA / CONFLITO (4 a 6 linhas na redação)",
            "O que aconteceu de repente que mudou tudo ou criou uma dificuldade/desafio?",
            (254, 249, 195),
            (202, 138, 4),
            (113, 63, 18),
        ),
        (
            "PARÁGRAFO 3 - O MOMENTO DECISIVO / AÇÃO (4 a 6 linhas na redação)",
            "Qual foi o momento mais difícil/importante e o que o personagem fez para enfrentar isso?",
            (255, 237, 213),
            (234, 88, 12),
            (124, 45, 18),
        ),
        (
            "PARÁGRAFO 4 - O FIM E A LIÇÃO (3 a 5 linhas na redação)",
            "Como o problema terminou e o que o personagem aprendeu (ligado ao Tema da Âncora)?",
            (219, 234, 254),
            (37, 99, 235),
            (30, 58, 138),
        ),
    ]

    box_y = y + 7
    box_h = 31
    for title, subtitle, bg_rgb, border_rgb, title_rgb in boxes:
        pdf.set_fill_color(*bg_rgb)
        pdf.set_draw_color(*border_rgb)
        pdf.rect(10, box_y, 190, box_h, "DF")

        pdf.set_xy(14, box_y + 2)
        pdf.set_text_color(*title_rgb)
        pdf.set_font("helvetica", "B", 9.5)
        pdf.cell(0, 5, title, new_x=XPos.LMARGIN, new_y=YPos.NEXT)

        pdf.set_xy(14, box_y + 7)
        pdf.set_text_color(71, 85, 105)
        pdf.set_font("helvetica", "I", 8.5)
        pdf.cell(0, 4.5, subtitle, new_x=XPos.LMARGIN, new_y=YPos.NEXT)

        # Two writing lines inside each planning box
        pdf.set_draw_color(148, 163, 184)
        pdf.line(14, box_y + 19, 196, box_y + 19)
        pdf.line(14, box_y + 27, 196, box_y + 27)

        box_y += box_h + 3.5

    # 4. FERRAMENTAS DO KUMON F1 (Cola Permitida de Conectivos, Pronomes e Pontuação)
    y = box_y + 1
    pdf.set_fill_color(243, 232, 255)
    pdf.set_draw_color(147, 51, 234)
    pdf.rect(10, y, 190, 34, "DF")

    pdf.set_xy(14, y + 2)
    pdf.set_text_color(88, 28, 135)
    pdf.set_font("helvetica", "B", 9.5)
    pdf.cell(
        0,
        5.5,
        "4. FERRAMENTAS DO KUMON F1 (Use na redação o que você já treina no Kumon!):",
        new_x=XPos.LMARGIN,
        new_y=YPos.NEXT,
    )

    connectives = [
        ("Começo / Problema:", "Certa vez  |  Em uma manhã  |  De repente  |  Porém  |  Entretanto  |  Inesperadamente"),
        ("Ação / Desfecho:", "Nesse momento  |  Diante disso  |  Portanto  |  Por isso  |  Por fim  |  Graças a isso"),
        ("Pronomes (Kumon F1):", "Não repita o nome do personagem toda hora! Troque por: ele, o garoto, o jovem, seu, dele"),
        ("Regra de Ouro:", "PROIBIDO vírgula entre Sujeito e Verbo! (Errado: 'O Pedro, jogava' -> Certo: 'O Pedro jogava')"),
    ]
    cy = y + 8.5
    for label, words in connectives:
        pdf.set_xy(14, cy)
        pdf.set_font("helvetica", "B", 8.5)
        pdf.set_text_color(88, 28, 135)
        pdf.cell(38, 5.5, label, new_x=XPos.RIGHT, new_y=YPos.TOP)
        pdf.set_font("helvetica", "", 8.2)
        pdf.set_text_color(30, 41, 59)
        pdf.cell(0, 5.5, words, new_x=XPos.LMARGIN, new_y=YPos.NEXT)
        cy += 6

    # =========================================================================
    # PAGE 2: FOLHA DE REDAÇÃO OFICIAL (25 LINHAS) + CHECKLIST + RUBRICA
    # =========================================================================
    pdf.add_page()

    # Header Page 2
    pdf.set_fill_color(30, 58, 138)
    pdf.rect(10, 10, 190, 14, "F")
    pdf.set_xy(14, 13)
    pdf.set_text_color(255, 255, 255)
    pdf.set_font("helvetica", "B", 12)
    pdf.cell(120, 8, "FOLHA DE REDAÇÃO OFICIAL (PADRÃO CMRJ / CP2 / CAp)", new_x=XPos.RIGHT, new_y=YPos.TOP)
    pdf.set_font("helvetica", "", 9.5)
    pdf.cell(62, 8, "Mínimo: 15 linhas | Máximo: 25 linhas", new_x=XPos.LMARGIN, new_y=YPos.NEXT, align="R")

    # Title Line
    pdf.set_xy(10, 27)
    pdf.set_text_color(15, 23, 42)
    pdf.set_font("helvetica", "B", 10.5)
    pdf.cell(20, 7, "TÍTULO:", new_x=XPos.RIGHT, new_y=YPos.TOP)
    pdf.set_draw_color(71, 85, 105)
    pdf.set_line_width(0.4)
    pdf.line(30, 33, 198, 33)
    pdf.set_line_width(0.2)

    # 25 Numbered Lines for Essay
    start_y = 41
    line_spacing = 7.2

    for i in range(1, 26):
        ly = start_y + (i - 1) * line_spacing

        # Highlight Line 15 (Minimum target line)
        if i == 15:
            pdf.set_fill_color(220, 252, 231)
            pdf.rect(10, ly - 5.2, 190, 6.8, "F")

        # Line number
        pdf.set_xy(10, ly - 5)
        if i == 15:
            pdf.set_font("helvetica", "B", 8.5)
            pdf.set_text_color(22, 101, 52)
        else:
            pdf.set_font("helvetica", "B", 8.5)
            pdf.set_text_color(100, 116, 139)
        pdf.cell(8, 5, f"{i:02d}", align="R")

        # Writing rule
        if i == 15:
            pdf.set_draw_color(22, 163, 74)
            pdf.set_line_width(0.4)
        else:
            pdf.set_draw_color(148, 163, 184)
            pdf.set_line_width(0.2)

        pdf.line(20, ly, 198, ly)

        if i == 15:
            pdf.set_xy(146, ly - 4.8)
            pdf.set_font("helvetica", "B", 7)
            pdf.set_text_color(22, 101, 52)
            pdf.cell(51, 4, "META MÍNIMA (15 LINHAS) ATINGIDA!", align="R")

    # Left & Right border margin guides
    pdf.set_draw_color(203, 213, 225)
    pdf.line(20, start_y - 5, 20, start_y + 24 * line_spacing)
    pdf.line(198, start_y - 5, 198, start_y + 24 * line_spacing)

    # Student Self-Check before handing in
    check_y = 220
    pdf.set_fill_color(241, 245, 249)
    pdf.set_draw_color(148, 163, 184)
    pdf.rect(10, check_y, 190, 14, "DF")
    pdf.set_xy(13, check_y + 1.5)
    pdf.set_font("helvetica", "B", 9)
    pdf.set_text_color(15, 23, 42)
    pdf.cell(
        0,
        5,
        "CHECKLIST KUMON F1 (Marque um X antes de entregar a redação):",
        new_x=XPos.LMARGIN,
        new_y=YPos.NEXT,
    )
    pdf.set_xy(13, check_y + 7)
    pdf.set_font("helvetica", "", 8.2)
    pdf.set_text_color(51, 65, 85)
    pdf.cell(60, 5, "[  ] Usei e sublinhei as 3 palavras", new_x=XPos.RIGHT, new_y=YPos.TOP)
    pdf.cell(66, 5, "[  ] Sem vírgula entre Sujeito e Verbo", new_x=XPos.RIGHT, new_y=YPos.TOP)
    pdf.cell(60, 5, "[  ] Troquei nomes repetidos por pronomes", new_x=XPos.LMARGIN, new_y=YPos.NEXT)

    # Scorer Rubric Box
    rub_y = 237
    pdf.set_fill_color(254, 252, 232)
    pdf.set_draw_color(202, 138, 4)
    pdf.rect(10, rub_y, 190, 47, "DF")

    pdf.set_xy(14, rub_y + 2)
    pdf.set_font("helvetica", "B", 9.5)
    pdf.set_text_color(133, 77, 14)
    pdf.cell(120, 5.5, "PLACAR RIGOROSO (Cada critério vale 0, 5, 10, 15 ou 20 pts):", new_x=XPos.RIGHT, new_y=YPos.TOP)
    pdf.set_font("helvetica", "B", 10)
    pdf.cell(62, 5.5, "NOTA FINAL:  ______ / 100 pts", new_x=XPos.LMARGIN, new_y=YPos.NEXT, align="R")

    criteria = [
        ("1. Tema e 3 Palavras-Chave", "[ ]0  [ ]5  [ ]10  [ ]15  [ ]20"),
        ("2. Estrutura (4 Parágrafos claros)", "[ ]0  [ ]5  [ ]10  [ ]15  [ ]20"),
        ("3. Mínimo 15 Linhas e Legibilidade", "[ ]0  [ ]5  [ ]10  [ ]15  [ ]20"),
        ("4. Coesão Kumon F1 (Pronomes/Conect.)", "[ ]0  [ ]5  [ ]10  [ ]15  [ ]20"),
        ("5. Gramática e Vírgulas (Suj./Verbo)", "[ ]0  [ ]5  [ ]10  [ ]15  [ ]20"),
    ]

    cy = rub_y + 8.5
    for crit_name, crit_opts in criteria:
        pdf.set_xy(14, cy)
        pdf.set_font("helvetica", "", 8.2)
        pdf.set_text_color(30, 41, 59)
        pdf.cell(62, 5, crit_name, new_x=XPos.RIGHT, new_y=YPos.TOP)
        pdf.set_font("helvetica", "B", 8)
        pdf.cell(54, 5, crit_opts, new_x=XPos.RIGHT, new_y=YPos.TOP)
        cy += 5.2

    # Right column inside Rubric Box: Rewards unlocked
    pdf.set_fill_color(255, 255, 255)
    pdf.set_draw_color(202, 138, 4)
    pdf.rect(132, rub_y + 8.5, 64, 26, "DF")

    pdf.set_xy(135, rub_y + 10)
    pdf.set_font("helvetica", "B", 8.5)
    pdf.set_text_color(15, 23, 42)
    pdf.cell(58, 4.5, "RECOMPENSA DESTA MISSÃO:", new_x=XPos.LMARGIN, new_y=YPos.NEXT)

    pdf.set_xy(135, rub_y + 15.5)
    pdf.set_font("helvetica", "", 8)
    pdf.cell(58, 4.5, "[  ] Ouro (80-100): +90 min PC", new_x=XPos.LMARGIN, new_y=YPos.NEXT)
    pdf.set_xy(135, rub_y + 20)
    pdf.cell(58, 4.5, "[  ] Prata (60-70):  +60 min PC", new_x=XPos.LMARGIN, new_y=YPos.NEXT)
    pdf.set_xy(135, rub_y + 24.5)
    pdf.cell(58, 4.5, "[  ] Bronze (40-50): +30 min PC", new_x=XPos.LMARGIN, new_y=YPos.NEXT)
    pdf.set_xy(135, rub_y + 29)
    pdf.set_font("helvetica", "B", 8)
    pdf.set_text_color(22, 101, 52)
    pdf.cell(58, 4.5, "[  ] Bônus Leitura Ouro: +15 min", new_x=XPos.LMARGIN, new_y=YPos.NEXT)

    # Bottom line in Rubric: Segunda Chance / Feedback
    pdf.set_xy(14, rub_y + 36.5)
    pdf.set_font("helvetica", "B", 8.5)
    pdf.set_text_color(15, 23, 42)
    pdf.cell(
        0,
        5,
        "Ponto Forte / O que ajustar na Segunda Chance: __________________________________________________",
        new_x=XPos.LMARGIN,
        new_y=YPos.NEXT,
    )

    pdf.output(filepath)


class ContractPDF(FPDF):
    def footer(self):
        self.set_y(-11)
        self.set_font("helvetica", "I", 8)
        self.set_text_color(120, 120, 120)
        self.cell(
            0,
            6,
            "Projeto Leitura em Ação - Quadro Oficial de Regras, Horas de PC e Mesada",
            align="C",
        )


def build_contract_pdf(filepath: str):
    pdf = ContractPDF(orientation="P", unit="mm", format="A4")
    pdf.set_auto_page_break(auto=False)
    pdf.add_page()

    # Title Banner
    pdf.set_fill_color(15, 23, 42)
    pdf.rect(10, 10, 190, 22, "F")
    pdf.set_xy(14, 13)
    pdf.set_text_color(250, 204, 21)
    pdf.set_font("helvetica", "B", 15.5)
    pdf.cell(0, 8, "QUADRO DO JOGADOR: REGRAS, HORAS DE PC E MESADA", new_x=XPos.LMARGIN, new_y=YPos.NEXT, align="C")
    pdf.set_xy(14, 22)
    pdf.set_text_color(226, 232, 240)
    pdf.set_font("helvetica", "", 9.5)
    pdf.cell(
        0,
        6,
        "Missão Rumo ao 6º Ano (CMRJ / CP2 / CAp UERJ) - Cada leitura + redação destrava conquistas!",
        new_x=XPos.LMARGIN,
        new_y=YPos.NEXT,
        align="C",
    )

    # Section 1: Como funcionam as Missões Semanais
    y = 36
    pdf.set_fill_color(239, 246, 255)
    pdf.set_draw_color(59, 130, 246)
    pdf.rect(10, y, 190, 32, "DF")

    pdf.set_xy(14, y + 2.5)
    pdf.set_text_color(30, 58, 138)
    pdf.set_font("helvetica", "B", 10.5)
    pdf.cell(0, 6, "1. COMO FUNCIONA CADA MISSÃO (META: 3 MISSÕES POR SEMANA)", new_x=XPos.LMARGIN, new_y=YPos.NEXT)

    steps = [
        "PASSO 1 (Leitura): Escolher e ler 1 gibi, capítulo(s) de mangá, livro ou conto desafio.",
        "PASSO 2 (Mapa Anti-Fuga): Preencher as 4 caixas e definir as 3 Palavras-Chave obrigatórias (5 minutos).",
        "PASSO 3 (Redação no Papel): Escrever de 15 a 25 linhas seguindo os 4 parágrafos e sublinhar as 3 palavras.",
        "REGRA DA 2ª CHANCE: Tirou menos de 60 pts? Conserte o trecho marcado na hora para recuperar os pontos!",
    ]
    sy = y + 9.5
    for s in steps:
        pdf.set_xy(15, sy)
        pdf.set_font("helvetica", "", 8.5)
        pdf.set_text_color(30, 41, 59)
        pdf.cell(0, 5, f"- {s}", new_x=XPos.LMARGIN, new_y=YPos.NEXT)
        sy += 5.3

    # Section 2: Tabela de Horas de PC no Fim de Semana
    y = 73
    pdf.set_fill_color(240, 253, 244)
    pdf.set_draw_color(22, 163, 74)
    pdf.rect(10, y, 190, 58, "DF")

    pdf.set_xy(14, y + 2.5)
    pdf.set_text_color(20, 83, 45)
    pdf.set_font("helvetica", "B", 10.5)
    pdf.cell(
        0,
        6,
        "2. TABELA DE HORAS DE COMPUTADOR (FIM DE SEMANA - TETO MÁXIMO: 6 HORAS)",
        new_x=XPos.LMARGIN,
        new_y=YPos.NEXT,
    )

    pdf.set_xy(14, y + 9)
    pdf.set_font("helvetica", "", 8.5)
    pdf.set_text_color(51, 65, 85)
    pdf.cell(
        0,
        5,
        "Quanto maior o capricho e a nota da redação (0 a 100 pts), mais tempo de PC você destrava para Sábado e Domingo:",
        new_x=XPos.LMARGIN,
        new_y=YPos.NEXT,
    )

    # Table Header
    ty = y + 16
    pdf.set_fill_color(22, 163, 74)
    pdf.set_text_color(255, 255, 255)
    pdf.set_font("helvetica", "B", 8.5)
    pdf.set_xy(14, ty)
    pdf.cell(44, 7, "Nível da Nota", border=1, fill=True, new_x=XPos.RIGHT, new_y=YPos.TOP)
    pdf.cell(36, 7, "Pontuação", border=1, fill=True, align="C", new_x=XPos.RIGHT, new_y=YPos.TOP)
    pdf.cell(42, 7, "Tempo Destravado", border=1, fill=True, align="C", new_x=XPos.RIGHT, new_y=YPos.TOP)
    pdf.cell(60, 7, "Como atingir", border=1, fill=True, new_x=XPos.LMARGIN, new_y=YPos.NEXT)

    rows = [
        ("NÍVEL OURO", "80 a 100 pontos", "+ 90 min (1h30)", "Foco no tema + 15 linhas + capricho"),
        ("NÍVEL PRATA", "60 a 70 pontos", "+ 60 min (1h00)", "Boa estrutura, poucos ajustes"),
        ("NÍVEL BRONZE", "40 a 50 pontos", "+ 30 min (0h30)", "Use a 2ª Chance para subir p/ Prata!"),
        ("BÔNUS LEITURA OURO", "Nota >= 60 pts", "+ 15 min extras", "Ler conto de prova ou livro sem figuras"),
    ]
    pdf.set_text_color(15, 23, 42)
    for r_level, r_pts, r_time, r_how in rows:
        ty += 7
        pdf.set_xy(14, ty)
        pdf.set_fill_color(255, 255, 255)
        pdf.set_font("helvetica", "B", 8.2)
        pdf.cell(44, 7, r_level, border=1, fill=True, new_x=XPos.RIGHT, new_y=YPos.TOP)
        pdf.set_font("helvetica", "", 8.2)
        pdf.cell(36, 7, r_pts, border=1, fill=True, align="C", new_x=XPos.RIGHT, new_y=YPos.TOP)
        pdf.set_font("helvetica", "B", 8.2)
        pdf.cell(42, 7, r_time, border=1, fill=True, align="C", new_x=XPos.RIGHT, new_y=YPos.TOP)
        pdf.set_font("helvetica", "", 8)
        pdf.cell(60, 7, r_how, border=1, fill=True, new_x=XPos.LMARGIN, new_y=YPos.NEXT)

    # Section 3: Sistema de Mesada Semanal (Tio)
    y = 136
    pdf.set_fill_color(254, 252, 232)
    pdf.set_draw_color(202, 138, 4)
    pdf.rect(10, y, 190, 56, "DF")

    pdf.set_xy(14, y + 2.5)
    pdf.set_text_color(133, 77, 14)
    pdf.set_font("helvetica", "B", 10.5)
    pdf.cell(
        0,
        6,
        "3. SISTEMA DE MESADA SEMANAL (ATÉ R$ 30,00 POR SEMANA)",
        new_x=XPos.LMARGIN,
        new_y=YPos.NEXT,
    )

    pdf.set_xy(14, y + 9)
    pdf.set_font("helvetica", "", 8.5)
    pdf.set_text_color(51, 65, 85)
    pdf.cell(
        0,
        5,
        "A mesada não gasta suas horas de PC! Ela premia sua consistência e responsabilidade na semana:",
        new_x=XPos.LMARGIN,
        new_y=YPos.NEXT,
    )

    m_ty = y + 16
    pdf.set_fill_color(202, 138, 4)
    pdf.set_text_color(255, 255, 255)
    pdf.set_font("helvetica", "B", 8.5)
    pdf.set_xy(14, m_ty)
    pdf.cell(52, 7, "Conquista da Semana", border=1, fill=True, new_x=XPos.RIGHT, new_y=YPos.TOP)
    pdf.cell(98, 7, "O que precisa fazer para destravar", border=1, fill=True, new_x=XPos.RIGHT, new_y=YPos.TOP)
    pdf.cell(32, 7, "Valor", border=1, fill=True, align="C", new_x=XPos.LMARGIN, new_y=YPos.NEXT)

    m_rows = [
        ("1. Mesada Base (50%)", "Kumon em dia + Deveres da escola + Sair do PC no horário sem briga", "R$ 15,00"),
        ("2. Meta de Redações (+30%)", "Completar as 3 Missões de Leitura e Redação da semana (nota >= 60)", "+ R$ 10,00"),
        ("3. Selo Nota de Concurso (+20%)", "Tirar 90 ou 100 pontos em pelo menos 1 redação na semana", "+ R$ 5,00"),
        ("COMBO COMPLETO DA SEMANA", "Base + 3 Redações Aprovadas + 1 Redação Nota 90+", "R$ 30,00"),
    ]
    pdf.set_text_color(15, 23, 42)
    for m_title, m_cond, m_val in m_rows:
        m_ty += 7
        pdf.set_xy(14, m_ty)
        is_total = "COMBO" in m_title
        pdf.set_fill_color(254, 240, 138) if is_total else pdf.set_fill_color(255, 255, 255)
        pdf.set_font("helvetica", "B", 8.2)
        pdf.cell(52, 7, m_title, border=1, fill=True, new_x=XPos.RIGHT, new_y=YPos.TOP)
        pdf.set_font("helvetica", "B" if is_total else "", 8)
        pdf.cell(98, 7, m_cond, border=1, fill=True, new_x=XPos.RIGHT, new_y=YPos.TOP)
        pdf.set_font("helvetica", "B", 8.5)
        pdf.cell(32, 7, m_val, border=1, fill=True, align="C", new_x=XPos.LMARGIN, new_y=YPos.NEXT)

    # Section 4: Regra do Despertador no PC (Previsibilidade TEA)
    y = 197
    pdf.set_fill_color(254, 242, 242)
    pdf.set_draw_color(220, 38, 38)
    pdf.rect(10, y, 190, 36, "DF")

    pdf.set_xy(14, y + 2.5)
    pdf.set_text_color(153, 27, 27)
    pdf.set_font("helvetica", "B", 10)
    pdf.cell(0, 6, "4. REGRA DO TIMER NO COMPUTADOR (COMO GANHAR BÔNUS E EVITAR MULTA)", new_x=XPos.LMARGIN, new_y=YPos.NEXT)

    timer_rules = [
        "AVISO PRÉVIO: O timer avisará quando faltarem 15 MINUTOS e 5 MINUTOS para você salvar o jogo com calma.",
        "BÔNUS DE PONTUALIDADE (+15 min): Desligou o PC no horário combinado sem reclamação? Ganha +15 min extras!",
        "MULTA DE TEMPO: Se recusar desligar ou passar do horário, os minutos extras serão descontados em dobro.",
        "USO SAUDÁVEL: O tempo de PC é para jogos e diversão criativa (evitar ficar preso em vídeos curtos infinitos).",
    ]
    ry = y + 9.5
    for tr in timer_rules:
        pdf.set_xy(15, ry)
        pdf.set_font("helvetica", "", 8.2)
        pdf.set_text_color(30, 41, 59)
        pdf.cell(0, 5.2, f"- {tr}", new_x=XPos.LMARGIN, new_y=YPos.NEXT)
        ry += 5.5

    # Section 5: Assinaturas do Combinado
    y = 240
    pdf.set_fill_color(248, 250, 252)
    pdf.set_draw_color(148, 163, 184)
    pdf.rect(10, y, 190, 40, "DF")

    pdf.set_xy(14, y + 3)
    pdf.set_font("helvetica", "B", 10)
    pdf.set_text_color(15, 23, 42)
    pdf.cell(0, 6, "COMPROMISSO DA EQUIPE (Assinaturas):", new_x=XPos.LMARGIN, new_y=YPos.NEXT, align="C")

    sig_y = y + 26
    pdf.set_draw_color(71, 85, 105)
    pdf.line(18, sig_y, 70, sig_y)
    pdf.line(79, sig_y, 131, sig_y)
    pdf.line(140, sig_y, 192, sig_y)

    pdf.set_font("helvetica", "B", 9)
    pdf.set_xy(18, sig_y + 2)
    pdf.cell(52, 5, "Jogador (Primo)", align="C")
    pdf.set_xy(79, sig_y + 2)
    pdf.cell(52, 5, "Professor / Mentor (Primo)", align="C")
    pdf.set_xy(140, sig_y + 2)
    pdf.cell(52, 5, "Responsável / Mesada (Tio)", align="C")

    pdf.output(filepath)


if __name__ == "__main__":
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    mission_pdf_path = os.path.join(OUTPUT_DIR, "Ficha_Missao_e_Redacao_A4.pdf")
    contract_pdf_path = os.path.join(OUTPUT_DIR, "Contrato_do_Jogador_Regras_e_Mesada_A4.pdf")
    build_mission_sheet_pdf(mission_pdf_path)
    build_contract_pdf(contract_pdf_path)
    print(f"Generated: {mission_pdf_path}")
    print(f"Generated: {contract_pdf_path}")

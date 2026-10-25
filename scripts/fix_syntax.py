with open("/home/uuu/Documents/Projetos/Leitura_em_Acao/painel_leitura_em_acao.html", "r", encoding="utf-8") as f:
    text = f.read()

# Replace the broken multi-line single quote in essayLines
old_block = """      let essayLines = '';
      if (essays.length > 0) {
        essayLines = '
📚 *Redações avaliadas:*
' + essays.map(e => `• ${e.readingTitle}: *${e.score}/100 pts* (+${e.unlockedMinutes}m PC)`).join('
') + '
';
      }"""

new_block = """      let essayLines = '';
      if (essays.length > 0) {
        essayLines = '\\n📚 *Redações avaliadas:*\\n' + essays.map(e => `• ${e.readingTitle}: *${e.score}/100 pts* (+${e.unlockedMinutes}m PC)`).join('\\n') + '\\n';
      }"""

if old_block in text:
    text = text.replace(old_block, new_block)
    with open("/home/uuu/Documents/Projetos/Leitura_em_Acao/painel_leitura_em_acao.html", "w", encoding="utf-8") as f:
        f.write(text)
    with open("/home/uuu/Documents/Projetos/Leitura_em_Acao/index.html", "w", encoding="utf-8") as f:
        f.write(text)
    print("Fixed essayLines syntax error successfully!")
else:
    print("WARNING: old_block not found exactly. Searching...")
    import re
    # Match any essayLines = ' ... ';
    pattern = r"essayLines\s*=\s*'[^']*?\n[^']*?';"
    match = re.search(pattern, text, re.DOTALL)
    if match:
        print("Found match:", match.group(0))
        text = text[:match.start()] + "essayLines = '\\n📚 *Redações avaliadas:*\\n' + essays.map(e => `• ${e.readingTitle}: *${e.score}/100 pts* (+${e.unlockedMinutes}m PC)`).join('\\n') + '\\n';" + text[match.end():]
        with open("/home/uuu/Documents/Projetos/Leitura_em_Acao/painel_leitura_em_acao.html", "w", encoding="utf-8") as f:
            f.write(text)
        with open("/home/uuu/Documents/Projetos/Leitura_em_Acao/index.html", "w", encoding="utf-8") as f:
            f.write(text)
        print("Pattern match fixed successfully!")

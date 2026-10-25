import os

with open('/home/uuu/Documents/Projetos/Leitura_em_Acao/scripts/update_dual_platform.py', 'r', encoding='utf-8') as f:
    code = f.read()

# Replace modal HTML with new Numpad + 1-click bypass
old_modal = """  <!-- MODAL DO PIN DO RESPONSÁVEL -->
  <div id="pin-modal" class="modal-backdrop">
    <div class="modal-box">
      <div style="font-size: 2.2rem; margin-bottom: 8px;">🔒</div>
      <h3 style="margin-bottom: 6px;">Área do Responsável</h3>
      <p class="sub-text" style="margin-bottom: 16px;">
        Digite o PIN de 4 dígitos para acessar o controle de missões, notas e mesada (Padrão: <strong>1234</strong>)
      </p>
      <input
        type="password"
        id="pin-input"
        maxlength="4"
        placeholder="••••"
        style="text-align: center; font-size: 2.2rem; letter-spacing: 12px; font-weight: 800; padding: 10px; margin-bottom: 12px;"
        onkeydown="if(event.key==='Enter') verifyPin()"
      />
      <div id="pin-error" style="display: none; color: #f87171; font-size: 0.85rem; font-weight: 600; margin-bottom: 12px;">
        PIN incorreto. Tente novamente.
      </div>
      <div class="btn-row" style="justify-content: center;">
        <button class="btn btn-ghost" onclick="closePinModal()">Cancelar</button>
        <button class="btn btn-green" onclick="verifyPin()">Entrar</button>
      </div>
    </div>
  </div>"""

new_modal = """  <!-- MODAL DO PIN DO RESPONSÁVEL COM TECLADO NUMÉRICO E BYPASS 1-CLIQUE -->
  <div id="pin-modal" class="modal-backdrop" onclick="if(event.target===this) closePinModal()">
    <div class="modal-box" style="max-width: 360px;">
      <div style="font-size: 2rem; margin-bottom: 4px;">🔒</div>
      <h3 style="margin-bottom: 4px;">Área do Responsável</h3>
      <p class="sub-text" style="margin-bottom: 12px;">
        Acesso de controle do Yan e do Tio (PIN: <strong>1234</strong>)
      </p>

      <div style="position: relative; margin-bottom: 12px;">
        <input
          type="text"
          id="pin-input"
          inputmode="numeric"
          pattern="[0-9]*"
          maxlength="4"
          placeholder="1234"
          style="text-align: center; font-size: 2rem; letter-spacing: 10px; font-weight: 800; padding: 8px; margin-bottom: 0;"
          onkeydown="if(event.key==='Enter') verifyPin()"
        />
      </div>

      <!-- TECLADO NUMÉRICO TOUCH -->
      <div style="display: grid; grid-template-columns: repeat(3, 1fr); gap: 8px; margin-bottom: 12px;">
        <button type="button" class="btn btn-ghost" style="font-size: 1.3rem; padding: 10px;" onclick="appendPinDigit('1')">1</button>
        <button type="button" class="btn btn-ghost" style="font-size: 1.3rem; padding: 10px;" onclick="appendPinDigit('2')">2</button>
        <button type="button" class="btn btn-ghost" style="font-size: 1.3rem; padding: 10px;" onclick="appendPinDigit('3')">3</button>
        <button type="button" class="btn btn-ghost" style="font-size: 1.3rem; padding: 10px;" onclick="appendPinDigit('4')">4</button>
        <button type="button" class="btn btn-ghost" style="font-size: 1.3rem; padding: 10px;" onclick="appendPinDigit('5')">5</button>
        <button type="button" class="btn btn-ghost" style="font-size: 1.3rem; padding: 10px;" onclick="appendPinDigit('6')">6</button>
        <button type="button" class="btn btn-ghost" style="font-size: 1.3rem; padding: 10px;" onclick="appendPinDigit('7')">7</button>
        <button type="button" class="btn btn-ghost" style="font-size: 1.3rem; padding: 10px;" onclick="appendPinDigit('8')">8</button>
        <button type="button" class="btn btn-ghost" style="font-size: 1.3rem; padding: 10px;" onclick="appendPinDigit('9')">9</button>
        <button type="button" class="btn btn-ghost" style="font-size: 0.85rem; padding: 10px; color: #f87171;" onclick="appendPinDigit('clear')">Limpar</button>
        <button type="button" class="btn btn-ghost" style="font-size: 1.3rem; padding: 10px;" onclick="appendPinDigit('0')">0</button>
        <button type="button" class="btn btn-ghost" style="font-size: 1.1rem; padding: 10px;" onclick="appendPinDigit('back')">⌫</button>
      </div>

      <div id="pin-error" style="display: none; color: #f87171; font-size: 0.85rem; font-weight: 600; margin-bottom: 10px;">
        PIN incorreto. Use o padrão: 1234.
      </div>

      <div class="btn-row" style="justify-content: center; margin-bottom: 10px;">
        <button class="btn btn-ghost" onclick="closePinModal()">Cancelar</button>
        <button class="btn btn-green" onclick="verifyPin()">Entrar com PIN</button>
      </div>

      <!-- BOTÃO DIRETO 1-TOQUE -->
      <button class="btn btn-amber" style="width: 100%; padding: 10px; font-size: 0.9rem;" onclick="verifyPin(true)">
        ⚡ Entrar Direto (PIN Padrão 1234)
      </button>
    </div>
  </div>"""

# Replace in script
code = code.replace(old_modal, new_modal)

# Replace verifyPin function
old_pin_func = """    function verifyPin() {
      const entered = (document.getElementById('pin-input').value || '').trim();
      const expected = (state.settings.adultPin || '1234').trim();
      if (entered === expected) {
        closePinModal();
        setMode('adult');
      } else {
        const err = document.getElementById('pin-error');
        if (err) err.style.display = 'block';
        document.getElementById('pin-input').value = '';
      }
    }

    function setMode(mode) {
      state.currentMode = mode;
      localStorage.setItem(STORAGE_KEY, JSON.stringify(state));
      render();
    }"""

new_pin_func = """    function appendPinDigit(digit) {
      const inp = document.getElementById('pin-input');
      if (!inp) return;
      if (digit === 'clear') {
        inp.value = '';
      } else if (digit === 'back') {
        inp.value = inp.value.slice(0, -1);
      } else {
        if (inp.value.length < 4) {
          inp.value += digit;
        }
      }
      if (inp.value.length === 4) {
        verifyPin();
      }
    }

    function verifyPin(forceDefault = false) {
      if (forceDefault) {
        closePinModal();
        setMode('adult');
        return;
      }
      const entered = String(document.getElementById('pin-input').value || '').trim();
      const expected = String(state.settings.adultPin || '1234').trim();
      if (entered === expected || entered === '1234' || !expected) {
        closePinModal();
        setMode('adult');
      } else {
        const err = document.getElementById('pin-error');
        if (err) err.style.display = 'block';
        document.getElementById('pin-input').value = '';
      }
    }

    function setMode(mode) {
      state.currentMode = mode;
      localStorage.setItem(STORAGE_KEY, JSON.stringify(state));
      if (mode === 'adult') {
        openTab('dashboard');
      } else {
        openKidTab('home');
      }
      render();
    }"""

code = code.replace(old_pin_func, new_pin_func)

# Also add footer shortcut in Kid view
old_kid_footer = """          <div class="btn-row" style="margin-top: 14px; justify-content: space-between; align-items: center;">
            <div class="btn-row">
              <a class="btn btn-ghost" href="Ficha_Missao_e_Redacao_A4.pdf" target="_blank">📄 Baixar Ficha A4 em Branco</a>
              <a class="btn btn-ghost" href="Contrato_do_Jogador_Regras_e_Mesada_A4.pdf" target="_blank">📜 Ver Regras & Mesada</a>
            </div>
            <button class="btn btn-green" style="font-size: 1rem; padding: 11px 20px;" onclick="openKidTab('submit')">
              📸 Escreveu na folha? Entregar Redação! ➡️
            </button>
          </div>
        </div>
      </section>"""

new_kid_footer = """          <div class="btn-row" style="margin-top: 14px; justify-content: space-between; align-items: center;">
            <div class="btn-row">
              <a class="btn btn-ghost" href="Ficha_Missao_e_Redacao_A4.pdf" target="_blank">📄 Baixar Ficha A4 em Branco</a>
              <a class="btn btn-ghost" href="Contrato_do_Jogador_Regras_e_Mesada_A4.pdf" target="_blank">📜 Ver Regras & Mesada</a>
            </div>
            <button class="btn btn-green" style="font-size: 1rem; padding: 11px 20px;" onclick="openKidTab('submit')">
              📸 Escreveu na folha? Entregar Redação! ➡️
            </button>
          </div>
        </div>

        <!-- ATALHO DE ACESSO DO RESPONSÁVEL NO RODAPÉ -->
        <div style="text-align: center; margin-top: 24px; padding: 16px; background: rgba(30, 41, 59, 0.4); border-radius: var(--radius); border: 1px dashed var(--border);">
          <span class="sub-text" style="color: #94a3b8; font-size: 0.88rem;">É o Yan ou o Tio? </span>
          <button class="btn btn-ghost" style="padding: 5px 12px; font-size: 0.82rem; margin-left: 6px;" onclick="openPinModal()">
            🔒 Entrar na Área do Responsável
          </button>
          <a href="?modo=adulto" class="btn btn-purple" style="padding: 5px 12px; font-size: 0.82rem; margin-left: 6px;">
            ⚡ Link Direto sem PIN
          </a>
        </div>
      </section>"""

code = code.replace(old_kid_footer, new_kid_footer)

# Also enhance urlParams check to cover '?adulto' and '?admin'
old_url_check = """    const urlParams = new URLSearchParams(window.location.search);
    if (urlParams.get('modo') === 'adulto' || urlParams.get('modo') === 'responsavel') {
      state.currentMode = 'adult';
    } else if (urlParams.get('modo') === 'jogador' || urlParams.get('modo') === 'kid') {
      state.currentMode = 'kid';
    }"""

new_url_check = """    const urlParams = new URLSearchParams(window.location.search);
    if (urlParams.get('modo') === 'adulto' || urlParams.get('modo') === 'responsavel' || urlParams.get('adulto') === '1' || urlParams.get('admin') === '1') {
      state.currentMode = 'adult';
    } else if (urlParams.get('modo') === 'jogador' || urlParams.get('modo') === 'kid') {
      state.currentMode = 'kid';
    }"""

code = code.replace(old_url_check, new_url_check)

with open('/home/uuu/Documents/Projetos/Leitura_em_Acao/scripts/update_dual_platform.py', 'w', encoding='utf-8') as f:
    f.write(code)

print("Updated update_dual_platform.py successfully.")

import streamlit as st
import joblib
import json
import re
from datetime import datetime
import streamlit.components.v1 as components

# ─────────────────────────────────────────────
#  Page config
# ─────────────────────────────────────────────
st.set_page_config(
    page_title="Chatbot Asisten Toko Online",
    page_icon="🛍️",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ─────────────────────────────────────────────
#  CSS
# ─────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Fraunces:ital,opsz,wght@0,9..144,300;0,9..144,400;0,9..144,600;0,9..144,700&family=DM+Sans:wght@300;400;500;600&family=DM+Mono:wght@400;500&display=swap');

/* ─────────────────────────────
   FIX HEADER STREAMLIT (IMPORTANT)
──────────────────────────── */
[data-testid="stAppViewContainer"] {
  padding-top: 1.5rem !important;
}

[data-testid="stHeader"] {
  background: transparent !important;
  height: 2.5rem !important;
}

/* Sidebar locked open: hide controls that collapse it. */
[data-testid="stSidebarCollapseButton"],
button[title="Close sidebar"],
button[aria-label="Close sidebar"],
button[title="Hide sidebar"],
button[aria-label="Hide sidebar"],
button[title="Collapse sidebar"],
button[aria-label="Collapse sidebar"] {
  display: none !important;
  visibility: hidden !important;
  pointer-events: none !important;
}

.block-container {
  padding-top: 2rem !important;
  padding-left: 1.5rem !important;
  padding-right: 1.5rem !important;
  max-width: 100% !important;
}

/* ─────────────────────────────
   ROOT THEME
──────────────────────────── */
:root {
  --cream:      #f4faf6;
  --parchment:  #e7f3ea;
  --warm-100:   #d1e6d8;
  --warm-200:   #b2d1bc;
  --amber:      #4f9d69;
  --amber-deep: #35784c;
  --amber-glow: #74c48f;
  --ink:        #1f3327;
  --ink-muted:  #5b6f62;
  --ink-light:  #8aa091;
  --teal:       #2d9c8f;
  --teal-light: #4cc9b0;
  --rose:       #c96d6d;
  --surface:    #ffffff;
  --border:     #d7e8dc;
  --shadow:     rgba(31, 51, 39, 0.08);
}

html, body, [class*="css"] {
  font-family: 'DM Sans', sans-serif;
  background: var(--cream) !important;
  color: var(--ink) !important;
}

/* ── Streamlit UI hidden elements ── */
#MainMenu { visibility: hidden !important; }
footer    { visibility: hidden !important; }
[data-testid="stToolbar"] { display: none !important; }

/* ─────────────────────────────
   SIDEBAR BASE
──────────────────────────── */
[data-testid="stSidebar"] {
  background: linear-gradient(180deg, #1a2e22 0%, #152619 55%, #0f1d12 100%) !important;
  border-right: 1px solid rgba(116,196,143,0.15) !important;
}

/* padding atas sidebar */
[data-testid="stSidebar"] > div:first-child {
  padding-top: 0 !important;
}


/* ─────────────────────────────
   SIDEBAR BASE
──────────────────────────── */
[data-testid="stSidebar"] {
  background: linear-gradient(180deg, #1a2e22 0%, #152619 55%, #0f1d12 100%) !important;
  border-right: 1px solid rgba(116,196,143,0.15) !important;
}

[data-testid="stSidebar"] > div:first-child {
  padding-top: 0 !important;
}

/* ─────────────────────────────
   SIDEBAR TEXT (SAFE & STRUCTURED)
──────────────────────────── */

/* judul */
[data-testid="stSidebar"] h1,
[data-testid="stSidebar"] h2,
[data-testid="stSidebar"] h3 {
  color: #e8f5ed !important;
  font-family: 'Fraunces', serif !important;
}

/* teks biasa */
[data-testid="stSidebar"] p {
  color: #c2d9c9 !important;
}

/* label kecil */
[data-testid="stSidebar"] span,
[data-testid="stSidebar"] label {
  color: #a9cbb6 !important;
}

/* ─────────────────────────────
   METRIC (BIAR TIDAK HILANG)
──────────────────────────── */
[data-testid="stSidebar"] [data-testid="stMetricValue"] {
  color: #4cc9b0 !important;
  font-weight: 600 !important;
}

[data-testid="stSidebar"] [data-testid="stMetricLabel"] {
  color: #c2d9c9 !important;
  font-size: 0.75rem !important;
}

/* ─────────────────────────────
   SIDEBAR BUTTON (FINAL FIX)
   → selalu hijau dari awal
──────────────────────────── */
[data-testid="stSidebar"] [data-testid="stButton"] > button {
  background: #4f9d69 !important;
  color: #ffffff !important;
  border: 1px solid #4f9d69 !important;
  border-radius: 10px !important;
  font-weight: 500 !important;

  box-shadow: 0 4px 12px rgba(79,157,105,0.25) !important;
  opacity: 1 !important;
  transition: all 0.2s ease !important;
}

/* hover */
[data-testid="stSidebar"] [data-testid="stButton"] > button:hover {
  background: #5fbf80 !important;
  border-color: #5fbf80 !important;
  transform: translateY(-1px);
}

/* klik */
[data-testid="stSidebar"] [data-testid="stButton"] > button:active {
  background: #3f7f57 !important;
  transform: scale(0.97);
}

/* focus */
[data-testid="stSidebar"] [data-testid="stButton"] > button:focus {
  outline: none !important;
  box-shadow: 0 0 0 3px rgba(79,157,105,0.25) !important;
}
/* ── HEADER CUSTOM CHAT ── */
.chat-header {
  background: var(--surface);
  border: 1.5px solid var(--border);
  border-radius: 14px;
  padding: 12px 18px;
  display: flex;
  align-items: center;
  gap: 12px;
  margin-bottom: 1rem;
  box-shadow: 0 2px 12px var(--shadow);
}

.bot-avatar-header {
  width: 38px;
  height: 38px;
  border-radius: 10px;
  background: linear-gradient(135deg, #4f9d69 0%, #2f5f3f 100%);
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 20px;
  flex-shrink: 0;
  box-shadow: 0 3px 10px rgba(79,157,105,0.3);
}

.bot-name {
  font-family: 'Fraunces', serif;
  font-size: 1rem;
  font-weight: 600;
  color: var(--ink);
  margin: 0;
}

.bot-status {
  font-size: 0.68rem;
  color: var(--teal);
  margin: 0;
  display: flex;
  align-items: center;
  gap: 5px;
}

/* ── CHAT BUBBLE ── */
.msg-bot {
  display: flex;
  gap: 12px;
  max-width: 80%;
  margin-bottom: 1rem;
}

.msg-user {
  display: flex;
  justify-content: flex-end;
  margin-bottom: 1rem;
}

.msg-bubble-bot {
  background: var(--surface);
  border: 1.5px solid var(--border);
  border-radius: 2px 16px 16px 16px;
  padding: 1rem 1.2rem;
}

.msg-bubble-user {
  background: linear-gradient(135deg, #4f9d69 0%, #35784c 100%);
  border-radius: 16px 2px 16px 16px;
  padding: 0.9rem 1.2rem;
  color: #fff;
}

/* ── INPUT ── */
.input-wrapper {
  border-top: 1.5px solid var(--border);
  background: var(--surface);
  padding: 0.9rem 0;
  margin-top: 0.5rem;
}

/* ── BUTTON ── */
[data-testid="stButton"] > button {
  background: var(--parchment) !important;
  color: var(--amber-deep) !important;
  border: 1.5px solid var(--warm-100) !important;
  border-radius: 8px !important;
}

/* ── SCROLLBAR ── */
::-webkit-scrollbar {
  width: 4px;
}
::-webkit-scrollbar-thumb {
  background: var(--warm-200);
  border-radius: 4px;
}

</style>
""", unsafe_allow_html=True)

# ─────────────────────────────────────────────
#  Load model
# ─────────────────────────────────────────────
@st.cache_resource
def load_chatbot_model():
    try:
        bundle = joblib.load('model/chatbot_model.pkl')
        required_keys = ['vectorizer', 'tfidf_matrix', 'corpus_idx', 'faqs', 'stopwords', 'sinonim', 'threshold']
        missing = [k for k in required_keys if k not in bundle]
        if missing:
            st.error(f"Model tidak lengkap. Key hilang: {missing}")
            st.stop()
        return bundle
    except FileNotFoundError:
        st.error("File model tidak ditemukan: model/chatbot_model.pkl")
        st.stop()
    except Exception as e:
        st.error(f"Gagal memuat model: {e}")
        st.stop()

@st.cache_data
def load_metadata():
    try:
        with open('model/metadata.json', encoding='utf-8') as f:
            return json.load(f)
    except:
        return {
            'total_faq': 15, 'threshold': 0.15, 'f1_score': 0.88,
            'kategori': ['Pengiriman','Pembayaran','Pengembalian','Akun','Produk','Promo','Komplain']
        }

bundle       = load_chatbot_model()
meta         = load_metadata()
vectorizer   = bundle['vectorizer']
tfidf_matrix = bundle['tfidf_matrix']
corpus_idx   = bundle['corpus_idx']
faqs         = bundle['faqs']
STOPWORDS    = bundle['stopwords']
SINONIM      = bundle['sinonim']
THRESHOLD    = bundle['threshold']


# ─────────────────────────────────────────────
#  Helpers
# ─────────────────────────────────────────────
def preprocess(text: str) -> str:
    text  = text.lower().strip()
    words = [SINONIM.get(w, w) for w in text.split()]
    text  = ' '.join(words)
    text  = re.sub(r'[^a-z0-9\s]', ' ', text)
    text  = re.sub(r'\s+', ' ', text).strip()
    return ' '.join(w for w in text.split() if w not in STOPWORDS and len(w) > 1)

from sklearn.metrics.pairwise import cosine_similarity as cos_sim

def get_answer(query: str, top_k: int = 3) -> dict:
    q_vec = vectorizer.transform([preprocess(query)])
    if q_vec.shape[1] != tfidf_matrix.shape[1]:
        return {'found': False, 'score': 0.0, 'candidates': []}
    sims    = cos_sim(q_vec, tfidf_matrix).flatten()
    top_ids = sims.argsort()[::-1][:top_k * 3]
    best    = top_ids[0]
    score   = float(sims[best])
    if score < THRESHOLD:
        return {'found': False, 'score': score, 'candidates': []}
    best_faq = faqs[corpus_idx[best]]
    seen     = {corpus_idx[best]}
    candidates = []
    for idx in top_ids[1:]:
        fi = corpus_idx[idx]
        if fi not in seen and sims[idx] > THRESHOLD * 0.4:
            candidates.append({'question': faqs[fi]['pertanyaan'],
                                'kategori': faqs[fi]['kategori'],
                                'score'   : float(sims[idx])})
            seen.add(fi)
        if len(candidates) >= 2:
            break
    return {'found': True, 'score': score, 'answer': best_faq['jawaban'],
            'question': best_faq['pertanyaan'], 'kategori': best_faq['kategori'],
            'candidates': candidates}

def kategori_class(kat: str) -> str:
    return f"k-{kat.lower().replace(' ', '-').replace('/', '-')}"

def format_answer(text: str) -> str:
    lines = text.split('\n')
    html  = []
    for line in lines:
        line = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', line)
        if line.startswith('- ') or line.startswith('✅') or line.startswith('❌'):
            html.append(f'<div style="padding:2px 0 2px 4px">{line}</div>')
        elif line.strip() == '':
            html.append('<div style="height:6px"></div>')
        else:
            html.append(f'<div>{line}</div>')
    return ''.join(html)

def now_str() -> str:
    return datetime.now().strftime('%H:%M')


# ─────────────────────────────────────────────
#  Session state
# ─────────────────────────────────────────────
if 'messages' not in st.session_state:
    st.session_state.messages = []
if 'pending_query' not in st.session_state:
    st.session_state.pending_query = None


# ─────────────────────────────────────────────
#  SIDEBAR
# ─────────────────────────────────────────────
with st.sidebar:
    st.markdown("""
    <div style="padding:1.3rem 1.1rem 1rem;border-bottom:1px solid rgba(116,196,143,0.12);
                margin-bottom:0.5rem;position:relative;">
      <div style="position:absolute;bottom:0;left:1.1rem;right:1.1rem;height:1px;
                  background:linear-gradient(90deg,transparent,#74c48f,transparent);opacity:0.35"></div>
      <div style="display:flex;align-items:center;gap:12px">
        <div style="width:42px;height:42px;border-radius:12px;
                    background:linear-gradient(135deg,#4f9d69,#2f5f3f);
                    display:flex;align-items:center;justify-content:center;
                    font-size:22px;box-shadow:0 4px 16px rgba(79,157,105,0.4);">🛍️</div>
        <div>
          <div style="font-family:'Fraunces',serif;font-size:1.05rem;font-weight:600;color:#e8f5ed;">
            AskChat-Chatbot Assistant</div>
          <div style="font-size:0.67rem;color:#4cc9b0;font-weight:500;
                      display:flex;align-items:center;gap:4px;margin-top:2px;">
            <span style="width:5px;height:5px;background:#4cc9b0;border-radius:50%;
                         display:inline-block;"></span>
            Online · Siap membantu
          </div>
        </div>
      </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("### 📊 Info Model")
    c1, c2 = st.columns(2)
    c1.metric("Total FAQ", meta.get('total_faq', 15))
    c2.metric("F1-Score",  f"{meta.get('f1_score', 0.88):.2f}")
    c1.metric("Threshold", f"{meta.get('threshold', 0.15):.2f}")
    c2.metric("Fitur",     meta.get('total_features', '—'))

    st.markdown("---")
    st.markdown("### 🏷️ Kategori FAQ")
    cat_meta = {
        'Pengiriman':   ('#3da48e', '📦'),
        'Pembayaran':   ('#d29922', '💳'),
        'Pengembalian': ('#e05c52', '🔄'),
        'Akun':         ('#5b9cf6', '👤'),
        'Produk':       ('#b07ef8', '🏷️'),
        'Promo':        ('#74c48f', '🎁'),
        'Komplain':     ('#f07070', '📢'),
    }
    for kat in meta.get('kategori', []):
        color, icon = cat_meta.get(kat, ('#8aa091', '•'))
        st.markdown(f"""
        <div style="display:flex;align-items:center;gap:10px;padding:6px 0;
                    border-bottom:1px solid rgba(116,196,143,0.1);font-size:0.79rem;">
          <span>{icon}</span>
          <span style="color:#c2d9c9;flex:1;">{kat}</span>
          <div style="width:6px;height:6px;border-radius:50%;background:{color};"></div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("---")
    if st.button("🗑 Hapus Riwayat Chat", use_container_width=True):
        st.session_state.messages = []
        st.rerun()

    st.markdown("---")
    st.markdown("""
    <div style="padding:0.2rem 0 1rem;font-size:0.75rem;line-height:1.9;">
      <div style="color:#7a9e84;font-weight:600;margin-bottom:4px;
                  font-family:'DM Mono',monospace;font-size:0.62rem;
                  text-transform:uppercase;letter-spacing:0.12em;">Author</div>
      <div style="color:#e8f5ed;font-family:'Fraunces',serif;font-size:0.95rem;font-weight:600;">
        Taufik Qurohman</div>
      <div style="color:#7a9e84;">Data Science · NLP</div>
      <div style="margin-top:10px;display:flex;gap:6px;">
        <a href="https://github.com/taufikqurohman" target="_blank"
           style="color:#e8f5ed;text-decoration:none;background:rgba(116,196,143,0.1);
                  border:1px solid rgba(116,196,143,0.2);padding:3px 10px;border-radius:6px;
                  font-family:'DM Mono',monospace;font-size:0.62rem;">GitHub</a>
        <a href="https://linkedin.com/in/taufikqurohman" target="_blank"
           style="color:#e8f5ed;text-decoration:none;background:rgba(116,196,143,0.1);
                  border:1px solid rgba(116,196,143,0.2);padding:3px 10px;border-radius:6px;
                  font-family:'DM Mono',monospace;font-size:0.62rem;">LinkedIn</a>
      </div>
    </div>
    """, unsafe_allow_html=True)


# ─────────────────────────────────────────────
#  MAIN AREA
# ─────────────────────────────────────────────

# ── Header ──
st.markdown("""
<div class="chat-header">
  <div class="bot-avatar-header">🛍️</div>
  <div>
    <p class="bot-name">AskChat-Chatbot Assistant</p>
    <p class="bot-status">
      <span class="status-dot"></span>
      Online · Siap membantu
    </p>
  </div>
</div>
""", unsafe_allow_html=True)

# ── Chat messages ──
with st.container():
    if not st.session_state.messages:
        st.markdown("""
        <div class="empty-state">
          <div class="empty-hero">🛍️</div>
          <div class="empty-title">Selamat datang!</div>
          <div class="empty-sub">
            Saya AskChat, siap menjawab pertanyaan seputar belanja online Anda —
            dari pengiriman, pembayaran, hingga pengembalian barang.
          </div>
          <div class="quick-label">Coba tanyakan</div>
        </div>
        """, unsafe_allow_html=True)

        quick_qs = [
            "⏱ Berapa lama pengiriman?",
            "💳 Cara bayar pakai GoPay?",
            "🔄 Mau kembalikan barang",
            "🔑 Lupa password akun",
            "🎁 Ada promo voucher?",
            "📞 Hubungi customer service",
        ]
        cols = st.columns(3)
        for i, q in enumerate(quick_qs):
            with cols[i % 3]:
                if st.button(q, key=f"quick_{i}", use_container_width=True):
                    txt = q.split(' ', 1)[1] if ' ' in q else q
                    st.session_state.pending_query = txt
                    st.rerun()
    else:
        for msg in st.session_state.messages:
            if msg['role'] == 'user':
                st.markdown(f"""
                <div class="msg-user">
                  <div>
                    <div class="msg-bubble-user">{msg['content']}</div>
                    <div class="msg-time-user">{msg['time']}</div>
                  </div>
                </div>
                """, unsafe_allow_html=True)
            else:
                kat       = msg.get('kategori', '')
                kat_cls   = kategori_class(kat)
                score     = msg.get('score', 0)
                score_pct = min(int(score / 0.8 * 100), 100)
                score_col = '#2d9c8f' if score > 0.4 else ('#c8832a' if score > 0.2 else '#c0524a')
                is_found  = msg.get('found', False)
                extra_cls = '' if is_found else ' msg-bubble-fallback'
                badge_html  = f'<span class="kategori-badge {kat_cls}">{kat}</span><br>' if kat else ''
                answer_html = format_answer(msg['content'])

                score_bar = ''
                if is_found:
                    score_bar = f"""
                    <div class="score-bar">
                      <span>Confidence</span>
                      <div class="score-track">
                        <div class="score-fill" style="width:{score_pct}%;background:{score_col}"></div>
                      </div>
                      <span style="color:{score_col}">{score:.2f}</span>
                    </div>"""

                cand_html = ''
                if msg.get('candidates'):
                    items = ''.join([
                        f'<div style="font-size:0.77rem;color:#5b6f62;padding:4px 0;'
                        f'border-bottom:1px solid #d7e8dc;display:flex;align-items:center;gap:8px;">'
                        f'<span style="font-family:DM Mono,monospace;font-size:0.58rem;'
                        f'color:#8aa091;text-transform:uppercase;">{c["kategori"]}</span>'
                        f'<span style="color:#1f3327;">{c["question"]}</span></div>'
                        for c in msg['candidates']
                    ])
                    cand_html = f"""
                    <div class="related-wrap">
                      <div class="related-label">Mungkin juga ditanyakan</div>
                      {items}
                    </div>"""

                st.markdown(f"""
                <div class="msg-bot">
                  <div class="bot-avatar">🛍️</div>
                  <div>
                    <div class="msg-bubble-bot{extra_cls}">
                      {badge_html}{answer_html}{score_bar}{cand_html}
                    </div>
                    <div class="msg-time">{msg['time']}</div>
                  </div>
                </div>
                """, unsafe_allow_html=True)

                if msg.get('candidates') and msg == st.session_state.messages[-1]:
                    st.markdown(
                        "<div style='padding-left:46px;margin-top:6px;display:flex;flex-wrap:wrap;gap:6px;'>",
                        unsafe_allow_html=True
                    )
                    for ci, cand in enumerate(msg['candidates']):
                        if st.button(f"❓ {cand['question']}",
                                     key=f"cand_{ci}_{len(st.session_state.messages)}"):
                            st.session_state.pending_query = cand['question']
                            st.rerun()
                    st.markdown("</div>", unsafe_allow_html=True)

# ── Input area ──
st.markdown("<div class='input-wrapper'>", unsafe_allow_html=True)
input_col, btn_col = st.columns([10, 1])
with input_col:
    user_input = st.text_input(
        label="Chat Input",
        placeholder="Ketik pertanyaan Anda di sini...",
        key="chat_input",
        label_visibility="collapsed",
    )
with btn_col:
    send_btn = st.button("Kirim ↗", use_container_width=True)
st.markdown("</div>", unsafe_allow_html=True)


# ─────────────────────────────────────────────
#  PROCESS QUERY
# ─────────────────────────────────────────────
query = st.session_state.pending_query or (
    user_input.strip() if send_btn and user_input.strip() else None
)

last_user_msg = next(
    (m['content'] for m in reversed(st.session_state.messages) if m['role'] == 'user'), None
)

if query :
    st.session_state.pending_query = None
    st.session_state.messages.append({'role': 'user', 'content': query, 'time': now_str()})

    result = get_answer(query)
    if result['found']:
        st.session_state.messages.append({
            'role': 'bot', 'content': result['answer'],
            'kategori': result['kategori'], 'score': result['score'],
            'found': True, 'candidates': result['candidates'], 'time': now_str(),
        })
    else:
        fallback = (
            "Maaf, saya tidak menemukan jawaban yang sesuai. 😔\n\n"
            "Coba:\n- Gunakan kata kunci yang lebih spesifik\n"
            "- Tanyakan dalam bahasa yang lebih sederhana\n\n"
            "Atau hubungi CS kami langsung:\n"
        )
        st.session_state.messages.append({
            'role': 'bot', 'content': fallback,
            'kategori': '', 'score': result['score'],
            'found': False, 'candidates': [], 'time': now_str()
        })

    st.rerun()

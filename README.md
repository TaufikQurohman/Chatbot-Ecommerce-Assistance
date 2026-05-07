# 🛍️ AskChat - Chatbot Asisten Toko Online

Chatbot FAQ berbasis NLP untuk e-commerce, dibangun menggunakan TF-IDF + Cosine Similarity dengan antarmuka chat modern menggunakan Streamlit.

![Python](https://img.shields.io/badge/Python-3.10+-blue?logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-1.32+-red?logo=streamlit&logoColor=white)
![scikit-learn](https://img.shields.io/badge/scikit--learn-1.3+-orange?logo=scikit-learn&logoColor=white)
![NLP](https://img.shields.io/badge/NLP-TF--IDF-purple)

---

## 📌 Demo Live

🔗 **[Buka Aplikasi]([https://taufikqurohman-tokobot.streamlit.app](https://chatbot-ecommerce-assistance-rn5dkox6wakjlepe4mkt4b.streamlit.app/))** ← ganti dengan URL deploy kamu

---

## 🎯 Tentang Project

AskChat adalah chatbot FAQ end-to-end yang menjawab pertanyaan pelanggan e-commerce secara otomatis menggunakan teknik **Information Retrieval berbasis NLP**:

- **Dataset FAQ custom** — 15 topik, 7 kategori, 75+ variasi pertanyaan dalam Bahasa Indonesia
- **Preprocessing** — normalisasi teks, stopwords removal, sinonim mapping
- **TF-IDF Vectorizer** — representasi teks dengan unigram + bigram
- **Cosine Similarity** — pencarian jawaban paling relevan dari corpus
- **Evaluasi threshold** — optimasi via F1-Score untuk menentukan batas kepercayaan
- **Chat UI** — tampilan dark mode modern layaknya aplikasi chat profesional

### Kategori FAQ yang Didukung

| Kategori | Jumlah Topik | Contoh |
|---|---|---|
| 📦 Pengiriman | 3 | Estimasi waktu, ekspres, tracking resi |
| 💳 Pembayaran | 3 | Metode, keamanan, pembayaran gagal |
| 🔄 Pengembalian | 2 | Prosedur retur, syarat pengembalian |
| 👤 Akun | 2 | Registrasi, reset password |
| 🏷️ Produk | 2 | Keaslian, cara pesan |
| 🎁 Promo | 2 | Voucher, poin reward |
| 📞 Komplain | 1 | Kontak customer service |

---

## 🗂️ Struktur Project

```
chatbot-faq/
│
├── data/
│   └── faq.json                  ← dataset FAQ (pertanyaan + variasi + jawaban)
│
├── notebook/
│   ├── eda_faq.ipynb             ← eksplorasi dataset & analisis TF-IDF
│   └── model_chatbot.ipynb       ← build model, evaluasi threshold, simpan pkl
│
├── model/
│   ├── chatbot_model.pkl         ← model bundle (auto-generated)
│   └── metadata.json             ← info model (auto-generated)
│
├── app.py                        ← Streamlit chat app
├── requirements.txt
└── README.md
```

---

## 🚀 Cara Menjalankan Lokal

### 1. Clone repository
```bash
git clone https://github.com/taufikqurohman/chatbot-faq.git
cd chatbot-faq
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Jalankan notebook (urutan penting!)
```bash
jupyter notebook

# Urutan:
# 1. notebook/eda_faq.ipynb          → eksplorasi dataset
# 2. notebook/model_chatbot.ipynb    → generate model/chatbot_model.pkl
```

### 4. Jalankan web app
```bash
streamlit run app.py
```

Buka browser di `http://localhost:8501`

---

## ☁️ Deploy ke Streamlit Cloud

1. Push semua file ke GitHub (pastikan folder `model/` ikut)
2. Buka [share.streamlit.io](https://share.streamlit.io)
3. Login dengan GitHub → **New app** → pilih repo → pilih `app.py`
4. Klik **Deploy**

---

## ✨ Fitur Aplikasi

- ✅ Chat UI dark mode modern dengan animasi bubble
- ✅ Badge kategori berwarna per jawaban
- ✅ Confidence score bar untuk setiap respons
- ✅ Saran pertanyaan terkait (interaktif)
- ✅ Quick-start chips untuk pertanyaan populer
- ✅ Tombol hapus riwayat chat
- ✅ Fallback response saat pertanyaan tidak ditemukan
- ✅ Preprocessing teks Bahasa Indonesia (stopwords + sinonim)

---

## 🛠️ Tech Stack

| Teknologi | Kegunaan |
|---|---|
| Python 3.10+ | Bahasa utama |
| scikit-learn | TF-IDF Vectorizer + Cosine Similarity |
| pandas / numpy | Manipulasi data |
| matplotlib / seaborn | Visualisasi EDA |
| Streamlit | Chat web app |
| joblib | Simpan & load model |

---

## 👤 Author

**Taufik Qurohman**
- GitHub: [@taufikqurohman](https://github.com/taufikqurohman)
- LinkedIn: [linkedin.com/in/taufikqurohman](https://linkedin.com/in/taufikqurohman)

MIT License

<div align="center">

```text
 ██████╗ ███████╗██████╗ ████████╗
 ██╔══██╗██╔════╝██╔══██╗╚══██╔══╝
 ██████╔╝█████╗  ██████╔╝   ██║   
 ██╔══██╗██╔══╝  ██╔══██╗   ██║   
 ██████╔╝███████╗██║  ██║   ██║   
 ╚═════╝ ╚══════╝╚═╝  ╚═╝   ╚═╝   
                                   
   Architecture Theory & Deep Dive
```



### 🎓 BERT Mimari Teori ve Derin Analiz

**Bidirectional Encoder Representations from Transformers**  
*Doğal Dil İşleme'de Devrim Yaratan Mimari*

---

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg?style=flat&logo=python)](https://python.org)
[![Transformers](https://img.shields.io/badge/🤗-Transformers-yellow.svg)](https://huggingface.co/transformers)
[![License](https://img.shields.io/badge/License-Educational-green.svg)](LICENSE)
[![Status](https://img.shields.io/badge/Status-Active-success.svg)](https://github.com)

</div>

---

## 🌟 Genel Bakış

Bu klasör, **BERT (Bidirectional Encoder Representations from Transformers)** mimarisinin derinlemesine incelenmesini içeren kapsamlı eğitim materyallerini barındırmaktadır. Modern NLP'nin temel taşlarından biri olan BERT'in teorik temellerinden pratik uygulamalarına kadar her şeyi öğreneceksiniz.

### 🎯 Bu Modül Size Neler Kazandıracak?

<table>
<tr>
<td width="50%">

**📚 Teorik Derinlik**
- ✅ Bağlam (Context) kavramının temelleri
- ✅ Çift yönlü (Bidirectional) anlama felsefesi
- ✅ Transformer mimarisinin BERT'e uyarlanması
- ✅ Self-Attention mekanizmasının gücü

</td>
<td width="50%">

**🛠️ Pratik Uygulama**
- ✅ WordPiece tokenization detayları
- ✅ Embedding katmanlarının yapısı
- ✅ MLM ve NSP eğitim stratejileri
- ✅ Fine-tuning ve transfer learning

</td>
</tr>
</table>

### 🎓 Hedef Kitle

- 📖 **Yeni Başlayanlar:** Hiç NLP bilmeyenler için sıfırdan anlatım
- 🚀 **Orta Seviye:** Transformer kavramlarını pekiştirmek isteyenler
- 🔬 **İleri Düzey:** BERT'in iç mekaniklerini anlamak isteyenler
- 💼 **YBS Öğrencileri:** Gerçek dünya uygulamaları ve iş senaryoları

---

## � İçindekiler

- [🌟 Genel Bakış](#-genel-bakış)
- [📂 Klasör İçeriği](#-klasör-içeriği)
  - [📓 Notebook 1: BERT Paper & Terminology](#-notebook-1-bert-paper--terminology)
  - [📓 Notebook 2: WordPiece & Training Fundamentals](#-notebook-2-wordpiece--training-fundamentals)
- [🎨 BERT Mimarisi Görselleştirme](#-bert-mimarisi-görselleştirme)
- [🔄 Tokenization Pipeline](#-tokenization-pipeline)
- [🎓 Training Pipeline](#-training-pipeline)
- [🚀 Nasıl Kullanılır](#-nasıl-kullanılır)
- [📚 Öğrenme Yol Haritası](#-öğrenme-yol-haritası)
- [⚙️ Gereksinimler](#️-gereksinimler)
- [💡 İpuçları](#-i̇puçları)
- [📖 Kaynaklar](#-kaynaklar)

---

## 📂 Klasör İçeriği

Bu klasörde **2 temel notebook** bulunmaktadır:

### 📓 Notebook 1: BERT Paper & Terminology

**Dosya:** `01.bertpaper-terminology.ipynb`  
**Süre:** ~120 dakika  
**Seviye:** 🟢 Başlangıç → 🟡 Orta

#### 🎯 Ne Öğreneceksiniz?

<div align="left">

```mermaid
%%{init: {'theme':'base', 'themeVariables': { 'primaryColor':'#FFE5E5','primaryTextColor':'#2C3E50','primaryBorderColor':'#FF9999','lineColor':'#FFB6C1','secondaryColor':'#E5F3FF','tertiaryColor':'#FFF9E5'}}}%%
mindmap
  root((BERT Terminoloji))
    Context Kavramı
      Çok Anlamlılık
      Bağlam Penceresi
      Türkçe Örnekler
    Tek vs Çift Yönlü
      Unidirectional
      Bidirectional
      Film Metaforu
    GPT vs BERT
      Karşılaştırma
      Kullanım Alanları
    Transformer
      Self-Attention
      Encoder-Decoder
    Eğitim Yöntemleri
      MLM
      NSP
```

</div>

#### 📋 Bölüm Detayları

| Adım | Konu | Açıklama | Süre |
|------|------|----------|------|
| **1** | 🎯 Bağlam (Context) | Kelime anlamlarının bağlama göre değişimi | 20 dk |
| **2** | 🎬 Tek vs Çift Yönlü | Film metaforu ile unidirectional/bidirectional farkı | 25 dk |
| **3** | 🏗️ Transformer Temelleri | Encoder-Decoder mimarisi, Self-Attention | 30 dk |
| **4** | 🤖 GPT vs BERT | İki mimarinin karşılaştırmalı analizi | 20 dk |
| **5** | 📚 MLM & NSP | Masked Language Model ve Next Sentence Prediction | 25 dk |

#### 💡 Öne Çıkan Özellikler

- ✨ Günlük hayattan örneklerle bağlam kavramı
- 🎭 Türkçe çok anlamlı kelimeler (yüz, kol, anahtar)
- 📊 İnteraktif Python kod örnekleri
- 💼 YBS perspektifinden gerçek dünya senaryoları
- 🎨 Görsel diyagramlar ve ASCII art
- 🔍 Adım adım detaylı açıklamalar

---

### 📓 Notebook 2: WordPiece & Training Fundamentals

**Dosya:** `02.bert-wordpiece-and-training-fundamentals.ipynb`  
**Süre:** ~180 dakika  
**Seviye:** 🟡 Orta → 🔴 İleri

#### 🎯 Ne Öğreneceksiniz?

<div align="left">

```mermaid
%%{init: {'theme':'base', 'themeVariables': { 'primaryColor':'#E5F3FF','primaryTextColor':'#2C3E50','primaryBorderColor':'#99CCFF','lineColor':'#B3D9FF','secondaryColor':'#FFF9E5','tertiaryColor':'#E5FFE5'}}}%%
mindmap
  root((BERT İç Yapı))
    WordPiece
      Tokenization
      Subword Units
      ## İşareti
    Özel Tokenlar
      CLS Token
      SEP Token
      MASK Token
    Embedding Sistemi
      Token Embedding
      Segment Embedding
      Position Embedding
    Training
      MLM Detayları
      NSP Detayları
      Fine-tuning
```

</div>

#### 📋 Bölüm Detayları

| Adım | Konu | Açıklama | Süre |
|------|------|----------|------|
| **1** | ✂️ WordPiece Tokenization | Kelimeleri neden ve nasıl parçalıyoruz | 35 dk |
| **2** | 🏷️ Özel Tokenlar | [CLS], [SEP], [MASK] token'larının işlevi | 30 dk |
| **3** | 🧩 Üç Katmanlı Embedding | Token + Segment + Position embedding sistemi | 40 dk |
| **4** | 🎓 BERT Eğitimi | MLM ve NSP eğitim stratejileri detaylı | 45 dk |
| **5** | 🔄 Fine-tuning | Transfer learning ve downstream görevler | 30 dk |

#### 💡 Öne Çıkan Özellikler

- 🔬 Hugging Face Transformers kütüphanesi kullanımı
- 🛠️ Gerçek kod örnekleri ve uygulamalar
- 📊 E-ticaret müşteri yorumu analizi senaryosu
- 🎨 Mermaid diyagramları ile görselleştirme
- 🧪 İnteraktif tokenization deneyleri
- 💻 Pratik fine-tuning örnekleri

---

## 🎨 BERT Mimarisi Görselleştirme

### 🏗️ BERT Genel Mimari

BERT'in temel mimarisini ve bilgi akışını gösteren kapsamlı diyagram:

```mermaid
%%{init: {'theme':'base', 'themeVariables': { 'primaryColor':'#FFF4E6','primaryTextColor':'#2C3E50','primaryBorderColor':'#FFB366','lineColor':'#FF9933','secondaryColor':'#E8F5E9','tertiaryColor':'#E3F2FD','fontSize':'14px'}}}%%
graph TB
    subgraph Input["🔤 GİRİŞ KATMANI"]
        A["Metin: 'Köpeğim oyun oynamayı seviyor'"]
        B["WordPiece Tokenization"]
        C["[CLS] köpek ##im oyun oyna ##ma ##yı sev ##iyor [SEP]"]
    end
    
    subgraph Embed["🧩 EMBEDDING KATMANI"]
        D["Token Embeddings<br/>Kelime temsilleri"]
        E["Segment Embeddings<br/>Cümle ID'leri"]
        F["Position Embeddings<br/>Pozisyon bilgisi"]
        G["Toplam Embedding<br/>(Token + Segment + Position)"]
    end
    
    subgraph Trans["🔄 TRANSFORMER ENCODER"]
        H1["Encoder Layer 1<br/>Multi-Head Self-Attention"]
        H2["Encoder Layer 2<br/>Feed Forward"]
        H3["... ... ..."]
        H4["Encoder Layer 12<br/>Contextualized Representations"]
    end
    
    subgraph Output["📤 ÇIKTI KATMANI"]
        I["[CLS] Çıktı<br/>Tüm cümle özeti"]
        J["Token Çıktıları<br/>Bağlamsal vektörler"]
    end
    
    subgraph Tasks["🎯 DOWNSTREAM GÖREVLER"]
        K["Sınıflandırma<br/>Sentiment Analysis"]
        L["NER<br/>Entity Recognition"]
        M["QA<br/>Question Answering"]
    end
    
    A --> B --> C
    C --> D
    C --> E
    C --> F
    D --> G
    E --> G
    F --> G
    G --> H1 --> H2 --> H3 --> H4
    H4 --> I
    H4 --> J
    I --> K
    J --> L
    J --> M
    
    style Input fill:#FFF4E6,stroke:#FFB366,stroke-width:3px,color:#2C3E50
    style Embed fill:#E8F5E9,stroke:#81C784,stroke-width:3px,color:#2C3E50
    style Trans fill:#E3F2FD,stroke:#64B5F6,stroke-width:3px,color:#2C3E50
    style Output fill:#F3E5F5,stroke:#BA68C8,stroke-width:3px,color:#2C3E50
    style Tasks fill:#FFE5E5,stroke:#FF9999,stroke-width:3px,color:#2C3E50
    
    style A fill:#FFE0B2,stroke:#FF9800,stroke-width:2px,color:#2C3E50
    style C fill:#FFF9C4,stroke:#FBC02D,stroke-width:2px,color:#2C3E50
    style G fill:#C8E6C9,stroke:#4CAF50,stroke-width:2px,color:#2C3E50
    style H4 fill:#BBDEFB,stroke:#2196F3,stroke-width:2px,color:#2C3E50
    style I fill:#E1BEE7,stroke:#9C27B0,stroke-width:2px,color:#2C3E50
```

### 🔑 Mimari Bileşenleri

| Katman | İşlev | Detay |
|--------|-------|-------|
| 🔤 **Giriş** | Metin → Token | WordPiece ile parçalama, özel token'lar ekleme |
| 🧩 **Embedding** | Token → Vektör | 3 tip embedding'in toplamı (Token+Segment+Position) |
| 🔄 **Transformer** | Vektör → Bağlam | 12 katman (Base) veya 24 katman (Large) encoder |
| 📤 **Çıktı** | Bağlam → Temsil | Her token için bağlamsal vektör |
| 🎯 **Task** | Fine-tuning | Sınıflandırma, NER, QA vb. görevler |

---

## 🔄 Tokenization Pipeline

### ✂️ WordPiece Tokenization Süreci

Bir cümlenin nasıl token'lara dönüştürüldüğünü adım adım gösteren diyagram:

```mermaid
%%{init: {'theme':'base', 'themeVariables': { 'primaryColor':'#E8F5E9','primaryTextColor':'#1B5E20','primaryBorderColor':'#66BB6A','lineColor':'#4CAF50','secondaryColor':'#FFF3E0','tertiaryColor':'#E1F5FE','fontSize':'13px'}}}%%
graph LR
    subgraph S1["1️⃣ HAM METİN"]
        A["Ürün kaliteli<br/>ve hızlı geldi"]
    end
    
    subgraph S2["2️⃣ NORMALIZE"]
        B["Lowercase<br/>ürün kaliteli<br/>ve hızlı geldi"]
    end
    
    subgraph S3["3️⃣ TOKENIZE"]
        C1["ürün"]
        C2["kalite"]
        C3["##li"]
        C4["ve"]
        C5["hızlı"]
        C6["gel"]
        C7["##di"]
    end
    
    subgraph S4["4️⃣ ÖZEL TOKENLAR"]
        D["[CLS] ürün kalite ##li<br/>ve hızlı gel ##di [SEP]"]
    end
    
    subgraph S5["5️⃣ ID'LERE ÇEVİR"]
        E["[101, 7854, 2156,<br/>3421, 1005, 8734,<br/>4521, 2134, 102]"]
    end
    
    subgraph S6["6️⃣ BERT'E HAZIR"]
        F["Token IDs ✅<br/>Attention Mask ✅<br/>Token Type IDs ✅"]
    end
    
    A --> B
    B --> C1 & C2 & C3 & C4 & C5 & C6 & C7
    C1 --> D
    C2 --> D
    C3 --> D
    C4 --> D
    C5 --> D
    C6 --> D
    C7 --> D
    D --> E
    E --> F
    
    style S1 fill:#FFE5E5,stroke:#FF9999,stroke-width:3px
    style S2 fill:#FFF9E5,stroke:#FFD966,stroke-width:3px
    style S3 fill:#E8F5E9,stroke:#81C784,stroke-width:3px
    style S4 fill:#E3F2FD,stroke:#64B5F6,stroke-width:3px
    style S5 fill:#F3E5F5,stroke:#BA68C8,stroke-width:3px
    style S6 fill:#C8E6C9,stroke:#4CAF50,stroke-width:4px
    
    style A fill:#FFCDD2,stroke:#E57373,color:#2C3E50
    style B fill:#FFF9C4,stroke:#FFF176,color:#2C3E50
    style D fill:#BBDEFB,stroke:#64B5F6,color:#2C3E50
    style E fill:#E1BEE7,stroke:#BA68C8,color:#2C3E50
    style F fill:#A5D6A7,stroke:#66BB6A,stroke-width:3px,color:#1B5E20
```

### 🔍 Tokenization Örnek Analizi

| Orijinal | Token'lar | Açıklama |
|----------|-----------|----------|
| **"playing"** | `["play", "##ing"]` | Kök + ek ayrımı |
| **"unbelievable"** | `["un", "##believe", "##able"]` | Önek + kök + sonek |
| **"kitaplık"** | `["kitap", "##lık"]` | Türkçe kök + ek |
| **"oynamayı"** | `["oyun", "##ma", "##yı"]` | Çoklu ek yapısı |

> 💡 **Not:** `##` işareti, token'ın kelimenin başında değil, devamı olduğunu gösterir!

---

## 🎓 Training Pipeline

### 📚 BERT Eğitim Süreci

BERT'in nasıl eğitildiğini gösteren tam pipeline:

```mermaid
%%{init: {'theme':'base', 'themeVariables': { 'primaryColor':'#E3F2FD','primaryTextColor':'#0D47A1','primaryBorderColor':'#42A5F5','lineColor':'#2196F3','secondaryColor':'#FFF3E0','tertiaryColor':'#F3E5F5','fontSize':'13px'}}}%%
graph TB
    subgraph Data["📊 VERİ HAZIRLIĞI"]
        A["Büyük Metin Korpusu<br/>Wikipedia + Books<br/>3.3 Milyar Kelime"]
        B["Cümle Çiftleri Oluştur<br/>(Sentence A, Sentence B)"]
        C["50% Ardışık<br/>50% Rastgele"]
    end
    
    subgraph MLM["🎭 MASKED LANGUAGE MODEL"]
        D["Her cümlenin %15'ini<br/>rastgele maskele"]
        E["80% [MASK]<br/>10% Rastgele<br/>10% Orijinal"]
        F["Model [MASK]'ı<br/>tahmin etmeye çalışır"]
    end
    
    subgraph NSP["🔗 NEXT SENTENCE PREDICTION"]
        G["Cümle A ve B<br/>veriliyor"]
        H["B, A'nın devamı mı?<br/>İkili sınıflandırma"]
        I["IsNext: 1<br/>NotNext: 0"]
    end
    
    subgraph Train["⚙️ EĞİTİM"]
        J["MLM Loss +<br/>NSP Loss"]
        K["Backpropagation<br/>Weight Update"]
        L["64 TPU Çipi<br/>4 Gün Eğitim"]
    end
    
    subgraph PreTrain["✅ PRE-TRAINED MODEL"]
        M["BERT Base<br/>110M Parameters"]
        N["Genel Dil Anlayışı<br/>Kazandı"]
    end
    
    subgraph FineTune["🔧 FINE-TUNING"]
        O["Task-Specific<br/>Dataset"]
        P["Sınıflandırma Katmanı<br/>Ekle"]
        Q["Az Veriyle<br/>Hızlı Eğitim"]
        R["Spesifik Görev<br/>İçin Hazır"]
    end
    
    A --> B --> C
    C --> D
    D --> E --> F
    C --> G
    G --> H --> I
    F --> J
    I --> J
    J --> K --> L
    L --> M --> N
    N --> O --> P --> Q --> R
    
    style Data fill:#FFF4E6,stroke:#FFB366,stroke-width:3px,color:#2C3E50
    style MLM fill:#FFE5E5,stroke:#FF9999,stroke-width:3px,color:#2C3E50
    style NSP fill:#E8F5E9,stroke:#81C784,stroke-width:3px,color:#2C3E50
    style Train fill:#E3F2FD,stroke:#64B5F6,stroke-width:3px,color:#0D47A1
    style PreTrain fill:#F3E5F5,stroke:#BA68C8,stroke-width:4px,color:#2C3E50
    style FineTune fill:#FFF9E5,stroke:#FFD966,stroke-width:3px,color:#2C3E50
    
    style M fill:#E1BEE7,stroke:#9C27B0,stroke-width:3px,color:#2C3E50
    style R fill:#C8E6C9,stroke:#4CAF50,stroke-width:3px,color:#1B5E20
```

### 🎯 Eğitim Stratejileri Karşılaştırma

<table>
<tr>
<th width="25%">🎭 MLM</th>
<th width="25%">🔗 NSP</th>
<th width="25%">⚖️ Combined</th>
<th width="25%">🔧 Fine-tuning</th>
</tr>
<tr>
<td>

**Amaç:**  
Maskelenmiş kelimeleri tahmin et

**Örnek:**  
"Köpeğim [MASK] seviyor"  
→ "oynamayı"

</td>
<td>

**Amaç:**  
İki cümle ardışık mı?

**Örnek:**  
A: "Hava güzel"  
B: "Yürüyüşe çıktım"  
→ IsNext ✅

</td>
<td>

**Sonuç:**  
İki görev birlikte

**Fayda:**  
Hem kelime hem de cümle seviyesi anlama

</td>
<td>

**Süreç:**  
Küçük dataset ile hızlı adaptasyon

**Avantaj:**  
Transfer learning gücü

</td>
</tr>
</table>

---

## 🚀 Nasıl Kullanılır

### 📥 1. Gerekli Kurulumlar

```bash
# Python ortamı oluştur (isteğe bağlı ama önerilen)
python -m venv bert_env
bert_env\Scripts\activate  # Windows
# source bert_env/bin/activate  # Linux/Mac

# Gerekli kütüphaneleri yükle
pip install transformers torch jupyter numpy pandas matplotlib
```

### 📚 2. Notebook'ları Çalıştırma

```bash
# Jupyter Notebook başlat
jupyter notebook

# Tarayıcıda açılan sayfadan sırasıyla:
# 1. 01.bertpaper-terminology.ipynb
# 2. 02.bert-wordpiece-and-training-fundamentals.ipynb
```

### 🎯 3. Önerilen Çalışma Sırası

```mermaid
%%{init: {'theme':'base', 'themeVariables': { 'primaryColor':'#E8F5E9','primaryTextColor':'#1B5E20','primaryBorderColor':'#66BB6A','lineColor':'#4CAF50'}}}%%
graph LR
    A["📓 Notebook 1<br/>Terminoloji"] --> B["📓 Notebook 2<br/>İç Yapı"]
    B --> C["💻 Pratik<br/>Projeler"]
    C --> D["🔧 Fine-tuning<br/>Denemeleri"]
    
    style A fill:#FFE5E5,stroke:#FF9999,stroke-width:3px,color:#2C3E50
    style B fill:#E3F2FD,stroke:#64B5F6,stroke-width:3px,color:#2C3E50
    style C fill:#FFF9E5,stroke:#FFD966,stroke-width:3px,color:#2C3E50
    style D fill:#C8E6C9,stroke:#4CAF50,stroke-width:3px,color:#1B5E20
```

---

## 📚 Öğrenme Yol Haritası

### 🗓️ Haftalık Plan

<table>
<tr>
<th width="15%">Hafta</th>
<th width="35%">Konu</th>
<th width="30%">Aktivite</th>
<th width="20%">Hedef</th>
</tr>
<tr>
<td align="center"><strong>1️⃣</strong></td>
<td>📓 <strong>Notebook 1</strong><br/>BERT Terminoloji</td>
<td>
• Her bölümü dikkatlice oku<br/>
• Kod örneklerini çalıştır<br/>
• Flash card'ları ezberle
</td>
<td>Temel kavramları anlama</td>
</tr>
<tr>
<td align="center"><strong>2️⃣</strong></td>
<td>📓 <strong>Notebook 2</strong><br/>WordPiece & Training</td>
<td>
• Tokenization deneyleri yap<br/>
• Embedding sistemini öğren<br/>
• MLM/NSP'yi uygula
</td>
<td>İç mekanikleri kavrama</td>
</tr>
<tr>
<td align="center"><strong>3️⃣</strong></td>
<td>💻 <strong>Pratik Proje</strong><br/>Kendi Dataset'in</td>
<td>
• Hugging Face kullan<br/>
• Sentiment analysis yap<br/>
• Kendi verinle fine-tune et
</td>
<td>Gerçek uygulama deneyimi</td>
</tr>
<tr>
<td align="center"><strong>4️⃣</strong></td>
<td>🚀 <strong>İleri Seviye</strong><br/>Optimizasyon</td>
<td>
• Farklı BERT varyantları<br/>
• Hiperparametre tuning<br/>
• Production deployment
</td>
<td>Profesyonel seviye</td>
</tr>
</table>

### 🎓 Öğrenme İpuçları

> 💡 **Başarı için 5 Altın Kural:**
>
> 1. **📖 Sabırlı Ol:** BERT karmaşık bir mimari, her şeyi ilk seferde anlamak zorunda değilsin
> 2. **💻 Pratik Yap:** Sadece okumakla yetinme, her kod bloğunu çalıştır
> 3. **🤔 Soru Sor:** Anlamadığın yerleri işaretle ve araştır
> 4. **🔄 Tekrar Et:** Bazı kavramları anlamak için 2-3 kez gözden geçir
> 5. **👥 Paylaş:** Öğrendiklerini başkalarına anlat, bu en iyi pekiştirme yöntemidir

---

## ⚙️ Gereksinimler

### 🐍 Python ve Kütüphaneler

```python
# requirements.txt
transformers>=4.35.0
torch>=2.0.0
jupyter>=1.0.0
numpy>=1.24.0
pandas>=2.0.0
matplotlib>=3.7.0
seaborn>=0.12.0
```

### 💻 Sistem Gereksinimleri

| Bileşen | Minimum | Önerilen |
|---------|---------|----------|
| **Python** | 3.8+ | 3.10+ |
| **RAM** | 8 GB | 16 GB+ |
| **Disk** | 5 GB | 10 GB+ |
| **GPU** | Yok (CPU ile çalışır) | NVIDIA GPU (CUDA) |

### 🌐 Online Alternatifler

Yerel kurulum yapamıyorsan:
- 🔵 **Google Colab:** Ücretsiz GPU ile çalıştır
- 🟣 **Kaggle Notebooks:** Hazır ortamda dene
- 🟢 **Hugging Face Spaces:** Demo oluştur ve paylaş

---

## 💡 İpuçları

### 🎯 Verimli Çalışma Stratejileri

<table>
<tr>
<td width="50%">

**✅ YAPILMASI GEREKENLER**

- 📝 Her bölüm sonunda notlar al
- 💻 Kod örneklerini değiştirerek dene
- 🎨 Diyagramları kendi kelimelerinle çiz
- 🤔 "Neden?" sorularını sor
- 📊 Farklı örneklerle test et
- 👥 Çalışma grubu oluştur

</td>
<td width="50%">

**❌ YAPILMAMASI GEREKENLER**

- 🚫 Sadece hızlıca göz gezdirme
- 🚫 Kod çalıştırmadan geçme
- 🚫 Anlamamışken devam etme
- 🚫 Bir seferde hepsini bitirmeye çalışma
- 🚫 Pratik yapmadan teoride kalma
- 🚫 Yalnız çalışıp yardım istememe

</td>
</tr>
</table>

### 🐛 Sık Karşılaşılan Sorunlar

<details>
<summary><strong>❓ BERT çok yavaş çalışıyor</strong></summary>

**Çözümler:**
- Daha küçük bir model kullan: `bert-base-uncased` → `distilbert-base-uncased`
- Batch size'ı azalt
- Sequence length'i kısalt (512 → 128)
- GPU kullan veya Google Colab'a geç

</details>

<details>
<summary><strong>❓ "Out of Memory" hatası alıyorum</strong></summary>

**Çözümler:**
- Batch size'ı küçült (32 → 16 → 8)
- Gradient accumulation kullan
- Mixed precision training dene (`fp16=True`)
- Daha küçük bir model seç

</details>

<details>
<summary><strong>❓ Tokenizer Türkçe metinlerde iyi çalışmıyor</strong></summary>

**Çözümler:**
- Türkçe için özel eğitilmiş model kullan: `dbmdz/bert-base-turkish-cased`
- Veya multilingual model: `bert-base-multilingual-cased`
- Kendi tokenizer'ınızı eğitin (ileri seviye)

</details>

<details>
<summary><strong>❓ Fine-tuning sonuçları kötü</strong></summary>

**Çözümler:**
- Learning rate'i ayarla (genellikle 2e-5 - 5e-5 arası)
- Daha fazla epoch dene
- Dataset'ini dengele (class imbalance kontrolü)
- Pre-trained model seçimini gözden geçir
- Data augmentation uygula

</details>

---

## 📖 Kaynaklar

### 📄 Orijinal Makaleler

1. **BERT Paper (2018)**  
   [BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding](https://arxiv.org/abs/1810.04805)  
   *Jacob Devlin, Ming-Wei Chang, Kenton Lee, Kristina Toutanova*

2. **Attention is All You Need (2017)**  
   [Transformer Architecture](https://arxiv.org/abs/1706.03762)  
   *Vaswani et al.*

### 🌐 Online Kaynaklar

| Kaynak | Açıklama | Link |
|--------|----------|------|
| 🤗 **Hugging Face** | BERT Dökümantasyonu | [transformers.docs](https://huggingface.co/docs/transformers) |
| 📺 **Jay Alammar** | Görsel BERT Açıklamaları | [The Illustrated BERT](http://jalammar.github.io/illustrated-bert/) |
| 📚 **Papers With Code** | BERT Implementations | [paperswithcode.com](https://paperswithcode.com/method/bert) |
| 🎓 **Stanford CS224N** | NLP Dersleri | [web.stanford.edu/class/cs224n/](https://web.stanford.edu/class/cs224n/) |

### 📚 Türkçe Kaynaklar

- 🇹🇷 **Türkçe NLP Workshop:** Pratik örnekler ve topluluk
- 🇹🇷 **Turkish BERT Models:** `dbmdz/bert-base-turkish-cased`
- 🇹🇷 **NLP Turkey Community:** Discord ve GitHub grubu

### 🎥 Video Kaynakları

- 📺 **StatQuest:** BERT clearly explained (İngilizce, görsel)
- 📺 **Yannic Kilcher:** BERT paper walkthrough (Detaylı)
- 📺 **DeepLearning.AI:** NLP Specialization (Coursera)

---

## ⭐ Teşekkürler

Bu notebook'ları faydalı bulduysan:
- ⭐ GitHub repo'ya yıldız ver
- 🔄 Arkadaşlarınla paylaş
- 📝 Geri bildirim bırak
- 🤝 Topluluğa katıl

---

<div align="center">

### 🎓 Mutlu Öğrenmeler! 

**"BERT'ü anlamak, modern NLP'nin kapılarını açmaktır."**

Made with ❤️ for NLP Enthusiasts by Cemal YÜKSEL | 2026

---

⬆️ [Başa Dön](#-i̇çindekiler)

</div>

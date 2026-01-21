"""
🎨 UI Components - Özel Tasarım Bileşenleri
============================================
Yeniden kullanılabilir UI bileşenleri
"""

import streamlit as st
from config import Colors, EMOTION_CONFIG, UIConfig, MetricsConfig


def load_custom_css():
    """Custom CSS dosyasını yükle"""
    import os
    from pathlib import Path
    
    css_path = Path(__file__).parent.parent / "assets" / "style.css"
    
    try:
        if css_path.exists():
            with open(css_path, encoding='utf-8') as f:
                st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
        else:
            # Inline CSS fallback
            st.markdown("""
                <style>
                @import url('https://fonts.cdnfonts.com/css/nexa-bold');
                @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600;700&display=swap');
                * { font-family: 'Nexa', 'Poppins', sans-serif; }
                </style>
            """, unsafe_allow_html=True)
    except Exception as e:
        st.markdown("""
            <style>
            @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600;700&display=swap');
            * { font-family: 'Poppins', sans-serif; }
            </style>
        """, unsafe_allow_html=True)


def create_hero_header():
    """
    Hero header bölümü - Dark Pastel gradient ile
    """
    st.markdown(f"""
        <div style='
            background: linear-gradient(135deg, #4a7c7e 0%, #356063 100%);
            padding: 3rem 2rem;
            border-radius: 20px;
            text-align: center;
            margin-bottom: 2rem;
            box-shadow: 0 8px 25px rgba(0, 0, 0, 0.5);
            border: 1px solid rgba(255, 255, 255, 0.1);
        '>
            <h1 style='
                color: #ffffff;
                font-size: 3.5rem;
                font-weight: 700;
                margin-bottom: 0.5rem;
                text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
                letter-spacing: -1px;
            '>
                🎭 BERT Emotion Analyzer
            </h1>
            <p style='
                color: #ffffff;
                font-size: 1.3rem;
                font-weight: 400;
                margin-bottom: 1rem;
                letter-spacing: 0.5px;
            '>
                Yapay Zeka Destekli Duygu Analizi Platformu
            </p>
            <div style='
                display: flex;
                justify-content: center;
                gap: 1rem;
                flex-wrap: wrap;
                margin-top: 1.5rem;
            '>
                <span style='
                    background: rgba(255, 255, 255, 0.15);
                    backdrop-filter: blur(10px);
                    padding: 0.5rem 1.5rem;
                    border-radius: 25px;
                    color: #ffffff;
                    font-weight: 600;
                    border: 1px solid rgba(255, 255, 255, 0.2);
                '>⚡ Gerçek Zamanlı</span>
                <span style='
                    background: rgba(255, 255, 255, 0.15);
                    backdrop-filter: blur(10px);
                    padding: 0.5rem 1.5rem;
                    border-radius: 25px;
                    color: #ffffff;
                    font-weight: 600;
                    border: 1px solid rgba(255, 255, 255, 0.2);
                '>🎯 6 Duygu Kategorisi</span>
                <span style='
                    background: rgba(255, 255, 255, 0.15);
                    backdrop-filter: blur(10px);
                    padding: 0.5rem 1.5rem;
                    border-radius: 25px;
                    color: #ffffff;
                    font-weight: 600;
                    border: 1px solid rgba(255, 255, 255, 0.2);
                '>🤖 BERT Powered</span>
            </div>
        </div>
    """, unsafe_allow_html=True)


def create_metrics_dashboard():
    """
    Üst metrik dashboard - Pastel kartlar
    """
    st.markdown("### 📊 Model Performans Metrikleri")
    st.markdown("<br>", unsafe_allow_html=True)
    
    col1, col2, col3, col4 = st.columns(4)
    
    metrics = [
        {
            "label": "Accuracy",
            "value": f"{MetricsConfig.ACCURACY:.1%}",
            "icon": "🎯",
            "color": "#a8dadc",
            "gradient": "linear-gradient(135deg, #a8dadc 0%, #7fa8c7 100%)"
        },
        {
            "label": "F1-Score",
            "value": f"{MetricsConfig.F1_SCORE:.1%}",
            "icon": "⭐",
            "color": "#ffd6a5",
            "gradient": "linear-gradient(135deg, #ffd6a5 0%, #ffb347 100%)"
        },
        {
            "label": "Precision",
            "value": f"{MetricsConfig.PRECISION:.1%}",
            "icon": "🔍",
            "color": "#ffb3c1",
            "gradient": "linear-gradient(135deg, #ffb3c1 0%, #fb6f92 100%)"
        },
        {
            "label": "Recall",
            "value": f"{MetricsConfig.RECALL:.1%}",
            "icon": "📈",
            "color": "#b5e7a0",
            "gradient": "linear-gradient(135deg, #b5e7a0 0%, #86d293 100%)"
        }
    ]
    
    cols = [col1, col2, col3, col4]
    
    for col, metric in zip(cols, metrics):
        with col:
            st.markdown(f"""
                <div style='
                    background: {metric["gradient"]};
                    padding: 1.5rem;
                    border-radius: 15px;
                    text-align: center;
                    box-shadow: 0 4px 15px rgba(0, 0, 0, 0.08);
                    transition: transform 0.3s ease, box-shadow 0.3s ease;
                    border: 1px solid rgba(255, 255, 255, 0.5);
                '>
                    <div style='font-size: 2.5rem; margin-bottom: 0.5rem;'>
                        {metric["icon"]}
                    </div>
                    <div style='
                        font-size: 2rem;
                        font-weight: 700;
                        color: white;
                        margin-bottom: 0.3rem;
                        text-shadow: 1px 1px 2px rgba(0,0,0,0.1);
                    '>
                        {metric["value"]}
                    </div>
                    <div style='
                        font-size: 0.9rem;
                        color: rgba(255, 255, 255, 0.9);
                        font-weight: 600;
                        letter-spacing: 0.5px;
                    '>
                        {metric["label"]}
                    </div>
                </div>
            """, unsafe_allow_html=True)


def create_emotion_palette():
    """
    Duygu paleti - Tüm duyguları göster
    """
    st.markdown("### 🎨 Duygu Kategorileri")
    st.markdown("<br>", unsafe_allow_html=True)
    
    cols = st.columns(6)
    
    for idx, col in enumerate(cols):
        emotion = EMOTION_CONFIG[idx]
        with col:
            st.markdown(f"""
                <div style='
                    background: {emotion["gradient"]};
                    padding: 1.5rem 1rem;
                    border-radius: 12px;
                    text-align: center;
                    box-shadow: 0 3px 12px rgba(0, 0, 0, 0.08);
                    transition: transform 0.2s ease;
                    border: 1px solid rgba(255, 255, 255, 0.4);
                    height: 180px;
                    display: flex;
                    flex-direction: column;
                    justify-content: center;
                '>
                    <div style='font-size: 3rem; margin-bottom: 0.5rem;'>
                        {emotion["emoji"]}
                    </div>
                    <div style='
                        font-size: 1.1rem;
                        font-weight: 700;
                        color: white;
                        margin-bottom: 0.3rem;
                        text-shadow: 1px 1px 2px rgba(0,0,0,0.1);
                    '>
                        {emotion["name"]}
                    </div>
                    <div style='
                        font-size: 0.75rem;
                        color: rgba(255, 255, 255, 0.85);
                        line-height: 1.3;
                    '>
                        {emotion["description"]}
                    </div>
                </div>
            """, unsafe_allow_html=True)


def create_divider(color="#e1e8ed", height="2px", margin="2rem 0"):
    """Özel divider"""
    st.markdown(f"""
        <div style='
            height: {height};
            background: {color};
            border-radius: 2px;
            margin: {margin};
        '></div>
    """, unsafe_allow_html=True)


def create_info_card(title, content, icon="ℹ️", color="#a8dadc"):
    """
    Bilgi kartı oluştur
    """
    st.markdown(f"""
        <div style='
            background: linear-gradient(135deg, {color}20 0%, {color}10 100%);
            border-left: 4px solid {color};
            padding: 1.5rem;
            border-radius: 10px;
            margin: 1rem 0;
        '>
            <div style='
                font-size: 1.5rem;
                margin-bottom: 0.5rem;
            '>{icon}</div>
            <h4 style='
                color: #2d3436;
                margin-bottom: 0.5rem;
                font-weight: 600;
            '>{title}</h4>
            <p style='
                color: #636e72;
                margin: 0;
                line-height: 1.6;
            '>{content}</p>
        </div>
    """, unsafe_allow_html=True)


def create_footer():
    """
    Footer bölümü
    """
    st.markdown("<br><br>", unsafe_allow_html=True)
    st.markdown(f"""
        <div style='
            text-align: center;
            padding: 2rem;
            color: #636e72;
            border-top: 2px solid #e1e8ed;
            margin-top: 3rem;
        '>
            <p style='font-size: 1rem; margin-bottom: 0.5rem;'>
                {UIConfig.FOOTER_TEXT}
            </p>
            <p style='font-size: 0.85rem; color: #95a5a6;'>
                {UIConfig.VERSION} | © 2026 BERT Emotion Analyzer
            </p>
        </div>
    """, unsafe_allow_html=True)


def create_text_input_section():
    """
    Metin girişi bölümü - Dark Pastel tasarım
    
    Returns:
        Tuple[str, bool]: (user_text, analyze_clicked)
    """
    # Başlık
    st.markdown("""
        <div style='
            text-align: center;
            margin: 2rem 0 1.5rem 0;
        '>
            <h2 style='
                color: #ffffff;
                font-size: 2rem;
                font-weight: 700;
                margin-bottom: 0.5rem;
            '>
                💬 Metninizi Analiz Edin
            </h2>
            <p style='
                color: #b0b0b0;
                font-size: 1rem;
            '>
                Aşağıdaki alana analiz etmek istediğiniz metni yazın
            </p>
        </div>
    """, unsafe_allow_html=True)
    
    # Örnek metinler için quick select
    st.markdown("### 🎯 Hızlı Örnekler")
    
    example_texts = {
        "😊 Mutluluk": "Bugün harika bir gün! Çok mutluyum ve enerjik hissediyorum.",
        "😢 Üzüntü": "Bugün çok üzgünüm, hiçbir şey istediğim gibi gitmiyor.",
        "❤️ Sevgi": "Seni çok seviyorum, seninle olmak beni çok mutlu ediyor.",
        "😠 Öfke": "Bu duruma çok sinirliyim! Artık dayanamıyorum!",
        "😨 Korku": "Çok korkuyorum, ne yapacağımı bilemiyorum.",
        "😮 Şaşkınlık": "Bu inanılmaz! Buna gerçekten şaşırdım, beklemiyordum."
    }
    
    cols = st.columns(3)
    selected_example = None
    
    for idx, (label, text) in enumerate(example_texts.items()):
        with cols[idx % 3]:
            if st.button(label, key=f"example_{idx}", use_container_width=True):
                selected_example = text
    
    # Text area
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Session state için text değeri
    if 'user_text' not in st.session_state:
        st.session_state.user_text = ""
    
    # Eğer örnek seçildiyse, text'i güncelle
    if selected_example:
        st.session_state.user_text = selected_example
    
    user_text = st.text_area(
        label="Metniniz",
        value=st.session_state.user_text,
        height=150,
        placeholder="Örnek: Bugün harika bir gün geçirdim! Çok mutluyum ve enerjik hissediyorum...",
        max_chars=500,
        help="Maksimum 500 karakter girebilirsiniz",
        label_visibility="collapsed"
    )
    
    # Text'i session state'e kaydet
    st.session_state.user_text = user_text
    
    # Karakter sayacı
    char_count = len(user_text)
    char_color = "#5a7c50" if char_count <= 500 else "#8b4f5c"
    
    st.markdown(f"""
        <div style='
            text-align: right;
            color: {char_color};
            font-size: 0.85rem;
            margin-top: 0.5rem;
        '>
            {char_count}/500 karakter
        </div>
    """, unsafe_allow_html=True)
    
    # Analiz butonu
    st.markdown("<br>", unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col2:
        analyze_clicked = st.button(
            "🔍 Analiz Et",
            type="primary",
            use_container_width=True,
            disabled=(len(user_text.strip()) == 0)
        )
    
    # Bilgi mesajı
    if len(user_text.strip()) == 0:
        st.info("💡 Analiz yapmak için lütfen metin girin veya yukarıdaki örneklerden birini seçin.", icon="ℹ️")
    
    return user_text, analyze_clicked

"""
🎭 BERT Emotion Analyzer
========================
Profesyonel Duygu Analizi Web Uygulaması

Author: Cemal
Date: 21 Ocak 2026
Version: 1.0.0
"""

import streamlit as st
import os
from pathlib import Path
from utils.ui_components import (
    load_custom_css,
    create_hero_header,
    create_metrics_dashboard,
    create_emotion_palette,
    create_divider,
    create_info_card,
    create_footer,
    create_text_input_section
)
from utils.model_loader import (
    load_bert_model,
    get_model_info,
    check_model_availability,
    get_device_info
)
from utils.predictor import (
    predict_emotion,
    get_top_emotions,
    format_confidence_level,
    get_confidence_color
)
from utils.database import AnalysisDatabase
from config import ModelConfig, EMOTION_CONFIG
import plotly.express as px
import plotly.graph_objects as go

# 📄 Sayfa Konfigürasyonu
st.set_page_config(
    page_title="BERT Emotion Analyzer",
    page_icon="🎭",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': 'https://github.com',
        'Report a bug': 'https://github.com',
        'About': "# BERT Emotion Analyzer\nProfesyonel duygu analizi uygulaması"
    }
)

# ============================================================================
# ANA UYGULAMA
# ============================================================================

def main():
    """Ana uygulama fonksiyonu"""
    
    # Custom CSS yükle (Nexa font dahil)
    load_custom_css()
    
    # ========================================================================
    # DATABASE INITIALIZATION
    # ========================================================================
    
    # Veritabanını başlat
    db = AnalysisDatabase()
    
    # ========================================================================
    # ADIM 4: MODEL LOADING & CACHING
    # ========================================================================
    
    # Model yolunu ayarla - os.getcwd() kullanarak
    current_working_dir = os.getcwd()
    
    # Eğer streamlit_app klasöründeysek, bir üst dizine çık
    if "streamlit_app" in current_working_dir:
        model_path = Path(current_working_dir).parent / "bert_emotion_model"
    else:
        # Eğer üst dizindeysek, doğrudan bert_emotion_model klasörüne git
        model_path = Path(current_working_dir) / "bert_emotion_model"
    
    model_path_str = str(model_path.resolve())
    
    # Debug: Model yolunu göster
    st.sidebar.markdown("### 📁 Debug Info")
    st.sidebar.code(f"CWD: {current_working_dir}\nModel: {model_path_str}")
    
    # Model kontrolü
    if not check_model_availability(model_path_str):
        st.error("❌ Model dosyaları bulunamadı!")
        st.info(f"📁 Beklenen model yolu: {model_path_str}")
        
        # Alternatif yolu dene: relative path
        alternative_path = "../bert_emotion_model"
        st.warning(f"🔍 Alternatif yol deneniyor: {alternative_path}")
        
        if check_model_availability(alternative_path):
            model_path_str = str(Path(alternative_path).resolve())
            st.success(f"✅ Model bulundu: {model_path_str}")
        else:
            st.error("❌ Alternatif yolda da model bulunamadı!")
            
        st.stop()
    
    # Model yükleme (loading spinner ile)
    with st.spinner("🤖 Model yükleniyor... (İlk yüklemede biraz zaman alabilir)"):
        try:
            model, tokenizer, emotion_labels, device = load_bert_model(model_path_str)
            model_info = get_model_info(model_path)
            device_info = get_device_info()
            
            # Başarılı yükleme mesajı (geçici)
            st.success("✅ Model başarıyla yüklendi!", icon="🎉")
            
        except Exception as e:
            st.error(f"❌ Model yükleme hatası: {str(e)}")
            st.stop()
    
    # ========================================================================
    # ADIM 3: HERO HEADER & BRANDING
    # ========================================================================
    
    # Hero Header - Gradient tasarım
    create_hero_header()
    
    # ========================================================================
    # ADIM 8: SIDEBAR FEATURES
    # ========================================================================
    
    with st.sidebar:
        st.markdown("# ⚙️ Ayarlar")
        
        # Model Bilgileri
        st.markdown("---")
        st.markdown("### 🤖 Model Bilgileri")
        st.markdown(f"""
        <div style='
            background: #16213e;
            padding: 1rem;
            border-radius: 10px;
            border-left: 4px solid #6b5b95;
        '>
            <p style='margin: 0.3rem 0;'><strong>Device:</strong> {device_info['device']}</p>
            <p style='margin: 0.3rem 0;'><strong>CUDA:</strong> {device_info['cuda_available']}</p>
            <p style='margin: 0.3rem 0;'><strong>Model:</strong> {model_info.get('model_name', 'BERT')}</p>
            <p style='margin: 0.3rem 0;'><strong>Duygular:</strong> {len(emotion_labels)}</p>
        </div>
        """, unsafe_allow_html=True)
        
        # Gelişmiş Ayarlar
        st.markdown("---")
        st.markdown("### 🎛️ Gelişmiş Ayarlar")
        
        # Max length slider
        max_token_length = st.slider(
            "Maksimum Token Uzunluğu",
            min_value=64,
            max_value=512,
            value=128,
            step=64,
            help="BERT modeli için maksimum token uzunluğu. Daha uzun metinler için artırın."
        )
        
        # Confidence threshold
        confidence_threshold = st.slider(
            "Güven Eşiği (%)",
            min_value=0,
            max_value=100,
            value=50,
            step=5,
            help="Bu değerin altındaki tahminler düşük güvenli olarak işaretlenir."
        )
        
        # Show probabilities
        show_all_probs = st.checkbox(
            "Tüm Olasılıkları Göster",
            value=True,
            help="Tüm duyguların olasılık dağılımını göster"
        )
        
        # Show technical details
        show_tech_details = st.checkbox(
            "Teknik Detayları Göster",
            value=True,
            help="İşlem süresi, token sayısı gibi teknik bilgileri göster"
        )
        
        # İstatistikler
        st.markdown("---")
        st.markdown("### 📊 Session İstatistikleri")
        
        # Session state için analiz sayacı
        if 'analysis_count' not in st.session_state:
            st.session_state.analysis_count = 0
        
        if 'total_inference_time' not in st.session_state:
            st.session_state.total_inference_time = 0.0
        
        # Veritabanı İstatistikleri
        st.markdown("---")
        st.markdown("### 🗄️ Veritabanı İstatistikleri")
        
        db_stats = db.get_statistics()
        
        col1, col2 = st.columns(2)
        with col1:
            st.metric("Toplam Kayıt", db_stats['total_count'])
        with col2:
            st.metric("Ort. Güven", f"{db_stats['avg_confidence']:.1f}%")
        
        # En popüler duygu
        if db_stats['emotion_distribution']:
            top_emotion = max(db_stats['emotion_distribution'].items(), key=lambda x: x[1])
            st.info(f"📊 **En Çok:** {top_emotion[0]} ({top_emotion[1]} kez)")
        
        # Raporlama butonu
        if st.button("📊 Detaylı Rapor Görüntüle", use_container_width=True):
            st.session_state.show_report = True
        
        # Hakkında
        st.markdown("---")
        st.markdown("### ℹ️ Hakkında")
        st.info("""
        **BERT Emotion Analyzer**
        
        🎭 6 Farklı Duygu
        🧠 BERT Modeli
        ⚡ Gerçek Zamanlı
        🎨 Dark Pastel UI
        🗄️ SQLite3 Logging
        
        v1.0.0 - 2026
        """)
        
        # Reset button
        if st.button("🔄 Session'ı Sıfırla", use_container_width=True):
            st.session_state.analysis_count = 0
            st.session_state.total_inference_time = 0.0
            st.rerun()
        
        # Database temizleme (dikkatli!)
        with st.expander("⚠️ Tehlikeli Bölge"):
            if st.button("🗑️ Tüm Veritabanını Temizle", type="secondary"):
                db.clear_all_data()
                st.success("✅ Veritabanı temizlendi!")
                st.rerun()
    
    # Session state'e ayarları kaydet
    if 'max_token_length' not in st.session_state:
        st.session_state.max_token_length = max_token_length
    if 'confidence_threshold' not in st.session_state:
        st.session_state.confidence_threshold = confidence_threshold
    if 'show_all_probs' not in st.session_state:
        st.session_state.show_all_probs = show_all_probs
    if 'show_tech_details' not in st.session_state:
        st.session_state.show_tech_details = show_tech_details
    
    # ========================================================================
    # Metrik Dashboard
    create_metrics_dashboard()
    
    # Divider
    create_divider(color="linear-gradient(90deg, #a8dadc 0%, #c8b6ff 100%)", height="3px")
    
    # Duygu Paletini Göster
    create_emotion_palette()
    
    # Divider
    create_divider()
    
    # ========================================================================
    # ADIM 5: USER INPUT INTERFACE
    # ========================================================================
    
    # Metin girişi ve analiz butonu
    user_text, analyze_clicked = create_text_input_section()
    
    # ========================================================================
    # ADIM 6: PREDICTION ENGINE
    # ========================================================================
    
    # Analiz butonuna basıldığında
    if analyze_clicked and user_text.strip():
        
        # İstatistikleri güncelle
        st.session_state.analysis_count += 1
        
        # Tahmin yap (sidebar'dan gelen max_token_length kullan)
        with st.spinner("🔮 Duygu analizi yapılıyor..."):
            predictions = predict_emotion(
                text=user_text,
                model=model,
                tokenizer=tokenizer,
                device=device,
                emotion_labels=emotion_labels,
                max_length=max_token_length
            )
        
        # İnference time'ı kaydet ve veritabanına kaydet
        if predictions.get("success"):
            st.session_state.total_inference_time += predictions.get("inference_time", 0)
            
            # EMOTION_CONFIG'den doğru emotion name'i al
            predicted_class = predictions["predicted_class"]
            emotion_name = EMOTION_CONFIG.get(predicted_class, {}).get('name', 'Bilinmiyor')
            
            # Predictions dictionary'yi güncelle
            predictions_with_correct_name = predictions.copy()
            predictions_with_correct_name["predicted_emotion"] = emotion_name
            
            # Veritabanına kaydet
            analysis_id = db.insert_analysis(
                text=user_text,
                predictions=predictions_with_correct_name,
                device=device_info['device'],
                model_name=model_info.get('model_name', 'BERT')
            )
        
        # Sonuçları kontrol et
        if predictions.get("success"):
            
            # Başarı mesajı
            st.success("✅ Analiz tamamlandı!", icon="🎉")
            
            # Ana sonuç kartı
            predicted_emotion = predictions["predicted_emotion"]
            predicted_class = predictions["predicted_class"]
            confidence = predictions["confidence"]
            confidence_pct = predictions["confidence_percentage"]
            confidence_level = format_confidence_level(confidence)
            confidence_color = get_confidence_color(confidence)
            
            # EMOTION_CONFIG'den bilgi al (index kullanarak)
            emotion_info = EMOTION_CONFIG.get(predicted_class, {
                "emoji": "❓",
                "name": predicted_emotion,
                "color": "#6b5b95",
                "gradient": "linear-gradient(135deg, #6b5b95 0%, #524470 100%)"
            })
            
            # Büyük sonuç kartı
            st.markdown(f"""
                <div style='
                    background: linear-gradient(135deg, {confidence_color}40 0%, {confidence_color}20 100%);
                    border-left: 6px solid {confidence_color};
                    padding: 2rem;
                    border-radius: 15px;
                    margin: 2rem 0;
                    text-align: center;
                '>
                    <div style='font-size: 4rem; margin-bottom: 1rem;'>
                        {emotion_info['emoji']}
                    </div>
                    <h2 style='
                        color: #ffffff;
                        font-size: 2.5rem;
                        font-weight: 700;
                        margin-bottom: 0.5rem;
                    '>
                        {emotion_info['name']}
                    </h2>
                    <p style='
                        color: #b0b0b0;
                        font-size: 1.3rem;
                        margin-bottom: 1rem;
                    '>
                        Güven Skoru: <strong style='color: {confidence_color};'>{confidence_pct:.1f}%</strong>
                    </p>
                    <div style='
                        display: inline-block;
                        background: {confidence_color};
                        color: white;
                        padding: 0.5rem 1.5rem;
                        border-radius: 25px;
                        font-weight: 600;
                    '>
                        {confidence_level}
                    </div>
                </div>
            """, unsafe_allow_html=True)
            
            # Tüm duyguların olasılıkları
            if show_all_probs:
                st.markdown("### 📊 Tüm Duygu Olasılıkları")
                
                # Emotion indexlerini al ve sırala
                emotion_probabilities = []
                for idx in range(len(EMOTION_CONFIG)):
                    emotion_name = emotion_labels.get(idx, f"Emotion_{idx}")
                    if emotion_name in predictions["all_emotions"]:
                        emotion_probabilities.append((
                            idx,
                            emotion_name,
                            predictions["all_emotions"][emotion_name]["probability"]
                        ))
                
                # Olasılığa göre sırala
                emotion_probabilities.sort(key=lambda x: x[2], reverse=True)
                
                for idx, emotion_name, prob in emotion_probabilities:
                    pct = prob * 100
                    
                    # Emotion config'den bilgi al
                    emotion_cfg = EMOTION_CONFIG.get(idx, {
                        "emoji": "🔹",
                        "name": emotion_name,
                        "color": "#6b5b95"
                    })
                    
                    emoji = emotion_cfg['emoji']
                    display_name = emotion_cfg['name']
                    color = emotion_cfg['color']
                
                # Progress bar
                st.markdown(f"""
                    <div style='margin: 1rem 0;'>
                        <div style='
                            display: flex;
                            justify-content: space-between;
                            margin-bottom: 0.5rem;
                        '>
                            <span style='color: #ffffff; font-weight: 600;'>
                                {emoji} {display_name}
                            </span>
                            <span style='color: {color}; font-weight: 700;'>
                                {pct:.1f}%
                            </span>
                        </div>
                        <div style='
                            background: #16213e;
                            border-radius: 10px;
                            height: 12px;
                            overflow: hidden;
                        '>
                            <div style='
                                background: {color};
                                width: {pct}%;
                                height: 100%;
                                border-radius: 10px;
                                transition: width 0.5s ease;
                            '></div>
                        </div>
                    </div>
                """, unsafe_allow_html=True)
            
            # Güven uyarısı
            if confidence_pct < confidence_threshold:
                st.warning(f"⚠️ Düşük Güven: Tahmin güveni belirlediğiniz eşik değerinin ({confidence_threshold}%) altında. Sonuçlar daha az güvenilir olabilir.")
            
            # Teknik detaylar (expander)
            if show_tech_details:
                with st.expander("🔍 Teknik Detaylar"):
                    col1, col2, col3 = st.columns(3)
                    
                    with col1:
                        st.metric("İşlem Süresi", f"{predictions['inference_time']*1000:.1f} ms")
                    
                    with col2:
                        st.metric("Token Sayısı", predictions['token_count'])
                    
                    with col3:
                        st.metric("Max Length", predictions['max_length'])
                    
                    st.markdown("**Analiz Edilen Metin:**")
                    st.code(user_text, language=None)
        
        else:
            # ====================================================================
            # ADIM 9: ERROR HANDLING
            # ====================================================================
            
            # Hata durumu - Gelişmiş hata gösterimi
            st.error("❌ Analiz Sırasında Hata Oluştu", icon="🚨")
            
            error_message = predictions.get('message', 'Bilinmeyen hata')
            error_detail = predictions.get('error', '')
            
            # Hata kartı
            st.markdown(f"""
                <div style='
                    background: #8b4f5c20;
                    border-left: 4px solid #8b4f5c;
                    padding: 1.5rem;
                    border-radius: 10px;
                    margin: 1rem 0;
                '>
                    <h4 style='color: #ffffff; margin-bottom: 0.5rem;'>
                        🔍 Hata Detayları
                    </h4>
                    <p style='color: #b0b0b0; margin: 0.5rem 0;'>
                        <strong>Mesaj:</strong> {error_message}
                    </p>
                </div>
            """, unsafe_allow_html=True)
            
            # Teknik hata detayı (expander)
            if error_detail:
                with st.expander("🛠️ Teknik Detaylar (Geliştiriciler İçin)"):
                    st.code(error_detail, language="python")
            
            # Çözüm önerileri
            st.markdown("### 💡 Çözüm Önerileri")
            st.info("""
            - ✅ Metin en az 3 karakter uzunluğunda olmalı
            - ✅ Özel karakterler soruna neden olabilir
            - ✅ Çok uzun metinler için token uzunluğunu artırın
            - ✅ Sayfa yenilenirse sorun çözülebilir
            """)
            
            # Tekrar dene butonu
            if st.button("🔄 Yeniden Dene", type="primary"):
                st.rerun()
    
    # ========================================================================
    # REPORTING SECTION
    # ========================================================================
    
    # Rapor görüntüleme
    if st.session_state.get('show_report', False):
        st.markdown("---")
        st.markdown("# 📊 Detaylı Analiz Raporu")
        
        # Genel İstatistikler
        stats = db.get_statistics()
        
        st.markdown("## 📈 Genel İstatistikler")
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            st.metric("Toplam Analiz", stats['total_count'])
        with col2:
            st.metric("Ort. Güven", f"{stats['avg_confidence']:.1f}%")
        with col3:
            st.metric("Ort. Süre", f"{stats['avg_inference_time']*1000:.0f}ms")
        with col4:
            st.metric("Toplam Token", f"{stats['total_tokens']:,}")
        
        # Duygu Dağılımı Grafiği
        if stats['emotion_distribution']:
            st.markdown("## 🎭 Duygu Dağılımı")
            
            emotions = list(stats['emotion_distribution'].keys())
            counts = list(stats['emotion_distribution'].values())
            
            # Renkleri EMOTION_CONFIG'den al
            colors = []
            for emotion in emotions:
                for idx, cfg in EMOTION_CONFIG.items():
                    if cfg['name'] == emotion:
                        colors.append(cfg['color'])
                        break
            
            fig = go.Figure(data=[go.Bar(
                x=emotions,
                y=counts,
                marker_color=colors,
                text=counts,
                textposition='auto',
            )])
            
            fig.update_layout(
                title="Duygu Kategorilerine Göre Analiz Sayıları",
                xaxis_title="Duygu",
                yaxis_title="Analiz Sayısı",
                plot_bgcolor='#1a1a2e',
                paper_bgcolor='#1a1a2e',
                font=dict(color='#ffffff'),
                height=400
            )
            
            st.plotly_chart(fig, use_container_width=True)
            
            # Pasta grafiği
            fig_pie = go.Figure(data=[go.Pie(
                labels=emotions,
                values=counts,
                marker=dict(colors=colors),
                hole=0.3
            )])
            
            fig_pie.update_layout(
                title="Duygu Dağılımı (Yüzdelik)",
                plot_bgcolor='#1a1a2e',
                paper_bgcolor='#1a1a2e',
                font=dict(color='#ffffff'),
                height=400
            )
            
            st.plotly_chart(fig_pie, use_container_width=True)
        
        # Son Analizler
        st.markdown("## 🕐 Son Analizler")
        recent = db.get_recent_analyses(limit=20)
        
        if recent:
            import pandas as pd
            df_recent = pd.DataFrame(recent)
            df_recent['timestamp'] = pd.to_datetime(df_recent['timestamp'])
            df_recent['confidence_percentage'] = df_recent['confidence_percentage'].round(1)
            df_recent['inference_time'] = (df_recent['inference_time'] * 1000).round(1)
            
            st.dataframe(
                df_recent[['timestamp', 'text', 'predicted_emotion', 'confidence_percentage', 'inference_time']],
                use_container_width=True,
                height=400
            )
        
        # Export Butonu
        st.markdown("## 💾 Veri Export")
        col1, col2 = st.columns(2)
        
        with col1:
            if st.button("📥 CSV Olarak İndir", use_container_width=True):
                import tempfile
                from datetime import datetime
                with tempfile.NamedTemporaryFile(delete=False, suffix='.csv') as tmp:
                    db.export_to_csv(tmp.name)
                    with open(tmp.name, 'rb') as f:
                        st.download_button(
                            label="⬇️ İndir",
                            data=f,
                            file_name=f"analysis_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv",
                            mime="text/csv"
                        )
        
        with col2:
            if st.button("❌ Raporu Kapat", use_container_width=True):
                st.session_state.show_report = False
                st.rerun()
    
    # ========================================================================
    # FOOTER
    # ========================================================================
    
    create_footer()

if __name__ == "__main__":
    main()

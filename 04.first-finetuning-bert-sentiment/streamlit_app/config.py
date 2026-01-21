"""
🎨 Konfigürasyon Dosyası - Pastel Tema
======================================
Merkezi yapılandırma ve tasarım ayarları
"""

import os
from pathlib import Path

# ============================================================================
# 📁 DOSYA YOLLARI
# ============================================================================

# Ana dizin
BASE_DIR = Path(__file__).parent
MODEL_DIR = BASE_DIR.parent / "bert_emotion_model"

# ============================================================================
# 🎨 PASTEL RENK PALETİ - Modern & Soft
# ============================================================================

class Colors:
    """Dark pastel renk şeması"""
    
    # Ana Dark Pastel Renkler
    PRIMARY = "#4a7c7e"          # Dark Cyan
    SECONDARY = "#8b4f5c"        # Dark Pink
    ACCENT = "#6b5b95"           # Dark Purple
    SUCCESS = "#5a7c50"          # Dark Green
    WARNING = "#8b7355"          # Dark Orange
    ERROR = "#8b6355"            # Dark Coral
    INFO = "#4a7c8e"             # Dark Blue
    
    # Gradient Backgrounds (Dark Pastel)
    GRADIENT_1 = "linear-gradient(135deg, #4a7c7e 0%, #356063 100%)"  # Dark blue gradient
    GRADIENT_2 = "linear-gradient(135deg, #8b4f5c 0%, #6b3d47 100%)"  # Dark pink gradient
    GRADIENT_3 = "linear-gradient(135deg, #6b5b95 0%, #524470 100%)"  # Dark purple gradient
    GRADIENT_4 = "linear-gradient(135deg, #5a7c50 0%, #445d3b 100%)"  # Dark green gradient
    GRADIENT_5 = "linear-gradient(135deg, #8b7355 0%, #6b5940 100%)"  # Dark orange gradient
    
    # Text Colors (Dark Theme)
    TEXT_DARK = "#ffffff"        # Beyaz (dark theme için)
    TEXT_LIGHT = "#b0b0b0"       # Açık gri
    TEXT_WHITE = "#ffffff"       # Beyaz
    
    # Background Colors (Dark Theme)
    BG_LIGHT = "#16213e"         # Dark blue-gray
    BG_WHITE = "#1a1a2e"         # Dark blue-gray
    BG_CARD = "#16213e"          # Card background
    
    # Border Colors (Dark Theme)
    BORDER_LIGHT = "#2d3e5f"     # Dark border
    BORDER_MEDIUM = "#3d4e6f"    # Medium dark border

# ============================================================================
# 🎭 DUYGU ETİKETLERİ VE RENK KODLARI (Dark Pastel)
# ============================================================================

EMOTION_CONFIG = {
    0: {
        "name": "Üzüntü",
        "emoji": "😢",
        "color": "#4a7c8e",          # Dark blue
        "description": "Üzgün, melankolik, hüzünlü",
        "gradient": "linear-gradient(135deg, #4a7c8e 0%, #356069 100%)"
    },
    1: {
        "name": "Mutluluk", 
        "emoji": "😊",
        "color": "#8b7355",          # Dark orange
        "description": "Mutlu, neşeli, sevinçli",
        "gradient": "linear-gradient(135deg, #8b7355 0%, #6b5940 100%)"
    },
    2: {
        "name": "Sevgi",
        "emoji": "❤️",
        "color": "#8b4f5c",          # Dark pink
        "description": "Sevgi dolu, şefkatli, romantic",
        "gradient": "linear-gradient(135deg, #8b4f5c 0%, #6b3d47 100%)"
    },
    3: {
        "name": "Öfke",
        "emoji": "😠",
        "color": "#8b6355",          # Dark coral
        "description": "Öfkeli, sinirli, kızgın",
        "gradient": "linear-gradient(135deg, #8b6355 0%, #6b4940 100%)"
    },
    4: {
        "name": "Korku",
        "emoji": "😨",
        "color": "#6b5b95",          # Dark purple
        "description": "Korkmuş, endişeli, tedirgin",
        "gradient": "linear-gradient(135deg, #6b5b95 0%, #524470 100%)"
    },
    5: {
        "name": "Şaşkınlık",
        "emoji": "😮",
        "color": "#5a7c50",          # Dark green
        "description": "Şaşırmış, hayret etmiş",
        "gradient": "linear-gradient(135deg, #5a7c50 0%, #445d3b 100%)"
    }
}

# ============================================================================
# ⚙️ MODEL AYARLARI
# ============================================================================

class ModelConfig:
    """Model yapılandırma parametreleri"""
    
    MODEL_PATH = str(MODEL_DIR)
    MAX_LENGTH = 66
    DEVICE = "cpu"  # "cuda" for GPU
    
    # Cache settings
    CACHE_TTL = 3600  # 1 saat

# ============================================================================
# 🎯 UI AYARLARI
# ============================================================================

class UIConfig:
    """Kullanıcı arayüzü ayarları"""
    
    # Sayfa başlığı
    PAGE_TITLE = "🎭 BERT Emotion Analyzer"
    PAGE_SUBTITLE = "Yapay Zeka Destekli Duygu Analizi Platformu"
    
    # Sidebar
    SIDEBAR_TITLE = "⚙️ Ayarlar & Bilgiler"
    
    # Animasyonlar
    LOADING_TEXT = "🔄 Model yükleniyor..."
    ANALYZING_TEXT = "🧠 Analiz ediliyor..."
    
    # Placeholder metinler
    EXAMPLE_TEXTS = [
        "I am so happy and excited about this wonderful news!",
        "This makes me really sad and disappointed.",
        "I love spending quality time with my family.",
        "I'm extremely angry about this situation!",
        "I'm scared and worried about what might happen.",
        "Wow! I can't believe this just happened!"
    ]
    
    # Footer
    FOOTER_TEXT = "Made with ❤️ using Streamlit & BERT by Cemal YÜKSEL for phD Thesis."
    VERSION = "v1.0.0"

# ============================================================================
# 📊 METRİK AYARLARI
# ============================================================================

class MetricsConfig:
    """Model metrikleri (gerçek değerler daha sonra yüklenecek)"""
    
    ACCURACY = 0.93
    F1_SCORE = 0.93
    PRECISION = 0.93
    RECALL = 0.93

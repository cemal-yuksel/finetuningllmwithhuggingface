"""
🤖 Model Loader - BERT Model Yükleme ve Önbellekleme
====================================================
Performans için @st.cache_resource ile optimize edilmiş
"""

import streamlit as st
import torch
from transformers import BertTokenizer, BertForSequenceClassification
from pathlib import Path
import json
from typing import Tuple, Dict, Optional
import time


@st.cache_resource(show_spinner=False)
def load_bert_model(model_path: str) -> Tuple[BertForSequenceClassification, BertTokenizer, Dict]:
    """
    BERT modelini ve tokenizer'ı yükler (önbelleklenmiş)
    
    Args:
        model_path: Model dizini
        
    Returns:
        Tuple[model, tokenizer, emotion_labels]
    """
    try:
        model_dir = Path(model_path)
        
        # Model dosyalarının varlığını kontrol et
        if not model_dir.exists():
            raise FileNotFoundError(f"Model dizini bulunamadı: {model_dir}")
        
        # Model dosyalarını kontrol et
        required_files = ["config.json", "pytorch_model.bin"]
        missing_files = [f for f in required_files if not (model_dir / f).exists()]
        
        if missing_files:
            raise FileNotFoundError(f"Eksik model dosyaları: {missing_files}")
        
        # Device ayarla (GPU varsa kullan)
        device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        
        # Tokenizer yükle
        tokenizer = BertTokenizer.from_pretrained(model_dir)
        
        # Model yükle
        model = BertForSequenceClassification.from_pretrained(model_dir)
        model.to(device)
        model.eval()
        
        # Emotion labels yükle
        emotion_labels_path = model_dir / "emotion_labels.json"
        if emotion_labels_path.exists():
            with open(emotion_labels_path, 'r', encoding='utf-8') as f:
                emotion_labels = json.load(f)
        else:
            # Default emotion labels
            emotion_labels = {
                0: "Üzüntü",
                1: "Mutluluk",
                2: "Sevgi",
                3: "Öfke",
                4: "Korku",
                5: "Şaşkınlık"
            }
        
        return model, tokenizer, emotion_labels, device
        
    except Exception as e:
        st.error(f"❌ Model yükleme hatası: {str(e)}")
        raise


def get_model_info(model_path: str) -> Dict:
    """
    Model bilgilerini okur
    
    Args:
        model_path: Model dizini
        
    Returns:
        Model bilgileri dictionary
    """
    try:
        model_dir = Path(model_path)
        info_path = model_dir / "model_info.json"
        
        if info_path.exists():
            with open(info_path, 'r', encoding='utf-8') as f:
                return json.load(f)
        else:
            return {
                "model_name": "BERT Emotion Classifier",
                "version": "1.0.0",
                "accuracy": "N/A",
                "training_date": "N/A"
            }
    except Exception as e:
        st.warning(f"⚠️ Model bilgileri okunamadı: {str(e)}")
        return {}


def check_model_availability(model_path: str) -> bool:
    """
    Model dosyalarının varlığını kontrol eder
    
    Args:
        model_path: Model dizini
        
    Returns:
        True/False
    """
    try:
        model_dir = Path(model_path)
        
        if not model_dir.exists():
            return False
        
        required_files = ["config.json", "pytorch_model.bin"]
        
        for file in required_files:
            if not (model_dir / file).exists():
                return False
        
        return True
        
    except Exception:
        return False


@st.cache_data(show_spinner=False)
def get_device_info() -> Dict[str, str]:
    """
    Cihaz bilgilerini döndürür
    
    Returns:
        Device bilgileri
    """
    device_info = {
        "device": "CPU",
        "cuda_available": "Hayır",
        "device_name": "CPU"
    }
    
    if torch.cuda.is_available():
        device_info["device"] = "GPU"
        device_info["cuda_available"] = "Evet"
        device_info["device_name"] = torch.cuda.get_device_name(0)
    
    return device_info


def display_loading_animation():
    """
    Model yüklenirken animasyon gösterir
    """
    with st.spinner(""):
        st.markdown("""
            <div style="text-align: center; padding: 2rem;">
                <div style="
                    display: inline-block;
                    width: 60px;
                    height: 60px;
                    border: 6px solid #16213e;
                    border-top: 6px solid #6b5b95;
                    border-radius: 50%;
                    animation: spin 1s linear infinite;
                "></div>
                <style>
                    @keyframes spin {
                        0% { transform: rotate(0deg); }
                        100% { transform: rotate(360deg); }
                    }
                </style>
                <p style="margin-top: 1rem; color: #ffffff; font-size: 1.1rem;">
                    🤖 Model yükleniyor...
                </p>
            </div>
        """, unsafe_allow_html=True)

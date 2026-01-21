"""
🔮 Predictor - BERT Duygu Tahmini Motoru
========================================
Model ile tahmin yapma ve sonuç işleme
"""

import torch
import numpy as np
from typing import Dict, List, Tuple
import time


def predict_emotion(
    text: str,
    model,
    tokenizer,
    device,
    emotion_labels: Dict[int, str],
    max_length: int = 128
) -> Dict:
    """
    Metin için duygu tahmini yapar
    
    Args:
        text: Analiz edilecek metin
        model: BERT modeli
        tokenizer: BERT tokenizer
        device: torch device (cpu/cuda)
        emotion_labels: Duygu etiketleri dictionary
        max_length: Maksimum token uzunluğu
        
    Returns:
        Tahmin sonuçları dictionary
    """
    
    # Başlangıç zamanı
    start_time = time.time()
    
    try:
        # Metni temizle
        text = text.strip()
        
        if not text:
            return {
                "success": False,
                "error": "Boş metin",
                "message": "Lütfen analiz edilecek bir metin girin"
            }
        
        # Tokenize et
        encoding = tokenizer.encode_plus(
            text,
            add_special_tokens=True,
            max_length=max_length,
            padding='max_length',
            truncation=True,
            return_attention_mask=True,
            return_tensors='pt'
        )
        
        # Device'a taşı
        input_ids = encoding['input_ids'].to(device)
        attention_mask = encoding['attention_mask'].to(device)
        
        # Tahmin yap
        model.eval()
        with torch.no_grad():
            outputs = model(
                input_ids=input_ids,
                attention_mask=attention_mask
            )
            
            logits = outputs.logits
            
            # Softmax ile olasılıkları hesapla
            probabilities = torch.softmax(logits, dim=1)
            probabilities = probabilities.cpu().numpy()[0]
            
            # En yüksek olasılıklı duyguyu bul
            predicted_class = np.argmax(probabilities)
            predicted_emotion = emotion_labels.get(predicted_class, "Bilinmiyor")
            confidence = float(probabilities[predicted_class])
        
        # Süre hesapla
        inference_time = time.time() - start_time
        
        # Tüm duyguların olasılıklarını hazırla
        all_emotions = {}
        for idx, prob in enumerate(probabilities):
            emotion_name = emotion_labels.get(idx, f"Emotion_{idx}")
            all_emotions[emotion_name] = {
                "probability": float(prob),
                "percentage": float(prob * 100),
                "index": idx
            }
        
        # Sonuçları döndür
        return {
            "success": True,
            "text": text,
            "predicted_emotion": predicted_emotion,
            "predicted_class": int(predicted_class),
            "confidence": confidence,
            "confidence_percentage": confidence * 100,
            "all_emotions": all_emotions,
            "inference_time": inference_time,
            "token_count": int(attention_mask.sum()),
            "max_length": max_length
        }
        
    except Exception as e:
        return {
            "success": False,
            "error": str(e),
            "message": f"Tahmin sırasında hata oluştu: {str(e)}"
        }


def get_top_emotions(predictions: Dict, top_n: int = 3) -> List[Tuple[str, float]]:
    """
    En yüksek olasılıklı duyguları döndür
    
    Args:
        predictions: Tahmin sonuçları
        top_n: Kaç tane duygu döndürülecek
        
    Returns:
        List of (emotion_name, probability) tuples
    """
    if not predictions.get("success"):
        return []
    
    all_emotions = predictions.get("all_emotions", {})
    
    # Olasılıklara göre sırala
    sorted_emotions = sorted(
        all_emotions.items(),
        key=lambda x: x[1]["probability"],
        reverse=True
    )
    
    # Top N'i döndür
    return [(name, data["probability"]) for name, data in sorted_emotions[:top_n]]


def format_confidence_level(confidence: float) -> str:
    """
    Güven seviyesini metinsel olarak döndür
    
    Args:
        confidence: Güven skoru (0-1)
        
    Returns:
        Güven seviyesi metni
    """
    if confidence >= 0.9:
        return "Çok Yüksek 🔥"
    elif confidence >= 0.75:
        return "Yüksek ✅"
    elif confidence >= 0.6:
        return "Orta 📊"
    elif confidence >= 0.4:
        return "Düşük ⚠️"
    else:
        return "Çok Düşük ⚡"


def get_confidence_color(confidence: float) -> str:
    """
    Güven skoruna göre renk döndür (dark pastel theme)
    
    Args:
        confidence: Güven skoru (0-1)
        
    Returns:
        Hex color code
    """
    if confidence >= 0.9:
        return "#5a7c50"  # Dark green
    elif confidence >= 0.75:
        return "#4a7c7e"  # Dark cyan
    elif confidence >= 0.6:
        return "#6b5b95"  # Dark purple
    elif confidence >= 0.4:
        return "#8b7355"  # Dark orange
    else:
        return "#8b4f5c"  # Dark pink

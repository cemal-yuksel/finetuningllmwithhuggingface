"""
🗄️ Database Manager - SQLite3 ile Analiz Geçmişi Yönetimi
==========================================================
Tüm analizleri kaydeder ve raporlama için veri sağlar
"""

import sqlite3
import json
from datetime import datetime
from pathlib import Path
from typing import List, Dict, Optional
import pandas as pd


class AnalysisDatabase:
    """Analiz veritabanı yöneticisi"""
    
    def __init__(self, db_path: str = "analysis_history.db"):
        """
        Args:
            db_path: SQLite database dosya yolu
        """
        self.db_path = db_path
        self.create_tables()
    
    def get_connection(self):
        """Veritabanı bağlantısı oluştur"""
        return sqlite3.connect(self.db_path)
    
    def create_tables(self):
        """Gerekli tabloları oluştur"""
        conn = self.get_connection()
        cursor = conn.cursor()
        
        # Analyses tablosu
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS analyses (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
                text TEXT NOT NULL,
                predicted_emotion TEXT NOT NULL,
                predicted_class INTEGER NOT NULL,
                confidence REAL NOT NULL,
                confidence_percentage REAL NOT NULL,
                all_emotions_json TEXT,
                inference_time REAL,
                token_count INTEGER,
                max_length INTEGER,
                device TEXT,
                model_name TEXT
            )
        """)
        
        # İndeksler
        cursor.execute("""
            CREATE INDEX IF NOT EXISTS idx_timestamp 
            ON analyses(timestamp DESC)
        """)
        
        cursor.execute("""
            CREATE INDEX IF NOT EXISTS idx_emotion 
            ON analyses(predicted_emotion)
        """)
        
        conn.commit()
        conn.close()
    
    def insert_analysis(
        self,
        text: str,
        predictions: Dict,
        device: str = "CPU",
        model_name: str = "BERT"
    ) -> int:
        """
        Analiz sonucunu veritabanına kaydet
        
        Args:
            text: Analiz edilen metin
            predictions: Tahmin sonuçları dictionary
            device: Kullanılan cihaz (CPU/GPU)
            model_name: Model adı
            
        Returns:
            Eklenen kaydın ID'si
        """
        if not predictions.get("success"):
            return -1
        
        conn = self.get_connection()
        cursor = conn.cursor()
        
        # all_emotions'ı JSON string'e çevir
        all_emotions_json = json.dumps(predictions.get("all_emotions", {}))
        
        cursor.execute("""
            INSERT INTO analyses (
                text, predicted_emotion, predicted_class,
                confidence, confidence_percentage,
                all_emotions_json, inference_time,
                token_count, max_length, device, model_name
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            text,
            predictions["predicted_emotion"],
            predictions["predicted_class"],
            predictions["confidence"],
            predictions["confidence_percentage"],
            all_emotions_json,
            predictions.get("inference_time", 0),
            predictions.get("token_count", 0),
            predictions.get("max_length", 128),
            device,
            model_name
        ))
        
        analysis_id = cursor.lastrowid
        conn.commit()
        conn.close()
        
        return analysis_id
    
    def get_all_analyses(self, limit: Optional[int] = None) -> pd.DataFrame:
        """
        Tüm analizleri DataFrame olarak getir
        
        Args:
            limit: Maksimum kayıt sayısı (None = hepsi)
            
        Returns:
            pandas DataFrame
        """
        conn = self.get_connection()
        
        query = """
            SELECT 
                id, timestamp, text, predicted_emotion,
                confidence_percentage, inference_time,
                token_count, device
            FROM analyses
            ORDER BY timestamp DESC
        """
        
        if limit:
            query += f" LIMIT {limit}"
        
        df = pd.read_sql_query(query, conn)
        conn.close()
        
        return df
    
    def get_statistics(self) -> Dict:
        """
        Genel istatistikleri hesapla
        
        Returns:
            İstatistik dictionary
        """
        conn = self.get_connection()
        cursor = conn.cursor()
        
        # Toplam analiz sayısı
        cursor.execute("SELECT COUNT(*) FROM analyses")
        total_count = cursor.fetchone()[0]
        
        # Duygu dağılımı
        cursor.execute("""
            SELECT predicted_emotion, COUNT(*) as count
            FROM analyses
            GROUP BY predicted_emotion
            ORDER BY count DESC
        """)
        emotion_distribution = dict(cursor.fetchall())
        
        # Ortalama güven skoru
        cursor.execute("SELECT AVG(confidence_percentage) FROM analyses")
        avg_confidence = cursor.fetchone()[0] or 0
        
        # Ortalama inference time
        cursor.execute("SELECT AVG(inference_time) FROM analyses")
        avg_inference_time = cursor.fetchone()[0] or 0
        
        # Toplam token sayısı
        cursor.execute("SELECT SUM(token_count) FROM analyses")
        total_tokens = cursor.fetchone()[0] or 0
        
        # İlk ve son analiz
        cursor.execute("SELECT MIN(timestamp), MAX(timestamp) FROM analyses")
        first_analysis, last_analysis = cursor.fetchone()
        
        # Device dağılımı
        cursor.execute("""
            SELECT device, COUNT(*) as count
            FROM analyses
            GROUP BY device
        """)
        device_distribution = dict(cursor.fetchall())
        
        conn.close()
        
        return {
            "total_count": total_count,
            "emotion_distribution": emotion_distribution,
            "avg_confidence": avg_confidence,
            "avg_inference_time": avg_inference_time,
            "total_tokens": total_tokens,
            "first_analysis": first_analysis,
            "last_analysis": last_analysis,
            "device_distribution": device_distribution
        }
    
    def get_recent_analyses(self, limit: int = 10) -> List[Dict]:
        """
        Son N analizi getir
        
        Args:
            limit: Maksimum kayıt sayısı
            
        Returns:
            Analiz listesi
        """
        conn = self.get_connection()
        cursor = conn.cursor()
        
        cursor.execute("""
            SELECT 
                id, timestamp, text, predicted_emotion,
                confidence_percentage, inference_time
            FROM analyses
            ORDER BY timestamp DESC
            LIMIT ?
        """, (limit,))
        
        columns = [desc[0] for desc in cursor.description]
        results = []
        
        for row in cursor.fetchall():
            results.append(dict(zip(columns, row)))
        
        conn.close()
        return results
    
    def search_by_emotion(self, emotion: str) -> pd.DataFrame:
        """
        Belirli bir duyguya göre arama yap
        
        Args:
            emotion: Aranacak duygu
            
        Returns:
            pandas DataFrame
        """
        conn = self.get_connection()
        
        query = """
            SELECT 
                id, timestamp, text, predicted_emotion,
                confidence_percentage, inference_time
            FROM analyses
            WHERE predicted_emotion = ?
            ORDER BY timestamp DESC
        """
        
        df = pd.read_sql_query(query, conn, params=(emotion,))
        conn.close()
        
        return df
    
    def clear_all_data(self):
        """Tüm verileri sil (dikkatli kullan!)"""
        conn = self.get_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM analyses")
        conn.commit()
        conn.close()
    
    def export_to_csv(self, filepath: str):
        """
        Tüm verileri CSV'ye export et
        
        Args:
            filepath: Hedef CSV dosya yolu
        """
        df = self.get_all_analyses()
        df.to_csv(filepath, index=False, encoding='utf-8-sig')
    
    def get_emotion_timeline(self) -> pd.DataFrame:
        """
        Zaman içinde duygu dağılımını getir
        
        Returns:
            pandas DataFrame
        """
        conn = self.get_connection()
        
        query = """
            SELECT 
                DATE(timestamp) as date,
                predicted_emotion,
                COUNT(*) as count
            FROM analyses
            GROUP BY date, predicted_emotion
            ORDER BY date DESC
        """
        
        df = pd.read_sql_query(query, conn)
        conn.close()
        
        return df

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Скрипт для создания единого timetable.json файла
из данных парсера транспорта Бреста
"""

import json
import os
from datetime import datetime
from pathlib import Path

def create_timetable():
    """Создает единый timetable.json файл"""
    
    # Загружаем все данные
    timetable = {
        "metadata": {
            "version": "1.0.0",
            "generated_at": datetime.now().isoformat(),
            "source": "brestgortrans.by",
            "transport_types": ["buses", "trolleybuses", "minibuses"],
            "total_routes": 0,
            "total_stops": 0
        },
        "data": {}
    }
    
    total_routes = 0
    total_stops = 0
    
    # Загружаем данные по типам транспорта
    for transport_type in ["buses", "trolleybuses", "minibuses"]:
        json_file = Path(f"data/{transport_type}.json")
        if json_file.exists():
            try:
                with open(json_file, "r", encoding="utf-8") as f:
                    transport_data = json.load(f)
                
                # Добавляем данные
                timetable["data"][transport_type] = transport_data
                
                # Подсчитываем статистику
                routes = transport_data.get("routes", [])
                total_routes += len(routes)
                
                for route in routes:
                    stops = route.get("stops", [])
                    total_stops += len(stops)
                    
                print(f"✓ {transport_type}: {len(routes)} маршрутов")
                
            except Exception as e:
                print(f"✗ Ошибка загрузки {transport_type}: {e}")
                timetable["data"][transport_type] = {"error": str(e)}
        else:
            print(f"⚠ Файл {transport_type}.json не найден")
            timetable["data"][transport_type] = {"error": "File not found"}
    
    # Обновляем общую статистику
    timetable["metadata"]["total_routes"] = total_routes
    timetable["metadata"]["total_stops"] = total_stops
    
    # Сохраняем единый файл
    output_file = Path("data/timetable.json")
    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(timetable, f, ensure_ascii=False, indent=2)
    
    print(f"\n✅ Timetable.json создан успешно!")
    print(f"📊 Всего маршрутов: {total_routes}")
    print(f"🚏 Всего остановок: {total_stops}")
    print(f"📁 Файл: {output_file.absolute()}")
    
    return timetable

def create_meta_json():
    """Создает meta.json с метаданными"""
    
    meta = {
        "last_updated": datetime.now().isoformat(),
        "version": "1.0.0",
        "source": "brestgortrans.by",
        "files": {
            "timetable.json": {
                "description": "Единый файл с данными всех типов транспорта",
                "format": "JSON",
                "encoding": "UTF-8"
            },
            "buses.json": {
                "description": "Данные автобусных маршрутов",
                "format": "JSON",
                "encoding": "UTF-8"
            },
            "trolleybuses.json": {
                "description": "Данные троллейбусных маршрутов", 
                "format": "JSON",
                "encoding": "UTF-8"
            },
            "minibuses.json": {
                "description": "Данные маршрутных такси",
                "format": "JSON",
                "encoding": "UTF-8"
            }
        }
    }
    
    # Сохраняем meta.json
    meta_file = Path("data/meta.json")
    with open(meta_file, "w", encoding="utf-8") as f:
        json.dump(meta, f, ensure_ascii=False, indent=2)
    
    print(f"✅ Meta.json создан: {meta_file.absolute()}")
    return meta

if __name__ == "__main__":
    print("🚌 Создание timetable.json для транспорта Бреста")
    print("=" * 50)
    
    # Создаем папку data если её нет
    Path("data").mkdir(exist_ok=True)
    
    # Создаем файлы
    timetable = create_timetable()
    meta = create_meta_json()
    
    print("\n🎉 Все файлы созданы успешно!")
    print("📱 Теперь можно использовать в мобильном приложении:")
    print("   https://cdn.jsdelivr.net/gh/USERNAME/transport_in_Brest-data@main/data/timetable.json")


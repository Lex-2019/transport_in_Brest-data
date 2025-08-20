# 🚌 Данные транспорта Бреста

**Репозиторий данных** для мобильного приложения общественного транспорта города Бреста.

## 📊 Структура данных

### **Основные файлы:**

- **`data/timetable.json`** - Единый файл со всеми данными транспорта
- **`data/buses.json`** - Автобусные маршруты
- **`data/trolleybuses.json`** - Троллейбусные маршруты  
- **`data/minibuses.json`** - Маршрутные такси
- **`data/meta.json`** - Метаданные и описание файлов

## 🚀 Использование в приложении

### **jsDelivr CDN:**
```javascript
const timetableUrl = 'https://cdn.jsdelivr.net/gh/USERNAME/transport_in_Brest-data@main/data/timetable.json';

fetch(timetableUrl)
  .then(response => response.json())
  .then(data => {
    console.log('Версия:', data.metadata.version);
    console.log('Обновлено:', data.metadata.generated_at);
    console.log('Типы транспорта:', data.metadata.transport_types);
  });
```

### **GitHub Pages (альтернатива):**
```javascript
const timetableUrl = 'https://USERNAME.github.io/transport_in_Brest-data/data/timetable.json';
```

### **GitHub Raw (фолбэк):**
```javascript
const timetableUrl = 'https://raw.githubusercontent.com/USERNAME/transport_in_Brest-data/main/data/timetable.json';
```

## 📱 Пример структуры данных

```json
{
  "metadata": {
    "version": "1.0.0",
    "generated_at": "2025-08-20T00:00:00",
    "source": "brestgortrans.by",
    "transport_types": ["buses", "trolleybuses", "minibuses"],
    "total_routes": 654,
    "total_stops": 1200
  },
  "data": {
    "buses": {
      "metadata": {
        "transport_type": "buses",
        "total_routes": 450
      },
      "routes": [...]
    },
    "trolleybuses": {
      "metadata": {
        "transport_type": "trolleybuses", 
        "total_routes": 120
      },
      "routes": [...]
    },
    "minibuses": {
      "metadata": {
        "transport_type": "minibuses",
        "total_routes": 84
      },
      "routes": [...]
    }
  }
}
```

## ⚡ Автоматическое обновление

Данные обновляются автоматически через **GitHub Actions**:

- **Расписание**: Ежедневно в 18:00 МСК (только рабочие дни)
- **Триггер**: Изменения в основном репозитории парсера
- **Процесс**: Скачивание → Конвертация → Публикация

## 🔧 Локальная разработка

### **Создание данных вручную:**
```bash
# Клонируем репозиторий
git clone https://github.com/USERNAME/transport_in_Brest-data.git
cd transport_in_Brest-data

# Запускаем скрипт генерации
python create_timetable.py
```

### **Тестирование:**
```bash
# Проверяем структуру
python -c "import json; data=json.load(open('data/timetable.json')); print('OK:', data['metadata']['version'])"

# Запускаем локальный сервер для тестирования
python -m http.server 8000
# http://localhost:8000/data/timetable.json
```

## 📈 Мониторинг

### **Статус обновлений:**
- GitHub Actions: [![Publish](https://github.com/USERNAME/transport_in_Brest-data/workflows/Publish%20Transport%20Data/badge.svg)](https://github.com/USERNAME/transport_in_Brest-data/actions)

### **Последнее обновление:**
- Проверьте `data/meta.json` для актуальной информации
- Или посмотрите на GitHub Actions

## 🚨 Важно

- **Не редактируйте файлы вручную** - они генерируются автоматически
- **Все изменения** должны идти через основной парсер
- **Версионирование** происходит автоматически через Git теги

## 📞 Поддержка

- **Issues**: Создавайте в основном репозитории парсера
- **Документация**: Обновляется с каждым релизом
- **Данные**: Автоматически синхронизируются с brestgortrans.by

---

**Данные обновляются автоматически. Для изменений используйте основной парсер.** 🚀


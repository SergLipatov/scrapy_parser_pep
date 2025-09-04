# Парсер PEP на Scrapy

Парсер для сбора информации о Python Enhancement Proposals (PEP) с официального сайта peps.python.org.

## Функциональность

- Сбор основных данных о каждом PEP: номер, название и статус
- Экспорт данных в CSV-файл
- Генерация отчета с количеством PEP по статусам
- Автоматическое создание папки для результатов

## Установка и запуск

1. Клонируйте репозиторий:
```bash
git clone https://github.com/SergLipatov/scrapy_parser_pep.git
cd scrapy_parser_pep
```

2. Установите зависимости:
```bash
pip install -r requirements.txt
```

3. Запустите парсер:
```bash
scrapy crawl pep
```

## Структура проекта

```
scrapy_parser_pep/
├── pep_parse/
│   ├── spiders/
│   │   └── pep.py          # Паук для сбора данных
│   ├── pipelines.py        # Обработка данных и генерация отчета
│   ├── items.py           # Определение структуры данных
│   └── settings.py        # Настройки Scrapy
├── results/               # Папка с результатами (создается автоматически)
└── README.md
```

## Выходные данные

После выполнения парсинга создаются два файла в папке `results`:

1. `pep_<временная_метка>.csv` - основные данные о PEP:
   - number - номер PEP
   - name - название
   - status - текущий статус

2. `status_summary_<временная_метка>.csv` - сводка по статусам:
   - Статус - наименование статуса
   - Количество - количество PEP с данным статусом
   - Total - общее количество PEP

## Настройки

Основные настройки проекта в `settings.py`:
- Кодировка UTF-8 для экспорта
- Формат и структура CSV-файла
- Активация pipeline для обработки данных

## Технологии

- Python 3.7+
- Scrapy 2.5+
- Модули collections, csv, datetime для обработки данных

## Автор

Сергей Липатов
- GitHub: [SergLipatov](https://github.com/SergLipatov)
- Проект: [scrapy_parser_pep](https://github.com/SergLipatov/scrapy_parser_pep)

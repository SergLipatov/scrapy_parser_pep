import re

import scrapy
from w3lib.html import remove_tags


class PepSpider(scrapy.Spider):
    name = 'pep'
    allowed_domains = ['peps.python.org']
    start_urls = ['https://peps.python.org/']

    def parse(self, response):
        all_peps_links = response.css('a[href*="pep-"]::attr(href)')
        for pep_link in all_peps_links:
            yield response.follow(pep_link, callback=self.parse_pep)

    def parse_pep(self, response):
        # Извлекаем весь HTML заголовка и удаляем теги
        title_html = response.css('h1.page-title').get()
        title_text = remove_tags(title_html).strip()

        # Расширенное регулярное выражение для различных форматов
        pattern = r"PEP\s+(\d+)\s*[:\-–—]\s*(.+)"
        match = re.search(pattern, title_text)

        # Если не нашли совпадение, пробуем альтернативный паттерн
        if not match:
            alt_pattern = r"PEP\s+(\d+)\s*(?:–|—|-|:)\s*(.+)"
            match = re.search(alt_pattern, title_text)

        if not match:
            self.logger.error(f"Failed to parse PEP title: {title_text}")
            return

        # Извлекаем статус
        status_abbr = response.css('abbr::text')
        status = status_abbr.get().strip() if status_abbr.get() else "Unknown"

        yield {
            'number': match.group(1),
            'name': match.group(2).strip(),
            'status': status,
        }

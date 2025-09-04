import csv
import os
from collections import Counter
from datetime import datetime
from pathlib import Path


class PepParsePipeline:
    def open_spider(self, spider):
        self.status_counter = Counter()
        self.settings = spider.settings

    def process_item(self, item, spider):
        self.status_counter[item['status']] += 1
        return item

    def close_spider(self, spider):
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        base_path = None
        if self.settings.get('FEEDS'):
            for feed_path in self.settings.get('FEEDS', {}).keys():
                feed_path_str = str(feed_path)
                if '%(time)s' in feed_path_str:
                    base_path = os.path.dirname(feed_path_str)
                    break
        if not base_path:
            base_path = 'results'
        Path(base_path).mkdir(parents=True, exist_ok=True)
        status_filename = os.path.join(
            base_path,
            f'status_summary_{timestamp}.csv'
        )

        with open(
                status_filename,
                'w', encoding='utf-8',
                newline=''
        ) as csvfile:
            fieldnames = ['Статус', 'Количество']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for status, count in self.status_counter.items():
                writer.writerow({'Статус': status, 'Количество': count})
            total = sum(self.status_counter.values())
            writer.writerow({'Статус': 'Total', 'Количество': total})

from functools import cached_property

from algorithm.mixins import CleaningMixin


class TableObject(CleaningMixin):
    """Represents a parsed table"""

    def __init__(self, obj):
        self.table_head = obj.find('thead')
        self.table_body = obj.find('tbody')

    @property
    def header(self):
        headers = self.table_head.find_all('th')
        for header in headers:
            yield self.clean_text(header.text)

    @property
    def data(self):
        for row in self.table_body.find_all('tr'):
            for col in row.find_all('td'):
                yield self.clean_text(col.text)

    @cached_property
    def construct(self):
        return [list(self.header), list(self.data)]

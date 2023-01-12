#
# (c) 2022, Yegor Yakubovich
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#


from adecty_design.elements.config import Config
from adecty_design.elements.text import Text


class Table:
    columns: list
    rows: list[list]

    def __init__(self, columns: list, rows: list[list]):
        self.columns = columns
        self.rows = rows

    def html_get(self, config: Config):
        table_html = '<table class="table"><tr>{columns}</tr>{rows}</table>'

        columns_html = ''
        for column in self.columns:
            column_element_html = Text(text=column, color=config.colors.background).html_get(config=config) \
                if type(column) is str else column.html_get(config=config)
            columns_html += '<th>{column_element}</th>'.format(column_element=column_element_html)

        rows_html = ''
        for row in self.rows:
            row_html = ''
            for element in row:
                row_element_html = Text(text=element).html_get(config=config) if type(element) is str else \
                    element.html_get(config=config)
                row_html += '<td>{row_element}</td>'.format(row_element=row_element_html)
            rows_html += '<tr>{row}</tr>'.format(row=row_html)

        table_html = table_html.format(
            columns=columns_html,
            rows=rows_html,
        )
        return table_html

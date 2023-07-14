#
# (c) 2023, Yegor Yakubovich
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
from adecty_design.properties import Font
# FIXME


from adecty_design.widgets.text import Text


class Table:
    columns: list
    rows: list[list]

    def __init__(self, columns: list, rows: list[list]):
        self.columns = columns
        self.rows = rows

    def html_get(self, **kwargs):
        table_html = '<table class="table"><tr>{columns}</tr>{rows}</table>'

        columns_html = ''
        for column in self.columns:
            column_element_html = Text(text=column, font=Font(color=kwargs.get('colors').background)).html_get(**kwargs) \
                if type(column) is str else column.html_get(**kwargs)
            columns_html += '<th>{column_element}</th>'.format(column_element=column_element_html)

        rows_html = ''
        for row in self.rows:
            row_html = ''
            for element in row:
                row_element_html = ''
                if type(element) is list:
                    row_element_html += ''.join([e.css_get(**kwargs) for e in element])
                elif type(element) is str:
                    row_element_html += Text(text=element).html_get(**kwargs)
                else:
                    row_element_html += element.html_get(**kwargs)
                row_html += '<td>{row_element}</td>'.format(row_element=row_element_html)
            rows_html += '<tr>{row}</tr>'.format(row=row_html)

        table_html = table_html.format(
            columns=columns_html,
            rows=rows_html,
        )
        return table_html

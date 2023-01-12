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


from adecty_design.elements.colors import Colors

from adecty_design.elements.fonts import Fonts
from adecty_design.markups.markups import MarkupsHtml, MarkupsStyles


class Config:
    name: str
    logo: str
    colors: Colors
    fonts: Fonts
    rounding = int

    def __init__(self, name: str, logo: str, colors: Colors, fonts: Fonts, rounding: int):
        self.name = name
        self.logo = logo
        self.colors = colors
        self.fonts = fonts
        self.rounding = rounding

    def html_get(self):
        html = '{fonts}{styles}'

        fonts = MarkupsHtml.fonts.format(font_main=self.fonts.main.html_init,
                                         font_secondary=self.fonts.secondary.html_init)
        styles_vars = ':root {' + \
                      '--background: {color_background};' \
                      '--background_secondary: {color_background_secondary};' \
                      '--primary: {color_primary};' \
                      '--text: {color_text};' \
                      '--selected: {color_selected};' \
                      '--unselected: {color_unselected};' \
                      '--error: {color_error};' \
                      '--rounding: {rounding}px;'.format(
                          color_background=self.colors.background,
                          color_background_secondary=self.colors.background_secondary,
                          color_primary=self.colors.primary,
                          color_text=self.colors.text,
                          color_selected=self.colors.selected,
                          color_unselected=self.colors.unselected,
                          color_error=self.colors.error,
                          rounding=self.rounding
                      ) + '}'
        styles = '<style>{styles_vars}{style_base}{style_header}{style_footer}{style_table}{style_dictionary}</style>'
        styles = styles.format(
            styles_vars=styles_vars,
            style_base=MarkupsStyles.base,
            style_header=MarkupsStyles.header,
            style_footer=MarkupsStyles.footer,
            style_table=MarkupsStyles.table,
            style_dictionary=MarkupsStyles.dictionary,
        )
        return html.format(fonts=fonts, styles=styles)

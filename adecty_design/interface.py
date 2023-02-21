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


from adecty_design.device import Device
from adecty_design.widgets.header import Header
from adecty_design.widgets.footer import Footer
from adecty_design.markups.markups import MarkupsHtml, MarkupsStyles
from adecty_design.colors import Colors
from adecty_design.font import Font
from adecty_design.widgets.container import Container


class Interface:
    logo: str
    logo_mini: str
    name: str
    colors: Colors
    font: Font
    rounding: int
    header: Header
    footer: Footer

    def __init__(self,
                 logo: str, logo_mini: str, name: str, rounding: int,
                 colors: Colors, font: Font,
                 header: Header = None, footer: Footer = None):
        self.logo = logo
        self.logo_mini = logo_mini
        self.name = name
        self.rounding = rounding
        self.colors = colors
        self.font = font
        self.header = header
        self.footer = footer

    def html_get(self, widgets: list[Container], device: Device):
        header_html = ''
        footer_html = ''

        kwargs = {
            'logo': self.logo,
            'logo_mini': self.logo_mini,
            'rounding': self.rounding,
            'colors': self.colors,
            'font': self.font,
            'device': device,
        }

        widgets_html = ''.join([widget.html_get(**kwargs) for widget in widgets])
        config_html = self.config_html_get()

        base_html_format = {
            'name': self.name,
            'config_html': config_html,
            'header_html': header_html,
            'widgets_html': widgets_html,
            'footer_html': footer_html,
        }
        interface_html = MarkupsHtml.interface_html.format(**base_html_format)
        return interface_html

    def config_html_get(self):
        html = '{fonts}{styles}'

        fonts = self.font.html_init
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

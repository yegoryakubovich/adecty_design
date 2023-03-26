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


from adecty_design.widgets.required.header import Header
from adecty_design.widgets.required import Footer
from adecty_design.markups.markups import MarkupsHtml, MarkupsStyles, MarkupsScripts
from adecty_design.properties.colors import Colors
from adecty_design.properties.font import Font
from adecty_design.widgets.required import Navigation
from adecty_design.widgets.icon import Icon
import adecty_design.widgets as widgets_list


class Interface:
    logo: Icon
    logo_mini: Icon
    name: str
    colors: Colors
    font: Font
    rounding: int
    navigation: Navigation
    header: Header
    footer: Footer

    def __init__(self,
                 logo: Icon, logo_mini: Icon, name: str, rounding: int,
                 colors: Colors, font: Font, navigation: Navigation,
                 header: Header = None, footer: Footer = None, ):
        self.logo = logo
        self.logo_mini = logo_mini
        self.name = name
        self.rounding = rounding
        self.colors = colors
        self.font = font
        self.navigation = navigation
        self.header = header
        self.footer = footer

    def html_get(self, widgets: list | tuple, active: str = '', navigation: Navigation = None):
        kwargs = {
            'logo': self.logo,
            'logo_mini': self.logo_mini,
            'rounding': self.rounding,
            'colors': self.colors,
            'font': self.font,
        }

        navigation_desktop_html, navigation_mobile_html = navigation.html_get(active=active, **kwargs) \
            if navigation else self.navigation.html_get(active=active, **kwargs)

        header_html = self.header.html_get(**kwargs)
        footer_html = self.footer.html_get(**kwargs, navigation_mobile_html=navigation_mobile_html)
        widgets_html = ''.join([
            widget.html_get(**kwargs) if type(widget).__name__ in widgets_list.__all__
            else '' for widget in widgets]
        )
        config_html = self.config_html_get()

        scripts_js = self.scripts_js_get()

        base_html_format = {
            'name': self.name,
            'config_html': config_html,
            'header_html': header_html,
            'scripts_js': scripts_js,
            'navigation_desktop_html': navigation_desktop_html,
            'widgets_html': widgets_html,
            'footer_html': footer_html,
        }
        interface_html = MarkupsHtml.interface_html.format(**base_html_format)
        return interface_html

    def config_html_get(self):
        html = '{fonts}{styles}'

        fonts = self.font.html_init
        styles_vars = ':root {' \
                      '--width: 75%;' + \
                      '--background: {color_background};' \
                      '--background_secondary: {color_background_secondary};' \
                      '--primary: {color_primary};' \
                      '--primary_secondary: {color_primary_secondary};' \
                      '--text: {color_text};' \
                      '--selected: {color_selected};' \
                      '--unselected: {color_unselected};' \
                      '--negative: {color_negative};' \
                      '--positive: {color_positive};' \
                      '--rounding: {rounding}px;'.format(
                          color_background=self.colors.background.color,
                          color_background_secondary=self.colors.background_secondary.color,
                          color_primary=self.colors.primary.color,
                          color_primary_secondary=self.colors.primary_secondary.color,
                          color_text=self.colors.text.color,
                          color_selected=self.colors.selected.color,
                          color_unselected=self.colors.unselected.color,
                          color_negative=self.colors.negative.color,
                          color_positive=self.colors.positive.color,
                          rounding=self.rounding,
                      ) + '}'
        styles = '<style>{styles_vars}{style_base}{style_header}{style_footer}{style_navigation}' \
                 '{style_table}{style_dictionary}{style_orientation}{style_view}</style>'
        styles = styles.format(
            styles_vars=styles_vars,
            style_base=MarkupsStyles.interface,
            style_header=MarkupsStyles.header,
            style_footer=MarkupsStyles.footer,
            style_navigation=MarkupsStyles.navigation,
            style_table=MarkupsStyles.table,
            style_dictionary=MarkupsStyles.dictionary,
            style_orientation=MarkupsStyles.orientation,
            style_view=MarkupsStyles.input_file,
        )
        return html.format(fonts=fonts, styles=styles)

    def scripts_js_get(self):
        return '\n'.join([
            '<script>{sctipt_js}</script>'.format(sctipt_js=sctipt_js)
            for sctipt_js in [
                MarkupsScripts.orientation,
            ]
        ])

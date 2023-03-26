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


from adecty_design.properties import Color


class Font:
    html_init: str
    css_init: str
    css: str
    size: int
    weight: int
    color: Color

    def __init__(
            self,
            html_init: str = None,
            css_init: str = None,
            css: str = None,
            size: int = 12,
            weight: int = 600,
            color: Color = None,
    ):
        self.html_init = html_init
        self.css_init = css_init
        self.css = css
        self.size = size
        self.weight = weight
        self.color = color

    def css_get(self, **kwargs):
        if not self.css:
            self.css = kwargs.get('font').css
        if self.color is None:
            self.color = kwargs.get('colors').text
        font_css = 'font-family: {css};' \
                   'font-size: {size}px;' \
                   'font-weight: {weight};' \
                   'color: {color};'.format(
            css=self.css,
            size=self.size,
            weight=self.weight,
            color=self.color.color,
        )

        return font_css

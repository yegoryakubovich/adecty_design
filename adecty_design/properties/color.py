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


class ColorType:
    text = 'text'
    background = 'background'
    fill = 'fill'


class Color:
    color: str
    type: str

    def __init__(
            self,
            color: str = None,
            type: str = None,
    ):
        self.color = color
        self.type = type

    def css_get(self, **kwargs):
        type = 'color'
        if self.type == ColorType.text:
            type = 'color'
        if self.type == ColorType.background:
            type = 'background-color'
        elif self.type == ColorType.fill:
            type = 'fill'

        color = self.color if self.color else kwargs.get('colors').primary.color

        color_css = '{type}: {color};'.format(
            type=type,
            color=color,
        )
        return color_css

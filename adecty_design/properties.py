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


from adecty_design.markups.markups import MarkupsHtml


class Margin:
    top: int | float | str
    down: int | float | str
    left: int | float | str
    right: int | float | str
    horizontal: int | float | str
    vertical: int | float | str

    def __init__(self,
                 top: int | float | str = None,
                 down: int | float | str = None,
                 left: int | float | str = None,
                 right: int | float | str = None,
                 horizontal: int | float | str = None,
                 vertical: int | float | str = None,
                 ):
        self.top = top
        self.down = down
        self.left = left
        self.right = right
        self.horizontal = horizontal
        self.vertical = vertical

    def html_get(self):
        top = '0'
        down = '0'
        left = '0'
        right = '0'

        if self.horizontal:
            top = '{top}{unit}'.format(top=self.horizontal, unit='' if type(self.horizontal) == str else 'px')
            down = '{top}{unit}'.format(top=self.horizontal, unit='' if type(self.horizontal) == str else 'px')
        if self.vertical:
            left = '{top}{unit}'.format(top=self.vertical, unit='' if type(self.vertical) == str else 'px')
            right = '{top}{unit}'.format(top=self.vertical, unit='' if type(self.vertical) == str else 'px')

        if self.top:
            top = '{top}{unit}'.format(top=self.top, unit='' if type(self.top) == str else 'px')
        if self.down:
            top = '{top}{unit}'.format(top=self.down, unit='' if type(self.down) == str else 'px')
        if self.left:
            top = '{top}{unit}'.format(top=self.left, unit='' if type(self.left) == str else 'px')
        if self.right:
            top = '{top}{unit}'.format(top=self.right, unit='' if type(self.right) == str else 'px')

        return '{top} {right} {down} {left}'.format(
            top=top,
            down=down,
            left=left,
            right=right,
        )


class Padding(Margin):
    pass


class Properties:
    margin: Margin
    padding: Padding
    background: str

    def __init__(self,
                 margin: Margin = None,
                 padding: Padding = None,
                 background: str = None):
        self.margin = margin
        self.padding = padding
        self.background = background

    def html_get(self, **kwargs):
        properties = []
        if self.margin:
            properties.append('margin: {margin};'.format(margin=self.margin.html_get()))
        if self.padding:
            properties.append('padding: {padding};'.format(padding=self.padding.html_get()))
        if self.background:
            properties.append('background-color: {background};'.format(background=self.background))

        properties_html = ''.join(properties)
        return properties_html

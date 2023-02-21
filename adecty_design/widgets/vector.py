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


from xml.etree import ElementTree
from xml.etree.ElementTree import Element

from lxml import etree


class Vector:
    svg: Element
    width: int
    height: int

    def __init__(self, svg: str):
        ElementTree.register_namespace('', 'http://www.w3.org/2000/svg')
        self.svg = ElementTree.fromstring(svg)
        self.width = int(self.svg.get('width'))
        self.height = int(self.svg.get('height'))

    def svg_get(self, height: int, color: str):
        svg_current = self.svg
        svg_current.set('width', str(int(self.width*height/self.height)))
        svg_current.set('height', str(int(height)))
        svg_current.set('fill', color)
        for e in svg_current:
            e.set('fill', color)
        return ElementTree.tostring(svg_current, encoding='unicode')

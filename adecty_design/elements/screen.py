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
from adecty_design.templates.get_element_html import get_element_html


class ScreenDirection:
    vertical = 'VERTICAL'
    horizontal = 'HORIZONTAL'


class Screen:
    config: Config
    direction: str
    elements: list

    def __init__(self, elements: list, direction: str = ScreenDirection.vertical):
        self.direction = direction
        self.elements = elements

    def generate_html(self, config: Config):
        self.config = config

        elements_html = ''
        for element in self.elements:
            elements_html += element.generate_html(config=config)

        page_html = get_element_html('screen').format(elements=elements_html)
        return page_html

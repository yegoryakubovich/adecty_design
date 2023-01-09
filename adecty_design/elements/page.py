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


from adecty_design.elements.screen import Screen
from adecty_design.elements.config import Config
from adecty_design.templates.get_element_html import get_element_html


class Page:
    title: str
    screens: list[Screen]

    def __init__(self, title: str, screens: list):
        self.title = title
        self.screens = screens

    def get_html(self, config: Config):
        screens_html = ''
        for screen in self.screens:
            screens_html += screen.get_html(config=config)

        page_html = get_element_html('page').format(screens=screens_html)

        return page_html
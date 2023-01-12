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
from adecty_design.elements.header_navigation_item import HeaderNavigationItem
from adecty_design.markups.markups import MarkupsHtml


class Header:
    logo: str
    name: str
    navigation_items: list[HeaderNavigationItem]

    def __init__(self, config: Config, navigation_items: list[HeaderNavigationItem]):
        self.logo = config.logo
        self.name = config.name
        self.navigation_items = navigation_items

    def html_get(self):
        header_html = MarkupsHtml.header

        header_navigation_items_html = ''
        for navigation_item in self.navigation_items:
            header_navigation_items_html += navigation_item.html_get()

        header_html = header_html.format(
            logo=self.logo,
            name=self.name,
            header_navigation_items_html=header_navigation_items_html)
        return header_html

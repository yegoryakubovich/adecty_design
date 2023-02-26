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


from adecty_design.markups.markups import MarkupsHtml
from adecty_design.properties import Font
from adecty_design.widgets.text import Text
from adecty_design.widgets.vector import Vector


class NavigationItem:
    id: str
    name: str
    url: str
    icon: Vector

    def __init__(self, id: str, name: str, url: str, icon: Vector = None):
        self.id = id
        self.name = name
        self.url = url
        self.icon = icon

    def html_get(self, active: bool, **kwargs):
        colors = kwargs.get('colors')

        desktop_name_html = Text(
            text=self.name,
            font=Font(
                color=colors.background if active else colors.primary_secondary,
                size=18,
                weight=600,
            ),
        ).html_get(**kwargs)
        desktop_icon_html = self.icon.svg_get(
            height=18,
            class_name='navigation__desktop__item__icon__active' if active else 'navigation__desktop__item__icon',
        )
        mobile_name_html = Text(
            text=self.name,
            font=Font(
                color=colors.primary if active else colors.background_secondary,
                size=10,
                weight=700,
            ),
        ).html_get(**kwargs)
        mobile_icon_html = self.icon.svg_get(
            height=28,
            class_name='navigation__mobile__item__icon__active' if active else 'navigation__mobile__item__icon',
        )

        navigation_desktop_item = MarkupsHtml.navigation_desktop_item.format(
            url=self.url,
            name_html=desktop_name_html,
            icon_html=desktop_icon_html,
        )
        navigation_mobile_item = MarkupsHtml.navigation_mobile_item.format(
            url=self.url,
            name_html=mobile_name_html,
            icon_html=mobile_icon_html,
        )
        return navigation_desktop_item, navigation_mobile_item


class Navigation:
    items: list[NavigationItem]
    desktop: list[NavigationItem]

    def __init__(self, items: list[NavigationItem]):
        self.items = items

    def html_get(self, active: str, **kwargs):
        navigation_desktop_items_html, navigation_mobile_items_html = '', ''
        for item in self.items:
            navigation_desktop_item_html, navigation_mobile_item_html = item.html_get(
                active=True if active == item.id else False,
                **kwargs,
            )
            navigation_desktop_items_html += navigation_desktop_item_html
            navigation_mobile_items_html += navigation_mobile_item_html

        navigation_desktop_html = MarkupsHtml.navigation_desktop.format(
            items_html=navigation_desktop_items_html,
        )
        navigation_mobile_html = MarkupsHtml.navigation_mobile.format(
            items_html=navigation_mobile_items_html,
        )

        return navigation_desktop_html, navigation_mobile_html

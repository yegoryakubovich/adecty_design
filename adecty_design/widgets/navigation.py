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

        name_html = Text(
            text=self.name,
            color=colors.primary if active else colors.background_secondary,
            font_size=8,
            font_weight=700,
        ).html_get(**kwargs)
        icon_html = self.icon.svg_get(
            height=18,
            class_name='navigation__mobile__item__icon__active' if active else 'navigation__mobile__item__icon',
        )

        navigation_mobile_item = MarkupsHtml.navigation_mobile_item.format(
            url=self.url,
            name_html=name_html,
            icon_html=icon_html)
        return navigation_mobile_item


class Navigation:
    mobile: list[NavigationItem]
    desktop: list[NavigationItem]

    def __init__(self, mobile: list[NavigationItem]):
        self.mobile = mobile

    def html_get(self, active: str, **kwargs):
        navigation_mobile_items_html = ''.join([navigation_mobile_item.html_get(
            active=True if active == navigation_mobile_item.id else False,
            **kwargs,
        ) for navigation_mobile_item in self.mobile])
        navigation_mobile_html = MarkupsHtml.navigation_mobile.format(
            navigation_mobile_items_html=navigation_mobile_items_html,
        )

        return navigation_mobile_html

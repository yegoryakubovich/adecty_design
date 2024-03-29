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
from adecty_design.functions import properties_css_get
from adecty_design.markups.markups import MarkupsHtml


class Footer:
    def __init__(self):
        pass

    def html_get(self, **kwargs):
        navigation_mobile_html = kwargs.get('navigation_mobile_html')

        # 'display: none;' if not navigation_mobile_html else ''
        properties_css = properties_css_get(
            properties_additional='',
        )
        footer_html = MarkupsHtml.footer.format(
            logo=kwargs.get('logo').html_get(height=16, class_name='footer__logo', color=False),
            navigation_mobile_html=navigation_mobile_html,
            properties_css=properties_css,
        )
        return footer_html

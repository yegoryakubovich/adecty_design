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
from adecty_design.elements.header import Header
from adecty_design.elements.footer import Footer
from adecty_design.elements.page import Page
from adecty_design.templates import get_css
from adecty_design.templates.get_element_html import get_element_html


class AdectyDesign:
    config: Config
    header: Header
    footer: Footer

    def __init__(self, config: Config, header: Header, footer: Footer):
        self.config = config
        self.header = header
        self.footer = footer

    def get_page_html(self, page: Page):
        page_html = page.get_html(config=self.config)

        config_html = self.config.get_html()

        base_html_format = {
            'title': page.title,
            'config': config_html,
            'header': self.header.get_html(),
            'page': page_html,
            'footer': self.footer.get_html(),
        }
        base_html = get_element_html('base').format(**base_html_format)
        return base_html

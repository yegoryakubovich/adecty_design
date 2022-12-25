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


class Footer:
    logo: str
    name: str

    def __init__(self, config: Config):
        self.logo = config.logo
        self.name = config.name

    def generate_html(self):
        footer_html = get_element_html('footer')
        footer_html = footer_html.format(logo=self.logo,
                                         name=self.name)
        return footer_html

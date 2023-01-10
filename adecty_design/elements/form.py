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


class Form:
    elements: list

    def __init__(self, elements: list):
        self.elements = elements

    def get_html(self, config: Config):
        elements_html = ''.join([element.get_html(config=config) for element in self.elements])
        form_html = '<form method="post" class="form">{elements}</form>'.format(elements=elements_html)
        return form_html

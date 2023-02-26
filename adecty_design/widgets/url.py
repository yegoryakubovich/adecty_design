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


from adecty_design.functions import properties_css_get, widgets_html_get


class Url:
    url: str
    widgets: list

    def __init__(self, url: str, widgets: list):
        self.url = url
        self.widgets = widgets

    def html_get(self, **kwargs):
        properties_css = properties_css_get(properties=[])
        widgets_html = widgets_html_get(widgets=self.widgets, **kwargs)

        url_html = '<a {properties_css} href="{url}">{widgets_html}</a>'.format(
            properties_css=properties_css,
            widgets_html=widgets_html,
            url=self.url,
        )

        return url_html

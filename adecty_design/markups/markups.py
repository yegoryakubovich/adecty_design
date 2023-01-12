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


from os.path import dirname, realpath


def html_get(name: str):
    path = dirname(realpath(__file__))
    return open('{path}/html/{name}.html'.format(path=path, name=name), 'r').read()


def css_get(name: str):
    path = dirname(realpath(__file__))
    return open('{path}/css/{name}.css'.format(path=path, name=name), 'r').read()


class MarkupsHtml:
    base = html_get('base')
    fonts = '{font_main}{font_secondary}'
    page = html_get('page')
    screen = html_get('screen')
    header = html_get('header')
    header_navigation_item = html_get('header_navigation_item')
    text = html_get('text')
    footer = html_get('footer')
    form = html_get('form')


class MarkupsStyles:
    base = css_get('base')
    header = css_get('header')
    footer = css_get('footer')
    table = css_get('table')

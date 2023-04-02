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


from os.path import dirname, realpath


def html_get(name: str):
    path = dirname(realpath(__file__))
    return open('{path}/html/{name}.html'.format(path=path, name=name), 'r').read()


def css_get(name: str):
    path = dirname(realpath(__file__))
    return open('{path}/css/{name}.css'.format(path=path, name=name), 'r').read()


def js_get(name: str):
    path = dirname(realpath(__file__))
    return open('{path}/js/{name}.js'.format(path=path, name=name), 'r').read()


class MarkupsHtml:
    interface_html = html_get('interface')
    header = html_get('header')
    header_navigation_item = html_get('header_navigation_item')
    footer = html_get('footer')

    navigation_mobile_item = html_get('navigation_mobile_item')
    navigation_desktop_item = html_get('navigation_desktop_item')

    text = html_get('text')

    button_default = html_get('button/default')
    button_chip = html_get('button/chip')

    container = html_get('container')
    card = html_get('card')


class MarkupsStyles:
    interface = css_get('interface')
    normalize = css_get('normalize')
    orientation = css_get('orientation')
    header = css_get('header')
    footer = css_get('footer')

    navigation = css_get('navigation')

    input_file = css_get('input_file')

    table = css_get('table')
    dictionary = css_get('dictionary')


class MarkupsScripts:
    orientation = js_get('orientation')

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


def properties_css_get(properties: list | tuple | set, properties_additional=None, **kwargs):
    styles = [propertie.css_get(**kwargs) for propertie in properties]
    if properties_additional:
        styles.append(properties_additional)
    styles = ''.join(styles)

    properties_css = 'style="{styles}"'.format(
        styles=styles,
    )
    return properties_css

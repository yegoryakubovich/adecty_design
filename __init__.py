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


from adecty_design.adecty_design import AdectyDesign
from adecty_design.elements.config import Config
from adecty_design.elements.fonts import Font
from adecty_design.elements.footer import Footer
from adecty_design.elements.form import Form
from adecty_design.elements.header import Header
from adecty_design.elements.input import InputTypes, Input
from adecty_design.elements.header_navigation_item import HeaderNavigationItem
from adecty_design.elements.page import Page
from adecty_design.elements.screen import ScreenDirection, Screen


__all__ = (
    'Config',
    'InputTypes',
    'Input',
    'Header',
    'Form',
    'Footer',
    'Font',
    'Page',
    'ScreenDirection',
    'Screen',
    'HeaderNavigationItem',
    'AdectyDesign',
)

__version__ = '0.0.1'

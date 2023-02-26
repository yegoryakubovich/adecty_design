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


class Colors:

    background: str
    background_secondary: str
    primary: str
    primary_secondary: str
    text: str
    selected: str
    unselected: str
    negative: str
    positive: str

    def __init__(self,
                 background: str,
                 background_secondary: str,
                 primary: str,
                 primary_secondary: str,
                 text: str,
                 selected: str,
                 unselected: str,
                 negative: str,
                 positive: str):

        """
        :param background: Application background color, will also be used as default text color on elements where
        color is primary
        :param background_secondary: For table rows
        :param primary: The main color of your application
        :param primary_secondary: Will be used where the primary background
        :param text: Color for all colors, except for links and texts located on elements with the primary color
        :param selected: This color will be on elements that are selected, clicked or hovered over
        :param unselected: This color will be on elements that are unselected (buttons, inputs & other)
        :param negative: For error window or text with an error
        """

        self.background = background
        self.background_secondary = background_secondary
        self.primary = primary
        self.primary_secondary = primary_secondary
        self.text = text
        self.selected = selected
        self.unselected = unselected
        self.negative = negative
        self.positive = positive

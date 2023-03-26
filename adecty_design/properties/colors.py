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


from adecty_design.properties import Color


class Colors:

    background: Color
    background_secondary: Color
    primary: Color
    primary_secondary: Color
    text: Color
    selected: Color
    unselected: Color
    negative: Color
    positive: Color

    def __init__(self,
                 background: str | Color,
                 background_secondary: str | Color,
                 primary: str | Color,
                 primary_secondary: str | Color,
                 text: str | Color,
                 selected: str | Color,
                 unselected: str | Color,
                 negative: str | Color,
                 positive: str | Color):

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

        self.background = background if background is Color else Color(color=background)
        self.background_secondary = background_secondary if background_secondary is Color else Color(color=background_secondary)
        self.primary = primary if primary is Color else Color(color=primary)
        self.primary_secondary = primary_secondary if primary_secondary is Color else Color(color=primary_secondary)
        self.text = text if text is Color else Color(color=text)
        self.selected = selected if selected is Color else Color(color=selected)
        self.unselected = unselected if unselected is Color else Color(color=unselected)
        self.negative = negative if negative is Color else Color(color=negative)
        self.positive = positive if positive is Color else Color(color=positive)

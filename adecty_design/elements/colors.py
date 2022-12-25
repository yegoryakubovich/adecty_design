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
    main: str
    secondary: str

    def __init__(self, background: str, main: str, secondary: str,):
        self.background = background
        self.main = main
        self.secondary = secondary

    def get_html(self):
        colors = '--background: {};\n--main: {};\n--secondary: {};'.format(self.background, self.main, self.secondary)
        return ':root {\n' + colors + '\n}'

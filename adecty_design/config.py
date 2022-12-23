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

    def __init__(self, colors: dict):
        self.background = colors['background']
        self.main = colors['main']
        self.secondary = colors['secondary']


class Config:
    name: str
    logo: str
    colors: Colors

    def __init__(self, config: dict):
        self.name = config['name']
        self.logo = config['logo']
        self.colors = Colors(config['colors'])

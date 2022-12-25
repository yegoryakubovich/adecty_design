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


class Authorization:
    def __init__(self, authorized, unauthorized):
        self.authorized = authorized
        self.unauthorized = unauthorized

    def generate_html(self, is_authorized=False):
        if is_authorized:
            return self.authorized.generate_html()
        else:
            return self.unauthorized.generate_html()

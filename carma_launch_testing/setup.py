# Copyright 2023 Leidos
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

import glob

from setuptools import setup

package_name = "carma_launch_testing"

setup(
    name=package_name,
    version="0.1.0",
    packages=[package_name],
    data_files=[
        ("share/ament_index/resource_index/packages", [f"resource/{package_name}"]),
        (f"share/{package_name}", ["package.xml"])
    ],
    install_requires=["setuptools"],
    zip_safe=True,
    maintainer="carma",
    maintainer_email="carma@dot.gov",
    description="Supplemental launch_testing functions",
    license="Apache 2.0",
    tests_require=["pytest"],
    entry_points={
        "console_scripts": [],
    },
)

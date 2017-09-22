#!/usr/bin/env python
# Copyright (c) 2016 Hewlett-Packard Development Company, L.P.
# Copyright (c) 2017 SUSE LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or
# implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import os
import setuptools


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setuptools.setup(
    name="certifi",
    version="99.0.0",
    description="Local replacement for certifi",
    long_description=read('README.md'),
    author="SUSE LLC",
    author_email="ardana@googlegroups.com",
    url="https://github.com/ArdanaCLM",
    classifiers=[
        "License :: OSI Approved :: Apache License",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 2.6",
    ],

    packages=[
        "certifi",
    ],
)

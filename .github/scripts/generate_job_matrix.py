#!/usr/bin/env python3
#
# Copyright (C) 2021-2022 F4PGA Authors
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# SPDX-License-Identifier: Apache-2.0

from sys import argv as sys_argv

isFork = len(sys_argv)>1 and sys_argv[1] != 'SymbiFlow/symbiflow-examples'

runs_on = (
    'ubuntu-latest'
    if isFork else
    ['self-hosted', 'Linux', 'X64']
)

examples = [
    "picosoc",
    "litex",
    "litex_linux",
    "button_controller",
    "pulse_width_led",
    "timer",
    "hello-a",
    "hello-b",
    "hello-c",
    "hello-d",
    "hello-e",
    "hello-f",
    "hello-g",
    "hello-h",
    "hello-i",
    "hello-j",
    "hello-k",
    "hello-l"
]

jobs = []

osvers = [
    ("ubuntu", "focal"),
    ("centos", "8"),
    ("debian", "buster"),
    ("debian", "bullseye"),
    ("debian", "sid"),
    ("fedora", "35"),
    ("fedora", "36"),
]

if not isFork:
    examples = [
        "counter",
        "litex_sata",
    ] + examples
    osvers += [
        ("ubuntu", "xenial"),
        ("ubuntu", "bionic"),
        ("centos", "7"),
    ]

for osver in osvers:
    jobs += [{
        'runs-on': runs_on,
        'fpga-fam': "xc7",
        'os': osver[0],
        'os-version': osver[1],
        'example': example
    } for example in examples]

jobs += [{
    'runs-on': runs_on,
    'fpga-fam': "eos-s3",
    'os': osver[0],
    'os-version': osver[1],
    'example': "counter"
} for osver in osvers]

print(f'::set-output name=matrix::{jobs!s}')

print(str(jobs))

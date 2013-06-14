# system76-driver: Universal driver for System76 computers
# Copyright (C) 2005-2013 System76, Inc.
#
# This file is part of `system76-driver`.
#
# `system76-driver` is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# `system76-driver` is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along
# with `system76-driver`; if not, write to the Free Software Foundation, Inc.,
# 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.

"""
Determin model of System76 product.
"""

from .mockable import SubProcess


KEYWORDS = (
    'system-uuid',
    'baseboard-product-name',
    'system-product-name',
    'system-version',
)

TABLES = {
    'system-uuid': {
        '00000000-0000-0000-0000-000000000001': 'koap1',
    },
    'baseboard-product-name': {
        'Z35FM': 'daru1',
        'Z35F': 'daru1',
        'MS-1221': 'daru2',
        'IFL91': 'panv3',
        'IFT01': 'gazv5',
        'IFT00': 'gazp5',
        'A8N8L': 'sabv1',
        'M2N8L': 'sabv2',
        'P5K-VM': 'sabv3',
        'IFL90': 'serp3',
        'JFL92': 'serp4',
        'MS-7250': 'wilp1',
        'A8V-MQ': 'ratv1',
        'P5VD2-MX': 'ratv2',
        'P5VD2-VM': 'ratv3',
        'D945GCPE': 'ratv4',
        'P5GC-MX/1333': 'ratv5',
        'MPAD-MSAE Customer Reference Boards': 'gazv2',
        'K8N-DL': 'wilp2',
        'KFN5-D SLI': 'wilp3',
        'DP35DP': 'wilp5',
    },
    'system-product-name': {
        'MS-1012': 'gazv1',
        'Z62FP': 'gazv3',
        'Z62FM': 'gazv4',
        'Z62F': 'gazp1',
        'Z62J': 'gazp2',
        'Z62JM': 'gazp3',
        'Z62JP': 'gazp3',
        'U-100': 'meec1',
        'Z96F': 'panv2',
        'Centoris V661': 'panv2',
        'Z96FM': 'panv2',
        'HEL80I': 'serp1',
        'HEL8X': 'serp1',
        'HEL80C': 'serp2',
        'UW1': 'star1',
        'star1': 'star1',
        'E10IS': 'star2',
        'E10IS2': 'star2',
        'Star2': 'star2',
        'A7V': 'bonp1',
        'M570TU': 'bonp2',
        'M720T/M730T': 'daru3',
        'M740T/M760T': 'panp4i',
        'M740TU/M760TU': 'panp4n',
        'M860TU': 'serp5',
    },
    'system-version': {
        'bonp2': 'bonp2',
        'bonp3': 'bonp3',
        'bonp4': 'bonp4',
        'bonp5': 'bonp5',
        'bonx6': 'bonx6',
        'gazu1': 'gazu1',
        'gazp6': 'gazp6',
        'gazp7': 'gazp7',
        'gazp8': 'gazp8',
        'gazp9': 'gazp9',
        'daru3': 'daru3',
        'panp4n': 'panp4n',
        'panp5': 'panp5',
        'panp6': 'panp6',
        'panp7': 'panp7',
        'panp8': 'panp8',
        'panp9': 'panp9',
        'lemu1': 'lemu1',
        'lemu2': 'lemu2',
        'lemu3': 'lemu3',
        'lemu4': 'lemu4',
        'leo1': 'leo1',
        'leox2': 'leox2',
        'leox3': 'leox3',
        'ment1': 'ment1',
        'ment2': 'ment2',
        'ment3': 'ment3',
        'ment5': 'ment5',
        'ratv6': 'ratv6',
        'ratu1': 'ratu1',
        'ratu2': 'ratu2',
        'ratp1': 'ratp1',
        'star3': 'star3',
        'star4': 'star4',
        'star5': 'star5',
        'wilb1': 'wilb1',
        'wilb2': 'wilb2',
        'wilp6': 'wilp6',
        'wilp7': 'wilp7',
        'wilp8': 'wilp8',
        'wilp9': 'wilp9',
        'serp5': 'serp5',
        'serp6': 'serp6',
        'serp7': 'serp7',
        'sabc1': 'sabc1',
    },
}


def dmidecode(keyword):
    cmd = ['sudo', 'dmidecode', '-s', keyword]
    return SubProcess.check_output(cmd).decode('utf-8').strip()


def get_dmi_info():
    return dict(
        (keyword, dmidecode(keyword)) for keyword in KEYWORDS
    )


def determine_model(info=None):
    """
    Determine the System76 model number.
    """
    if info is None:
        info = get_dmi_info()

    for keyword in KEYWORDS:
        value = info[keyword]
        table = TABLES[keyword]
        if value in table:
            return table[value]

    return 'nonsystem76'
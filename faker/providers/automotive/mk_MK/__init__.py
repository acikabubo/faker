# coding=utf-8

from __future__ import unicode_literals
from string import ascii_uppercase
from .. import Provider as AutomotiveProvider


class Provider(AutomotiveProvider):
    # from https://en.wikipedia.org/wiki/Vehicle_registration_plates_of_the_Republic_of_Macedonia
    license_plate_letters = (
        'BE', 'BT', 'DB', 'DE', 'DH',
        'DK', 'GE', 'GV', 'KA', 'KI',
        'KO', 'KR', 'KP', 'KS', 'KU',
        'MB', 'MK', 'NE', 'OH', 'PP',
        'PS', 'RA', 'RE', 'SK', 'SN',
        'SU', 'SR', 'ST', 'TE', 'VA',
        'VE', 'VI', 'VV'
    )

    def license_plate(self):
        return self.random_element(self.license_plate_letters) + \
            self.numerify(self.generator.parse('####')) + \
            self.random_element(ascii_uppercase) + \
            self.random_element(ascii_uppercase)

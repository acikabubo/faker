# coding=utf-8
from __future__ import unicode_literals

from collections import OrderedDict

from .. import Provider as ColorProvider

localized = True


class Provider(ColorProvider):
    all_colors = OrderedDict((
        ('Маслинеста', '#808000'),
        ('Сина', '#0000FF'),
        ('Сива', '#808080'),
        ('Црвена', '#FF0000'),
        ('Зелена', '#008000'),
        ('Виолетова', '#EE82EE'),
        ('Црна', '#000000'),
        ('Кафеава', '#A52A2A'),
        ('Портокалова', '#FFA500'),
        ('Жолта', '#FFFF00'),
        ('Златна', '#FFD700'),
        ('Розева', '#FFC0CB'),
        ('Бела', '#FFFFFF'),
        ('Тиркизна', '#40E0D0'),
        ('Сребрена', '#C0C0C0'),
    ))

    safe_colors = (
        'Маслинеста', 'Сина', 'Сива', 'Црвена', 'Зелена', 'Виолетова',
        'Црна', 'Кафеава', 'Портокалова', 'Жолта', 'Златна',
        'Розева', 'Бела', 'Тиркизна', 'Сребрена')

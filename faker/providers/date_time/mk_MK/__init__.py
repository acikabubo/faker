# coding: utf-8
from __future__ import unicode_literals
from .. import Provider as DateTimeProvider


class Provider(DateTimeProvider):

    @classmethod
    def day_of_week(cls):
        day = cls.date('%w')
        DAY_NAMES = {
            "0": "Недела",
            "1": "Понеделник",
            "2": "Вторник",
            "3": "Среда",
            "4": "Четврток",
            "5": "Петок",
            "6": "Сабота",
        }
        return DAY_NAMES[day]

    @classmethod
    def month_name(cls):
        month = cls.month()
        MONTH_NAMES = {
            "01": "Јануари",
            "02": "Февруари",
            "03": "Март",
            "04": "Април",
            "05": "Мај",
            "06": "Јуни",
            "07": "Јули",
            "08": "Август",
            "09": "Септември",
            "10": "Октомври",
            "11": "Ноември",
            "12": "Декември",
        }
        return MONTH_NAMES[month]
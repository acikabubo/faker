# coding=utf-8
from __future__ import unicode_literals
from .. import Provider as InternetProvider


class Provider(InternetProvider):

    user_name_formats = (
        '{{last_name_female}}.{{first_name_female}}',
        '{{first_name_female}}.{{last_name_female}}',
        '{{last_name_male}}.{{first_name_male}}',
        '{{first_name_male}}.{{last_name_male}}',
        '{{first_name}}##',
        '{{last__name}}##',
        '?{{last_name}}',
        '{{first_name}}{{year}}'
    )

    email_formats = (
        '{{user_name}}@{{free_email_domain}}',
        '{{user_name}}@{{domain_name}}')

    free_email_domains = (
        'gmail.com', 'yahoo.com', 'hotmail.com', 'mail.mk'
    )

    tlds = ('mk', 'com', 'biz', 'info', 'net', 'org', 'edu')

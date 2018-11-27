from __future__ import unicode_literals
from .. import Provider as PhoneNumberProvider


class Provider(PhoneNumberProvider):
    formats = (
        '02 ### ####',
        '03# ## ####',
        '04# ## ####',
        '05# #####',
        '07# ### ###',
        '0800 #####'
    )

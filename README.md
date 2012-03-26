# Autoauth

Autoauth will log your users in automatically when they click a link.

## Installation

#. Install django-autoauth
#. add ``autoauth`` to your ``INSTALLED_APPS``
#. ``syncdb`` (or ``migrate``, if you're that awesome)
#. generate some keys

## Security

 - The link is only good once
 - It also expires

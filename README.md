# Autoauth

[![Build Status](https://secure.travis-ci.org/BrianHicks/autoauth.png?branch=develop)](http://travis-ci.org/BrianHicks/autoauth)

Autoauth will log your users in automatically when they click a link.

## Installation

1. Install django-autoauth
2. add ``autoauth`` to your ``INSTALLED_APPS``
3. ``syncdb`` (or ``migrate``, if you're that awesome)
4. generate some keys

## Security

 - The link is only good once
 - It also expires

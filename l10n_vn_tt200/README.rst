.. image:: https://img.shields.io/badge/licence-AGPL--3-blue.svg
   :target: http://www.gnu.org/licenses/agpl-3.0-standalone.html
   :alt: License: AGPL-3

Vietnamese Chart of Accounts
============================

With the new development, the module is now:
--------------------------------------------
* fully in compliance with the Circular #200/2014/TT-BTC dated Dec 22, 2014 by the Ministry of Finance which came into force on Jan 1, 2015
* partially in compliance with the Circular #133/2016/TT-BTC dated Aug 26, 2016 by the Ministry of Finance which came into force on Jan 1, 2017.

The folling has been done and integrated
----------------------------------------
* More common taxes (e.g. import, export, special consumption, nature resource usage, etc)
* Complete Chart of Accounts
* Add one more field named code to the model account.account.tag so that Vietnamese accountants can use it the way of parent view account (like what was before Odoo 9). This bring peace to the accountants.
* New account tags data has been added to use in the similar way of parent view accounts before Odoo 9. For example, accountant now can group all accounts 111xxx using account the tag 111.
* Accounts now link to the tags having corresponding code. E.g. account 1111 and 1112 .... 111x have the same account tag of 111.
* According to Vietnam law, sale and purchase journals must have a dedicated sequence for any refund.

Installation
============

Note that this module conflicts with l10n_vn, just install only one of them.

Known issues / Roadmap
======================

* There are a few accounts conflicts between those two circular (e.g. 3385, 3386, etc) which can be handled manually in the meantime. Future development should allow admin to select an appropriate COA (either c200 or c133)

Bug Tracker
===========

Bugs are tracked on `GitHub Issues <https://github.com/trobz/l10n-vn/issues>`_.
In case of trouble, please check there if your issue has already been reported.
If you spotted it first, help us smashing it by providing a detailed and welcomed feedback.

Credits
=======

* General Solutions.
* Trobz
* ERPOnline

Images
------

* Odoo Community Association: `Icon <https://github.com/OCA/maintainer-tools/blob/master/template/module/static/description/icon.svg>`_.

Contributors
------------

* Cuong Pham Khac <cuongpk@trobz.com>

Maintainer
----------

.. image:: https://odoo-community.org/logo.png
   :alt: Odoo Community Association
   :target: https://odoo-community.org

This module is maintained by the OCA.

OCA, or the Odoo Community Association, is a nonprofit organization whose
mission is to support the collaborative development of Odoo features and
promote its widespread use.

To contribute to this module, please visit https://odoo-community.org.

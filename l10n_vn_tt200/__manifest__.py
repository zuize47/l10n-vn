# Copyright 2009-2018 Trobz (http://trobz.com)
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

{
    "name": "Vietnam - Accounting",
    "version": "11.0.1",
    "category": "Localization/Account Charts",
    "description": """
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

Installation:
-------------
* Note that this module conflicts with l10n_vn, just install only one of them.

Known issues
-------------
* There are a few accounts conflicts between those two circular (e.g. 3385, 3386, etc) which can be handled manually in the meantime. Future development should allow admin to select an appropriate COA (either c200 or c133)

Credits
-------
* General Solutions
* Trobz
* ERPOnline

""",
    "author": "General Solutions, Trobz, ERPOnline, Odoo Community Association (OCA)",
    "website": "http://trobz.com",
    "depends": [
        "account",
        "base_iban",
    ],
    "data": [
        # DATA
        'data/account_tag_data.xml',
        'data/l10n_vn_chart_data.xml',
        'data/account_data.xml',
        'data/account_tax_data.xml',
        'data/account_chart_template_data.yml',
        'data/update_account_chart_data.yml',
    ],
    'post_init_hook': '_preserve_tag_on_taxes',
}

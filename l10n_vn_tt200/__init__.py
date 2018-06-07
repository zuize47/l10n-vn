# Copyright 2009-2018 Trobz (http://trobz.com)
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from . import models


def _preserve_tag_on_taxes(cr, registry):
    from odoo.addons.account.models.chart_template \
        import preserve_existing_tags_on_taxes
    preserve_existing_tags_on_taxes(cr, registry, 'l10n_vn_tt200')

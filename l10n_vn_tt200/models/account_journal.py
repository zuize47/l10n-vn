# Copyright 2009-2018 Trobz (http://trobz.com)
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import api, models


class AccountJournal(models.Model):
    _inherit = "account.journal"

    @api.model
    def _prepare_liquidity_account(self, name, company, currency_id, type):
        # Override to set Type of account 111, 112 to Current Assets
        res = super(AccountJournal, self)._prepare_liquidity_account(
            name, company, currency_id, type
        )
        current_asset_type = self.env.ref(
            'account.data_account_type_current_assets')
        res['user_type_id'] = current_asset_type and \
            current_asset_type.id or False

        return res

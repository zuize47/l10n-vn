# Copyright 2009-2018 Trobz (http://trobz.com)
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import models, fields, api


class AccountAccountTag(models.Model):
    _inherit = 'account.account.tag'

    code = fields.Char(
        'Code', help='The unique code of the tag. For example,'
                     '111 for cash, 112 for cash in banks, etc.')

    @api.multi
    def name_get(self):
        parent_result = super(AccountAccountTag, self).name_get()
        result = []
        for tag in self:
            if tag.code:
                result.append((tag.id, '%s - %s' % (tag.code, tag.name)))
            else:
                result.append((tag.id, tag.name))
        if len(result) > 0:
            return result
        return parent_result

    @api.model
    def name_search(self, name, args=None, operator='ilike', limit=100):
        args = args or []
        domain = []
        if name:
            domain = ['|', ('code', '=ilike', name + '%'),
                      ('name', operator, name)]
        tags = self.search(domain + args, limit=limit)
        return tags.name_get()

# -*- coding: utf-8 -*-

from openerp import models, api


class ResPartner(models.Model):
    _inherit = 'res.partner'

    @api.onchange('street')
    def onchange_street(self):
        self.street2 = 'BP60'

    @api.onchange('street2')
    def onchange_street2(self):
        if self.street2 == 'BP60':
            self.city = 'Lausanne'

    @api.onchange('city')
    def onchange_city(self):
        if self.city == 'Lausanne':
            self.country_id = self.env.ref('base.ch')

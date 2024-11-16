# -*- coding: utf-8 -*-
from odoo import models,fields


class ResPartner(models.Model):
    _inherit = 'res.partner'

    is_driver = fields.Boolean(string="Conducteur")
    email = fields.Char(string="Adresse e-mail")
    
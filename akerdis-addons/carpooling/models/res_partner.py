# -*- coding: utf-8 -*-
from odoo import models,fields,api
from odoo.api import depends_context, depends


class ResPartner(models.Model):
    _inherit = 'res.partner'

    is_driver = fields.Boolean(string="Conducteur")
    email = fields.Char(string="Adresse e-mail")

    @api.depends_context("lang")
    @api.depends("display_name")
    def _compute_display_name(self):
        super()._compute_display_name()
        for rec in self:
            if rec.is_driver:
                rec.display_name = rec.display_name + " Conducteur" if "Conducteur" not in rec.display_name else rec.display_name
            else:
                rec.display_name = rec.display_name.replace("Conducteur","")  if "Conducteur"  in rec.display_name else rec.display_name


    

# -*- coding: utf-8 -*-
from odoo import models,fields
from odoo.exceptions import ValidationError


class CarpoolingWizard(models.TransientModel):
    _name = "carpooling.wizard"
    _description = "Carpooling wizard"

    departure = fields.Char(string="Departure city")
    destination =fields.Char(string="Destination city")
    departure_date=fields.Date(string="Departure date")

    def search_trip(self):
        carpool=self.env['carpooling.carpooling'].search([('departure_city','=',self.departure),('destination_city','=',self.destination),('departure_date','=',self.departure_date)])

        if carpool:
            raise ValidationError(f'Carpool corespondant à votre demande exist déja id : {carpool.id}')
        else:
            raise ValidationError('Pas de  carpool ne corespondant à cotre demande')

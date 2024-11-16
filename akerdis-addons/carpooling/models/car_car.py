from odoo import models,fields


class Car(models.Model):
    _name="car.car"
    _description = "Car models"

    name=fields.Char(string="Car")
    carpooling_ids = fields.One2many("carpooling.carpooling",'car_id',string="Carpoolings")
    brand=fields.Char(string="Brand")
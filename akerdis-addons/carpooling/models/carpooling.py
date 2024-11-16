# -*- coding: utf-8 -*-
from odoo import models,fields,api
from odoo.api import onchange
from odoo.exceptions import ValidationError
from urllib3.util.wait import select_wait_for_socket

states = [
    ('new',"New"),
    ('available',"has a seat available"),
    ('full',"Full")
    ]

class TestAbstract(models.AbstractModel):
    _name = "test.abstract"
    _description = "Test Abstract"

    @onchange('name')
    def on_change_name(self):
        if self.name:
            self.name+=" un suffixe"

class Carpooling(models.Model):
    _name="carpooling.carpooling"
    _description="""This is a model for carpooling"""
    _inherit = ['mail.thread','mail.activity.mixin','test.abstract']
    _order = 'sequence asc'

    name=fields.Char("Name")
    taken_seats=fields.Integer(string="Taken Seat",tracking=True)
    departure_time=fields.Float(name="Departure time")
    departure_date=fields.Date(name="Departure date")
    note = fields.Text('Note')
    is_free = fields.Boolean(name = "Is free")
    state = fields.Selection(selection=states,default='new')
    company_currency = fields.Many2one('res.currency',string="Currency",compute="_compute_company_currency")
    amount_per_km = fields.Monetary(string="Amount per km",currency_field="company_currency")
    resume = fields.Html('Resume')
    image = fields.Binary(string="Image")
    car_id = fields.Many2one("car.car",string="Car")
    brand= fields.Char(string="Marque",related="car_id.brand", readonly=False)
    tag_ids = fields.Many2many('tag.tag',string='Tags')
    km = fields.Float(string="KM")
    cost = fields.Monetary(string="Cost",currency_field="company_currency",compute="_compute_cost")
    departure_city =fields.Char(string="Departure city")
    destination_city =fields.Char(string="Destination city")
    sequence = fields.Integer("Sequence")


    def _run_cron(self):
        for car in self.search([]):
            car.taken_seats +=1



    @api.onchange('car_id')
    def on_change_car_id(self):
        cars = (self.env['car.car'].search([])
                .filtered(lambda car: "voiture" in car.name)
                .sorted(key=lambda car:car.name,reverse=True))
        print(cars)
        for rec in cars:
            print(rec.name)
    

    @api.onchange('departure_date')
    def on_change_km(self):
        self.increment_departure_time()

    @api.constrains('km')
    def _chek_km(self):
        for rec in self:
            if rec.km < 0:
                raise ValidationError("Le kilométrage doit être supérieur a zéro")
        
    @api.depends('km','amount_per_km')
    def _compute_cost(self):
        for rec in self:
            rec.cost = rec.km * rec.amount_per_km

    def _compute_company_currency(self):
        for rec in self:
            rec.company_currency = self.env.company.currency_id.id

    def increment_departure_time(self):
       return {
           'type':'ir.actions.act_window',
           'name':'Increment departure time',
           'res_model':'carpooling.wizard',
           'view_mode':'form',
           'target':'new'

       }
from odoo import models, fields, api


class StockPicking(models.Model):
    _inherit = 'stock.picking'

    label_bultos_count = fields.Integer(
        string='Cantidad de Bultos',
        default=1,
        help='Cantidad de bultos/paquetes a etiquetar para este envío. '
             'Se imprimirá una etiqueta por cada bulto (BULTO X / N).',
    )
    label_reference = fields.Char(
        string='Referencia de Etiqueta',
        help='Texto adicional a mostrar en la etiqueta, '
             'por ejemplo: "Es un PH", "Dpto 3B", etc.',
    )

    def action_print_shipping_labels(self):
        """Abre el reporte PDF con las etiquetas de envío."""
        self.ensure_one()
        if self.label_bultos_count <= 0:
            self.label_bultos_count = 1
        return self.env.ref(
            'stock_shipping_labels.action_report_shipping_labels'
        ).report_action(self)

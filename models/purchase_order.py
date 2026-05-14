from odoo import models, api


from odoo import models, api


class PurchaseOrderLine(models.Model):
    _inherit = 'purchase.order.line'

    @api.onchange('product_id')
    def _onchange_product_set_vendor(self):

        if not self.product_id:
            return

        suppliers = self.product_id.product_tmpl_id.seller_ids
        if not suppliers:
            return

        vendor_ids = suppliers.mapped('partner_id').ids

        # ✅ MUST use self.env.context copy
        ctx = dict(self.env.context)
        ctx.update({'allowed_vendor_ids': vendor_ids})

        return {
            'context': ctx
        }
class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'

    @api.onchange('partner_id')
    def _onchange_partner_id_filter_products(self):

        if not self.partner_id:
            return {
                'domain': {
                    'order_line.product_id': [('purchase_ok', '=', True)]
                }
            }

        return {
            'domain': {
                'order_line.product_id': [
                    ('purchase_ok', '=', True),
                    ('seller_ids.partner_id', '=', self.partner_id.id)
                ]
            }
        }
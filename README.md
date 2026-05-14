# Vendor Product Binding

![Version](https://img.shields.io/badge/version-19.0.1.0.0-blue)
![Category](https://img.shields.io/badge/category-Purchase-green)
![License](https://img.shields.io/badge/license-LGPL-3-orange)

| | |
|---|---|
| **Name** | Vendor Product Binding |
| **Version** | 19.0.1.0.0 |
| **Category** | Purchase |
| **License** | LGPL-3 |
| **Application** | No (Addon) |

## Description

Bind products to vendors on Purchase Orders

## Functionality

### Models & Fields

#### Extends `purchase.order.line, purchase.order`

**File:** `models/purchase_order.py`

**Inherits:** `purchase.order.line`, `purchase.order`

**Key Methods:**

- `_onchange_product_set_vendor()` — Onchange handler
- `_onchange_partner_id_filter_products()` — Onchange handler

## Dependencies

| Module | Type |
|--------|------|
| `purchase` | Odoo Core |

## File Structure

```
vendor_product_binding/
├── LICENSE
├── README.md
├── __init__.py
├── __manifest__.py
├── models/
│   ├── __init__.py
│   └── purchase_order.py
└── views/
    └── purchase_order_view.xml
```

## Installation

This module is part of the **[odoo-purchase-vendor-suite](https://github.com/tejas7287/odoo-purchase-vendor-suite)** suite.

1. Place this module in your Odoo addons directory
2. Update the apps list: **Settings** → **Apps** → **Update Apps List**
3. Search for **"Vendor Product Binding"** and click **Install**

## License

LGPL-3

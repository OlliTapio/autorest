# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from .base_product import BaseProduct


class SimpleProduct(BaseProduct):
    """
    The product documentation.

    :param str product_id: Unique identifier representing a specific product
     for a given latitude & longitude. For example, uberX in San Francisco
     will have a different product_id than uberX in Los Angeles.
    :param str description: Description of product.
    :param str max_product_display_name: Display name of product.
    :param str capacity: Capacity of product. For example, 4 people. Default
     value: "Large" .
    :param str odatavalue: URL value.
    """ 

    _validation = {
        'product_id': {'required': True},
        'max_product_display_name': {'required': True},
        'capacity': {'required': True},
    }

    _attribute_map = {
        'product_id': {'key': 'base_product_id', 'type': 'str'},
        'description': {'key': 'base_product_description', 'type': 'str'},
        'max_product_display_name': {'key': 'details.max_product_display_name', 'type': 'str'},
        'capacity': {'key': 'details.max_product_capacity', 'type': 'str'},
        'odatavalue': {'key': 'details.max_product_image.@odata\\.value', 'type': 'str'},
    }

    def __init__(self, product_id, max_product_display_name, description=None, odatavalue=None, **kwargs):
        super(SimpleProduct, self).__init__(product_id=product_id, description=description, **kwargs)
        self.max_product_display_name = max_product_display_name
        self.capacity = "Large"
        self.odatavalue = odatavalue
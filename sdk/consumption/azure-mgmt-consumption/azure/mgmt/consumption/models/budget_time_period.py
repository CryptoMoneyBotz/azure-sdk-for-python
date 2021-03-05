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

from msrest.serialization import Model


class BudgetTimePeriod(Model):
    """The start and end date for a budget.

    All required parameters must be populated in order to send to Azure.

    :param start_date: Required. The start date for the budget.
    :type start_date: datetime
    :param end_date: The end date for the budget. If not provided, we default
     this to 10 years from the start date.
    :type end_date: datetime
    """

    _validation = {
        'start_date': {'required': True},
    }

    _attribute_map = {
        'start_date': {'key': 'startDate', 'type': 'iso-8601'},
        'end_date': {'key': 'endDate', 'type': 'iso-8601'},
    }

    def __init__(self, **kwargs):
        super(BudgetTimePeriod, self).__init__(**kwargs)
        self.start_date = kwargs.get('start_date', None)
        self.end_date = kwargs.get('end_date', None)
# -*- coding: utf-8 -*-
#
# This file is part of SENAITE.HEALTH
#
# Copyright 2018 by it's authors.
# Some rights reserved. See LICENSE.rst, CONTRIBUTORS.rst.

from bika.health.browser.samples.folder_view import SamplesView
from Products.CMFCore.utils import getToolByName


class SamplesView(SamplesView):

    def __init__(self, context, request):
        super(SamplesView, self).__init__(context, request)
        self.contentFilter['getDoctorUID'] = self.context.UID()

"""
Copyright (c) 2018 Keitaro AB

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Affero General Public License as
published by the Free Software Foundation, either version 3 of the
License, or (at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Affero General Public License for more details.

You should have received a copy of the GNU Affero General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""

import ckan.plugins as plugins
import ckan.plugins.toolkit as toolkit

from ckanext.mk_dcatap.validators import request_data_only_members_in_org_validator, request_data_only_required
from ckanext.mk_dcatap.helpers import get_spatial_uri, get_spatial_location_name

class Mk_DcatapPlugin(plugins.SingletonPlugin):
    plugins.implements(plugins.IConfigurer)
    plugins.implements(plugins.IValidators)
    plugins.implements(plugins.ITemplateHelpers)

    # IConfigurer

    def update_config(self, config_):
        toolkit.add_template_directory(config_, 'templates')
        toolkit.add_public_directory(config_, 'public')
        toolkit.add_resource('fanstatic', 'mk_dcatap')
    
    def get_validators(self):
        return {
            'request_data_only_members_in_owner_org': request_data_only_members_in_org_validator,
            'request_data_only_required': request_data_only_required
        }
    
    def get_helpers(self):
        return {
            'mk_dcatap_spatial_uri_from_code': get_spatial_uri,
            'mk_dcatap_spatial_name_from_code': get_spatial_location_name,
        }
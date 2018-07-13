import ckan.plugins as plugins
import ckan.plugins.toolkit as toolkit

from ckanext.mk_dcatap.validators import request_data_only_members_in_org_validator, request_data_only_required
from ckanext.mk_dcatap.helpers import get_spatial_uri

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
            'mk_dcatap_spatial_uri_from_code': get_spatial_uri
        }
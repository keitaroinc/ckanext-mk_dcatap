import os
import inspect
import json


def _load_resource_from_path(url):
    """
    Given a path like "ckanext.mk_dcatap:resource.json"
    find the second part relative to the import path of the first
    """

    module, file_name = url.split(':', 1)
    try:
        # __import__ has an odd signature
        m = __import__(module, fromlist=[''])
    except ImportError:
        raise
    p = os.path.join(os.path.dirname(inspect.getfile(m)), file_name)
    with open(p) as resource_file:
        return resource_file.read()


_SPATIAL_CODES_MAP = None

def _load_spatial_codes(mapping_file):
    mappings = _load_resource_from_path(mapping_file)
    mappings = json.loads(mappings)
    return mappings


def _get_spatial_codes_mappings():
    global _SPATIAL_CODES_MAP
    if not _SPATIAL_CODES_MAP:
        _SPATIAL_CODES_MAP = json.loads(_load_resource_from_path('ckanext.mk_dcatap:codes_spatial_mapping.json'))
    return _SPATIAL_CODES_MAP

def get_spatial_uri(code):
    """Translates an ISO-3166-2 codes for Macedonia into URI references.

    :param str code: The ISO-3166-2 code for the location. This must be a location in Macedonia. See
        the file ``codes_spatial_mappings.json`` for all available mappings.

    :returns: the spatial URI for that location.
    """
    mappings = _get_spatial_codes_mappings()
    mapping = mappings.get(code)
    if mapping:
        return mapping['spatial_uri']
    return None
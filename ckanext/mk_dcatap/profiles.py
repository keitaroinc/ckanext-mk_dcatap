from rdflib.namespace import Namespace, RDF, XSD, SKOS, RDFS
from rdflib import Literal, URIRef, BNode
from ckanext.dcat.profiles import EuropeanDCATAPProfile, namespaces as dcat_namespaces
from ckanext.dcat.utils import resource_uri
from ckan.lib.i18n import get_available_locales
from ckan.model.license import LicenseRegister
from ckanext.dcat.utils import resource_uri, publisher_uri_from_dataset_dict
from ckanext.mk_dcatap.helpers import get_spatial_uri

from ckantoolkit import config

from geomet import wkt, InvalidGeoJSONException

from datetime import datetime
import json


DCT = Namespace("http://purl.org/dc/terms/")
DCAT = Namespace("http://www.w3.org/ns/dcat#")
ADMS = Namespace("http://www.w3.org/ns/adms#")
VCARD = Namespace("http://www.w3.org/2006/vcard/ns#")
FOAF = Namespace("http://xmlns.com/foaf/0.1/")
SCHEMA = Namespace('http://schema.org/')
TIME = Namespace('http://www.w3.org/2006/time')
LOCN = Namespace('http://www.w3.org/ns/locn#')
GSP = Namespace('http://www.opengis.net/ont/geosparql#')
OWL = Namespace('http://www.w3.org/2002/07/owl#')
SPDX = Namespace('http://spdx.org/rdf/terms#')


GEOJSON_IMT = 'https://www.iana.org/assignments/media-types/application/vnd.geo+json'


namespaces = {
    'dct': DCT,
    'dcat': DCAT,
    'adms': ADMS,
    'vcard': VCARD,
    'foaf': FOAF,
    'schema': SCHEMA,
    'time': TIME,
    'skos': SKOS,
    'locn': LOCN,
    'gsp': GSP,
    'owl': OWL,
}


DCAT_CATALOG_IS_PART_OF = "ckan.dcat.catalog.is_part_of"
DCAT_CATALOG_HAS_PART = "ckan.dcat.catalog.has_part"
DCAT_RIGHTS_STATEMENT = "ckan.dcat.rights_statement"


class MacedonianDCATAPProfile(EuropeanDCATAPProfile):
    """
    An RDF profile based on the DCAT-AP for data portals in Europe.

    More information and specification:
    https://joinup.ec.europa.eu/asset/dcat_application_profile
    """

    def parse_dataset(self, dataset_dict, dataset_ref):
        super(MacedonianDCATAPProfile, self).parse_dataset(dataset_dict, dataset_ref)
    
    def graph_from_dataset(self, dataset_dict, dataset_ref):

        g = self.g

        for prefix, namespace in namespaces.items():
            g.bind(prefix, namespace)

        # -- start
        g.add((dataset_ref, RDF.type, DCAT.Dataset))

        # Basic fields
        items = [
            ('title', DCT.title, None, Literal),
            ('notes', DCT.description, None, Literal),
            ('url', DCAT.landingPage, None, URIRef),
            ('identifier', DCT.identifier, ['guid', 'id'], Literal),
            ('version', OWL.versionInfo, ['dcat_version'], Literal),
            ('version_notes', ADMS.versionNotes, None, Literal),
            ('frequency', DCT.accrualPeriodicity, None, URIRef),
            ('subject', DCT.subject, None, URIRef),  # Mentioned in the vocabulary
            ('provenance', DCT.provenance, None, URIRef)
        ]
        self._add_triples_from_dict(dataset_dict, dataset_ref, items)

        # Tags
        for tag in dataset_dict.get('tags', []):
            g.add((dataset_ref, DCAT.keyword, Literal(tag['name'])))

        # Dates
        items = [
            ('issued', DCT.issued, ['metadata_created'], Literal),
            ('modified', DCT.modified, ['metadata_modified'], Literal),
        ]
        self._add_date_triples_from_dict(dataset_dict, dataset_ref, items)

        #  Lists
        items = [
            ('language', DCT.language, None, URIRef),
            ('theme', DCAT.theme, None, URIRef),
            ('spatial_uri', DCT.spatial, None, URIRef),
            ('conforms_to', DCT.conformsTo, None, URIRef),
            ('alternate_identifier', ADMS.identifier, None, Literal),
            ('documentation', FOAF.page, None, URIRef),
            ('access_rights', DCT.accessRights, None, URIRef),            
            ('related_resource', DCT.relation, None, URIRef),
            ('has_version', DCT.hasVersion, None, Literal),
            ('is_version_of', DCT.isVersionOf, None, Literal),
            ('source', DCT.source, None, Literal),
            ('sample', ADMS.sample, None, Literal)
        ]
        self._add_list_triples_from_dict(dataset_dict, dataset_ref, items)

        # Contact details
        if any([
            self._get_dataset_value(dataset_dict, 'contact_uri'),
            self._get_dataset_value(dataset_dict, 'contact_name'),
            self._get_dataset_value(dataset_dict, 'contact_email'),
            self._get_dataset_value(dataset_dict, 'maintainer'),
            self._get_dataset_value(dataset_dict, 'maintainer_email'),
        ]):

            contact_uri = self._get_dataset_value(dataset_dict, 'contact_uri')
            if contact_uri:
                contact_details = URIRef(contact_uri)
            else:
                contact_details = BNode()

            g.add((contact_details, RDF.type, VCARD.Kind))
            g.add((dataset_ref, DCAT.contactPoint, contact_details))

            items = [
                ('contact_name', VCARD.fn, ['maintainer'], Literal),
                ('contact_email', VCARD.hasEmail, ['maintainer_email'], Literal),
            ]

            self._add_triples_from_dict(dataset_dict, contact_details, items)

        # Publisher
        if any([
            self._get_dataset_value(dataset_dict, 'publisher_uri'),
            self._get_dataset_value(dataset_dict, 'publisher_name'),
            self._get_dataset_value(dataset_dict, 'publisher_identifier'),
            dataset_dict.get('organization'),
        ]):

            publisher_uri = publisher_uri_from_dataset_dict(dataset_dict)
            if publisher_uri:
                publisher_details = URIRef(publisher_uri)
            else:
                # No organization nor publisher_uri
                publisher_details = BNode()

            g.add((publisher_details, RDF.type, FOAF.Agent))
            g.add((dataset_ref, DCT.publisher, publisher_details))

            publisher_name = self._get_dataset_value(dataset_dict, 'publisher_name')
            if not publisher_name and dataset_dict.get('organization'):
                publisher_name = dataset_dict['organization']['title']

            g.add((publisher_details, FOAF.name, Literal(publisher_name)))
            # TODO: It would make sense to fallback these to organization
            # fields but they are not in the default schema and the
            # `organization` object in the dataset_dict does not include
            # custom fields
            items = [
                ('publisher_email', FOAF.mbox, None, Literal),
                ('publisher_identifier', DCT.identifier, None, Literal),
                ('publisher_url', FOAF.homepage, None, URIRef),
                ('publisher_type', DCT.type, None, Literal)
            ]

            self._add_triples_from_dict(dataset_dict, publisher_details, items)

        # Temporal
        start = self._get_dataset_value(dataset_dict, 'temporal_start')
        end = self._get_dataset_value(dataset_dict, 'temporal_end')
        if start or end:
            temporal_extent = BNode()

            g.add((temporal_extent, RDF.type, DCT.PeriodOfTime))
            if start:
                self._add_date_triple(temporal_extent, SCHEMA.startDate, start)
            if end:
                self._add_date_triple(temporal_extent, SCHEMA.endDate, end)
            g.add((dataset_ref, DCT.temporal, temporal_extent))
        
        # parts - has part/is part of

        if any([
            self._get_dataset_value(dataset_dict, 'has_part'),
            self._get_dataset_value(dataset_dict, 'is_part_of')
        ]):
            items = [
                ('has_part', DCT.hasPart, None, URIRef),
                ('is_part_of', DCT.isPartOf, None, URIRef)
            ]

            self._add_list_triples_from_dict(dataset_dict, dataset_ref, items)


        # Spatial
        spatial_uri = self._get_dataset_value(dataset_dict, 'spatial_uri')
        spatial_text = self._get_dataset_value(dataset_dict, 'spatial_text')
        spatial_geom = self._get_dataset_value(dataset_dict, 'spatial')

        if spatial_uri:
            spatial_uri = get_spatial_uri(spatial_uri)  # map from code to URI

        if spatial_uri or spatial_text or spatial_geom:
            if spatial_uri:
                spatial_ref = URIRef(spatial_uri)
            else:
                spatial_ref = BNode()

            g.add((spatial_ref, RDF.type, DCT.Location))
            g.add((dataset_ref, DCT.spatial, spatial_ref))

            if spatial_text:
                g.add((spatial_ref, SKOS.prefLabel, Literal(spatial_text)))

            if spatial_geom:
                # GeoJSON
                g.add((spatial_ref,
                       LOCN.geometry,
                       Literal(spatial_geom, datatype=GEOJSON_IMT)))
                # WKT, because GeoDCAT-AP says so
                try:
                    g.add((spatial_ref,
                           LOCN.geometry,
                           Literal(wkt.dumps(json.loads(spatial_geom),
                                             decimals=4),
                                   datatype=GSP.wktLiteral)))
                except (TypeError, ValueError, InvalidGeoJSONException):
                    pass

        # Resources
        for resource_dict in dataset_dict.get('resources', []):

            distribution = URIRef(resource_uri(resource_dict))

            g.add((dataset_ref, DCAT.distribution, distribution))

            g.add((distribution, RDF.type, DCAT.Distribution))

            if 'license' not in resource_dict and 'license_id' in dataset_dict:
                lr = LicenseRegister()
                _license = lr.get(dataset_dict['license_id'])
                if _license:
                    resource_dict['license'] = _license.url

            #  Simple values
            items = [
                ('name', DCT.title, None, Literal),
                ('description', DCT.description, None, Literal),
                ('status', ADMS.status, None, Literal),
                ('rights', DCT.rights, None, Literal),
                ('license', DCT.license, None, URIRef),
            ]

            self._add_triples_from_dict(resource_dict, distribution, items)

            #  Lists
            items = [
                ('documentation', FOAF.page, None, URIRef),
                ('language', DCT.language, None, URIRef),
                ('conforms_to', DCT.conformsTo, None, URIRef),
            ]
            self._add_list_triples_from_dict(resource_dict, distribution, items)

            # Format
            if '/' in resource_dict.get('format', ''):
                g.add((distribution, DCAT.mediaType,
                       Literal(resource_dict['format'])))
            else:
                if resource_dict.get('format'):
                    g.add((distribution, DCT['format'],
                           Literal(resource_dict['format'])))

                if resource_dict.get('mimetype'):
                    g.add((distribution, DCAT.mediaType,
                           Literal(resource_dict['mimetype'])))

            # URL
            url = resource_dict.get('url')
            download_url = resource_dict.get('download_url')
            if download_url:
                g.add((distribution, DCAT.downloadURL, URIRef(download_url)))
            if (url and not download_url) or (url and url != download_url):
                g.add((distribution, DCAT.accessURL, URIRef(url)))

            # Dates
            items = [
                ('issued', DCT.issued, None, Literal),
                ('modified', DCT.modified, None, Literal),
            ]

            self._add_date_triples_from_dict(resource_dict, distribution, items)

            # Numbers
            if resource_dict.get('size'):
                try:
                    g.add((distribution, DCAT.byteSize,
                           Literal(float(resource_dict['size']),
                                   datatype=XSD.decimal)))
                except (ValueError, TypeError):
                    g.add((distribution, DCAT.byteSize,
                           Literal(resource_dict['size'])))
            # Checksum
            if resource_dict.get('hash'):
                checksum = BNode()
                g.add((checksum, SPDX.checksumValue,
                       Literal(resource_dict['hash'],
                               datatype=XSD.hexBinary)))

                if resource_dict.get('hash_algorithm'):
                    if resource_dict['hash_algorithm'].startswith('http'):
                        g.add((checksum, SPDX.algorithm,
                               URIRef(resource_dict['hash_algorithm'])))
                    else:
                        g.add((checksum, SPDX.algorithm,
                               Literal(resource_dict['hash_algorithm'])))
                g.add((distribution, SPDX.checksum, checksum))
    
    def graph_from_catalog(self, catalog_dict, catalog_ref):

        g = self.g

        for prefix, namespace in namespaces.items():
            g.bind(prefix, namespace)

        g.add((catalog_ref, RDF.type, DCAT.Catalog))

        g.add((catalog_ref, DCT.description, Literal('Data catalogue of the Government of Macedonia')))

        if config.get('ckan.dcat.publisher', False):
            publisher_details = URIRef(config.get('ckan.dcat.publisher'))
        else:
            publisher_details = URIRef('{}/publisher/'.format(config.get('ckan.site_url')))
        g.add((catalog_ref, DCT.publisher, publisher_details))

        self.g.add((publisher_details, DCT.identifier, Literal(config.get('ckan.dcat.publisher.identifier', 'MISA'))))
        self.g.add((publisher_details, FOAF.homepage, URIRef(config.get('ckan.dcat.publisher.webpage', 'https://opendata.gov.mk'))))
        self.g.add((publisher_details, RDF.type, FOAF.Agent))

        
        g.add((catalog_ref, DCT.title, Literal(config.get('ckan.dcat.catalog.title', 'data.gov.mk'))))

        locales = get_available_locales()
        for locale in locales:
            g.add((catalog_ref, DCT.language, Literal(str(locale))))
        
        g.add((catalog_ref, DCT.license, URIRef(config.get('ckan.dcat.catalog.license_url','https://creativecommons.org/publicdomain/zero/1.0/'))))

        issued = config.get('ckan.dcat.catalog.issued')  # Should be string with supported datetime format
        if issued:
            self._add_date_triple(catalog_ref, DCT.issued, issued)

        g.add((catalog_ref, DCAT.themeTaxonomy, URIRef(config.get('ckan.dcat.theme_taxonomy_uri',"http://publications.europa.eu/mdr/authority/data-theme/"))))

        if config.get(DCAT_CATALOG_HAS_PART, False):
            g.add((catalog_ref, DCT.hasPart, URIRef(config.get(DCAT_CATALOG_HAS_PART))))
        
        if config.get(DCAT_CATALOG_IS_PART_OF, False):
            g.add((catalog_ref, DCT.isPartOf, URIRef(config.get(DCAT_CATALOG_IS_PART_OF))))

        if config.get(DCAT_RIGHTS_STATEMENT, False):
            g.add((catalog_ref, DCT.rights, Literal(config.get(DCAT_RIGHTS_STATEMENT))))
        
        g.add((catalog_ref, DCT.spatial, URIRef(config.get('ckan.dcat.spatial', "http://www.geonames.org/718075"))))
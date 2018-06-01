from rdflib.namespace import Namespace
from rdflib import Literal, URIRef, BNode, RDF
from ckanext.dcat.profiles import EuropeanDCATAPProfile, namespaces as dcat_namespaces
from ckanext.dcat.utils import resource_uri
from ckan.lib.i18n import get_available_locales

from ckantoolkit import config

from datetime import datetime


DCT = Namespace("http://purl.org/dc/terms/")
FOAF = Namespace("http://xmlns.com/foaf/0.1/")
DCAT = Namespace("http://www.w3.org/ns/dcat#")
RDFS = Namespace('http://www.w3.org/2000/01/rdf-schema#')
SKOS = Namespace('http://www.w3.org/2004/02/skos/core#')
VCARD = Namespace('http://www.w3.org/2006/vcard/ns#')
ADMS = Namespace('http://www.w3.org/ns/adms#')
OWL = Namespace('http://www.w3.org/2002/07/owl#')
SPDX = Namespace('http://spdx.org/rdf/terms#')
SCHEMA = Namespace('http://schema.org/')

namespaces = {
    'dct': DCT,
    'foaf': FOAF,
    'dcat': DCAT,
    'rdfs': RDFS,
    'skos': SKOS,
    'vcard': VCARD,
    'adms': ADMS,
    'owl': OWL,
    'spdx': SPDX,
    "schema": SCHEMA,
}


dcat_namespaces.update(namespaces)  # extend DCATs default namespaces

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

            for extra in dataset_dict.get('extras', []):
                if extra.get("key") == "related_resource":
                    g.add((dataset_ref, DCT.relation, URIRef(extra.get("value"))))
                elif extra.get("key") == "conforms_to":
                    g.add((dataset_ref, DCT.conformsTo, URIRef(extra.get("value"))))
                elif extra.get("key") == "language":
                    g.add((dataset_ref, DCT.language, Literal(extra.get("value"))))
                elif extra.get("key") == "dataset_type":
                    g.add((dataset_ref, DCT.type, Literal(extra.get("value"))))
            
            g.add((dataset_ref, DCT.modified, Literal(dataset_dict['metadata_modified'])))
    
    def graph_from_catalog(self, catalog_dict, catalog_ref):

        g = self.g

        g.add((catalog_ref, DCT.description, Literal('Data catalogue of the Government of Macedonia')))

        publisher_details = URIRef('{}/publisher/'.format(config.get('ckan.site_url')))
        g.add((catalog_ref, DCT.publisher, publisher_details))

        self.g.add((publisher_details, DCT.identifier, Literal(config.get('ckan.dcat.publisher.identifier', 'Publisher should be set in config: ckan.publisher.identifier'))))
        self.g.add((publisher_details, FOAF.homepage, URIRef(config.get('ckan.dcat.publisher.webpage', 'https://opendata.gov.mk'))))
        self.g.add((publisher_details, RDF.type, FOAF.Agent))

        
        g.add((catalog_ref, DCT.title, Literal(config.get('ckan.dcat.catalog.title', 'data.gov.mk'))))

        locales = get_available_locales()
        for locale in locales:
            g.add((catalog_ref, DCT.language, Literal(str(locale))))
        
        g.add((catalog_ref, DCT.license, Literal(config.get('ckan.dcat.catalog.license','CC0'))))

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
        
        g.add((catalog_ref, DCT.spatial, Literal(config.get('ckan.dcat.spatial', "MKD"))))
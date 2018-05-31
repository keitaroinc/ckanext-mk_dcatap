from rdflib.namespace import Namespace
from rdflib import Literal, URIRef, BNode, RDF
from ckanext.dcat.profiles import RDFProfile, namespaces as dcat_namespaces
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
}


dcat_namespaces.update(namespaces)  # extend DCATs default namespaces

DCAT_CATALOG_IS_PART_OF = "ckan.dcat.catalog.is_part_of"
DCAT_CATALOG_HAS_PART = "ckan.dcat.catalog.has_part"
DCAT_RIGHTS_STATEMENT = "ckan.dcat.rights_statement"


class MacedonianDCATAPProfile(RDFProfile):
    
    def parse_dataset(self, dataset_dict, dataset_ref):
        pass
    
    def graph_from_dataset(self, dataset_dict, dataset_ref):

            g = self.g
    
    def graph_from_catalog(self, catalog_dict, catalog_ref):

        g = self.g

        g.add((catalog_ref, DCT.description, Literal('Data catalogue of the Government of Macedonia')))

        agent = BNode()
        g.add((agent, RDF.type, FOAF.Organization))
        g.add((agent, FOAF.name, Literal('MISA')))
        g.add((catalog_ref, DCT.publisher, agent))
        
        g.add((catalog_ref, DCT.title, Literal('data.gov.mk')))

        # g.add((catalog_ref, FOAF.homepage, URIRef('https://opendata.gov.mk')))  # This is set to ckan.site_url

        locales = get_available_locales()
        for locale in locales:
            g.add((catalog_ref, DCT.language, Literal(str(locale))))
        
        g.add((catalog_ref, DCT.license, Literal("CC0")))

        g.add((catalog_ref, DCT.issued, Literal(datetime.now().strftime("d.m.Y"))))  # FIXME: Actual catalog issued date here

        g.add((catalog_ref, DCAT.themeTaxonomy, Literal("http://publications.europa.eu/mdr/authority/data-theme/")))

        if config.get(DCAT_CATALOG_HAS_PART, False):
            g.add((catalog_ref, DCT.hasPart, URIRef(config.get(DCAT_CATALOG_HAS_PART))))
        
        if config.get(DCAT_CATALOG_IS_PART_OF, False):
            g.add((catalog_ref, DCT.isPartOf, URIRef(config.get(DCAT_CATALOG_IS_PART_OF))))

        if config.get(DCAT_RIGHTS_STATEMENT, False):
            g.add((catalog_ref, DCT.rights, Literal(config.get(DCAT_RIGHTS_STATEMENT))))
        
        g.add((catalog_ref, DCT.spatial, Literal("MKD")))
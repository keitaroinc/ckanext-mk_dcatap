from rdflib.namespace import Namespace
from rdflib import Literal, URIRef
from ckanext.dcat.profiles import RDFProfile, namespaces as dcat_namespaces


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


class MacedonianDCATAPProfile(RDFProfile):
    
    def parse_dataset(self, dataset_dict, dataset_ref):
        pass
    
    def graph_from_dataset(self, dataset_dict, dataset_ref):

            g = self.g
    
    def graph_from_catalog(self, catalog_dict, catalog_ref):

        g = self.g

        g.add((catalog_ref, DCT.description, Literal('Data catalogue of the Government of Macedonia')))
        print('catalog_ref -> ', catalog_ref)

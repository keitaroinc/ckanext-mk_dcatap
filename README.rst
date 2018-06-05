.. You should enable this project on travis-ci.org and coveralls.io to make
   these badges work. The necessary Travis and Coverage config files have been
   generated for you.

.. image:: https://travis-ci.org//ckanext-mk_dcatap.svg?branch=master
    :target: https://travis-ci.org//ckanext-mk_dcatap

.. image:: https://coveralls.io/repos//ckanext-mk_dcatap/badge.svg
  :target: https://coveralls.io/r//ckanext-mk_dcatap

.. image:: https://pypip.in/download/ckanext-mk_dcatap/badge.svg
    :target: https://pypi.python.org/pypi//ckanext-mk_dcatap/
    :alt: Downloads

.. image:: https://pypip.in/version/ckanext-mk_dcatap/badge.svg
    :target: https://pypi.python.org/pypi/ckanext-mk_dcatap/
    :alt: Latest Version

.. image:: https://pypip.in/py_versions/ckanext-mk_dcatap/badge.svg
    :target: https://pypi.python.org/pypi/ckanext-mk_dcatap/
    :alt: Supported Python versions

.. image:: https://pypip.in/status/ckanext-mk_dcatap/badge.svg
    :target: https://pypi.python.org/pypi/ckanext-mk_dcatap/
    :alt: Development Status

.. image:: https://pypip.in/license/ckanext-mk_dcatap/badge.svg
    :target: https://pypi.python.org/pypi/ckanext-mk_dcatap/
    :alt: License

=============
ckanext-mk_dcatap
=============

.. Put a description of your extension here:
   What does it do? What features does it have?
   Consider including some screenshots or embedding a video!


------------
Requirements
------------

For example, you might want to mention here which versions of CKAN this
extension works with.


------------
Installation
------------

.. Add any additional install steps to the list below.
   For example installing any non-Python dependencies or adding any required
   config settings.

To install ckanext-mk_dcatap:

1. Activate your CKAN virtual environment, for example::

     . /usr/lib/ckan/default/bin/activate

2. Install the ckanext-mk_dcatap Python package into your virtual environment::

     pip install ckanext-mk_dcatap

3. Add ``mk_dcatap`` to the ``ckan.plugins`` setting in your CKAN
   config file (by default the config file is located at
   ``/etc/ckan/default/production.ini``).

4. Restart CKAN. For example if you've deployed CKAN with Apache on Ubuntu::

     sudo service apache2 reload


---------------
Config Settings
---------------

Document any optional config settings here. For example::

    # The minimum number of hours to wait before re-checking a resource
    # (optional, default: 24).
    ckanext.mk_dcatap.some_setting = some_default_value


------------------------
Development Installation
------------------------

To install ckanext-mk_dcatap for development, activate your CKAN virtualenv and
do::

    git clone https://github.com//ckanext-mk_dcatap.git
    cd ckanext-mk_dcatap
    python setup.py develop
    pip install -r dev-requirements.txt


-----------------
Running the Tests
-----------------

To run the tests, do::

    nosetests --nologcapture --with-pylons=test.ini

To run the tests and produce a coverage report, first make sure you have
coverage installed in your virtualenv (``pip install coverage``) then run::

    nosetests --nologcapture --with-pylons=test.ini --with-coverage --cover-package=ckanext.mk_dcatap --cover-inclusive --cover-erase --cover-tests


---------------------------------
Registering ckanext-mk_dcatap on PyPI
---------------------------------

ckanext-mk_dcatap should be availabe on PyPI as
https://pypi.python.org/pypi/ckanext-mk_dcatap. If that link doesn't work, then
you can register the project on PyPI for the first time by following these
steps:

1. Create a source distribution of the project::

     python setup.py sdist

2. Register the project::

     python setup.py register

3. Upload the source distribution to PyPI::

     python setup.py sdist upload

4. Tag the first release of the project on GitHub with the version number from
   the ``setup.py`` file. For example if the version number in ``setup.py`` is
   0.0.1 then do::

       git tag 0.0.1
       git push --tags


----------------------------------------
Releasing a New Version of ckanext-mk_dcatap
----------------------------------------

ckanext-mk_dcatap is availabe on PyPI as https://pypi.python.org/pypi/ckanext-mk_dcatap.
To publish a new version to PyPI follow these steps:

1. Update the version number in the ``setup.py`` file.
   See `PEP 440 <http://legacy.python.org/dev/peps/pep-0440/#public-version-identifiers>`_
   for how to choose version numbers.

2. Create a source distribution of the new version::

     python setup.py sdist

3. Upload the source distribution to PyPI::

     python setup.py sdist upload

4. Tag the new release of the project on GitHub with the version number from
   the ``setup.py`` file. For example if the version number in ``setup.py`` is
   0.0.2 then do::

       git tag 0.0.2
       git push --tags

---------------------------
CKAN Configuration Settings
---------------------------

To use the Macedonian RDF DCAT profile you need to install this extension and set up some properties in CKAN:

* ``ckan.site_url`` (URL)- set this to your site.
* ``ckan.dcat.publisher`` (URI) - sets ``dct:publisher`` (``URIRef``) in the DCAT Catalog. If not set, then ``ckan.site_url`` + ``"/publisher/"`` is used as the publisher URI.
* ``ckan.dcat.publisher.identifier`` - sets ``dct:identifier`` (``Literal``) in the DCAT Catalog. The identifier of the data catalog publisher. The default value is ``MISA``.
* ``ckan.dcat.publisher.webpage`` - sets ``foaf:homepage`` (``URIRef``) in the DCAT Catalog. The webpage of the publisher. Default is ``https://opendata.gov.mk``.
* ``ckan.dcat.catalog.title`` - sets ``dct:title`` (``Literal``) in the DCAT Catalog. Data catalog title. Default: ``data.gov.mk``
* ``ckan.dcat.catalog.license_url`` - sets ``dct:license`` (``URIRef``) in the DCAT Catalog. This is the data catalog license (not data license). Default: ``https://creativecommons.org/publicdomain/zero/1.0/``
* ``ckan.dcat.catalog.issued`` - sets ``dct:issues`` (``Literal``) in the DCAT Catalog. Date of issuing of the catalog. Must be in format ``dd.mm.YYY``, for example: ``24.05.2018``
* ``ckan.dcat.theme_taxonomy_uri`` - sets ``dcat:themeTaxonomy`` (``URIRef``) in the DCAT Catalog. Taxonomy theme URI. Default: ``http://publications.europa.eu/mdr/authority/data-theme/``.
* ``ckan.dcat.spatial`` - sets ``dct:spatial`` (``URIRef``) in the DCAT Catalog. Spatial location. Default value is: ``http://www.geonames.org/718075``.
* ``ckan.dcat.catalog.is_part_of`` - sets ``dct:isPartOf`` (``URIRef``) in the DCAT Catalog. URI to the catalog of which this catalog is part of. Not used by default.
* ``ckan.dcat.catalog.has_part`` - sets ``dct:hasPart`` (``URIRef``) in the DCAT Catalog. URI to the catalog that is part of this catalog. Not used by default.
* ``ckan.dcat.catalog.rights_statement`` - sets ``dct:rights`` (``Literal``) in the DCAT Catalog. The access rights statement. Not used by default.





--------------------------------
RDF DCAT to CKAN dataset mapping
--------------------------------

The follwing table describes the mapping between CKAN dataset field and RDF DCAT fields.




+-------------------+------------------------+-------------------------------------------+--------------------------------+-----------+---------------------------------------------------------------------------------------------------------------------------------------------------------------+
| DCAT class        | DCAT property          | CKAN dataset field                        | CKAN fallback fields           | Stored as |                                                                                                                                                               |
+-------------------+------------------------+-------------------------------------------+--------------------------------+-----------+---------------------------------------------------------------------------------------------------------------------------------------------------------------+
| dcat:Dataset      |                        | extra:uri                                 |                                | text      | See note about URIs                                                                                                                                           |
+-------------------+------------------------+-------------------------------------------+--------------------------------+-----------+---------------------------------------------------------------------------------------------------------------------------------------------------------------+
| dcat:Dataset      | dct:title              | title                                     |                                | text      |                                                                                                                                                               |
+-------------------+------------------------+-------------------------------------------+--------------------------------+-----------+---------------------------------------------------------------------------------------------------------------------------------------------------------------+
| dcat:Dataset      | dct:description        | notes                                     |                                | text      |                                                                                                                                                               |
+-------------------+------------------------+-------------------------------------------+--------------------------------+-----------+---------------------------------------------------------------------------------------------------------------------------------------------------------------+
| dcat:Dataset      | dcat:keyword           | tags                                      |                                | text      |                                                                                                                                                               |
+-------------------+------------------------+-------------------------------------------+--------------------------------+-----------+---------------------------------------------------------------------------------------------------------------------------------------------------------------+
| dcat:Dataset      | dcat:theme             | extra:theme                               |                                | list      | See note about lists                                                                                                                                          |
+-------------------+------------------------+-------------------------------------------+--------------------------------+-----------+---------------------------------------------------------------------------------------------------------------------------------------------------------------+
| dcat:Dataset      | dct:identifier         | extra:identifier                          | extra:guid, id                 | text      |                                                                                                                                                               |
+-------------------+------------------------+-------------------------------------------+--------------------------------+-----------+---------------------------------------------------------------------------------------------------------------------------------------------------------------+
| dcat:Dataset      | adms:identifier        | extra:alternate_identifier                |                                | text      |                                                                                                                                                               |
+-------------------+------------------------+-------------------------------------------+--------------------------------+-----------+---------------------------------------------------------------------------------------------------------------------------------------------------------------+
| dcat:Dataset      | dct:issued             | extra:issued                              | metadata_created               | text      |                                                                                                                                                               |
+-------------------+------------------------+-------------------------------------------+--------------------------------+-----------+---------------------------------------------------------------------------------------------------------------------------------------------------------------+
| dcat:Dataset      | dct:modified           | extra:modified                            | metadata_modified              | text      |                                                                                                                                                               |
+-------------------+------------------------+-------------------------------------------+--------------------------------+-----------+---------------------------------------------------------------------------------------------------------------------------------------------------------------+
| dcat:Dataset      | owl:versionInfo        | version                                   | extra:dcat_version             | text      |                                                                                                                                                               |
+-------------------+------------------------+-------------------------------------------+--------------------------------+-----------+---------------------------------------------------------------------------------------------------------------------------------------------------------------+
| dcat:Dataset      | adms:versionNotes      | extra:version_notes                       |                                | text      |                                                                                                                                                               |
+-------------------+------------------------+-------------------------------------------+--------------------------------+-----------+---------------------------------------------------------------------------------------------------------------------------------------------------------------+
| dcat:Dataset      | dct:language           | extra:language                            |                                | list      | See note about lists                                                                                                                                          |
+-------------------+------------------------+-------------------------------------------+--------------------------------+-----------+---------------------------------------------------------------------------------------------------------------------------------------------------------------+
| dcat:Dataset      | dcat:landingPage       | url                                       |                                | text      |                                                                                                                                                               |
+-------------------+------------------------+-------------------------------------------+--------------------------------+-----------+---------------------------------------------------------------------------------------------------------------------------------------------------------------+
| dcat:Dataset      | dct:accrualPeriodicity | extra:frequency                           |                                | text      |                                                                                                                                                               |
+-------------------+------------------------+-------------------------------------------+--------------------------------+-----------+---------------------------------------------------------------------------------------------------------------------------------------------------------------+
| dcat:Dataset      | dct:conformsTo         | extra:conforms_to                         |                                | list      | See note about lists                                                                                                                                          |
+-------------------+------------------------+-------------------------------------------+--------------------------------+-----------+---------------------------------------------------------------------------------------------------------------------------------------------------------------+
| dcat:Dataset      | dct:accessRights       | extra:access_rights                       |                                | text      |                                                                                                                                                               |
+-------------------+------------------------+-------------------------------------------+--------------------------------+-----------+---------------------------------------------------------------------------------------------------------------------------------------------------------------+
| dcat:Dataset      | foaf:page              | extra:documentation                       |                                | list      | See note about lists                                                                                                                                          |
+-------------------+------------------------+-------------------------------------------+--------------------------------+-----------+---------------------------------------------------------------------------------------------------------------------------------------------------------------+
| dcat:Dataset      | dct:provenance         | extra:provenance                          |                                | text      |                                                                                                                                                               |
+-------------------+------------------------+-------------------------------------------+--------------------------------+-----------+---------------------------------------------------------------------------------------------------------------------------------------------------------------+
| dcat:Dataset      | dct:type               | extra:dcat_type                           |                                | text      | As of DCAT-AP v1.1 there's no controlled vocabulary for this field                                                                                            |
+-------------------+------------------------+-------------------------------------------+--------------------------------+-----------+---------------------------------------------------------------------------------------------------------------------------------------------------------------+
| dcat:Dataset      | dct:hasVersion         | extra:has_version                         |                                | list      | See note about lists. It is assumed that these are one or more URIs referring to another dcat:Dataset                                                         |
+-------------------+------------------------+-------------------------------------------+--------------------------------+-----------+---------------------------------------------------------------------------------------------------------------------------------------------------------------+
| dcat:Dataset      | dct:isVersionOf        | extra:is_version_of                       |                                | list      | See note about lists. It is assumed that these are one or more URIs referring to another dcat:Dataset                                                         |
+-------------------+------------------------+-------------------------------------------+--------------------------------+-----------+---------------------------------------------------------------------------------------------------------------------------------------------------------------+
| dcat:Dataset      | dct:source             | extra:source                              |                                | list      | See note about lists. It is assumed that these are one or more URIs referring to another dcat:Dataset                                                         |
+-------------------+------------------------+-------------------------------------------+--------------------------------+-----------+---------------------------------------------------------------------------------------------------------------------------------------------------------------+
| dcat:Dataset      | adms:sample            | extra:sample                              |                                | list      | See note about lists. It is assumed that these are one or more URIs referring to dcat:Distribution instances                                                  |
+-------------------+------------------------+-------------------------------------------+--------------------------------+-----------+---------------------------------------------------------------------------------------------------------------------------------------------------------------+
| dcat:Dataset      | dct:spatial            | extra:spatial_uri                         |                                | text      | If the RDF provides them, profiles should store the textual and geometric representation of the location in extra:spatial_text and extra:spatial respectively |
+-------------------+------------------------+-------------------------------------------+--------------------------------+-----------+---------------------------------------------------------------------------------------------------------------------------------------------------------------+
| dcat:Dataset      | dct:temporal           | extra:temporal_start + extra:temporal_end |                                | text      | None, one or both extras can be present                                                                                                                       |
+-------------------+------------------------+-------------------------------------------+--------------------------------+-----------+---------------------------------------------------------------------------------------------------------------------------------------------------------------+
| dcat:Dataset      | dct:publisher          | extra:publisher_uri                       |                                | text      | See note about URIs                                                                                                                                           |
+-------------------+------------------------+-------------------------------------------+--------------------------------+-----------+---------------------------------------------------------------------------------------------------------------------------------------------------------------+
| foaf:Agent        | foaf:name              | extra:publisher_name                      |                                | text      |                                                                                                                                                               |
+-------------------+------------------------+-------------------------------------------+--------------------------------+-----------+---------------------------------------------------------------------------------------------------------------------------------------------------------------+
| foaf:Agent        | foaf:mbox              | extra:publisher_email                     | organization:title             | text      |                                                                                                                                                               |
+-------------------+------------------------+-------------------------------------------+--------------------------------+-----------+---------------------------------------------------------------------------------------------------------------------------------------------------------------+
| foaf:Agent        | foaf:homepage          | extra:publisher_url                       |                                | text      |                                                                                                                                                               |
+-------------------+------------------------+-------------------------------------------+--------------------------------+-----------+---------------------------------------------------------------------------------------------------------------------------------------------------------------+
| foaf:Agent        | dct:type               | extra:publisher_type                      |                                | text      |                                                                                                                                                               |
+-------------------+------------------------+-------------------------------------------+--------------------------------+-----------+---------------------------------------------------------------------------------------------------------------------------------------------------------------+
| dcat:Dataset      | dcat:contactPoint      | extra:contact_uri                         |                                | text      | See note about URIs                                                                                                                                           |
+-------------------+------------------------+-------------------------------------------+--------------------------------+-----------+---------------------------------------------------------------------------------------------------------------------------------------------------------------+
| vcard:Kind        | vcard:fn               | extra:contact_name                        | maintainer, author             | text      |                                                                                                                                                               |
+-------------------+------------------------+-------------------------------------------+--------------------------------+-----------+---------------------------------------------------------------------------------------------------------------------------------------------------------------+
| vcard:Kind        | vcard:hasEmail         | extra:contact_email                       | maintainer_email, author_email | text      |                                                                                                                                                               |
+-------------------+------------------------+-------------------------------------------+--------------------------------+-----------+---------------------------------------------------------------------------------------------------------------------------------------------------------------+
| dcat:Dataset      | dcat:distribution      | resources                                 |                                | text      |                                                                                                                                                               |
+-------------------+------------------------+-------------------------------------------+--------------------------------+-----------+---------------------------------------------------------------------------------------------------------------------------------------------------------------+
| dcat:Distribution |                        | resource:uri                              |                                | text      | See note about URIs                                                                                                                                           |
+-------------------+------------------------+-------------------------------------------+--------------------------------+-----------+---------------------------------------------------------------------------------------------------------------------------------------------------------------+
| dcat:Distribution | dct:title              | resource:name                             |                                | text      |                                                                                                                                                               |
+-------------------+------------------------+-------------------------------------------+--------------------------------+-----------+---------------------------------------------------------------------------------------------------------------------------------------------------------------+
| dcat:Distribution | dcat:accessURL         | resource:url                              |                                | text      | If accessURL is not present, downloadURL will be used as resource url                                                                                         |
+-------------------+------------------------+-------------------------------------------+--------------------------------+-----------+---------------------------------------------------------------------------------------------------------------------------------------------------------------+
| dcat:Distribution | dcat:downloadURL       | resource:download_url                     |                                | text      |                                                                                                                                                               |
+-------------------+------------------------+-------------------------------------------+--------------------------------+-----------+---------------------------------------------------------------------------------------------------------------------------------------------------------------+
| dcat:Distribution | dct:description        | resource:description                      |                                | text      |                                                                                                                                                               |
+-------------------+------------------------+-------------------------------------------+--------------------------------+-----------+---------------------------------------------------------------------------------------------------------------------------------------------------------------+
| dcat:Distribution | dcat:mediaType         | resource:mimetype                         |                                | text      |                                                                                                                                                               |
+-------------------+------------------------+-------------------------------------------+--------------------------------+-----------+---------------------------------------------------------------------------------------------------------------------------------------------------------------+
| dcat:Distribution | dct:format             | resource:format                           |                                | text      | This is likely to require extra logic to accommodate how CKAN deals with formats (eg ckan/ckanext-dcat#18)                                                    |
+-------------------+------------------------+-------------------------------------------+--------------------------------+-----------+---------------------------------------------------------------------------------------------------------------------------------------------------------------+
| dcat:Distribution | dct:license            | resource:license                          |                                | text      | See note about dataset license                                                                                                                                |
+-------------------+------------------------+-------------------------------------------+--------------------------------+-----------+---------------------------------------------------------------------------------------------------------------------------------------------------------------+
| dcat:Distribution | adms:status            | resource:status                           |                                | text      |                                                                                                                                                               |
+-------------------+------------------------+-------------------------------------------+--------------------------------+-----------+---------------------------------------------------------------------------------------------------------------------------------------------------------------+
| dcat:Distribution | dcat:byteSize          | resource:size                             |                                | number    |                                                                                                                                                               |
+-------------------+------------------------+-------------------------------------------+--------------------------------+-----------+---------------------------------------------------------------------------------------------------------------------------------------------------------------+
| dcat:Distribution | dct:issued             | resource:issued                           |                                | text      |                                                                                                                                                               |
+-------------------+------------------------+-------------------------------------------+--------------------------------+-----------+---------------------------------------------------------------------------------------------------------------------------------------------------------------+
| dcat:Distribution | dct:modified           | resource:modified                         |                                | text      |                                                                                                                                                               |
+-------------------+------------------------+-------------------------------------------+--------------------------------+-----------+---------------------------------------------------------------------------------------------------------------------------------------------------------------+
| dcat:Distribution | dct:rights             | resource:rights                           |                                | text      |                                                                                                                                                               |
+-------------------+------------------------+-------------------------------------------+--------------------------------+-----------+---------------------------------------------------------------------------------------------------------------------------------------------------------------+
| dcat:Distribution | foaf:page              | resource:documentation                    |                                | list      | See note about lists                                                                                                                                          |
+-------------------+------------------------+-------------------------------------------+--------------------------------+-----------+---------------------------------------------------------------------------------------------------------------------------------------------------------------+
| dcat:Distribution | dct:language           | resource:language                         |                                | list      | See note about lists                                                                                                                                          |
+-------------------+------------------------+-------------------------------------------+--------------------------------+-----------+---------------------------------------------------------------------------------------------------------------------------------------------------------------+
| dcat:Distribution | dct:conformsTo         | resource:conforms_to                      |                                | list      | See note about lists                                                                                                                                          |
+-------------------+------------------------+-------------------------------------------+--------------------------------+-----------+---------------------------------------------------------------------------------------------------------------------------------------------------------------+
| spdx:Checksum     | spdx:checksumValue     | resource:hash                             |                                | text      |                                                                                                                                                               |
+-------------------+------------------------+-------------------------------------------+--------------------------------+-----------+---------------------------------------------------------------------------------------------------------------------------------------------------------------+
| spdx:Checksum     | spdx:algorithm         | resource:hash_algorithm                   |                                | text      |                                                                                                                                                               |
+-------------------+------------------------+-------------------------------------------+--------------------------------+-----------+---------------------------------------------------------------------------------------------------------------------------------------------------------------+

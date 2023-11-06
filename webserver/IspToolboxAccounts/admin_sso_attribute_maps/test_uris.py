# (c) Meta Platforms, Inc. and affiliates. Copyright
__author__ = 'rolandh'

EDUPERSON_OID = "urn:oid:1.3.6.1.4.1.5923.1.1.1."
X500ATTR_OID = "urn:oid:2.5.4."
NOREDUPERSON_OID = "urn:oid:1.3.6.1.4.1.2428.90.1."
NETSCAPE_LDAP = "urn:oid:2.16.840.1.113730.3.1."
UCL_DIR_PILOT = 'urn:oid:0.9.2342.19200300.100.1.'
PKCS_9 = "urn:oid:1.2.840.113549.1.9.1."
UMICH = "urn:oid:1.3.6.1.4.1.250.1.57."
SCHAC = "urn:oid:1.3.6.1.4.1.25178.1.2."

MAP = {
    "identifier": "urn:oasis:names:tc:SAML:2.0:attrname-format:unspecified",
    "fro": {
        EDUPERSON_OID+'2': 'eduPersonNickname',
        EDUPERSON_OID+'9': 'eduPersonScopedAffiliation',
        EDUPERSON_OID+'11': 'eduPersonAssurance',
        EDUPERSON_OID+'10': 'eduPersonTargetedID',
        EDUPERSON_OID+'4': 'eduPersonOrgUnitDN',
        NOREDUPERSON_OID+'6': 'norEduOrgAcronym',
        NOREDUPERSON_OID+'7': 'norEduOrgUniqueIdentifier',
        NOREDUPERSON_OID+'4': 'norEduPersonLIN',
        EDUPERSON_OID+'1': 'eduPersonAffiliation',
        NOREDUPERSON_OID+'2': 'norEduOrgUnitUniqueNumber',
        NETSCAPE_LDAP+'40': 'userSMIMECertificate',
        NOREDUPERSON_OID+'1': 'norEduOrgUniqueNumber',
        NETSCAPE_LDAP+'241': 'displayName',
        UCL_DIR_PILOT+'37': 'associatedDomain',
        EDUPERSON_OID+'6': 'eduPersonPrincipalName',
        NOREDUPERSON_OID+'8': 'norEduOrgUnitUniqueIdentifier',
        NOREDUPERSON_OID+'9': 'federationFeideSchemaVersion',
        X500ATTR_OID+'53': 'deltaRevocationList',
        X500ATTR_OID+'52': 'supportedAlgorithms',
        X500ATTR_OID+'51': 'houseIdentifier',
        X500ATTR_OID+'50': 'uniqueMember',
        X500ATTR_OID+'19': 'physicalDeliveryOfficeName',
        X500ATTR_OID+'18': 'postOfficeBox',
        X500ATTR_OID+'17': 'postalCode',
        X500ATTR_OID+'16': 'postalAddress',
        X500ATTR_OID+'15': 'businessCategory',
        X500ATTR_OID+'14': 'searchGuide',
        EDUPERSON_OID+'5': 'eduPersonPrimaryAffiliation',
        X500ATTR_OID+'12': 'title',
        X500ATTR_OID+'11': 'ou',
        X500ATTR_OID+'10': 'o',
        X500ATTR_OID+'37': 'cACertificate',
        X500ATTR_OID+'36': 'userCertificate',
        X500ATTR_OID+'31': 'member',
        X500ATTR_OID+'30': 'supportedApplicationContext',
        X500ATTR_OID+'33': 'roleOccupant',
        X500ATTR_OID+'32': 'owner',
        NETSCAPE_LDAP+'1': 'carLicense',
        PKCS_9+'1': 'email',
        NETSCAPE_LDAP+'3': 'employeeNumber',
        NETSCAPE_LDAP+'2': 'departmentNumber',
        X500ATTR_OID+'39': 'certificateRevocationList',
        X500ATTR_OID+'38': 'authorityRevocationList',
        NETSCAPE_LDAP+'216': 'userPKCS12',
        EDUPERSON_OID+'8': 'eduPersonPrimaryOrgUnitDN',
        X500ATTR_OID+'9': 'street',
        X500ATTR_OID+'8': 'st',
        NETSCAPE_LDAP+'39': 'preferredLanguage',
        EDUPERSON_OID+'7': 'eduPersonEntitlement',
        X500ATTR_OID+'2': 'knowledgeInformation',
        X500ATTR_OID+'7': 'l',
        X500ATTR_OID+'6': 'c',
        X500ATTR_OID+'5': 'serialNumber',
        X500ATTR_OID+'4': 'sn',
        X500ATTR_OID+'3': 'cn',
        UCL_DIR_PILOT+'60': 'jpegPhoto',
        X500ATTR_OID+'65': 'pseudonym',
        NOREDUPERSON_OID+'5': 'norEduPersonNIN',
        UCL_DIR_PILOT+'3': 'mail',
        UCL_DIR_PILOT+'25': 'dc',
        X500ATTR_OID+'40': 'crossCertificatePair',
        X500ATTR_OID+'42': 'givenName',
        X500ATTR_OID+'43': 'initials',
        X500ATTR_OID+'44': 'generationQualifier',
        X500ATTR_OID+'45': 'x500UniqueIdentifier',
        X500ATTR_OID+'46': 'dnQualifier',
        X500ATTR_OID+'47': 'enhancedSearchGuide',
        X500ATTR_OID+'48': 'protocolInformation',
        X500ATTR_OID+'54': 'dmdName',
        NETSCAPE_LDAP+'4': 'employeeType',
        X500ATTR_OID+'22': 'teletexTerminalIdentifier',
        X500ATTR_OID+'23': 'facsimileTelephoneNumber',
        X500ATTR_OID+'20': 'telephoneNumber',
        X500ATTR_OID+'21': 'telexNumber',
        X500ATTR_OID+'26': 'registeredAddress',
        X500ATTR_OID+'27': 'destinationIndicator',
        X500ATTR_OID+'24': 'x121Address',
        X500ATTR_OID+'25': 'internationaliSDNNumber',
        X500ATTR_OID+'28': 'preferredDeliveryMethod',
        X500ATTR_OID+'29': 'presentationAddress',
        EDUPERSON_OID+'3': 'eduPersonOrgDN',
        NOREDUPERSON_OID+'3': 'norEduPersonBirthDate',
        UMICH+'57': 'labeledURI',
        UCL_DIR_PILOT+'1': 'uid',
        SCHAC+'1': 'schacMotherTongue',
        SCHAC+'2': 'schacGender',
        SCHAC+'3': 'schacDateOfBirth',
        SCHAC+'4': 'schacPlaceOfBirth',
        SCHAC+'5': 'schacCountryOfCitizenship',
        SCHAC+'6': 'schacSn1',
        SCHAC+'7': 'schacSn2',
        SCHAC+'8': 'schacPersonalTitle',
        SCHAC+'9': 'schacHomeOrganization',
        SCHAC+'10': 'schacHomeOrganizationType',
        SCHAC+'11': 'schacCountryOfResidence',
        SCHAC+'12': 'schacUserPresenceID',
        SCHAC+'13': 'schacPersonalPosition',
        SCHAC+'14': 'schacPersonalUniqueCode',
        SCHAC+'15': 'schacPersonalUniqueID',
        SCHAC+'17': 'schacExpiryDate',
        SCHAC+'18': 'schacUserPrivateAttribute',
        SCHAC+'19': 'schacUserStatus',
        SCHAC+'20': 'schacProjectMembership',
        SCHAC+'21': 'schacProjectSpecificRole',
    },
    "to": {
        'roleOccupant': X500ATTR_OID+'33',
        'gn': X500ATTR_OID+'42',
        'norEduPersonNIN': NOREDUPERSON_OID+'5',
        'title': X500ATTR_OID+'12',
        'facsimileTelephoneNumber': X500ATTR_OID+'23',
        'mail': UCL_DIR_PILOT+'3',
        'postOfficeBox': X500ATTR_OID+'18',
        'fax': X500ATTR_OID+'23',
        'telephoneNumber': X500ATTR_OID+'20',
        'norEduPersonBirthDate': NOREDUPERSON_OID+'3',
        'rfc822Mailbox': UCL_DIR_PILOT+'3',
        'dc': UCL_DIR_PILOT+'25',
        'countryName': X500ATTR_OID+'6',
        'emailAddress': PKCS_9+'1',
        'employeeNumber': NETSCAPE_LDAP+'3',
        'organizationName': X500ATTR_OID+'10',
        'eduPersonAssurance': EDUPERSON_OID+'11',
        'norEduOrgAcronym': NOREDUPERSON_OID+'6',
        'registeredAddress': X500ATTR_OID+'26',
        'physicalDeliveryOfficeName': X500ATTR_OID+'19',
        'associatedDomain': UCL_DIR_PILOT+'37',
        'l': X500ATTR_OID+'7',
        'stateOrProvinceName': X500ATTR_OID+'8',
        'federationFeideSchemaVersion': NOREDUPERSON_OID+'9',
        'pkcs9email': PKCS_9+'1',
        'givenName': X500ATTR_OID+'42',
        'givenname': X500ATTR_OID+'42',
        'x500UniqueIdentifier': X500ATTR_OID+'45',
        'eduPersonNickname': EDUPERSON_OID+'2',
        'houseIdentifier': X500ATTR_OID+'51',
        'street': X500ATTR_OID+'9',
        'supportedAlgorithms': X500ATTR_OID+'52',
        'preferredLanguage': NETSCAPE_LDAP+'39',
        'postalAddress': X500ATTR_OID+'16',
        'email': PKCS_9+'1',
        'norEduOrgUnitUniqueIdentifier': NOREDUPERSON_OID+'8',
        'eduPersonPrimaryOrgUnitDN': EDUPERSON_OID+'8',
        'c': X500ATTR_OID+'6',
        'teletexTerminalIdentifier': X500ATTR_OID+'22',
        'o': X500ATTR_OID+'10',
        'cACertificate': X500ATTR_OID+'37',
        'telexNumber': X500ATTR_OID+'21',
        'ou': X500ATTR_OID+'11',
        'initials': X500ATTR_OID+'43',
        'eduPersonOrgUnitDN': EDUPERSON_OID+'4',
        'deltaRevocationList': X500ATTR_OID+'53',
        'norEduPersonLIN': NOREDUPERSON_OID+'4',
        'supportedApplicationContext': X500ATTR_OID+'30',
        'eduPersonEntitlement': EDUPERSON_OID+'7',
        'generationQualifier': X500ATTR_OID+'44',
        'eduPersonAffiliation': EDUPERSON_OID+'1',
        'edupersonaffiliation': EDUPERSON_OID+'1',
        'eduPersonPrincipalName': EDUPERSON_OID+'6',
        'edupersonprincipalname': EDUPERSON_OID+'6',
        'localityName': X500ATTR_OID+'7',
        'owner': X500ATTR_OID+'32',
        'norEduOrgUnitUniqueNumber': NOREDUPERSON_OID+'2',
        'searchGuide': X500ATTR_OID+'14',
        'certificateRevocationList': X500ATTR_OID+'39',
        'organizationalUnitName': X500ATTR_OID+'11',
        'userCertificate': X500ATTR_OID+'36',
        'preferredDeliveryMethod': X500ATTR_OID+'28',
        'internationaliSDNNumber': X500ATTR_OID+'25',
        'uniqueMember': X500ATTR_OID+'50',
        'departmentNumber': NETSCAPE_LDAP+'2',
        'enhancedSearchGuide': X500ATTR_OID+'47',
        'userPKCS12': NETSCAPE_LDAP+'216',
        'eduPersonTargetedID': EDUPERSON_OID+'10',
        'norEduOrgUniqueNumber': NOREDUPERSON_OID+'1',
        'x121Address': X500ATTR_OID+'24',
        'destinationIndicator': X500ATTR_OID+'27',
        'eduPersonPrimaryAffiliation': EDUPERSON_OID+'5',
        'surname': X500ATTR_OID+'4',
        'jpegPhoto': UCL_DIR_PILOT+'60',
        'eduPersonScopedAffiliation': EDUPERSON_OID+'9',
        'edupersonscopedaffiliation': EDUPERSON_OID+'9',
        'protocolInformation': X500ATTR_OID+'48',
        'knowledgeInformation': X500ATTR_OID+'2',
        'employeeType': NETSCAPE_LDAP+'4',
        'userSMIMECertificate': NETSCAPE_LDAP+'40',
        'member': X500ATTR_OID+'31',
        'streetAddress': X500ATTR_OID+'9',
        'dmdName': X500ATTR_OID+'54',
        'postalCode': X500ATTR_OID+'17',
        'pseudonym': X500ATTR_OID+'65',
        'dnQualifier': X500ATTR_OID+'46',
        'crossCertificatePair': X500ATTR_OID+'40',
        'eduPersonOrgDN': EDUPERSON_OID+'3',
        'authorityRevocationList': X500ATTR_OID+'38',
        'displayName': NETSCAPE_LDAP+'241',
        'businessCategory': X500ATTR_OID+'15',
        'serialNumber': X500ATTR_OID+'5',
        'norEduOrgUniqueIdentifier': NOREDUPERSON_OID+'7',
        'st': X500ATTR_OID+'8',
        'carLicense': NETSCAPE_LDAP+'1',
        'presentationAddress': X500ATTR_OID+'29',
        'sn': X500ATTR_OID+'4',
        'cn': X500ATTR_OID+'3',
        'domainComponent': UCL_DIR_PILOT+'25',
        'labeledURI': UMICH+'57',
        'uid': UCL_DIR_PILOT+'1',
        'schacMotherTongue': SCHAC+'1',
        'schacGender': SCHAC+'2',
        'schacDateOfBirth': SCHAC+'3',
        'schacPlaceOfBirth': SCHAC+'4',
        'schacCountryOfCitizenship': SCHAC+'5',
        'schacSn1': SCHAC+'6',
        'schacSn2': SCHAC+'7',
        'schacPersonalTitle': SCHAC+'8',
        'schacHomeOrganization': SCHAC+'9',
        'schacHomeOrganizationType': SCHAC+'10',
        'schacCountryOfResidence': SCHAC+'11',
        'schacUserPresenceID': SCHAC+'12',
        'schacPersonalPosition': SCHAC+'13',
        'schacPersonalUniqueCode': SCHAC+'14',
        'schacPersonalUniqueID': SCHAC+'15',
        'schacExpiryDate': SCHAC+'17',
        'schacUserPrivateAttribute': SCHAC+'18',
        'schacUserStatus': SCHAC+'19',
        'schacProjectMembership': SCHAC+'20',
        'schacProjectSpecificRole': SCHAC+'21',
    }
}

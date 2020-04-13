# Use this for Azure AD authentication
from msrestazure.azure_active_directory import AADTokenCredentials

# Required for Data Lake Storage Gen1 account management
from azure.mgmt.datalake.store import DataLakeStoreAccountManagementClient
from azure.mgmt.datalake.store.models import DataLakeStoreAccount

# Required for Data Lake Storage Gen1 filesystem management
from azure.datalake.store import core, lib, multithread

# Common Azure imports
import adal
from azure.mgmt.resource.resources import ResourceManagementClient
from azure.mgmt.resource.resources.models import ResourceGroup

# Use these as needed for your application
import logging, getpass, pprint, uuid, time

import os

authority_host_uri = 'https://login.microsoftonline.com'
tenant = os.environ.get('TENANT_ID')
authority_uri = authority_host_uri + '/' + tenant
resource = 'https://datalake.azure.net/'
client_id = os.environ.get('CLIENT_ID')
client_secret = os.environ.get('CLIENT_SECRET')

# Authentication
adlCreds = lib.auth(tenant_id = tenant,
                client_secret = client_secret,
                client_id = client_id,
                resource = resource)

# Create Filesystem client
## Declare variables
subscriptionId = os.environ.get('SUBSCRIPTION_ID')
adlsAccountName = os.environ.get('ADL_ACCOUNT_NAME')

## Create a filesystem client object
adlsFileSystemClient = core.AzureDLFileSystem(adlCreds, store_name=adlsAccountName)

# Listar ficheros
lista = adlsFileSystemClient.listdir(path="/", detail=False, invalidate_cache=True)
print(lista)



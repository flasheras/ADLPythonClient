import os

# Use this for Azure AD authentication
from msrestazure.azure_active_directory import AADTokenCredentials

# Required for Azure Data Lake Storage Gen1 account management
from azure.mgmt.datalake.store import DataLakeStoreAccountManagementClient
from azure.mgmt.datalake.store.models import DataLakeStoreAccount

# Required for Azure Data Lake Storage Gen1 filesystem management
from azure.datalake.store import core, lib, multithread

# Common Azure imports
import adal
from azure.mgmt.resource.resources import ResourceManagementClient
from azure.mgmt.resource.resources.models import ResourceGroup

# Use these as needed for your application
import logging, pprint, uuid, time


def auth():
    #authority_host_url = "https://login.microsoftonline.com"
    tenant = os.environ.get('TENANT_ID')
    
    adlCreds = lib.auth(tenant_id=tenant, resource = 'https://datalake.azure.net/')
    #adlCreds = lib.auth()
    return adlCreds

def seeTestFile(adlCreds):
    
    adlsAccountName = os.environ.get('ADL_ACCOUNT_NAME')
    
    ## Create a filesystem client object
    adlsFileSystemClient = core.AzureDLFileSystem(adlCreds,
                                store_name=adlsAccountName)

    
    # Listar ficheros
    lista = adlsFileSystemClient.listdir(path="/raw/jupyter/allowed", detail=False, invalidate_cache=True)
    print(lista)
    print("fin listado ficheros")


if __name__ == "__main__":
    adlCreds = auth()
    seeTestFile(adlCreds)
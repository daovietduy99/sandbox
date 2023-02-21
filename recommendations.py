import csv
from azure.mgmt.advisor import AdvisorManagementClient
from azure.mgmt.subscription import SubscriptionClient
from azure.identity import ClientSecretCredential
from azure.mgmt.storage import StorageManagementClient
from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient

# Azure credentials
client_id = os.environ['CLIENT_ID']
client_secret = os.environ['CLIENT_SECRET']
tenant_id = os.environ['TENANT_ID']

# Set Azure Storage account and container name
storage_account_name = os.environ['SA_NAME']
container_name = os.environ['CONTAINER']
resource_group_name = os.environ['RG_NAME']

# Authenticate to Azure
credentials = ClientSecretCredential(
    client_id=client_id,
    client_secret=client_secret,
    tenant_id=tenant_id
)

def get_recommendations_to_csv(subscription):
    subscription_id = subscription.subscription_id
    subscription_name = subscription.display_name
    # Initialize Storage Management client
    storage_client = StorageManagementClient(credentials, subscription_id)

    # Initialize the Advisor client
    advisor_client = AdvisorManagementClient(credentials, subscription_id)

    # Get storage account key
    keys = storage_client.storage_accounts.list_keys(resource_group_name, storage_account_name)
    storage_account_key = keys.keys[0].value

    # Initialize Blob Service client
    blob_service_client = BlobServiceClient(account_url=f"https://" + storage_account_name + ".blob.core.windows.net/", credential=storage_account_key)

    # Get all recommendations
    recommendations = advisor_client.recommendations.list()

    # Write recommendations to a CSV file
    with open(subscription_name + '.csv', mode='w', newline='') as csv_file:
        fieldnames = ['name', 'category', 'impact', 'short_description']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()

        for recommendation in recommendations:
            writer.writerow({'name': recommendation.name,
                            'category': recommendation.category,
                            'impact': recommendation.impact,
                            'short_description': recommendation.short_description})

    # Upload CSV to blob storage
    with open(subscription_name + '.csv', 'rb') as data:
        blob_client = blob_service_client.get_blob_client(container=container_name, blob=subscription_name + '.csv')
        blob_client.upload_blob(data)

sub_list = SubscriptionClient(credentials).subscriptions.list()
for s in sub_list:
    print(s.subscription_id)
    get_recommendations_to_csv(s)

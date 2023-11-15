import requests
from dnac_login import get_token
from prettytable import PrettyTable

table = PrettyTable()

status_code, token = get_token()

# print(token)

def get_client_details(token, entity_type, entity_value):
    headers = {
        'Content-Type': 'application/json',
        'x-auth-token': token,
        'entity-type': entity_type,
        'entity-value': entity_value
    }
    url = 'https://sandboxdnac2.cisco.com/dna/intent/api/v1/client-enrichment-details'

    response = requests.get(url=url,headers=headers,verify=False)
    return response.status_code, response.json()

if __name__ == '__main__':
    status_code, clients = get_client_details(token=token)
    # table.field_names = ['Site ID', 'Client Count']
    # for site in clients['response']:
    #     for score in site['scoreDetail']:
    #         table.add_row([site['siteId'], score['clientCount']])
    # print(table)
    

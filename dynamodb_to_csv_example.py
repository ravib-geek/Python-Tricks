
from __future__ import print_function # Python 2/3 compatibility
import sys
import csv
import boto3
import json
import decimal
from boto3.dynamodb.conditions import Key, Attr

endpoint = 'tablename'
filename = 'outputfile.csv'
region = 'AWS Region'

# Helper class to convert a DynamoDB item to JSON.
class DecimalEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, decimal.Decimal):
            if o % 1 > 0:
                return float(o)
            else:
                return int(o)
        return super(DecimalEncoder, self).default(o)

def get_data():
    session = boto3.Session()
    dynamodb = session.resource('dynamodb', region_name=region)

    table = dynamodb.Table(endpoint)

    # Timestamp in epoch format
    fe = Key('end_ts').between(1546300800, 1553990400)

    response = table.scan(FilterExpression=fe)

    renewals_data = response['Items']
    return renewals_data

def main():
    #write data to csv
    outputfile = open(filename, 'w')
    csvwriter = csv.writer(outputfile)

    count = 0
    renewals_data = get_data()
    for renew in renewals_data:
        if count == 0:
            header = renew.keys()
            csvwriter.writerow(header)
            count += 1

        csvwriter.writerow(renew.values())
    outputfile.close()


if __name__=='__main__':
    main()

import boto3 ;

#get the service Resource.
dynamodb = boto3.resource('dynamodb')

# Create the Dynamodb table
table= dynamodb.create_table(
    TableName='aml_lookup',
    KeySchema=[
        {
            'AttributeName' : 'aml_unique_id',
            'KeyType' : 'HASH'
        },
        {
            'AttributeName' : 'aml_hash_key',
            'KeyType' : 'RANGE'

        }
    ], AttributeDefinitions=[
        {
            'AttributeName': 'aml_unique_id',
            'AttributeType': 'S'
        },
         {
            'AttributeName': 'aml_hash_key',
            'AttributeType': 'S'
        }
    ],
    ProvisionedThroughput={
        'ReadCapacityUnits': 5,
        'WriteCapacityUnits': 5
    }
)

#Print out some data about table

print(table.item_count)
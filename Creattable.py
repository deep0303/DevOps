import boto3

# Initialize a session using your preferred AWS region
dynamodb = boto3.resource('dynamodb', region_name='us-east-1')  # Replace 'us-east-1' with your AWS region

# Create the DynamoDB table
table = dynamodb.create_table(
    TableName='MoviesTable',  # Name of the table
    KeySchema=[
        {
            'AttributeName': 'MovieID',  # Partition key
            'KeyType': 'HASH'  # 'HASH' denotes the partition key
        },
        {
            'AttributeName': 'Title',  # Sort key
            'KeyType': 'RANGE'  # 'RANGE' denotes the sort key
        }
    ],
    AttributeDefinitions=[
        {
            'AttributeName': 'MovieID',  # Define the data type for the partition key
            'AttributeType': 'N'  # 'N' means Number
        },
        {
            'AttributeName': 'Title',  # Define the data type for the sort key
            'AttributeType': 'S'  # 'S' means String
        }
    ],
    ProvisionedThroughput={
        'ReadCapacityUnits': 5,
        'WriteCapacityUnits': 5
    }
)

# Wait until the table is created
table.meta.client.get_waiter('table_exists').wait(TableName='Movies')

print(f"Table '{table.table_name}' created successfully!")

import boto3

# Initialize a session using your preferred AWS region
dynamodb = boto3.client('dynamodb', region_name='us-east-1')

# Prepare the batch write request
batch_items = {
    'MediaTable': [  # Replace 'MediaTable' with your table name
        {
            'PutRequest': {
                'Item': {
                    'PK': {'S': 'MOVIE#4'},
                    'SK': {'S': 'TITLE#The Prestige'},
                    'Type': {'S': 'Movie'},
                    'Genre': {'S': 'Drama'},
                    'Director': {'S': 'Christopher Nolan'},
                    'Year': {'N': '2006'}
                }
            }
        },
        # Add more items as needed...
    ]
}

# Function to perform batch write
def batch_write_items():
    while True:
        response = dynamodb.batch_write_item(RequestItems=batch_items)
        # Check if there are any unprocessed items
        if response['UnprocessedItems']:
            print("Retrying unprocessed items...")
            batch_items = response['UnprocessedItems']
        else:
            break

    print("Batch write completed successfully!")

# Call the function
batch_write_items()

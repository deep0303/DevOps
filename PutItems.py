import boto3

# Initialize a session using your preferred AWS region
dynamodb = boto3.resource('dynamodb', region_name='us-east-1')  # Replace 'us-east-1' with your AWS region

# Reference the DynamoDB table
table = dynamodb.Table('Movies')  # Replace 'Movies' with your table name

# Insert items into the DynamoDB table
try:
    # Item 1
    response = table.put_item(
        Item={
            'MovieID': 1,  # Partition key
            'Title': 'Inception',  # Sort key
            'Genre': 'Sci-Fi',
            'Director': 'Christopher Nolan',
            'Year': 2010
        }
    )
    print("PutItem succeeded for Inception:", response)

    # Item 2
    response = table.put_item(
        Item={
            'MovieID': 2,  # Partition key
            'Title': 'The Matrix',  # Sort key
            'Genre': 'Action',
            'Director': 'Lana Wachowski, Lilly Wachowski',
            'Year': 1999
        }
    )
    print("PutItem succeeded for The Matrix:", response)

    # Item 3
    response = table.put_item(
        Item={
            'MovieID': 3,  # Partition key
            'Title': 'Interstellar',  # Sort key
            'Genre': 'Sci-Fi',
            'Director': 'Christopher Nolan',
            'Year': 2014
        }
    )
    print("PutItem succeeded for Interstellar:", response)

except Exception as e:
    print("Error putting items into the Movies table:", e)

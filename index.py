def lambda_handler(event, context):
    # Extract the Authorization token from the incoming event
    authorization_token = event.get('headers', {}).get('Authorization', '')


    # For simplicity, let's assume a basic check for the presence of the token
    if not authorization_token:
        # Modified: Return "Hello, World!" for 403 Forbidden
        return {
            'statusCode': 403,
            'body': 'Hello, World!'
        }


    response_body = 'Hello, World!'

    return {
        'statusCode': 200,
        'headers': {
            'Content-Type': 'application/json',
            'Access-Control-Allow-Origin': '*'  # Adjust CORS as needed
        },
        'body': response_body
    }

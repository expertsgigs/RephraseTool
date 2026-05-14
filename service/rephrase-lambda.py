import json

def lambda_handler(event, context):

    body = json.loads(event['body'])

    username = body['username']
    password = body['password']

    if username == "admin" and password == "1234":

        return {
            'statusCode': 200,
            'body': json.dumps({
                'status': 'success',
                'message': 'Login successful'
            })
        }

    return {
        'statusCode': 401,
        'body': json.dumps({
            'status': 'failed',
            'message': 'Invalid credentials'
        })
    }
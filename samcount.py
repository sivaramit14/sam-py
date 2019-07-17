import os

def my_handler(event, context):
    message = 'Hello {} {}!'.format(event['first_name'], 
                                    event['last_name'])  
    originURL = os.environ['origin']
    print('origin:', originURL)
    totalSAMs = 20
    response = {
        "statusCode": 200,
        "body": totalSAMs,
        "headers":
        {
            "Access-Control-Allow-Headers": "Content-Type,X-Amz-Date,Authorization,X-Api-Key,X-Amz-Security-Token",
            "Access-Control-Allow-Methods": "GET,OPTIONS",
            "Access-Control-Allow-Origin": originURL
        }
    }
    return response  

import json
import psycopg2

# Had to find and change the ARN for the layer for the us-east-1 region:
#  arn:aws:lambda:us-east-1:898466741470:layer:psycopg2-py38:2

def lambda_handler(event, context):
    user = event['request']['userAttributes']
    print('-------userAttributes--------')
    print(user)

    user_display_name = user['name']
    user_email = user['email']
    user_handle = user['preferred_username']
    user_cognito_id = user['sub']
    
    try:
        conn = psycopg2.connect(
            host=(os.getenv('CONNECTION_URL'))
        )
        cur = conn.cursor()
        

        sql = f"""
        INSERT INTO users (display_name, handle, cognito_user_id) 
        VALUES(
            {user_display_name},
            {user_email}, 
            {user_handle}, 
            {user_cognito_id})")
        """
        cur.execute(sql)
        conn.commit() 

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
        
    finally:
        if conn is not None:
            cur.close()
            conn.close()
            print('Database connection closed.')

    return event
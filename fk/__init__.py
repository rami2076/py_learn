import json
import boto3
import psycopg2


def lambda_handler(event, context):
    endpoint = "rds-proxy-xxxxx.proxy-xxxxxx.ap-northeast-1.rds.amazonaws.com"
    port = "5432"
    usr = "test_user"
    region = "ap-northeast-1"

    client = boto3.client('rds')

    # IAM認証を行いトークンを取得
    token = client.generate_db_auth_token(DBHostname=endpoint, Port=port, DBUsername=usr, Region=region)

    # 取得したトークンをパスワードとしてデータベースへ接続
    connection = psycopg2.connect(host=endpoint, database="test_db2", user=usr, password=token, sslmode='require')

    cur = connection.cursor()
    cur.execute('SELECT * FROM employee')
    results = cur.fetchall()

    for r in results:
        print(r)

    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }

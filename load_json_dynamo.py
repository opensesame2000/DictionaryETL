# coding=utf-8
import boto3
import json

dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
dbtable = dynamodb.Table('tester')


def batch_write():
    with open("data.json") as json_file:
        lexemes = json.load(json_file)

        with dbtable.batch_writer() as batch:
            for lexeme in lexemes:
                batch.put_item(Item = lexeme)


def seq_write():
    for lexeme in lexemes:
        word = lexeme['Word']
        d_id = lexeme['dict_id']
        created = lexeme['Created']
        updated = lexeme['Updated']
        meanings = lexeme['Meanings']
        print("Adding lexeme:", word, d_id)
        dbtable.put_item(Item={'Word': word, 'd_id': d_id, 'Created':created, 'Updated':updated, 'Meanings': meanings})



if __name__ == '__main__':
   batch_write()


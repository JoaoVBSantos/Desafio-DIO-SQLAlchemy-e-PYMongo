import pymongo as pyM
import pprint
from MongoClient import mongo_client

client = pyM.MongoClient(mongo_client)
db = client.pymongo
collection = db.pymongo_collection
print(db.pymongo_collection)

post = [{
 'nome': 'joao',
 'cpf': '18456493676',
 'endereco': 'Rua Embaixada, 123',
 'tipo': 'Conta corrente',
 'agencia': '0001',
 'numero': 1,
 'saldo': 546.00
   },
 {
  'nome': 'matheus',
  'cpf': '15406784523',
  'endereco': 'Rua Canada,254',
  'tipo': 'Conta corrente',
  'agencia': '0001',
  'numero': 2,
  'saldo': 468.31
   },
 {
  'nome': 'rodrigo',
  'cpf': '18453795623',
  'endereco': 'Rua Esperança, 41',
  'tipo': 'Conta corrente',
  'agencia': '0001',
  'numero': 3,
  'saldo': 247.12
   },
 {
  'nome': 'lucas',
  'cpf': '94615475692',
  'endereco': 'Rua das Aves, 562',
  'tipo': 'Conta corrente',
  'agencia': '0001',
  'numero': 4,
  'saldo': 10.00
   },
 {
  'nome': 'vinicius',
  'cpf': '17583563412',
  'endereco': 'Rua Castelo Branco, 426',
  'tipo': 'Conta corrente',
  'agencia': '0001',
  'numero': 5,
  'saldo': 2456.30
}]

#posts = db.posts
#post_id = posts.insert_many(post)
#print(post_id)

pprint.pprint(db.posts.find_one())
pprint.pprint(db.posts.find_one({'nome': 'matheus'}))
pprint.pprint(db.posts.find_one({'cpf': '18453795623'}))
pprint.pprint(db.posts.find_one({'endereco': 'Rua das Aves, 562'}))
pprint.pprint(db.posts.find_one({'numero': 5}))


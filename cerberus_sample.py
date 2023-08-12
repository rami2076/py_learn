from cerberus import Validator

# schema = {'name': {'type': 'string'}}
# v: Validator = Validator(schema)

# print(type(v))
#
# document = {'name': 'a'}
#
# r: bool = v.validate(document)
#
# print(type(r))
#
v = Validator()
# r = v.validate(document, schema)
# print(r)
#
# document = {
#     'time': 'time',
#     'picture_info': [
#         {
#             'name': 'ken',
#             'id': 1
#         },
#         {
#             'name': 'kenji',
#             'id': 2
#         }
#     ]
# }
#
# schema = {
#     'time': {'type': 'string'},
#     'picture_info': {
#         'type': 'dict',
#         'schema': {
#             'name': {'type': 'string'},
#             'id': {'type': 'number'}
#
#         }
#     }
# }
#
# r = v.validate(document, schema)
# print(v.errors)
#
# schema = {
#     'results': {
#         'type': 'list',
#         'items': [{'type': 'string'}]
#
#     }
# }
#
# document = {
#     'results': [
#         {"key": "value"},
#         {"key": "value"},
#         {"key": "value"}
#     ]
# }
# r = v.validate(document, schema)
# print(r)
# print(v.errors)

# schema = {
#     'rows': {
#         'type': 'list',
#         'schema': {
#             'sku': {'type': 'string'},
#             'price': {'type': 'integer'}
#         }
#     }
# }
# document = {
#     'rows': [
#         {
#             'sku': 'KT123',
#             'price': 100
#         }
#     ]
# }
# r = v.validate(document, schema)
# print(r)


schema = {
    'rows': {
        'type': 'list',
        'schema': {
            'type': 'dict',
            'schema': {
                'sku': {'type': 'string'},
                'price': {'type': 'integer'}
            }
        }
    }
}
document = {'rows': [{'sku': 'KT123', 'price': 100}]}
r = v.validate(document, schema)
print(r)

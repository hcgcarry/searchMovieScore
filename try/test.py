# -*- coding: utf-8 -*-
import json

carry='法克由'
print(carry)
carry8=carry.encode('UTF-8')
print("carry8:",carry8)

carrydump=json.dumps(carry)
print("carrydump:",carrydump)

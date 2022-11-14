"""
This is an example usage of signing verifiable credential using https://github.com/extremeheat/JSPyBridge library
The original TS testcase can be found there https://github.com/digitalcredentials/sign-and-verify-core/blob/main/test/issuer.spec.ts
"""

from javascript import require

s_v = require("@digitalcredentials/sign-and-verify-core")

print(s_v)

print(dir(s_v))

import json

with open("./unlocked-did:key.json") as file:
    unlockedDID = json.load(file)

controller = 'did:key:z6MkqanD5cmEVf154z5xExoxNKENAzVr3gdPo4wD2R2aCUzj'
keyId = 'did:key:z6MkqanD5cmEVf154z5xExoxNKENAzVr3gdPo4wD2R2aCUzj#z6MkqanD5cmEVf154z5xExoxNKENAzVr3gdPo4wD2R2aCUzj'


create_issuer = s_v.createIssuer([unlockedDID], controller)
print(create_issuer)

dccCredential = {
  '@context': [
    'https://www.w3.org/2018/credentials/v1',
    'https://w3c-ccg.github.io/vc-ed/plugfest-1-2022/jff-vc-edu-plugfest-1-context.json'
  ],
  'type': [
    'VerifiableCredential',
    'OpenBadgeCredential'
  ],
  'issuer': {
    'type': 'Profile',
    'id': controller,
    'name': 'Jobs for the Future (JFF)',
    'url': 'https://www.jff.org/',
    'image': 'https://w3c-ccg.github.io/vc-ed/plugfest-1-2022/images/JFF_LogoLockup.png'
  },
  'issuanceDate': '2022-05-01T00:00:00Z',
  'credentialSubject': {
    'type': 'AchievementSubject',
    'achievement': {
      'type': 'Achievement',
      'name': 'Sample test credential to prep for JFF Plugfest #1 2022',
      'description': 'This wallet can display this Open Badge 3.0',
      'criteria': {
        'type': 'Criteria',
        'narrative': 'The first cohort of the JFF Plugfest 1 in May/June of 2022 collaborated to push interoperability of VCs in education forward.'
      },
      'image': 'https://w3c-ccg.github.io/vc-ed/plugfest-1-2022/images/plugfest-1-badge-image.png'
    }
  }
}
options = {
        'verificationMethod': keyId
      }

result = create_issuer.sign(dccCredential, options)

print(result)


assert result.valueOf().get('issuer', {}).get("id") == controller

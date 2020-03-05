import base64
str='admin'
str=str.encode('utf-8')
#加密
bs64=base64.b64encode(str)
print(bs64)
#结果是  b'YWRtaW4='

bs32=base64.b32encode(str)
print(bs32)
#结果是  b'MFSG22LO'

bs16=base64.b16encode(str)
print(bs16)
#结果是  b'61646D696E'

#解密
debs64=base64.b64decode(bs64)
print(debs64)
#结果是  b'admin'

debs32=base64.b32decode(bs32)
print(debs32)
#结果是  b'admin'

debs16=base64.b16decode(bs16)
print(debs16)
#结果是  b'admin'

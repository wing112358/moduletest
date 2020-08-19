import hashlib
import json


def sign(params,key):
    paramsdict = json.loads(params)
    #列表生成式，将原本参数生成key=value格式
    a = ["".join(i) for i in paramsdict.items()  if i[1] and i[0]!= "sign"]
    print(a)

    #将参数名按照ASCII码从小到大排序
    strA = "".join(sorted(a))
    print(strA)

    #在strA基础上拼接key得到结果
    strsign = strA + key
    print(strsign)

    m = hashlib.md5()
    m.update(strsign.lower().encode('UTF-8'))

    sign = m.hexdigest()

    paramsdict['sign'] = sign
    print(paramsdict)

    paramsstr=json.dumps(paramsdict)
    print(paramsdict)
    return paramsdict




if __name__=='__main__':
    key = "1234567890"
    params={
        "useraname":"uusjsjjs",
        "password":"ahagyd5882"
    }

    jsonparam = json.dumps(params)

    result = sign(params,key)

    print(result)

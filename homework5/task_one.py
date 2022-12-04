number = list(input())
notvalid = {
  "success": False,
  "description": "Причины ошибки"
}
valid = {
  "success": True,
  "phone": None,
  "operator": None
}
if ''.join(number[4:6]) == '25':
    valid['phone'] = ''.join(number)
    valid['operator'] = 'life'
    print(valid)
elif ''.join(number[4:7]) == '291':
    valid['phone'] = ''.join(number)
    valid['operator'] = 'A1'
    print(valid)
elif ''.join(number[4:7]) == '292':
    valid['phone'] = ''.join(number)
    valid['operator'] = 'MTC'
    print(valid)
elif ''.join(number[4:7]) == '293':
    valid['phone'] = ''.join(number)
    valid['operator'] = 'A1'
    print(valid)
elif ''.join(number[4:7]) == '295':
    valid['phone'] = ''.join(number)
    valid['operator'] = 'MTC'
    print(valid)
elif ''.join(number[4:7]) == '296':
    valid['phone'] = ''.join(number)
    valid['operator'] = 'A1'
    print(valid)
elif ''.join(number[4:7]) == '297':
    valid['phone'] = ''.join(number)
    valid['operator'] = 'MTC'
    print(valid)
elif ''.join(number[4:7]) == '298':
    valid['phone'] = ''.join(number)
    valid['operator'] = 'MTC'
    print(valid)
elif ''.join(number[4:7]) == '299':
    valid['phone'] = ''.join(number)
    valid['operator'] = 'A1'
    print(valid)
elif ''.join(number[4:6]) == '33':
    valid['phone'] = ''.join(number)
    valid['operator'] = 'MTC'
    print(valid)
elif ''.join(number[4:6]) == '44':
    valid['phone'] = ''.join(number)
    valid['operator'] = 'A1'
    print(valid)
else:
    print(notvalid)

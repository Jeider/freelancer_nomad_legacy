"""Shared parking sale policy and the authored refusal branch."""
import copy
import re

DENIAL_RU = 'Не могу продать тебе место. Твоя репутация у нашей фракции должна быть положительной.'
DENIAL_EN = 'I cannot sell you a berth. Your reputation with our faction must be positive.'


def parking_scenario(data):
    data=copy.deepcopy(data)
    data['rules']['reputation']={'enabled':True,'faction':'contact.affiliation',
                               'minimum':0,'strict':True,'enforced_by':'server.parking'}
    name=data['id']+'_frag0023'
    row={'id':name,'role':'vendor','pool':'bad_reputation','ru':DENIAL_RU,'en':DENIAL_EN}
    existing=next((f for f in data['fragments'] if f['id']==name),None)
    if existing is not None and existing!=row:
        raise ValueError('Parking refusal fragment ID already occupied: '+name)
    if existing is None:data['fragments'].append(row)
    data['nodes']['parking_bad_reputation']={'pool':'bad_reputation','choices':'result'}
    for choice in ('buy','confirm'):
        data['choices'][choice].setdefault('outcomes',{})['bad_reputation']='parking_bad_reputation'
    return data


def parking_rules(content, affiliations):
    """Preserve prices, ownership limits and sellers; bind sales to their factions."""
    result=[]
    for block in re.split(r'(?m)(?=^\[)',content):
        if block.strip().lower().startswith('[parkingbase]'):
            match=re.search(r'(?im)^base\s*=\s*([^\r\n;]+)',block)
            base=match[1].strip().lower() if match else ''
            if base in affiliations:
                faction=affiliations[base]
                if not re.fullmatch(r'[a-z0-9_]+',faction):raise ValueError('Invalid parking faction: '+base)
                block=re.sub(r'(?im)^reputation_faction\s*=[^\r\n]*\r?\n?', '',block)
                block=block.rstrip()+'\nreputation_faction = '+faction+'\n\n'
        result.append(block)
    return ''.join(result)


def parking_denial_ini(content):
    if re.search(r'(?im)^nickname\s*=\s*parking_bad_reputation\s*$',content):return content
    return content.rstrip()+f'''

[DialogNode]
nickname = parking_bad_reputation
text_ru = {DENIAL_RU}
text_en = {DENIAL_EN}

[DialogChoice]
node = parking_bad_reputation
text_ru = Назад
text_en = Back
goto = parking_start

[DialogChoice]
node = parking_bad_reputation
text_ru = До встречи
text_en = Goodbye
action = close
'''

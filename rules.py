from production import IF, AND, THEN, OR, DELETE, NOT, FAIL

def get_class_field_values(cls):
    values = {value for key, value in cls.__dict__.items() if not (key.startswith('__') or key.startswith('_'))}
    
    for base in cls.__bases__:
        values.update(get_class_field_values(base))
        
    return list(values)

class Common:
    is_tall = '(?x) is tall'
    is_average = '(?x) is average'
    _has_money = '(?x) is rich'
    looks_scared = '(?x) looks scared'
    has_leather = '(?x) has leather'
    has_big_eyes = '(?x) has big eyes'
    has_small_mouth = '(?x) has small mouth'

class Loonling:
    _conclusion = '(?x) is a Loonling'
    
    
class Earthling:
    _conclusion = '(?x) is an Earthling'
    
class Marsian:
    is_redhead = '(?x) is redhead'
    strongly_built = '(?x) is strongly built'
    _conclusion = '(?x) is a Marsian'
    
class Alien:
    is_smart = '(?x) is smart'
    _conclusion = '(?x) is an Alien'

class Plutonian:
    _is_silent = '(?x) is silent'
    _conclusion = '(?x) is a Plutonian'
    

TOURIST_RULES = (
    IF(AND(Common.has_leather), THEN(Common._has_money)),
    IF(AND(Common._has_money, Common.is_tall), THEN(Loonling._conclusion)),
    IF(AND(Common._has_money, Common.is_average), THEN(Earthling._conclusion)),
    IF(AND(Marsian.is_redhead, Marsian.strongly_built), THEN(Marsian._conclusion)),
    IF(AND(Common.has_big_eyes, Alien.is_smart), THEN(Alien._conclusion)),
    IF(OR(Common.has_small_mouth, Common.looks_scared), THEN(Plutonian._is_silent)),
    IF(AND(Plutonian._is_silent, Common.has_big_eyes), THEN(Plutonian._conclusion))
)

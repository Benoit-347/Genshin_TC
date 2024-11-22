import damage_calculator as calc

def get_intristic_stat():
    char_base_atk = 446
    ascention_ = 0
    passive_buff = 0
    skill_ = 2.0
    weapon_base_atk = 450
    weapon_secondary = 0.45
    weapon_passive = 0.40
    return char_base_atk+weapon_base_atk, ascention_, passive_buff, skill_, weapon_secondary, weapon_passive

base_atk, ascention, passive_buff, weapon_secondary, weapon_passive, skill = get_intristic_stat()

def simulate():
    atk = calc.calc_atk(base_atk,)

atk = calc.calc_atk(945.32, 0.59416+0.571+0.6, 62.26+1627.68)
er_ = 3.122
ele_dmg_ = (er_-1)*0.4+0.466+0.484
burst_dmg_ = min(0.75,0.25*er_)+0.27
dmg_ = ele_dmg_ + burst_dmg_
cr = 0.703
cd = 1.683
skill = 8.517+(0.083*60)
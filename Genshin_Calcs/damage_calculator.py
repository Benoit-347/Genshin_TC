def calc_atk(base_atk, atk_, falt_atk_buff=0):
    return base_atk*(1+atk_)+311+falt_atk_buff

def calc_raw_damage(total_atk, dmg_, CR, CD, skill_multiplier):
    damage = total_atk*(1+dmg_)*(1+CR*CD)*skill_multiplier
    return damage

def calc_real_damage(damage, char_lev=90, enemy_level=95, res_shred=0, def_multi_shred=0, def_shred=0):
    enemy_def = (enemy_level+100)*(1-def_multi_shred)*(1-def_shred)
    char_lev_effect = (char_lev+100)
    def_multiplier = char_lev_effect/(enemy_def+char_lev_effect)
    if res_shred > 0.1:
        res_multiplier = (1+(res_shred-0.1)/2)
    else:
        res_multiplier = (1 - (0.1 - res_shred))
    real_damage = damage*res_multiplier*def_multiplier
    return real_damage



if __name__ == "__main__":
    attack = 4614
    dmg_ = 2.8188
    CR =0.703
    cd = 1.083 + 0.60
    skill = 8.517+(0.083*60)
    damage = calc_raw_damage(attack, dmg_, CR, cd, skill)
    print(f"\nTheory damage: {damage}\n")
    print(f"Real damage is: {calc_real_damage(damage, 90, 95,0.4,0.6)}\n")
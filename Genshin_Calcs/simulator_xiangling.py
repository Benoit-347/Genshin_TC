import damage_calculator as calc
def calc_xiangling(atk, cr, cd):
    return calc.calc_real_damage(calc.calc_raw_damage(atk, dmg_, cr, cd, skill, 1.5), 90, 90, 0.4, 0, 0)
atk = 0
er_ = 1
ele_dmg_ = 0
burst_dmg_ = 0
dmg_ = ele_dmg_ + burst_dmg_
cr = 0
cd = 0
skill = 0

def get_intristic_stat():
    char_base_atk = 225.14
    ascention_ = 96
    passive_buff = 0    #pyro res shred = 0.15
    skill_ = 2.016*8
    weapon_base_atk = 	510
    weapon_secondary = 0
    weapon_passive_1 = 0.32
    weapon_passive_2 = 0.12
    return char_base_atk+weapon_base_atk, ascention_, passive_buff, skill_, weapon_secondary, weapon_passive_1, weapon_passive_2

base_atk, ascention, passive_buff, skill, weapon_secondary, dmg_, cr = get_intristic_stat()

def update_values_from_artifact_set():
    global er_, ele_dmg_, cr
    er_ += 0.2
    #main
    er_ += 0.518
    #gob
    ele_dmg_ += 0.466
    #circlet
    cr += 0.311
    #dmg_ += er/4

def get_count(list):
    set1 = set(list)
    counted = []
    for i in set1:
        counted.append([i, list.count(i)])
    return counted

def get_atk_roll_dmg(sim_atk, sim_cr, sim_cd, atk_roll):
    sim_atk += atk_roll
    current_damage = calc_xiangling(sim_atk, sim_cr, sim_cd)
    return current_damage

def get_cr_roll_dmg(sim_atk, sim_cr, sim_cd, cr_roll):
    sim_cr += cr_roll
    current_damage = calc_xiangling(sim_atk, sim_cr, sim_cd)
    return current_damage

def get_cd_roll_dmg(sim_atk, sim_cr, sim_cd, cd_roll):
    sim_cd += cd_roll
    current_damage = calc_xiangling(sim_atk, sim_cr, sim_cd)
    return current_damage

def get_optimal(total_rolls):

    #copying stats
    sim_atk = atk
    sim_atk += calc.calc_atk(base_atk, 0)
    sim_dmg_ = dmg_
    sim_cr = cr
    sim_cd = cd

    #putting stat for each roll 
    atk_roll = 0.04955
    er_roll = 0.05505
    cd_roll = 0.0661
    cr_roll = 0.03305

    rolls_list = [sim_atk, sim_dmg_, sim_cr, sim_cd]
    sim_list = []   #to hold the top stats during sim
    prev_atk_dmg =prev_cd_dmg=prev_cr_dmg = calc_xiangling(sim_atk, sim_cr, sim_cd)
    atk_CM_list = []
    cd_CM_list = []
    cr_CM_list = []

    for i in range(total_rolls):

        atk_dmg = get_atk_roll_dmg(sim_atk, sim_cr, sim_cd, atk_roll)
        atk_CM_list.append(roundzatk_dmg/prev_atk_dmg)
        prev_atk_dmg = atk_dmg
        cr_dmg = get_cr_roll_dmg(sim_atk, sim_cr, sim_cd, cr_roll)
        cr_CM_list.append(cr_dmg/prev_cr_dmg)
        prev_cr_dmg = cr_dmg
        cd_dmg = get_cd_roll_dmg(sim_atk, sim_cr, sim_cd, cd_roll)
        cd_CM_list.append(cd_dmg/prev_cd_dmg)
        prev_cd_dmg = cd_dmg

        if cr_dmg > atk_dmg :
            current_best = "cr"
            temp = cr_dmg
        if cd_dmg > temp:
            current_best = "cd"
            temp = cd_dmg
        if atk_dmg > temp:
            current_best = "atk"
            
        if current_best == "cr":
            sim_cr += cr_roll
        elif current_best == "cd":
            sim_cd += cd_roll
        else:
            sim_atk += atk_roll
        sim_list.append(current_best)
    print(get_count(sim_list))
    print(atk_CM_list)
    print(cd_CM_list)
    print(cr_CM_list)
            


#main
cr += 0.05
cd += 0.5
update_values_from_artifact_set()
get_optimal(70)
import damage_calculator as calc
def calc_xiangling(atk, cr, cd, em, er_):
    temp_dmg_ = dmg_ + er_/4
    return calc.calc_real_damage(calc.calc_raw_damage(atk, temp_dmg_, cr, cd, skill, 1.5, em), 90, 90, 0.4, 0, 0)
atk = 0
er_ = 1
em = 0
ele_dmg_ = 0
burst_dmg_ = 0
dmg_ = ele_dmg_ + burst_dmg_
cr = 0
cd = 0
res_shred = 0
def_shred = 0
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

def get_atk_roll_dmg(sim_atk, sim_cr, sim_cd, sim_em, sim_er, atk_roll):
    sim_atk += atk_roll
    current_damage = calc_xiangling(sim_atk, sim_cr, sim_cd, sim_em, sim_er)
    print(current_damage)
    return current_damage

def get_cr_roll_dmg(sim_atk, sim_cr, sim_cd, sim_em, sim_er , cr_roll):
    sim_cr += cr_roll
    current_damage = calc_xiangling(sim_atk, sim_cr, sim_cd, sim_em, sim_er)
    print(current_damage)
    return current_damage

def get_cd_roll_dmg(sim_atk, sim_cr, sim_cd, sim_em, sim_er, cd_roll):
    sim_cd += cd_roll
    current_damage = calc_xiangling(sim_atk, sim_cr, sim_cd, sim_em, sim_er)
    print(current_damage)
    return current_damage

def get_em_roll_dmg(sim_atk, sim_cr, sim_cd, sim_em, sim_er, em_roll):
    sim_em += em_roll
    current_damage = calc_xiangling(sim_atk, sim_cr, sim_cd, sim_em, sim_er)
    print(current_damage)
    return current_damage


def get_er_roll_dmg(sim_atk, sim_cr, sim_cd, sim_em, sim_er, er_roll):
    sim_er += er_roll
    current_damage = calc_xiangling(sim_atk, sim_cr, sim_cd, sim_em, sim_er)
    print(current_damage)
    return current_damage


def get_optimal(total_rolls):

    #copying stats
    sim_atk = atk
    sim_atk = calc.calc_atk(base_atk, 0)
    sim_em = em
    sim_er = er_
    sim_dmg_ = dmg_
    sim_cr = cr
    sim_cd = cd
    sim_res_shred = res_shred
    sim_def_shred = def_shred

    #putting stat for each roll 
    atk_roll = 0.04955
    er_roll = 0.05505
    em_roll = 0
    cd_roll = 0.0661
    cr_roll = 0.03305

    rolls_list = [sim_atk, sim_dmg_, sim_cr, sim_cd]
    sim_list = []   #to hold the top stats during sim


    for i in range(total_rolls):

        atk_dmg = get_atk_roll_dmg(sim_atk, sim_cr, sim_cd, sim_em, sim_er, atk_roll)
        cr_dmg = get_cr_roll_dmg(sim_atk, sim_cr, sim_cd, sim_em, sim_er, cr_roll)
        cd_dmg = get_cd_roll_dmg(sim_atk, sim_cr, sim_cd, sim_em, sim_er, cd_roll)
        em_dmg = get_em_roll_dmg(sim_atk, sim_cr, sim_cd, sim_em, sim_er, em_roll)
        er_dmg = get_er_roll_dmg(sim_atk, sim_cr, sim_cd, sim_em, sim_er, er_roll)
        
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
            


#main
cr += 0.05
cd += 0.5
update_values_from_artifact_set()
get_optimal(31)

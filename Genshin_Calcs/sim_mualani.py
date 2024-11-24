#need to add timer for buffs

import damage_calculator as calc
def calc_xiangling(atk, cr, cd, em, er_):
    return calc.calc_real_damage(calc.calc_raw_damage(atk, dmg_, cr, cd, skill, elemental_multiplier, em), 90, 90, res_shred, 0, 0)
    
def get_intrinsic_stat():
    char_base_hp = 358.77
    ascention_ = 0.384      #cd
    passive_buff = 0.35    #atk
    skill_ = ((2.304 + 1.44)*7 + 8.0064 + 5.76)/15
    weapon_secondary = 0.276
    weapon_passive_1 = 0.32
    weapon_passive_2 = 0
    return char_base_hp, ascention_, passive_buff, skill_, weapon_secondary, weapon_passive_1


def update_values_from_artifact_set():
    global atk_, ele_dmg_, cr
    cr += 0.4
    #main
    atk_ += 0.466
    #gob
    ele_dmg_ += 0.466
    #circlet
    cr += 0.311
    #dmg_ += er/4

def update_buffs(bennet= 0, kazuha= 0, xilonen= 0, candace= 0, furina = 0):
    global atk, atk_, dmg_, res_shred, em
    if bennet == 1:
        atk += 1045.11328
        atk_+= 0.4
    if kazuha == 1:
        res_shred += 0.4
        dmg_ += 0.58
    if xilonen == 1:
        res_shred += 0.36
        dmg_ += 0.4
        atk_ += 0.48
    if candace == 1:
        dmg_ += 0.3
        em += 120

    if furina:
        dmg_ += 0.30
        em += 160
        



def cons(con):
    if con > 0:
        global atk_
        atk_ += 0.40

    if con > 1:
        global base_atk
        base_atk += 300
        if g_type:
            global skill
            skill += 1.5
        else:
            global def_shred
            def_shred += 0.2

def is_weapon(flag = 0):
    if flag:
        global base_atk, dmg_, atk_, cr, cd
        atk_ += - weapon_secondary - weapon_passive + 0.28*1.75
        base_atk += 146
        cr += 0.11
        cd += 0.2*1.75

def get_count(list):
    set1 = set(list)
    counted = []
    for i in set1:
        counted.append([i, list.count(i)])
    return counted

def get_atk_roll_dmg(sim_atk, sim_cr, sim_cd, sim_em, sim_er, atk_roll):
    sim_atk += atk_roll*base_atk
    current_damage = calc_xiangling(sim_atk, sim_cr, sim_cd, sim_em, sim_er)
    return current_damage

def get_cr_roll_dmg(sim_atk, sim_cr, sim_cd, sim_em, sim_er , cr_roll):
    sim_cr += cr_roll
    current_damage = calc_xiangling(sim_atk, sim_cr, sim_cd, sim_em, sim_er)
    return current_damage

def get_cd_roll_dmg(sim_atk, sim_cr, sim_cd, sim_em, sim_er, cd_roll):
    sim_cd += cd_roll
    current_damage = calc_xiangling(sim_atk, sim_cr, sim_cd, sim_em, sim_er)
    return current_damage

def get_em_roll_dmg(sim_atk, sim_cr, sim_cd, sim_em, sim_er, em_roll):
    sim_em += em_roll
    current_damage = calc_xiangling(sim_atk, sim_cr, sim_cd, sim_em, sim_er)
    return current_damage


def get_er_roll_dmg(sim_atk, sim_cr, sim_cd, sim_em, sim_er, er_roll):
    sim_er += er_roll
    current_damage = calc_xiangling(sim_atk, sim_cr, sim_cd, sim_em, sim_er)
    return current_damage


def get_optimal(total_rolls):

    #copying stats
    sim_atk = atk
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
    em_roll = 19.815
    cd_roll = 0.0661
    cr_roll = 0.03305

    sim_list = []   #to hold the top stats during sim



    temp = calc_xiangling(sim_atk, sim_cr, sim_cd, sim_em, sim_er)

    for _ in range(total_rolls):


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
            temp = atk_dmg
        if em_dmg > temp:
            current_best = "em"
            temp = em_dmg
        if er_dmg > temp:
            current_best = "er"
            temp = er_dmg
            
        if current_best == "cr":
            sim_cr += cr_roll
        elif current_best == "cd":
            sim_cd += cd_roll
        elif current_best == "em":
            sim_em += em_roll
        elif current_best == "atk":
            sim_atk += atk_roll
        else:
            sim_er += er_roll
        sim_list.append(current_best)
    
    print(sim_cr)
    print(f"Max damage in sim: {round(temp, 2)}")
    print(get_count(sim_list))
            
def write_to_csv_cm(total_rolls, file_name):
    import csv, os

    #copying stats
    sim_atk1 = sim_atk = atk
    sim_em1 = sim_em = em
    sim_er1 = sim_er = er_
    sim_dmg_ = dmg_
    sim_cr2 = sim_cr1 = sim_cr = cr
    sim_cd2 = sim_cd1 = sim_cd = cd
    sim_res_shred = res_shred
    sim_def_shred = def_shred

    #putting stat for each roll 
    atk_roll = 0.04955
    er_roll = 0.05505
    em_roll = 19.815
    cd_roll = 0.0661
    cr_roll = 0.03305

    prev_atk_dmg = prev_cr_dmg = prev_cd_dmg = prev_em_dmg = prev_er_dmg = calc_xiangling(sim_atk, sim_cr, sim_cd, sim_em, sim_er)
    
    result = []
    for i in range(total_rolls):
        
        atk_dmg = get_atk_roll_dmg(sim_atk1, sim_cr, sim_cd, sim_em, sim_er, atk_roll)
        cm_atk = round((atk_dmg/prev_atk_dmg-1)*100, 2)
        prev_atk_dmg = atk_dmg
        sim_atk1+=atk_roll*base_atk

        cr_dmg = get_cr_roll_dmg(sim_atk, sim_cr1, sim_cd1, sim_em, sim_er, cr_roll)
        cm_cr = round((cr_dmg/prev_cr_dmg-1)*100, 2)
        prev_cr_dmg = cr_dmg
        sim_cr1+=cr_roll/2
        sim_cd1+=cd_roll/2

        cd_dmg = get_cd_roll_dmg(sim_atk, sim_cr2, sim_cd2, sim_em, sim_er, cd_roll)
        cm_cd = round((cd_dmg/prev_cd_dmg-1)*100, 2)
        prev_cd_dmg = cd_dmg
        sim_cd2+=cd_roll/2
        sim_cr2+=cr_roll/2

        em_dmg = get_em_roll_dmg(sim_atk, sim_cr, sim_cd, sim_em1, sim_er, em_roll)
        cm_em = round((em_dmg/prev_em_dmg-1)*100, 2)
        prev_em_dmg = em_dmg
        sim_em1+=em_roll

        er_dmg = get_er_roll_dmg(sim_atk, sim_cr, sim_cd, sim_em, sim_er1, er_roll)
        cm_er = round((er_dmg/prev_er_dmg-1)*100, 2)
        prev_er_dmg = er_dmg
        sim_er1+=er_roll

        result.append([atk_dmg, cm_atk, cr_dmg, cm_cr, cd_dmg, cm_cd, em_dmg, cm_em, er_dmg, cm_er])

    with open(file_name, 'w') as file1:
        writer = csv.writer(file1)
        writer.writerow(['atk_dmg', 'atk_cm','cr_dmg', 'cr_cm','cd_dmg', 'cd_cm','em_dmg','em_cm','er_dmg','er_cm'])
        writer.writerows(result)
    os.startfile(file_name)
#main

base_atk, ascention, passive_buff, skill, weapon_secondary, weapon_passive = get_intrinsic_stat()

atk_ = 0 + weapon_secondary + weapon_passive + passive_buff
atk = 0
er_ = 1 
em = 0 + ascention
ele_dmg_ = 0
burst_dmg_ = 0
dmg_ =  ele_dmg_ + burst_dmg_
cr = 0.05
cd = 0.5 + ascention
res_shred = 0 
def_shred = 0
skill = skill

update_values_from_artifact_set()
update_buffs(bennet= 0, kazuha= 1, xilonen = 1, furina = 1, candace= 0)
gameplay_type(on_field=1, vap= 1)
cons(con = 2)
is_weapon(0)
atk += calc.calc_atk(base_atk, atk_)
get_optimal(33)
#write_to_csv_cm(40, "mauvika_off_field_stat_cumulative_increase.csv")
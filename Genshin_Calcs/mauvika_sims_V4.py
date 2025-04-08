#need to add timer for buffs and vapability
#type rotation  #calc damage for each sec then to hit  #add vap individually

import damage_calculator as calc

def calc_mauvika(atk,dmg_, cr, cd, skill, elemental_multiplier, em):
    return calc.calc_real_damage(calc.calc_raw_damage(atk, dmg_, cr, cd, skill, elemental_multiplier, em), 90, 90, res_shred, 0, 0)
    
def get_intrinsic_stat():
    char_base_atk = 358.77
    ascention_ = 0.384      #cd
    passive_buff = 0.35    #atk
    skill_ = ((2.304 + 5.76)*7 + 8.0064)/15
    weapon_base_atk = 	565
    weapon_secondary = 0.276
    weapon_passive_1 = 0.32
    weapon_passive_2 = 0
    return char_base_atk+weapon_base_atk, ascention_, passive_buff, skill_, weapon_secondary, weapon_passive_1


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

def update_buffs_global(bennet= 0, kazuha= 0, xilonen= 0, candace= 0, furina = 0):
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

def update_buff_uptime_temp(sec, buff_atk, buff_atk_, buff_dmg_, buff_res_shred, buff_em, bennet_time_start, bennet_time_stop, kazuha_time_start, kazuha_time_stop, xilonen_time_start, xilonen_time_stop, candace_time_start, candace_time_stop, furina_time_start, furina_time_stop):


    if bennet_time_start >= sec and sec >=  bennet_time_stop:
        buff_atk  += 1045.11328
        buff_atk_ += 0.4


    if kazuha_time_start >= sec and sec >  kazuha_time_stop:
        buff_res_shred += 0.4
        buff_dmg_ += 0.58

    if xilonen_time_start >= sec and sec >  xilonen_time_stop:
        buff_res_shred += 0.36
        buff_dmg_ += 0.4
        buff_atk_ += 0.48

    if candace_time_start >= sec and sec >  candace_time_stop:
        buff_dmg_ += 0.3
        buff_em += 120     

    if furina_time_start >= sec and sec >  furina_time_stop:
        buff_dmg_ += 0.30
        buff_em += 160
    return buff_atk, buff_atk_, buff_dmg_, buff_res_shred, buff_em
        


def rotation(atk, atk_, dmg_, cr, cd, elemental_multiplier, em):
    s_0 = "na"
    s_1 = "na"
    s_2 = "na"
    s_3 = "na"
    s_4 = "na"
    s_5 = "na"
    s_6 = "na"
    s_7 = "na"
    s_8 = "na"
    s_9 = "na"
    s_10 ="na"
    s_11 = "na"
    s_12 = "na"
    s_13 = "na"
    s_14 = "na"
    s_15 = "na"
    s_16 = "na"
    s_17 = "na"
    s_18 = "na"
    s_19 = "na"
    s_20 = "na"

#Mav E, kaz EQ, Xil EQ, Furina EQ = 10s
    s_0 = "e"
    s_2 = "e"
    s_4 = "e"
    s_6 = "e"
    s_8 = "e"
    s_10 = "q"
    s_12 = "calc"
    s_13 = "calc"
    s_14 = "calc"
    s_15 = "calc"
    s_16 = "calc"
    s_17 = "e"
    s_18 = "e"
    s_19 = "na"
    s_20 = "na"
    list_seconds = [s_0, s_1, s_2, s_3, s_4, s_5, s_6, s_7, s_8, s_9, s_10, s_11, s_12, s_13, s_14, s_15, s_16, s_17, s_18, s_19, s_20]
    dps_list = []
    dpr = 0
    sec = 0
    global e_skill, q_skill, ca_skill
    for i in list_seconds:

        buff_atk, buff_atk_, buff_dmg_, buff_res_shred, buff_em = update_buff_uptime_temp(sec, atk, atk_, dmg_, res_shred, em, bennet_time_start=0, bennet_time_stop= 0, kazuha_time_start=0, kazuha_time_stop= 21, xilonen_time_start= 0, xilonen_time_stop=21, candace_time_start = 0, candace_time_stop = 0, furina_time_start=0, furina_time_stop=21)
        total_atk = buff_atk + calc.calc_atk(base_atk, buff_atk_)

        if i == "na":
            continue
        elif i == "e":
            dps = calc_mauvika(total_atk, buff_dmg_, cr, cd, e_skill, elemental_multiplier, buff_em)
        elif i == "calc":
            dps = dps = calc_mauvika(total_atk, buff_dmg_, cr, cd, ca_skill, elemental_multiplier, buff_em)
        elif i == "q":
            dps = dps = calc_mauvika(total_atk, buff_dmg_, cr, cd, q_skill, elemental_multiplier, buff_em)
        else:
            print("\n\nunknown str encountered\n\n")
            break
        dps_list.append(dps)
        dpr += dps
        sec += 1
    return dps_list, dpr

def gameplay_type(on_field = 0, vap = 0):
    global g_type, elemental_multiplier
    g_type = 0
    if vap:
        elemental_multiplier = 0.5
    else:
        elemental_multiplier = 0
    if on_field:
        global dmg_
        dmg_ += 0.15 + 0.38
        g_type = 1


def cons(con):
    if con > 0:
        global atk_
        atk_ += 0.40

    if con > 1:
        global base_atk
        base_atk += 300
        if g_type:
            global ca_skill
            ca_skill += 1.5
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

def get_atk_roll_dmg(sim_atk, sim_atk_, sim_cr, sim_cd, sim_em, atk_roll):
    sim_atk_ += atk_roll
    na, current_damage = rotation(atk = sim_atk, atk_ = sim_atk_, dmg_ = dmg_, cr = sim_cr, cd = sim_cd, elemental_multiplier = 0.5, em = sim_em)
    return current_damage

def get_cr_roll_dmg(sim_atk, sim_atk_, sim_cr, sim_cd, sim_em, cr_roll):
    sim_cr += cr_roll
    na, current_damage = rotation(atk = sim_atk, atk_ = sim_atk_, dmg_ = dmg_, cr = sim_cr, cd = sim_cd, elemental_multiplier = 0.5, em = sim_em)
    return current_damage

def get_cd_roll_dmg(sim_atk, sim_atk_, sim_cr, sim_cd, sim_em, cd_roll):
    sim_cd += cd_roll
    na, current_damage = rotation(atk = sim_atk, atk_ = sim_atk_, dmg_ = dmg_, cr = sim_cr, cd = sim_cd, elemental_multiplier = 0.5, em = sim_em)
    return current_damage

def get_em_roll_dmg(sim_atk, sim_atk_, sim_cr, sim_cd, sim_em, em_roll):
    sim_em += em_roll
    na, current_damage = rotation(atk = sim_atk, atk_ = sim_atk_, dmg_ = dmg_, cr = sim_cr, cd = sim_cd, elemental_multiplier = 0.5, em = sim_em)
    return current_damage



def get_optimal(total_rolls):

    #copying stats
    sim_atk = atk
    sim_atk_ = atk_
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



    temp = rotation(atk = sim_atk, atk_ = sim_atk_, dmg_ = dmg_, cr = sim_cr, cd = sim_cd, elemental_multiplier = 0.5, em = sim_em)

    for _ in range(total_rolls):


        atk_dmg = get_atk_roll_dmg(sim_atk, sim_atk_, sim_cr, sim_cd, sim_em, atk_roll)
        cr_dmg = get_cr_roll_dmg(sim_atk, sim_atk_, sim_cr, sim_cd, sim_em, cr_roll)
        cd_dmg = get_cd_roll_dmg(sim_atk, sim_atk_, sim_cr, sim_cd, sim_em, cd_roll)
        em_dmg = get_em_roll_dmg(sim_atk, sim_atk_, sim_cr, sim_cd, sim_em, em_roll)
        
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
    damge_list, total_damage = rotation(atk = sim_atk, atk_ = sim_atk_, dmg_ = dmg_, cr = sim_cr, cd = sim_cd, elemental_multiplier = 0.5, em = sim_em)
    print(f"Max damage in sim: {round(total_damage, 2)}")
    j = 0
    for i in damge_list:
        j+= 1
        print(f"Max dps in sim: {j, round(i, 2)}")
    print(get_count(sim_list))
            
def write_to_csv_cm(total_rolls, file_name):
    import csv, os

    #copying stats
    sim_atk1 = sim_atk = atk + calc.calc_atk(base_atk, atk_)
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

    prev_atk_dmg = prev_cr_dmg = prev_cd_dmg = prev_em_dmg = prev_er_dmg = rotation(atk = sim_atk, atk_ = 0, dmg_ = dmg_, cr = sim_cr, cd = sim_cd, elemental_multiplier = 0.5, em = sim_em)
    
    result = []
    for i in range(total_rolls):
        
        atk_dmg = get_atk_roll_dmg(sim_atk1, 0, sim_cr, sim_cd, sim_em, sim_er, atk_roll)
        cm_atk = round((atk_dmg/prev_atk_dmg-1)*100, 2)
        prev_atk_dmg = atk_dmg
        sim_atk1+=atk_roll*base_atk

        cr_dmg = get_cr_roll_dmg(sim_atk, 0, sim_cr1, sim_cd1, sim_em, sim_er, cr_roll)
        cm_cr = round((cr_dmg/prev_cr_dmg-1)*100, 2)
        prev_cr_dmg = cr_dmg
        sim_cr1+=cr_roll/2
        sim_cd1+=cd_roll/2

        cd_dmg = get_cd_roll_dmg(sim_atk, 0, sim_cr2, sim_cd2, sim_em, sim_er, cd_roll)
        cm_cd = round((cd_dmg/prev_cd_dmg-1)*100, 2)
        prev_cd_dmg = cd_dmg
        sim_cd2+=cd_roll/2
        sim_cr2+=cr_roll/2

        em_dmg = get_em_roll_dmg(sim_atk, 0, sim_cr, sim_cd, sim_em1, sim_er, em_roll)
        cm_em = round((em_dmg/prev_em_dmg-1)*100, 2)
        prev_em_dmg = em_dmg
        sim_em1+=em_roll

        result.append([atk_dmg, cm_atk, cr_dmg, cm_cr, cd_dmg, cm_cd, em_dmg, cm_em])

    with open(file_name, 'w') as file1:
        writer = csv.writer(file1)
        writer.writerow(['atk_dmg', 'atk_cm','cr_dmg', 'cr_cm','cd_dmg', 'cd_cm','em_dmg','em_cm','er_dmg','er_cm'])
        writer.writerows(result)
    os.startfile(file_name)

def get_rotaion_damage():
    pass #read temp
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
fighting_spirit = 200
e_skill = 2.304
q_skill = 8.0064 + 0.0288*200
ca_skill = 2.176 + 2.992 + 0.0144*200

update_values_from_artifact_set()
gameplay_type(on_field=1, vap= 1)
cons(con = 2)
is_weapon(0)
get_optimal(33)
#write_to_csv_cm(40, "mauvika_off_field_stat_cumulative_increase.csv")
import damage_calculator as calc
import matplotlib.pyplot as plt

def calc_mauvika(atk,dmg_, cr, cd, skill, elemental_multiplier, em,res_shred, def_shred= 0):
    return calc.calc_real_damage(calc.calc_raw_damage(atk, dmg_, cr, cd, skill, elemental_multiplier, em), 90, 90, res_shred, def_shred, 0)
    
def get_intrinsic_stat():
    char_base_atk = 358.77
    ascention_ = 0.384      #cd
    passive_buff = 0.30    #atk
    skill_ = ((2.304 + 5.76)*7 + 8.0064)/15
    weapon_base_atk = 	565
    weapon_secondary = 0.276
    weapon_passive_1 = 0.32
    weapon_passive_2 = 0
    return char_base_atk+weapon_base_atk, ascention_, passive_buff, skill_, weapon_secondary, weapon_passive_1

def update_values_from_artifact_set():
    global atk_, dmg_, cr
    cr += 0.4
    #main
    atk_ += 0.466
    #gob
    dmg_ += 0.466
    #circlet
    cr += 0.311
    #dmg_ += er/4

def cons(con):
    global con_flag
    con_flag = 0
    if con > 0:
        global atk_
        atk_ += 0.40

    if con > 1:
        global base_atk
        base_atk += 200

        global ca_skill1, ca_skill2
        ca_skill1 += 0.9
        ca_skill2 += 0.9
        con_flag = 2
        #def_shred += 0.2

def is_weapon(flag = 0):
    if flag:
        global base_atk, dmg_, atk_, cr, cd
        atk_ += - weapon_secondary - weapon_passive + 0.28*1.75
        base_atk += 146
        cr += 0.11
        cd += 0.2*1.75

def return_buffed_for_uptime(sec, buff_atk, buff_atk_, buff_dmg_, buff_res_shred, buff_em, bennet_time_start, bennet_time_stop, kazuha_time_start, kazuha_time_stop, xilonen_time_start, xilonen_time_stop, candace_time_start, candace_time_stop, furina_time_start, furina_time_stop):


    if bennet_time_start <= sec and sec <  bennet_time_stop:
        buff_atk  += 1045.11328
        buff_atk_ += 0.2 + 0.25


    if kazuha_time_start <= sec and sec <  kazuha_time_stop:
        buff_res_shred += 0.4
        buff_dmg_ += 0.58
        buff_em += 200

    if xilonen_time_start <= sec and sec <  xilonen_time_stop:
        buff_res_shred += 0.36
        buff_dmg_ += 0.4
        buff_atk_ += 0.45

    if candace_time_start <= sec and sec <  candace_time_stop:
        buff_dmg_ += 0.3
        buff_em += 120     

    if furina_time_start <= sec and sec <  furina_time_stop:
        buff_dmg_ += 0.30
        buff_em += 104.55
        buff_atk_ += 0.2
    return buff_atk, buff_atk_, buff_dmg_, buff_res_shred, buff_em


def rotation(atk, atk_, dmg_, cr, cd, elemental_multiplier, em):
    s_0 = "na"
    s_0_5 = "na"
    s_1 = "na"
    s_1_5 = "na"
    s_2 = "na"
    s_2_5 = "na"
    s_3 = "na"
    s_3_5 = "na"
    s_4 = "na"
    s_4_5 = "na"
    s_5 = "na"
    s_5_5 = "na"
    s_6 = "na"
    s_6_5 = "na"
    s_7 = "na"
    s_7_5 = "na"
    s_8 = "na"
    s_8_5 = "na"
    s_9 = "na"
    s_9_5 = "na"
    s_10 ="na"
    s_10_5 = "na"
    s_11 = "na"
    s_11_5 = "na"
    s_12 = "na"
    s_12_5 = "na"
    s_13 = "na"
    s_13_5 = "na"
    s_14 = "na"
    s_14_5 = "na"
    s_15 = "na"
    s_15_5 = "na"
    s_16 = "na"
    s_16_5 = "na"
    s_17 = "na"
    s_17_5 = "na"
    s_18 = "na"
    s_18_5 = "na"
    s_19 = "na"
    s_19_5 = "na"
#Mav E, Furina EQ, kaz EQ, Xil EQ, = 10s
#Furina E       1s
#Xilonen EN2Q   3s
#Furina Q       2s
#Mav E          2s
#Bennet EQN1    2s
#Xilonen EN2    2s
#Mav Q8CA       6+2s
#Total          20s
    s_7 = "evap"
    s_9 = "evap"
    s_11 = "evap"
    s_12_5 = "evap"
    s_13 = "qvap"
    s_13_5 = "ca1vap"
    s_14_5 = "ca1"
    s_15 = "ca1"
    s_16 = "ca1vap"
    s_16_5 = "ca1vap"
    s_17_5 = "ca1"
    s_18 = "ca1"
    s_19 = "ca1vap"
    list_seconds = [s_0, s_0_5, s_1, s_1_5, s_2, s_2_5, s_3, s_3_5, s_4, s_4_5, s_5, s_5_5, s_6, s_6_5, s_7, s_7_5, s_8, s_8_5, s_9, s_9_5, s_10, s_10_5, s_11, s_11_5, s_12, s_12_5, s_13, s_13_5, s_14, s_14_5, s_15, s_15_5, s_16, s_16_5, s_17, s_17_5, s_18, s_18_5, s_19, s_19_5]
    dps_list = []
    dps = 0
    dpr = 0
    sec = 0
    for i in list_seconds:
                                                                                                                                                            #Furina E       1s  0
                                                                                                                                                            #Xilonen EN2Q   3s  2
                                                                                                                                                            #Furina Q       2s  6
                                                                                                                                                            #Mav E          2s  7
                                                                                                                                                            #Bennet EQN1    2s  9
                                                                                                                                                            #Xilonen EN2    2s  12
                                                                                                                                                            #Mav Q8CA       6+2s 14, to 20
                                                                                                                                                            #Total          20s
        buff_atk, buff_atk_, buff_dmg_, buff_res_shred, buff_em = return_buffed_for_uptime(sec, atk, atk_, dmg_, res_shred, em, bennet_time_start=9, bennet_time_stop= 20, kazuha_time_start=0, kazuha_time_stop= 0, xilonen_time_start= 2, xilonen_time_stop=20, candace_time_start = 0, candace_time_stop = 0, furina_time_start=6, furina_time_stop=20)
        total_atk = buff_atk + calc.calc_atk(base_atk, buff_atk_)

        if i == "na":
            damage = 0
        elif i == "e":
            damage = calc_mauvika(total_atk, buff_dmg_, cr, cd, e_skill, 0, buff_em, buff_res_shred)
        elif i == "ca1":
            damage =  calc_mauvika(total_atk, buff_dmg_+ 0.15 + 0.35, cr, cd, ca_skill1, 0, buff_em, buff_res_shred)
        elif i == "ca2":
            damage =  calc_mauvika(total_atk, buff_dmg_+ 0.15 + 0.35, cr, cd, ca_skill2, 0, buff_em, buff_res_shred)
        elif i == "q":
            damage =  calc_mauvika(total_atk, buff_dmg_+ 0.15 + 0.45, cr, cd, q_skill, 0, buff_em, buff_res_shred)
        elif i == "evap":
            damage = calc_mauvika(total_atk, buff_dmg_, cr, cd, e_skill, elemental_multiplier, buff_em, buff_res_shred)
        elif i == "ca1vap":
            damage =  calc_mauvika(total_atk, buff_dmg_+ 0.15 + 0.35, cr, cd, ca_skill1, elemental_multiplier, buff_em, buff_res_shred)
        elif i == "ca2vap":
            damage =  calc_mauvika(total_atk, buff_dmg_+ 0.15 + 0.35, cr, cd, ca_skill2, elemental_multiplier, buff_em, buff_res_shred)
        elif i == "qvap":
            damage =  calc_mauvika(total_atk, buff_dmg_+ 0.15 + 0.35, cr, cd, q_skill, elemental_multiplier, buff_em, buff_res_shred)
        else:
            print("\n\nunknown str encountered\n\n")
            break
        dps += damage
        external_dps = 294000/(len(list_seconds)//2)
        if sec % 1 == 0:
            dps += external_dps
            dps_list.append([int(sec), round(dps)])
            dps = 0
        dpr += damage + external_dps/2
        sec += 0.5
    return dps_list, dpr

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



    na, temp = rotation(atk = sim_atk, atk_ = sim_atk_, dmg_ = sim_dmg_, cr = sim_cr, cd = sim_cd, elemental_multiplier = 0.5, em = sim_em)

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

    
    print(f"\nOptimal rolls are: {get_count(sim_list)}\n\n----------------------")
    return sim_list

def get_rotation_damage(optimal_num):
    sim_atk = atk
    sim_atk_ = atk_
    sim_em = em
    sim_er = er_
    sim_dmg_ = dmg_
    sim_cr = cr
    sim_cd = cd
    sim_res_shred = res_shred
    sim_def_shred = def_shred

    atk_roll = 0.04955
    er_roll = 0.05505
    em_roll = 19.815
    cd_roll = 0.0661
    cr_roll = 0.03305

    sim_list = get_optimal(optimal_num)

    for i in sim_list:
        if i == "cr":
            sim_cr += cr_roll
        elif i == "cd":
            sim_cd += cd_roll
        elif i == "em":
            sim_em += em_roll
        elif i == "atk":
            sim_atk += atk_roll
    damage_list, total_damage = rotation(atk = sim_atk, atk_ = sim_atk_, dmg_ = sim_dmg_, cr = sim_cr, cd = sim_cd, elemental_multiplier = 0.5, em = sim_em)
    x_list, y_list = [],[]
    for i in damage_list:
        if i[0] == 10:
            print(i)
        x_list.append(i[0])
        y_list.append(i[1])

        
    print(f"\nMax dps: {round(total_damage/20)}\n")
    return x_list, y_list

base_atk, ascention, passive_buff, skill, weapon_secondary, weapon_passive = get_intrinsic_stat()

atk_ = 0 + weapon_secondary + weapon_passive + passive_buff
atk = 0
er_ = 1 
em = 0 
ele_dmg_ = 0
burst_dmg_ = 0
dmg_ =  ele_dmg_ + burst_dmg_
cr = 0.05
cd = 0.5 + ascention
res_shred = 0 
def_shred = 0
fighting_spirit = 200
e_skill = 2.304
q_skill = 8.0064 + 0.029*fighting_spirit
ca_skill1 = 1.955 + 0.012*fighting_spirit
ca_skill2 = 2.72 + 0.012*fighting_spirit

update_values_from_artifact_set()
cons(0)
is_weapon(0)
plot = 0
x, y = get_rotation_damage(optimal_num=33)
#all graphs
if plot ==1:
    plt.figure(figsize=(20, 10))
    plt.plot(x, y)
    plt.title("Dps Graph")
    plt.grid()
    plt.show()
    def get_cm(y):
        cm_list = []
        cm = 0
        for i in y:
            cm += i
            cm_list.append(cm)
        return cm_list
    y = get_cm(y)
    plt.figure(figsize=(20, 10))
    plt.plot(x, y)
    plt.title("Cumulative Damage Graph")
    plt.grid()
    plt.show()
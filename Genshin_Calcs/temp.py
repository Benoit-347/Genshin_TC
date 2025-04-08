def update_buff_uptime_temp(sec, bennet_time_start, bennet_time_stop, kazuha_time_start, kazuha_time_stop, xilonen_time_start, xilonen_time_stop, candace_time_start, candace_time_stop, furina_time_start, furina_time_stop):

    buff_atk, buff_atk_, buff_dmg_, buff_res_shred, buff_em = atk, atk_, dmg_, res_shred, em

    if bennet_time_start >= sec and sec >=  bennet_time_stop:
        buff_atk  += 1045.11328
        buff_atk_ += 0.4


    if kazuha_time_start >= sec and sec >=  kazuha_time_stop:
        buff_res_shred += 0.4
        buff_dmg_ += 0.58

    if xilonen_time_start >= sec and sec >=  xilonen_time_stop:
        buff_res_shred += 0.36
        buff_dmg_ += 0.4
        buff_atk_ += 0.48

    if candace_time_start >= sec and sec >=  candace_time_stop:
        buff_dmg_ += 0.3
        buff_em += 120     

    if furina_time_start >= sec and sec >=  furina_time_stop:
        buff_dmg_ += 0.30
        buff_em += 160
    return buff_atk, buff_atk_, buff_dmg_, buff_res_shred, buff_em
        

#Mav E, kaz EQ, Xil EQ, Furina EQ = 10s
def rotation():
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
    sec = 0
    for i in list_seconds:

        buff_atk, buff_atk_, buff_dmg_, buff_res_shred, buff_em = update_buff_uptime_temp(sec, bennet_time_start, bennet_time_stop, kazuha_time_start, kazuha_time_stop, xilonen_time_start, xilonen_time_stop, candace_time_start, candace_time_stop, furina_time_start, furina_time_stop)
        
        if i == "na":
            continue
        elif i == "e":
            
            dps = cal(damage, skill, sec)
        elif i == "calc":
            dps = cal(damage, attack, sec)
        elif i == "q":
            dps = cal(damage, burst, sec)
        else:
            print("\n\nunknown str encountered\n\n")
            break
        dps_list.append(dps)
        sec += 1
    return 
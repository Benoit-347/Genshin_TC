import damage_calculator as calc

atk = calc.calc_atk(945.32, 0.59416+0.571+0.6, 62.26+1627.68)
er_ = 3.122
ele_dmg_ = (er_-1)*0.4+0.466+0.484
burst_dmg_ = min(0.75,0.25*er_)+0.27
dmg_ = ele_dmg_ + burst_dmg_
cr = 0.703
cd = 1.683
skill = 8.517+(0.083*60)
a = calc.calc_raw_damage(atk, dmg_, cr, cd, skill)
print(calc.calc_real_damage(a, 90, 95, 0.4, 0.6))
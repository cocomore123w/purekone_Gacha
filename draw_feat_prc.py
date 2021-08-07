import random
import lib



###############
#with open("psc_tw.json", "r", encoding="utf8") as psc_data:
# json_psc_data = json.load(psc_data)
#10連抽
#
#
#
#
rare = ['r', 'sr', 'ssr']
##公主季池 ssr 兩倍
#r      77%
#sr     18%
#ssr    5%
#保底
#sr     5%
#ssr    95%
####
#

####
r_value = lib.permanent_character_tw_Quantity_r
sr_value = lib.permanent_character_tw_Quantity_sr
ssr_value = lib.permanent_character_tw_Quantity_ssr + lib.permanent_character_tw_Quantity_prc_l

r = 77 * 0.01
sr = 18 * 0.01
ssr = 5.0 * 0.01
card_num = (lib.permanent_character_tw_Quantity + lib.permanent_character_tw_Quantity_prc_l)* (r_value * sr_value * ssr_value)  * 1000  ##


############################
r_token = int(r*card_num)    #
sr_token = int(sr*card_num)  #
ssr_token =int(ssr*card_num) #
pool = []
########################### 分類稀有度
def rare_by(num):
 weight =  random.randint(1, num)
 result = []
 if(weight<=ssr_token):     #ssr 250<=
     result.append(weight)
     result.append(rare[2])
     return result
 elif(weight<=(sr_token + ssr_token) and weight>ssr_token):   #sr 250 ~ (250+1800)
     result.append(weight)
     result.append(rare[1])
     return result
 elif(weight>(sr_token + ssr_token) ):   #r (250+1800)>
     result.append(weight)
     result.append(rare[0])
     return result
 else:
     return  weight
###### 分類稀有度(保底)
##
##
def rare_by_Guaranteed(num):
    weight = random.randint(1, num)
    result = []
    if (weight <= ssr_token):  # ssr 250<=
        result.append(weight)
        result.append(rare[2])
        return result
    elif (weight >ssr_token):  # sr 250 ~ num
        result.append(weight)
        result.append(rare[1])
        return result
    else:
        return weight
##===================================
##回傳抽到的角色
##非保底狀態
def rare_by_feat(weight):

    if (weight <= ssr_token):  # ssr 250<=
        return rare_by_feat_r(weight,ssr_value)
    elif (weight <= (sr_token + ssr_token) and weight > ssr_token):  # sr 251 ~ (250+1800)
        return rare_by_feat_g(weight,sr_value)
    elif (weight > (sr_token + ssr_token)):  # r (250+1800)>   -----   2051~10000
        return rare_by_feat_s(weight,r_value)
##回傳抽到的角色
##保底狀態
def rare_by_Guaranteed_feat(weight):
    if (weight <= ssr_token):  # ssr 250<=
        return rare_by_feat_r(weight, ssr_value)
    elif (weight > ssr_token):  # sr 250 ~ num
        return rare_by_Guaranteed_feat_g(weight, sr_value)

###############################################
##分配抽到的角色(銀卡)
##
def rare_by_feat_s(num,feat_value):
    ##   num  46435950
    space = r_token
    status = int(space / feat_value)
    #weight = random.randint(1, num)
    result = []
    for i in range(feat_value+1):
        if(num<=status * (i+1) + card_num- r_token + 1):
            #result.append(weight)
            result.append(lib.draw_feat_data_tw_nor_s[i])
            break
    return result

##分配抽到的角色(金卡)
##
def rare_by_feat_g(num,feat_value):
    ##   num  46435950
    space = sr_token
    status = int(space / feat_value)
    #weight = random.randint(1, num)
    result = []
    for i in range(feat_value+1):
        if(num<=status * (i+1) + ssr_token +1):
            #result.append(weight)
            result.append(lib.draw_feat_data_tw_nor_g[i])
            break
    return result
##分配抽到的角色(彩卡)
##
def rare_by_feat_r(num,feat_value):
    ##   num  46435950
    space = ssr_token
    status = int(space / feat_value)
    temp = lib.draw_feat_data_tw_nor_r + lib.draw_feat_data_tw_nor_r_p
    #weight = random.randint(1, num)
    result = []
    for i in range(feat_value+1):
        if(num<=status * (i+1) + 1):
            #result.append(weight)
            result.append(temp[i])
            break
    return result
#############################################################
##分配抽到的角色(金卡)
##保底
def rare_by_Guaranteed_feat_g(num,feat_value):
    space = sr_token + r_token
    status = int(space / feat_value)
    # weight = random.randint(1, num)
    result = []
    for i in range(feat_value + 1):
        if (num <= status * (i + 1) + ssr_token + 1):
            # result.append(weight)
            result.append(lib.draw_feat_data_tw_nor_g[i])
            break
    return result

##====================================
##統計抽卡結果
##
def statistics(input,List = []):
    List = input
    i=0
    r = 0
    sr = 0
    ssr = 0
    for i in range(len(List)) :
        if(List[i][1] =='r'):
            r+=1
        elif(List[i][1]=='sr'):
            sr+=1
        elif(List[i][1]=='ssr'):
            ssr+=1
    #result = [r,sr,ssr]
    return r,sr,ssr
###########################
##抽卡
def draw_():

 i=0
 j = 0
 run = 1
 draw_times = 10
 Guaranteed_weight=0

 #print(r_token)
 #print(sr_token)
 #print(ssr_token)
 #a = rare_by(card_num)
 #print(a)
 for j in range(run):
    draw = []


    for i in range(draw_times-1):
     #print(rare_by_Guaranteed(card_num))
     draw_once = rare_by(card_num) # [0]=weight
     draw_once.append(rare_by_feat(draw_once[0]))
     draw.append(draw_once)

     #print(draw_once)
     #Guaranteed_weight = Guaranteed_weight + draw[i][0]
     i+=1

    #if(Guaranteed_weight>(sr_token +ssr_token)*10):
    Guaranteed_card = rare_by_Guaranteed(card_num)
    Guaranteed_card.append(rare_by_Guaranteed_feat(Guaranteed_card[0]))
    draw.append(Guaranteed_card)
    #print(draw)
    return draw, statistics(draw)
    #######
    ##draw
    ##
    #######
    #else:
   # draw_once = rare_by(card_num)
   # draw.append(draw_once)

    #print()


     #if()


    #print(a[0])
    #print(a[1])
    #print(a[2])

#for i in card_num:
#   pool.append()
if __name__ == '__main__':

     for i in range(0,1000):
      a = draw_()
     #a = rare_by_feat_s(r_token,11)
     #b = rare_by_feat_g(sr_token, 18)
     #c = rare_by_feat_r(ssr_token, 30)

      print(a)
      i+=1
     #print(a[0][1][2][0])
     #print(a[0][1][1])
     #print(type(a[0][1][2][0]))

     #print(b)
     #print(c)
     #print(a[0])
     #print(type(a[1][0]))
     #print(a[1][1])
     #print(a[1][2])

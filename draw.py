import random




###############
#10連抽
#
#
#
#
rare = ['r', 'sr', 'ssr']
##
#r      79.5%
#sr     18%
#ssr    2.5%
#保底
#sr     2.5%
#ssr    97.5%
####
r = 79.5*0.01
sr = 18*0.01
ssr = 2.5*0.01
card_num = 10000

r_token = int(r*card_num)    #7950
sr_token = int(sr*card_num)  #
ssr_token =int(ssr*card_num) #
pool = []
###########################   分類稀有度
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
###################################保底
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
##====================================統計抽卡結果
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
     draw_once = rare_by(card_num)
     draw.append(draw_once)
     #print(draw_once)
     Guaranteed_weight = Guaranteed_weight + draw[i][0]
     i+=1

    #if(Guaranteed_weight>(sr_token +ssr_token)*10):
    Guaranteed_card = rare_by_Guaranteed(card_num)
    draw.append(Guaranteed_card)
    return draw, statistics(draw)
    #######
    ##draw
    ##
    #######
    #else:
   # draw_once = rare_by(card_num)
   # draw.append(draw_once)

    #print()

    #print(draw)
     #if()


    #print(a[0])
    #print(a[1])
    #print(a[2])

#for i in card_num:
#   pool.append()

################# test
if __name__ == '__main__':
     a = draw_()
     print(a[0])
     print(type(a[1][0]))
     print(a[1][1])
     print(a[1][2])

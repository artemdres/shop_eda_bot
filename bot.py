import telebot
import json
import datetime





menu_items = [
        {"name": "Грибной суп", "price": "450 руб.", "photo": "mushroom_soup.png"},
        {"name": "Салат Цезарь", "price": "550 руб.", "photo": "caesar.png"},
        {"name": "Утка с апельсинами", "price": "700 руб.", "photo": "duck_orange.png"},
        {"name": "Бефстроганов", "price": "650 руб.", "photo": "stroganoff.png"},
        {"name": "Ризотто", "price": "500 руб.", "photo": "risotto.png"},
        {"name": "Тирамису", "price": "400 руб.", "photo": "tiramisu.png"},
        {"name": "Блины", "price": "300 руб.", "photo": "pancakes.png"},
        {"name": "Паста Карбонара", "price": "550 руб.", "photo": "carbonara.png"},
        {"name": "Гаспачо", "price": "350 руб.", "photo": "gazpacho.png"},
        {"name": "Фалафель", "price": "400 руб.", "photo": "falafel.png"}

]



def ima_pol (message):
    fail=open("infa.json", "r", encoding="UTF-8")
    slovar=json.load(fail)
    slovar_pol=slovar[str(message.chat.id)]
    slovar_pol["neme"]=message.text
    fail.close()
    fail=open("infa.json", "w", encoding="UTF-8")
    json.dump(slovar, fail, ensure_ascii=False, indent=4)
    fail.close()
    bot.send_message(message.chat.id, "ваш номер")
    bot.register_next_step_handler_by_chat_id(message.chat.id, nomer_pol)

def nomer_pol(message):
    fail=open("infa.json", "r", encoding="UTF-8")
    slovar=json.load(fail)
    slovar_pol=slovar[str(message.chat.id)]
    slovar_pol["nomer"]=message.text
    fail.close()
    fail=open("infa.json", "w", encoding="UTF-8")
    json.dump(slovar, fail, ensure_ascii=False, indent=4)
    fail.close()
    bot.send_message(message.chat.id, "ваш адрес")
    bot.register_next_step_handler_by_chat_id(message.chat.id, adres_pol)
    
def adres_pol(message):
    fail=open("infa.json", "r", encoding="UTF-8")
    slovar=json.load(fail)
    slovar_pol=slovar[str(message.chat.id)]
    slovar_pol["adres"]=message.text
    slovar_pol["korzina"]={}
    fail.close()
    fail=open("infa.json", "w", encoding="UTF-8")
    json.dump(slovar, fail, ensure_ascii=False, indent=4)
    fail.close()
    bot.send_message(message.chat.id, "ваш заказ скоро доставят")
    













tokin="7850309479:AAHWkVIP5mpstHMbzFBacaeZxW6W0S701qQ"


bot=telebot.TeleBot(tokin)
@bot.message_handler(["start"])
def obrabotak_start(message):
    knopki=knopka()
    bot.send_message(message.chat.id, "добро пожаловать", reply_markup=knopki)

def true(message):
    return True


@bot.message_handler(func=true)
def obrabotka_soopseni(message):
    
    if message.text=="меню":
        knopki_eda=knopki_name_blyda()
        bot.send_message(message.chat.id, "вот меню", reply_markup=knopki_eda)
        
    elif message.text=="корзина":
        fail_pol=open("infa.json", "r", encoding="UTF-8")
        slovar=json.load(fail_pol)
        info_pol=slovar[str(message.chat.id)]
        korzina_pol=info_pol["korzina"]
        fail_pol.close()
        if len(korzina_pol)!=0:
            
            
            
            bot.send_message(message.chat.id, "вот корзина", reply_markup=knopka_s_blydami_v_karzine(message.chat.id))
        else:
            bot.send_message(message.chat.id, "у вас нечего нет" )





def knopki_name_blyda():
    spisok_knopok=telebot.types.InlineKeyboardMarkup()
    for slovar_blyda in menu_items:
        name=slovar_blyda["name"]
        knopka=telebot.types.InlineKeyboardButton(name, callback_data="blydo_"+ name)
        spisok_knopok.add(knopka)
    return spisok_knopok





def cena_blyd(neem_blyd):
    for slovar_blyd in menu_items:
        if slovar_blyd["name"]== neem_blyd:
            return slovar_blyd["price"]
        
        
    








@bot.callback_query_handler(func=true)
def nazatie(clic):
    rzdelitel_po_probelam=clic.data.split("_")
   
    if rzdelitel_po_probelam[0] == "blydo":
        name_blyda=rzdelitel_po_probelam[1]
        cena=cena_blyd(name_blyda)
        dobavlenie_v_kozine(str(clic.message.chat.id), name_blyda, cena, 1)  
    
    
    
    
    
    
    if rzdelitel_po_probelam[0]=="+":
        dobavlenie_v_kozine(str(clic.message.chat.id), rzdelitel_po_probelam[1], 0, 1)
        bot.edit_message_text("вот карзина", clic.message.chat.id, clic.message.message_id,  reply_markup=knopka_s_blydami_v_karzine(clic.message.chat.id) )
    elif rzdelitel_po_probelam[0]=="-":
        
        
        dobavlenie_v_kozine(str(clic.message.chat.id), rzdelitel_po_probelam[1], 0, -1)
        fail=open("infa.json", "r", encoding="UTF-8")
        slovar=json.load(fail)
        info_pol=slovar[str(clic.message.chat.id)]
        korzina_pol=info_pol["korzina"]
        if len(korzina_pol)!=0:
            
            bot.edit_message_text("вот карзина", clic.message.chat.id, clic.message.message_id,  reply_markup=knopka_s_blydami_v_karzine(clic.message.chat.id) )
        else:
            bot.edit_message_text("а тут нечего нет", clic.message.chat.id, clic.message.message_id,   )
    
    
    
    
    
    if rzdelitel_po_probelam[0]=="x":
        
        
        nazvanie_blyda=rzdelitel_po_probelam[1]
        fail=open("infa.json", "r", encoding="UTF-8")
        slovar=json.load(fail)
        slovar_pol=slovar[str(clic.message.chat.id)]
        korzina_pol=slovar_pol["korzina"]
        fail.close()
        
        del korzina_pol[nazvanie_blyda]
        if len(korzina_pol)!=0:
            fail=open("infa.json", "w", encoding="UTF-8")
            json.dump(slovar, fail, ensure_ascii=False, indent=4)
            fail.close()
        
            
            bot.edit_message_text("вот корзина", clic.message.chat.id, clic.message.message_id,  reply_markup=knopka_s_blydami_v_karzine(clic.message.chat.id) )
        else:
            bot.edit_message_text("у вас нечего нет", clic.message.chat.id, clic.message.message_id   )
    
    
    
    
    
    if rzdelitel_po_probelam[0]=="zakaz":
        chek_pol=ceheki(str(clic.message.chat.id))
        knopki=telebot.types.InlineKeyboardMarkup()
        knopka_ok=telebot.types.InlineKeyboardButton("✅", callback_data="ok")
        knopka_no=telebot.types.InlineKeyboardButton("🚫", callback_data="no")
        knopki.add(knopka_no, knopka_ok)
        bot.send_message(clic.message.chat.id, chek_pol, reply_markup=knopki)
    
    
    
    
    if rzdelitel_po_probelam[0]=="ok":
        
        bot.send_message(clic.message.chat.id, "ваше имя")
        bot.register_next_step_handler_by_chat_id(clic.message.chat.id, ima_pol )
    
    
    
    
    if rzdelitel_po_probelam[0]=="no":
        fail=open("infa.json", "r", encoding="UTF-8")
        slovar=json.load(fail)
        slovar_pol=slovar[str(clic.message.chat.id)]
        korzina_pol=slovar_pol["korzina"]
        fail.close()
        if len(korzina_pol)==0:
            bot.send_message(clic.message.chat.id, "у вас нечего нет" )
        else:
            bot.send_message(clic.message.chat.id, "вот карзина",    reply_markup=knopka_s_blydami_v_karzine(clic.message.chat.id) )











def knopka ():
    
    spisok_knopok=telebot.types.ReplyKeyboardMarkup()
    knopka_1=telebot.types.KeyboardButton("меню")
    knopka_2=telebot.types.KeyboardButton("корзина")
    spisok_knopok.add(knopka_1, knopka_2)
    return spisok_knopok



def dobavlenie_v_kozine(Id, blydo, cena, kolicestvo):
    fail=open("infa.json", "r", encoding="UTF-8")
    slovar_infor=json.load(fail)
    if Id not in slovar_infor:
        slovar_infor[Id]={"neme":"", "nomer":"","adres":"", "korzina":{blydo:[cena, kolicestvo ]}}
    else:
        inform_o_polzav=slovar_infor[Id]
        korzina_pol=inform_o_polzav["korzina"]
        if blydo in korzina_pol:
            bludo_pol=korzina_pol[blydo]
            bludo_pol[1]=bludo_pol[1]+kolicestvo
            if bludo_pol[1]==0:
                del korzina_pol[blydo]
        else:
            korzina_pol[blydo]=[cena, kolicestvo]
    fail.close()
    fail=open("infa.json", "w", encoding="UTF-8")
    json.dump(slovar_infor, fail, ensure_ascii=False, indent=4)
    fail.close()

  



def ceheki(id):
    fail=open("infa.json", "r", encoding="UTF-8")
    
    slovar=json.load(fail)
    slovar_pol=slovar[id]
    korzina_pol=slovar_pol["korzina"]
    fail.close()
    chek=" "
    itog_chena=0
    for nazvanie_blyda in korzina_pol:
        
        spisok_indor_blyd=korzina_pol[nazvanie_blyda]
        
        cena_s_text=spisok_indor_blyd[0]
        rzdelitel_po_probelam=cena_s_text.split(" ")
        cena=int(rzdelitel_po_probelam[0])
        
        colicestvo=spisok_indor_blyd[1]
        cena_v_obcem_blyda=cena*colicestvo
        info_o_blyde=nazvanie_blyda+", "+str(colicestvo)+"* "+str(cena)+"= "+str(cena_v_obcem_blyda)+"\n"
        chek=chek+info_o_blyde
        itog_chena=cena_v_obcem_blyda+itog_chena
    chek=chek+"\n\n"+"итог  "+str(itog_chena)
    return chek




def knopka_s_blydami_v_karzine(id):
    
    fail=open("infa.json","r", encoding="UTF-8" )
    slovar=json.load(fail)
    fail.close()
    slovar_polzovatela=slovar[str(id)]
    korzina_pozovatela=slovar_polzovatela["korzina"]
    knopki=telebot.types.InlineKeyboardMarkup()
    for nazvanie_blyd in korzina_pozovatela:
        colicesta_zakaza_in_cena=korzina_pozovatela[nazvanie_blyd]
        knopka_ydlit=telebot.types.InlineKeyboardButton("❌", callback_data="x_"+nazvanie_blyd)
        knopka_plys=telebot.types.InlineKeyboardButton("➕", callback_data="+_"+nazvanie_blyd)
        knopka=telebot.types.InlineKeyboardButton(nazvanie_blyd+"="+str(colicesta_zakaza_in_cena[1]),callback_data="blua_karzina" )
        knopka_minys=telebot.types.InlineKeyboardButton("➖", callback_data="-_"+nazvanie_blyd)
        knopki.add( knopka_minys, knopka, knopka_plys, knopka_ydlit)
    knopka_zakazat=telebot.types.InlineKeyboardButton("заказать", callback_data="zakaz")
    knopki.add(knopka_zakazat)
    return knopki
    








































bot.polling()
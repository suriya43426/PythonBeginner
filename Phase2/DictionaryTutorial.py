# list , tuple
lis=["สีแดง","สีเหลือง","สีเขียว"]
tup=("สีแดง","สีเหลือง","สีเขียว")

#dictionary => key (การเข้าถึงข้อมูล), value (ค่าของข้อมูล)

market={
    "ร้านป้าพร":{
        "name":"ป้าพร",
        "menu":["กะเพราไก่","ก๋วยเตี๋ยว"],
        "zone":'ตะวันออก'
    },
    "ร้านลุงป้อม":{
        "name":"น้าจ๊อบ",
        "menu":["มะม่วง","ทุเรียน"],
        "zone":'ทางเข้าตลาด'
    },
    "ร้านน้าใจ":{
        "name":"น้าใจ",
        "menu":["นมปั่น","ชาเย็น"],
        "zone":'ข้าง 7-11'
    }
}

if "ทุเรียน" in market["ร้านป้าพร"]["menu"]:
    print("เป็น")
else :
    print("ไม่เป็น")

from flask import Flask, render_template, request
import pymongo
app = Flask('app')

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]

basliklar = []


@app.route('/')
def home_page():
    dosya = open("sozluk_dosyalar/basliklar.txt", "r", encoding="utf-8")
    dosyadan_basliklar = dosya.readlines()
    basliklar.clear()

    for b in dosyadan_basliklar:
        parcalar = b.split("|")
        basliklar.append(
            {
                "id": parcalar[0],
                "baslik": parcalar[1],

            }

        )
    return render_template("ana_sayfa.html", basliklar=basliklar)


@app.route("/baslik/<baslik_id>")
def baslik_goster(baslik_id):
    mycol =mydb["yazilar"]
    veritabanindan_yazilar = list(mycol.find({"baslik_id": int(baslik_id)}))

    baslik_tablosu = mydb["basliklar"]
    baslik_kaydi = baslik_tablosu.find_one({"id": int(baslik_id)})
    baslik_metin = baslik_kaydi["baslik"]
    return render_template("baslik_icerik.html", baslik=baslik_metin, yazilar=veritabanindan_yazilar, baslik_id=baslik_id)

@app.route('/yazi-ekle',methods = ["POST"])
def yazi_ekle():
    baslik_id = request.form.get('txtBaslikId')
    yazi = request.form.get('txtYazi')

    mycol = mydb["yazilar"]
    yeni_yazi = {"baslik_id":int(baslik_id),"yazi": yazi}
    x = mycol.insert_one(yeni_yazi)
    

    return render_template("baslik_icerik.html", baslik=baslik_metin, yazilar=veritabanindan_yazilar, baslik_id=baslik_id)


app.run(debug=True, host='0.0.0.0', port=5000)

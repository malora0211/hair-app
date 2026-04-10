from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def home():
    return '''
    <h2>🌿 نظام تكثيف الشعر - 8 أسابيع</h2>
    <form action="/result">
        اسمك: <input name="name"><br><br>
        نوع شعرك:
        <select name="hair">
            <option>دهني</option>
            <option>جاف</option>
            <option>مختلط</option>
        </select><br><br>
        مشكلتك:
        <select name="problem">
            <option>تساقط</option>
            <option>فراغات</option>
            <option>ضعف</option>
        </select><br><br>
        <button type="submit">احصلي على خطتك</button>
    </form>
    '''

@app.route('/result')
def result():
    name = request.args.get("name")
    hair = request.args.get("hair")
    problem = request.args.get("problem")

    plan = ""

    if hair == "دهني":
        plan += "✔️ اغسل شعرك 3 مرات أسبوعياً<br>"
    elif hair == "جاف":
        plan += "✔️ استخدم زيت الخروع + ترطيب<br>"
    else:
        plan += "✔️ روتين متوازن<br>"

    if problem == "تساقط":
        plan += "🛑 تدليك يومي<br>"
    elif problem == "فراغات":
        plan += "🔥 زيت روزماري<br>"
    else:
        plan += "💪 ماسكات تقوية<br>"

    plan += "<br>📅 خطة 8 أسابيع:<br>"

    for week in range(1, 9):
        plan += f"الأسبوع {week}: التزام بالروتين<br>"

    return f"<h3>✨ أهلاً {name}</h3><p>{plan}</p>"

app.run()

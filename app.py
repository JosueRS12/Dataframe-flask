from flask import Flask, render_template, request
from src.services.CovidService import CovidService


app = Flask(__name__)

@app.route("/")
def home():
    covidService = CovidService()
    showAll = covidService.showDataFrame()
    return render_template('index.html', showAll = showAll)

@app.route("/maxByTypeVac", methods=['POST'])
def byMax():
    covidService = CovidService()
    showAll = covidService.showDataFrame()
    if request.method == 'POST':
        typeVac = request.form.get('typeVac')
        res = covidService.maxByTypeVac(typeVac)
        name = f"Con mayor cantidad de vacunas {typeVac}"
    return render_template('service.html', showAll = showAll, res = res,
                           name=name)

@app.route("/byCount", methods=['POST'])
def byCount():
    covidService = CovidService()
    showAll = covidService.showDataFrame()
    if request.method == 'POST':
        count = request.form.get('byCount')
        res = covidService.byCountVaccines(count)
        name = f"por cantidad > {count}"
    return render_template('service.html', showAll = showAll, res = res,
                           name=name)

@app.route("/byColVal", methods=['POST'])
def byColVal():
    covidService = CovidService()
    showAll = covidService.showDataFrame()
    name = "por columna y valor expecíficos"
    if request.method == 'POST':
        col = request.form.get('byCol')
        val = request.form.get('byVal')
        res = covidService.byColumnValue(col, val)
    return render_template('service.html', showAll = showAll, res = res,
                           name=name)

@app.route("/byColumn", methods=['POST'])
def byColumn():
    covidService = CovidService()
    showAll = covidService.showDataFrame()
    name = "por Columna"
    if request.method == 'POST':
        col = request.form.get('byCol')
        res = covidService.byColumn(col)
    return render_template('service.html', showAll = showAll, res = res,
                           name=name)

@app.route("/byField", methods=['POST'])
def byField():
    covidService = CovidService()
    showAll = covidService.showDataFrame()
    name = "por Campo específico"
    if request.method == 'POST':
        field = request.form.get('byField')
        res = covidService.byValueTerritory(field)
    return render_template('service.html', showAll = showAll, res = res, name = name)

if __name__ == "__main__":
    app.run(debug=True)

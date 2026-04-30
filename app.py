from flask import Flask, render_template, request, send_file
import pandas as pd
import time
from algorithms import quick_sort, merge_sort, counting_sort, radix_sort

app = Flask(__name__)
results = []

@app.route("/", methods=["GET", "POST"])
def index():
    global results
    if request.method == "POST":
        file = request.files["file"]
        column = request.form["column"]
        algorithm = request.form["algorithm"]
        order = request.form["order"]

        df = pd.read_csv(file)
        data = df[column].tolist()

        start = time.time()

        if algorithm == "quick":
            sorted_data = quick_sort(data)
        elif algorithm == "merge":
            sorted_data = merge_sort(data)
        elif algorithm == "counting":
            sorted_data = counting_sort(data)
        elif algorithm == "radix":
            sorted_data = radix_sort(data)
        else:
            sorted_data = data

        if order == "desc":
            sorted_data.reverse()

        end = time.time()
        exec_time = round((end - start) * 1000, 2)

        df[column] = sorted_data
        output_path = "sorted.csv"
        df.to_csv(output_path, index=False)

        results.append({
            "algorithm": algorithm,
            "time": exec_time,
            "type": "Comparativo" if algorithm in ["quick","merge"] else "No comparativo"
        })

        return render_template("index.html", columns=df.columns, results=results, download=True)

    return render_template("index.html", columns=None, results=results, download=False)

@app.route("/download")
def download():
    return send_file("sorted.csv", as_attachment=True)

if __name__ == "__main__":
    app.run(debug=True)

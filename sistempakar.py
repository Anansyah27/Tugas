from flask import Flask, render_template, request

app = Flask(__name__)

# Halaman utama yang hanya menampilkan home.html
@app.route("/")
def home_page():
    return render_template("home.html")

# Halaman untuk menampilkan pertanyaan
@app.route("/questions", methods=["GET", "POST"])
def questions_page():
    if request.method == "POST":
        # Ambil data yang dikirimkan oleh form
        answers = request.form.to_dict()
        # Proses jawaban untuk mendapatkan hasil
        result = process_answers(answers)
        return render_template("result.html", result=result)
    return render_template("questions.html")

def process_answers(answers):
    # Fungsi untuk memproses jawaban dan menghasilkan hasilnya
    minat = {
        'kreatif': [],
        'olahraga': [],
        'riset': [],
        'pramuka': []
    }

    # Menyortir jawaban ke kategori yang sesuai
    for question, answer in answers.items():
        if answer == 'ya':
            if question in ['menulis', 'membaca', 'membuat_buku', 'mahir_artikel', 'menggambar', 'seni_budaya']:
                minat['kreatif'].append(question)
            elif question == 'olahraga':
                minat['olahraga'].append(question)
            elif question == 'riset':
                minat['riset'].append(question)
            elif question == 'pramuka':
                minat['pramuka'].append(question)

    # Menghasilkan hasil berdasarkan jawaban
    result = []
    if minat['kreatif']:
        result.append("Kreatif (Menulis, Membaca, Menggambar, Seni Budaya, dll)")
    if minat['olahraga']:
        result.append("Olahraga")
    if minat['riset']:
        result.append("Riset dan Penelitian")
    if minat['pramuka']:
        result.append("Pramuka")

    if not result:
        return "Tidak ada minat yang kuat terdeteksi."
    return ", ".join(result)

if __name__ == "__main__":
    app.run(debug=True)

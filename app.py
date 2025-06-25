from flask import Flask, render_template, request, make_response
from weasyprint import HTML

app = Flask(__name__)

@app.route('/download', methods=['POST'])
def download():
    data = request.form
    template_name = data.get('template', 'classic')

    rendered = render_template(f'{template_name}.html', data=data, preview=False)
    pdf = HTML(string=rendered).write_pdf()
    response = make_response(pdf)
    response.headers['Content-Type'] = 'application/pdf'
    response.headers['Content-Disposition'] = 'attachment; filename=resume.pdf'
    return response

@app.route('/')
def form():
    return render_template('forms.html')

@app.route('/resume', methods=['POST'])
def resume():
    data = request.form
    data = data.to_dict()
    template_name = data.get('template', 'classic')
    return render_template(f'{template_name}.html', data=data, preview=True)  

if __name__ == '__main__':
    app.run(debug=True)
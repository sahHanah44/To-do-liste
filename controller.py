from flask import Flask, render_template, request, redirect, url_for
import model

app = Flask(__name__)

@app.route('/')
def index():
    todo = model.afficher_la_liste()
    return render_template('index.html', todo = todo)

@app.route('/update', methods=['POST'])
def update():
    tache =  request.form['tache']
    description = request.form['description']
    model.update(tache, description)
    return redirect(url_for('index'))

@app.route('/coche/<int:todo_id>', methods=['POST'])
def cocher(todo_id):
    model.cocher(id=todo_id)
    return redirect(url_for('index'))

@app.route('/modifier/<int:todo_id>', methods=['POST'])
def modifier_TD(todo_id):
    tache =  request.form['tache']
    description = request.form['description']
    model.modifier(tache, description, id= todo_id)
    return redirect("/")

@app.route('/delete/<int:todo_id>')
def delete(todo_id):
    model.delete(id=todo_id)
    return redirect(url_for('index'))



if __name__ == '__main__':
    model.tab()  # Crée la table si elle n'existe pas
    app.run(debug=True)
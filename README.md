# To-Do App

![Python](https://img.shields.io/badge/Python-3.11-blue)
![Flask](https://img.shields.io/badge/Flask-Framework-red)
![Docker](https://img.shields.io/badge/Docker-Ready-blue)

Piccola e semplice applicazione To-Do realizzata con **Flask**, che consente di gestire attività direttamente da browser in modo leggero e veloce.  

---

## Funzionalità principali

- Aggiunta nuova attività
- Blocco dei duplicati
- Segna attività come completate/non completate
- Filtri: Tutte | Da fare | Completate
- Conteggio: da fare, completate, totali
- Pulizia attività completate

---

## Demo online

https://todo-app-02vw.onrender.com

---

## Avvio con Docker

```
docker build -t todo-app .
docker run -p 5000:5000 todo-app
```

Apri il browser:  
http://localhost:5000

---

## Avvio locale

```
pip install -r requirements.txt
python app.py
```

Apri il browser:  
http://localhost:5000

---

## Tecnologie utilizzate

- Python + Flask
- HTML / CSS (Jinja2)
- File JSON per storage locale
- Docker per containerizzazione

---

**Autrice:** Concetta Rubino

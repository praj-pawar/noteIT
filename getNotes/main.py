from website import create_app

app=create_app()

if __name__=='__main__':                   #if makes sure app created only when main.py is ran and not just imported
    app.run(debug=True)

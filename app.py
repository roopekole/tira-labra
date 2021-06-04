from src import app

#app.logger.addHandler(logging.StreamHandler(sys.stdout))
#app.logger.setLevel(logging.ERROR)


if __name__ == '__main__':
    app.secret_key = '12345'
    app.run(debug=True)
from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

kwiat_jabloni1 = {
    "performer": "Kwiat Jabłoni", "albums": ("Moglo byl nic", "Niemozliwe"),
    "songs": ({"name": "Buka", "time": "3:35", "format": ".mp3"},
              {"name": "Moglo byc nic", "time": "4:11", "format": ".mp3"},
              {"name": "Drogi proste", "time": "3:55", "format": ".mp3"},
              {"name": "Byle jak", "time": "4:20", "format": ".mp3"},
              {"name": "Nie ma mnie", "time": "3:33", "format": ".mp3"},
              {"name": "Kometa", "time": "3:37", "format": ".mp3"},
              {"name": "Zaczniemy od zera", "time": "4:01", "format": ".mp3"},
              {"name": "Maska", "time": "4:08", "format": ".mp3"},
              {"name": "Bankiet", "time": "3:59", "format": ".mp3"},
              {"name": "Wyjscie z bankietu", "time": "2:11", "format": ".mp3"},
              {"name": "Przezroczysty swiat", "time": "4:13", "format": ".mp3"},
              {"name": "Idzie zima", "time": "3:45", "format": ".mp3"})
}


class Songs(Resource):
    def get(self):
        return kwiat_jabloni1


api.add_resource(Songs, '/')

if __name__ == '__main__':
    app.run(debug=True)

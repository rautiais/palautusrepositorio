from urllib import request
from project import Project
import toml

class ProjectReader:
    def __init__(self, url):
        self._url = url

    def get_project(self):
        # tiedoston merkkijonomuotoinen sisältö
        content = request.urlopen(self._url).read().decode("utf-8")
        print(content)
        # deserialisoi TOML-formaatissa oleva merkkijono ja muodosta Project-olio sen tietojen perusteella
        parsed_toml = toml.loads(content)
        lista_a = []
        if "dependencies" in parsed_toml["tool"]["poetry"]:
            for i in parsed_toml["tool"]["poetry"]["dependencies"]:
                lista_a.append(i)
     
        lista_b = []
        if "dev-dependencies" in parsed_toml["tool"]["poetry"]:
            for i in parsed_toml["tool"]["poetry"]["dev-dependencies"]:
                lista_b.append(i)

        print(parsed_toml)

        return Project(parsed_toml["tool"]["poetry"]["name"], parsed_toml["tool"]["poetry"]["description"], lista_a, lista_b)

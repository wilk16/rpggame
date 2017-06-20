import pickle


def save(hero):
    with open('.//save//save.json', 'wb') as outfile:
        pickle.dump(hero, outfile)


def load():
    with open('.//save//save.json', 'wb') as outfile:
        hero = pickle.load(outfile)
        return hero

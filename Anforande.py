class Anforande:
    def __init__(self, filnamn, parti, ledamot, text, år):
        self.filnamn = filnamn
        self.parti = parti
        self.ledamot = ledamot
        self.text = text
        self.år = år

    def get_parti(self):
        return self.parti

    def get_datum(self):
        return self.datum

    def get_ledamot(self):
        return self.ledamot

    def get_text(self):
        return self.text



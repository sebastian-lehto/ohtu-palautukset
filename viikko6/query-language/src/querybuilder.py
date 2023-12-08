from matchers import And, HasAtLeast, PlaysIn, Or, HasFewerThan, All

class QueryBuilder:

    def __init__(self, query = All()):
        self.query = query
    
    def build(self):
        return self.query

    def playsIn(self, team):
        return QueryBuilder(And(self.query, PlaysIn(team)))

    def hasAtLeast(self, attr, value):
        return QueryBuilder(And(self.query, HasAtLeast(attr, value)))

    def hasFewerThan(self, attr, value):
        return QueryBuilder(And(self.query, HasFewerThan(attr, value)))

    def oneOf(self, q1, q2):
        return QueryBuilder(Or(q1, q2))
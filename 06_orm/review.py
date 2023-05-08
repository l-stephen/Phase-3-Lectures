#Create a movies and actors class
#Movies should have a title, and actors should have a name
class Movies:
    def __init__(self,title):
        self.title = title
        pass
class Actors:
    def __init__(self,name):
        self.name = name
        pass
#Join actors and movies on a credits object
#Credits should be initialized with a movie and actor, only if the type is movies and actors
#Create a method to delete the credits
class Credits:
    def __init__(self,movie,actor):
        if type(movie) is Movies and type(actor) is Actors:
            self.movie = movie
            self.actor = actor
    def delself(self):
        print("Deleting")
        del self.actor

avatar = Movies("Avatar")
cocainebear = Movies("Cocaine Bear")
spacebear = Actors("Space Bear")
bear1 = Credits(avatar,spacebear)
bear2 = Credits(cocainebear,spacebear)

bear1.delself()
#print(bear1.actor.name)
print(bear2.actor.name)
#Review Sql Basics and running a seeds file
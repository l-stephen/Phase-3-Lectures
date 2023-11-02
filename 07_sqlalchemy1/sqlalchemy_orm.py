#Start with imports

#Define declarative_base()


#create a class that is a child of Base

    #create a table name

    #create models

    #create a validation

    #create a repr

#create a class that is a child of BASE

    #create a table name

    #create models

    #create a validation

    #create a repr

if __name__ == "__main__":

    #create the database engine with create_engine()

    #delete tables using .drop(engine)

    #Create the table with create_all()

    #with Session object create a session
        ''' 
        The session object will allow use to perform CRUD on our models
        Session.add()
        Session.add_all([])
        Session.query()
            .all()
            .orderby() ex: Table.name.desc()
            .limit()  ex: limit(2)
            .filter() ex Table.name = "name"
            .update() ex {Table.name: newname}
        Session.delete()
        Session.commit()
        '''
        #query all students from the database, use order_by() and sort in asc order, use limit() and all()

        #take user input for a name

        #query from the student database using user input, use filter() and first()

        #if the student exists, delete them from the session

        #commit the change!

        #else print not a student

        #take in user input to create a new student

        #add the new student to the session

        #take in user input to create a new teacher

        #add the new student to the session

        #query from database using user input

        #demonstrate add() and add_all()

        #commit the change!

















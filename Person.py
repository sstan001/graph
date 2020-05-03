class Person:

    def __init__(self, ID, state='S', contamination_day=None, confinement_mode='None', confinement_day=None):
        """
        Parameters
        ----------
        ID is a constant number which identifies a Person
        state is a character: S for Sain, M for Malade, R for Rémission, D for Décédé
        contamination_day is a constant number, the date of contamination
        confinement_mode says whether or not a Person is confined and how
        confinement_day is a constant number, the date of confinement
        """
        self.ID = ID
        self.state = state
        self.contamination_day = contamination_day
        self.confinement_mode = confinement_mode
        self.confinement_day = confinement_day
        self.current_day_contacts = []
        # self.visited = [0 for i in range(disease_time)]

    def __str__(self):
        # return "Person ID {} / state {}".format(self.ID,self.state)
        return str(self.ID)

    def __repr__(self):
        return self.__str__()

    def is_confined(self):
        return not (self.confinement_mode == 'None')

    def add_current_day_contacts(self, person):
        """ Adds person to the list of current day contacts of self. """
        self.current_day_contacts.append(person)

    def free_current_day_contacts(self):
        """ Frees the current_day_contacts of self (at the end of the day --> reset). """
        self.current_day_contacts.clear()


'''
## Update the list 'visited'
def update_visited(self, disease_time):
    for i in range(disease_time):
        if self.visited[i][1] > disease_time:
            to_delete.append(i)
        else:
            self.visited[i][1] += 1
    for k in range(len(to_delete)):
        self.visited.pop(to_delete[k])


def confine_all(self):
    for i in range(disease_time):
        self.visited[i][0].is_confined = True
        
    '''

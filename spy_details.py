#spy_name='Tushar'
#spy_salutation='mr.'
#spy_age=21
#spy_rating=5.0
#spy_online=True

#spy={'name': 'Tushar',
 #     'salutation': 'Mr.',
 #     'age': 25,
  #     'rating': 4.5,
   #    'is_online': True

class spy:
    def __init__(self,name,salutation,age,rating):
        self.name = name
        self.salutation = salutation
        self.age = age
        self.rating = rating
        self.is_online = True
        self.current_status_message =  None
        self.avg=[]
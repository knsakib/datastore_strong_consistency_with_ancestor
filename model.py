from google.appengine.ext import ndb



class database1(ndb.Model):
     email=ndb.StringProperty()
     message=ndb.StringProperty()
     last_touch_date_time = ndb.DateTimeProperty(auto_now=True) #auto_now=true is telling constructor to keep track of dtate of time
     
     
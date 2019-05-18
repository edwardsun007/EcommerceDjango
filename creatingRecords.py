# from apps.ecommerce.models import *
# from ..models import Product
from apps.products.models import Product
from django.db import connection, transaction  # -- This works!!!!
import datetime
# import bcrypt
import django
import sys
import os
# find this setting project directory wsgi.py file
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ecommerce.settings")
# project root directory
sys.path.append('/Volumes/Develop/Django/djanEcomEnv')
django.setup()
print('passed here')
# your imports, e.g. Django models # change it to your app name

'''
Remember these imports are necessary for running customized script from anywhere 
'''

if __name__ == '__main__':
    # print ('All users:')
    # users = User.objects.all()
    # print(users)

    # search
    # items = Item.objects.all()
    # for item in items:
    #     print('*********************************************')
    #     print(item)

    ps = Product.objects.all()
    print('*****************')
    print(ps)
    print('*****************')
    # Item.objects.create(model_number='a51600',
    # manufacturer='amd',
    # name="AMD Ryzen 5 1600 3.2 GHz 6-Core Processor - 19 MB - Socket AM4Intel 8th Gen Core i5-8600K",
    # description="Bank on solid, efficient computing performance with this six-core AMD Ryzen 5 desktop processor. Its 3.6GHz maximum turbo core speed sufficiently supports 1080p and VR gaming, and its 16MB L3 cache memory provides an enhanced CPU memory operation. The 65W default thermal design power of this AMD Ryzen 5 desktop processor lets you build a power-efficient computer system. 19 MB CacheSocket AM46 Cores/12 threads",
    # rating=4.5,
    # price=179.99,
    # item_type="cpu",
    # picture="../../static/amd_a51600.jpg")
    # Item.objects.create(
    # model_number='vega64',
    # manufacturer='amd',
    # name="AMD Radeon RX Vega 64 8 GB",
    # description="High resolution gaming, maximum frame rates, intense visuals, and cutting edge technologies – Radeon RX Vega graphics is designed for extreme gaming.",
    # rating=3,
    # price=700,
    # item_type="gpu",
    # picture="../../static/amd_vega64.png")

    # Item.objects.create(
    # model_number='f43200c',
    # manufacturer='gskill',
    # name="G.SKILL TridentZ RGB Series 32GB (4 x 8GB) 288-Pin DDR4",
    # description="The Ultimate DDR4 Just Got Better! Featuring a completely exposed light bar with vibrant RGB LEDs, merged with the award-winning Trident Z heatspreader designed, and constructed with the highest quality components, the Trident Z RGB DDR4 memory kit combines the most vivid RGB lighting with uncompromised performance.",
    # rating=5,
    # price=399.99,
    # item_type="ram",
    # picture="../../static/gskill_tridentz.png")

    # first = Item.objects.first()
    # print(first.name)
    # print(first.price)
    # print(first.description)

    #coco = User.objects.get(id=3)
    # Job.objects.create(name='Replace light bulbs',desc="replace the bulb simply and easy!", location="1920 zanker road, San Jose, CA 95116",poster=poster)
    # Job.objects.create(name='Mow lawn',desc="Mow lawn!", location="1920 zanker road, San Jose, CA 95116",poster=poster)
    # Job.objects.create(name='Clean Garage',desc="Clean Garage!", location="1920 zanker road, San Jose, CA 95116",poster=poster)
    # Job.objects.create(name='Paint Fence',desc="Paint Fence!", location="1920 zanker road, San Jose, CA 95116",poster=poster)
    # Job.objects.create(name='Walk a dog',desc="Walk a dog!", location="1920 zanker road, San Jose, CA 95116",poster=poster)

    # this_job.poster = poster
    # print(Job.objects.last().poster)
    # this_job.accepter = me
    # this_job.save()
    # this_job.accepter.add(me)

    # print('accetped job id:')
    # print(me.accepted_jobs.all()[0].id)

    # print('other job:')
    # print(Job.objects.exclude(me.accepted_jobs.all()))
    # print(me.add_jobs.filter(id=1))
    # print(this_job.poster)
    # this_job.taker.add(me)
    # this_job.save()
    # me.save()
    # print(me.add_jobs)
    # cmt = "Agreed From Dane!"
    # Dane = User.objects.get(id=3)
    # msg = Message.objects.get(id=1)
    # Comment.objects.create(comment=cmt,user=Dane,message=msg)

    # cmtTM = datetime.datetime(2018,5,15,13,15,5)
    # cmt = Comment.objects.last()
    #text = "Once you joined Coding Dojo, forget about having a life for 3 months, LOL T.T"
    # cmt.created_at=cmtTM
    # cmt.save()
    # print(Message.objects.last())

    #message = Message.objects.last()
    #message.message="You want to be good at something first you need be interested in it, rule of thumb! "
    #message.created_at = msgtm
    # message.save()
    # user.first_name = 'Brand'
    # user.last_name = 'Guy'
    # user.save()

    # result = bcrypt.checkpw('$2b$12$FQE.GjVH73LxmjRtwhNG0.NwD0c5kMHUf9V1bWb8yUd2RyiKeoYtu'.encode(),user.password.encode())
    # print(result)
    #results= User.objects.raw("SELECT * FROM Users_User ORDER BY create_at DESC")
    # print(results[0].first_name)

    # last = User.objects.get(id=3)
    # last.last_name = "conquer"
    # last.save()

    #email = 'newguy@123.net'
    # try:
    #     User.objects.get(email_address=email)
    # except DoesNotExist as e:
    #     print('New guy!')

    # Dojos.objects.create(name='CDSV',city='SanJose', state='CA')
    # Dojos.objects.create(name='CDSEA',city='Seattle', state='WA')
    # Dojos.objects.create(name='CDNY',city='New York', state='NY')

    # results = Dojos.objects.all()
    # print(results)

    # Ninjas.objects.create(dojo_id=Dojos.objects.get(id=1),first_name='Neva Giveup', last_name='Neva Stop')
    # Ninjas.objects.create(dojo_id=Dojos.objects.get(id=1),first_name='Shawn', last_name='Shane')
    # Ninjas.objects.create(dojo_id=Dojos.objects.get(id=1),first_name='Go', last_name='big')

    # results = Ninjas.objects.all()
    # print(results)

    # results = Dojos.objects.get(id=5).ninjas.all()
    # print(results)

    # first_nin=Ninjas.objects.first().dojo_id
    # print(first_nin)

    # Dojos.objects.create(name='CDSC',city='Sin City', state='NV')
    # Dojos.objects.create(name='CDFE',city='For Evil', state='CA')
    # Dojos.objects.create(name='CDSA',city='San Antonio', state='TA')

    # Ninjas.objects.create(dojo_id=Dojos.objects.get(id=3),first_name='Pudge', last_name='Hook')
    # Ninjas.objects.create(dojo_id=Dojos.objects.get(id=4),first_name='Invoker', last_name='Magic')
    # Ninjas.objects.create(dojo_id=Dojos.objects.get(id=5),first_name='Seven', last_name='Tank')
    # Author.objects.create(first_name='Master',last_name='C#',email='c#@gmail.com')
    # Author.objects.create(first_name='Master',last_name='C#One',email='c#1@gmail.com')
    # Author.objects.create(first_name='Master',last_name='C#Two',email='c#2@gmail.com')
    # Author.objects.create(first_name='Master',last_name='JAVA',email='JAVA@gmail.com')
    # Author.objects.create(first_name='Master',last_name='Python',email='PY@gmail.com')
    # Author.objects.create(first_name='Master',last_name='PHP',email='PHP@gmail.com')
    # Author.objects.create(first_name='Master',last_name='Ruby',email='Ruby@gmail.com')
    # Book.objects.create(name='C Sharp',desc='C#')
    # print('after create book')
    # author_one = Author.objects.get(last_name='C#One')
    # print(author_one)
    # Book.objects.get(id=1).authors.add(author_one)

    # result=
    # this_author = Author.objects.get(id=2)
    # print(this_author)
    # this_book = Book.objects.get(id=1)
    # this_book.authors.add(this_author)

    # another_author = Author.objects.get(id=3)
    # this_book.authors.add(another_author)
    # print(this_book.authors.all())

    # Author.objects.create(first_name='Mike',last_name='TeachC#',email='MY@gmail.com')
    # Author.objects.create(first_name='Speros',last_name='TeachJAVA',email='Speros@gmail.com')
    # Author.objects.create(first_name='John',last_name='TeachPython',email='John@gmail.com')
    # Author.objects.create(first_name='Jadee',last_name='TeachPHP',email='Jadee@gmail.com')
    # Author.objects.create(first_name='Jay',last_name='TeachRuby',email='Jay@gmail.com')

    # Book.objects.create(name='Python',desc='py')
    # Book.objects.create(name='JAVA',desc='Java')
    # Book.objects.create(name='PHP',desc='php')
    # Book.objects.create(name='Ruby',desc='ruby')
    # first_author = Author.objects.get(id=1)
    # third_author = Author.objects.get(id=3)
    # third_book = Book.objects.get(id=3)
    # second_book = Book.objects.get(id=2)

    # first_book.authors.add(first_author)
    # second_book.authors.add(first_author)
    # Author.objects.raw("UPDATE book_authors_Author SET first_name='Ketual' WHERE id=5")
    # third_book.authors.add(third_author)
    # print(first_book.authors.all())
    # print(second_book.authors.all())
    # print(third_book.authors.all())

    # User.objects.create(first_name='John',last_name='Hannson',email='jh@gmail.com')
    # User.objects.create(first_name='Shawn',last_name='Dawn',email='sd@gmail.com')
    # User.objects.create(first_name='Travy',last_name='Vestica',email='tv@gmail.com')
    # User.objects.create(first_name='John', last_name='Conner', email_address='jc@gmail.com', age=100)
    # User.objects.create(first_name='Steve', last_name='Nash', email_address='sn@gmail.com' , age=50)
    # User.objects.create(first_name='Magic', last_name='Johnson', email_address='mj@gmail.com' , age=50)
    # User.objects.create(first_name='Tracy', last_name='McGrady', email_address='T-Mac@gmail.com' , age=50)

    # u=User.objects.get(id=3)
    # u.raw("UPDATE User SET first_name='Lebron' WHERE id=3")

    # u.first_name = first_name
    # u.last_name = last_name
    # u.email_address = email
    # u.save()

    #raw('UPDATE User SET first_name=%s,last_name=%s,email_address=%s WHERE id=%s',[request.POST['first_name'],request.POST['last_name'],request.POST['email'],number])

    #results= User.objects.filter(created_at__gte='2018-06-21')
    # print(results)
    # cursor = connection.cursor()
    # cursor.execute("DELETE FROM user_login_User WHERE id=0;")
    #cursor.execute("SELECT * FROM user_login_User WHERE created_at > '2018-06-19';")
    # transaction.commit()
    #row = cursor.fetchall()
    # print(row)  # this works, so lets stay the fuck on cursor for fuck sake!
    # print(User.objects.all())
    # transaction.commit()
    # results = User.objects.filter(created_at__gr='2016-6-18')
    # print(results)
    #results = user_login.objects.all()
    # print(results)
    # Book.objects.create(name='GiantStory',desc='kb',uploader=uone)
    # Book.objects.create(name='Adventure',desc='ADJungle',uploader=utwo)
    # Book.objects.create(name='GoneWithTheWind',desc='GWTW',uploader=uthree)
    # bone.liked_users.add(uone)
    # btwo.liked_users.add(utwo)
    # btwo.liked_users.add(uone)
    # b3.liked_users.add(uone)
    # b3.liked_users.add(utwo)
    # b3.liked_users.add(uthree)

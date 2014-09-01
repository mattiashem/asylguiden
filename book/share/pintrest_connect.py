


from pinata.client import PinterestPinata

pinata = PinterestPinata(email='matte.hemmingsson@gmail.com', password='EkJ1LmqFMi6ktylQrIIU', username='mattehemmingsso')
#pinata.create_board(name='my test board', category='food_drink', description='my first board')
pinata.pin(board_id='423690346132858544', description='New articel on asylguiden with photot', image_url='http://www.asylguiden.se/static/image', link="http://www.asylguiden.se/book/post/id")
#print pinata.boards(username='mattehemmingsso')
#pinata.pin()
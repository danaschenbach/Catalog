from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
 
from database_setup import Category, Base, Item, Username
 
engine = create_engine('sqlite:///catalog.db')
Base.metadata.bind = engine
 
DBSession = sessionmaker(bind=engine)
session = DBSession()
user = Username(id = "1", name = "Bob", email = "danasch@yahoo.com")
#Items for Backyard
category1 = Category(user=user, name = "Backyard")

session.add(category1)
session.commit()

Item1 = Item(user=user, name="BBQ PIT", description="200 inch grill with 20,000 btu burners", price="$126.99", category=category1)

session.add(Item1)
session.commit()

Item2 = Item(user=user, name="Volley Ball", description="Standered size net with poles and 2 balls", price="$150.00", category=category1)

session.add(Item2)
session.commit()

#Items for kitchen
category2 = Category(user=user, name="Kitchen")

session.add(category2)
session.commit()


Item1 = Item(user=user, name="Super Duper Juicer", description="Pick your choice of color, this juicer will handle the tuffest foods & turn them into sweet juice", price="$300.00", category=category2)

session.add(Item1)
session.commit()

Item2 = Item(user=user, name="Mixing Bowls", description="Stackable bowls, comes 12 to a pack, with lids", price="$25.00", category=category2)

session.add(Item2)
session.commit()

#Items for Bath
category3 = Category(user=user, name="Bath")

session.add(category3)
session.commit()


Item1 = Item(user=user, name="Quality Towles", description="Soft plush towels that could dry an elephant", price="$24.00", category=category3)

session.add(Item1)
session.commit()

Item2 = Item(user=user, name="Despenser", description="A 3 in 1 despenser, that handles body soap, shampoo & conditioner", price="$15.99", category=category3)

session.add(Item2)
session.commit()

#Items for Automotive
category4 = Category(user=user, name="Automotive")

session.add(category4)
session.commit()


Item1 = Item(user=user, name="Head lights", description="Powerful beams of light to see your way home", price="$69.99", category=category4)

session.add(Item1)
session.commit()

Item2 = Item(user=user, name="Car Air freshner", description="Air freshner will remove even the stinkiest of oders", price="$9.99", category=category4)

session.add(Item2)
session.commit()

#Items for Electronics
category5 = Category(user=user, name = "Electronics")

session.add(category5)
session.commit()


Item1 = Item(user=user, name = "Stereo", description="2000watt 6.2 surround", price="$560.00", category=category5)

session.add(Item1)
session.commit()

Item2 = Item(user=user, name="Akai professional speakers", description="300watt peak handeling, 12in. subwoofer, 6in mid & 1in tweeter", price="$400.00 per", category=category5)

session.add(Item2)
session.commit()

#Items for Kids
category6 = Category(user=user, name="Kids")

session.add(category6)
session.commit()


Item1 = Item(user=user, name="Building blocks", description="Blocks with brick print, come 500 to a pack", price="$100.00", category=category6)

session.add(Item1)
session.commit()

Item2 = Item(user=user, name="Play mat", description="5x6ft Play mat with road print", price="$12.99", category=category6)

session.add(Item2)
session.commit()

print "added Catalog items!"

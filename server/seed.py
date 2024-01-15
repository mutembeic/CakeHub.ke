from app import db, Category, Cake

def seed_data():
    # Create categories
    birthday_cakes = Category(name='Birthday Cakes')
    wedding_cakes = Category(name='Wedding Cakes')
    cup_cakes = Category(name='Cupcakes')

    db.session.add_all([birthday_cakes, wedding_cakes, cup_cakes])
    db.session.commit()

    # Create cakes
    cakes_data = [
        {'name': 'Chocolate Cake', 'description': 'Delicious chocolate cake', 'price': 25.0, 'category': birthday_cakes, 'image_url': 'chocolate_cake.jpg'},
        {'name': 'Vanilla Cake', 'description': 'Classic vanilla cake', 'price': 20.0, 'category': birthday_cakes, 'image_url': 'vanilla_cake.jpg'},
        {'name': 'Red Velvet Cake', 'description': 'Rich red velvet cake', 'price': 30.0, 'category': birthday_cakes, 'image_url': 'red_velvet_cake.jpg'},
        {'name': 'Wedding Bliss Cake', 'description': 'Elegant wedding cake', 'price': 40.0, 'category': wedding_cakes, 'image_url': 'wedding_bliss_cake.jpg'},
        {'name': 'Lemon Cupcake', 'description': 'Zesty lemon cupcake', 'price': 15.0, 'category': cup_cakes, 'image_url': 'lemon_cupcake.jpg'},
        {'name': 'Strawberry Shortcake', 'description': 'Fresh strawberry shortcake', 'price': 22.0, 'category': birthday_cakes, 'image_url': 'strawberry_shortcake.jpg'},
        {'name': 'Raspberry Cheesecake', 'description': 'Decadent raspberry cheesecake', 'price': 35.0, 'category': birthday_cakes, 'image_url': 'raspberry_cheesecake.jpg'},
        # Add more cakes as needed
    ]

    for cake_data in cakes_data:
        cake = Cake(**cake_data)
        db.session.add(cake)

    db.session.commit()

if __name__ == '__main__':
    # Run the seed_data function when the script is executed
    seed_data()

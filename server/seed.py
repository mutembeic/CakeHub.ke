from app import app, db, Category, Cake

def seed_data():
    with app.app_context():
        # Create categories
        birthday_cakes = Category(name='Birthday Cakes')
        wedding_cakes = Category(name='Wedding Cakes')
        cup_cakes = Category(name='Cupcakes')

        db.session.add_all([birthday_cakes, wedding_cakes, cup_cakes])
        db.session.commit()

        # Create cakes
        cakes_data = [
            {'name': 'Chocolate Cake', 'description': 'Delicious chocolate cake', 'price': 25.0, 'category': birthday_cakes, 'image_url': 'https://bluebowlrecipes.com/wp-content/uploads/2023/08/chocolate-truffle-cake-8844.jpg'},
            {'name': 'Vanilla Cake', 'description': 'Classic vanilla cake', 'price': 20.0, 'category': birthday_cakes, 'image_url': 'https://foodhub.scene7.com/is/image/woolworthsltdprod/2105-vanilla-cake:Mobile-1300x1150'},
            {'name': 'Red Velvet Cake', 'description': 'Rich red velvet cake', 'price': 30.0, 'category': birthday_cakes, 'image_url': 'https://cdn-media.indiacakes.com/media/catalog/product/cache/0b945dd31857d9e2e2ef055978ab9981/d/e/delicious-red-velvet-cake-half-kgs.webp'},
            {'name': 'Wedding Bliss Cake', 'description': 'Elegant wedding cake', 'price': 40.0, 'category': wedding_cakes, 'image_url': 'https://theperfectgift.ae/cdn/shop/products/IMG_4143.jpg?v=1684425081'},
            {'name': 'Lemon Cupcake', 'description': 'Zesty lemon cupcake', 'price': 15.0, 'category': cup_cakes, 'image_url': 'https://joyfoodsunshine.com/wp-content/uploads/2022/10/lemon-cupcakes-recipe-12-1-500x500.jpg'},
            {'name': 'Strawberry Shortcake', 'description': 'Fresh strawberry shortcake', 'price': 22.0, 'category': birthday_cakes, 'image_url': 'https://stordfkenticomedia.blob.core.windows.net/df-us/rms/media/recipemediafiles/recipes/retail/x17/2017_strawberry-shortcake_600x600.jpg?ext=.jpg'},
            {'name': 'Raspberry Cheesecake', 'description': 'Decadent raspberry cheesecake', 'price': 35.0, 'category': birthday_cakes, 'image_url': 'https://images.squarespace-cdn.com/content/v1/5373ea4de4b0cc867098115d/3a8be2ab-f09c-4846-8d1d-b68746ce8dec/White+Chocolate+Raspberry+Cheesecake+2.jpg'},
            # Add more cakes as needed
        ]

        for cake_data in cakes_data:
            cake = Cake(**cake_data)
            db.session.add(cake)

        db.session.commit()

if __name__ == '__main__':
    # Run the seed_data function when the script is executed
    seed_data()

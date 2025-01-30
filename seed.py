import random
from app import create_app, db
from app.models.productORM import Product 
from faker import Faker
import faker_commerce

app = create_app()
fake = Faker()
fake.add_provider(faker_commerce.Provider)  

def populate_products(n=20):
    with app.app_context():
        for _ in range(n):
            product = Product(
                name=fake.ecommerce_name(),  
                description=fake.catch_phrase(), 
                price=round(random.uniform(5, 2000), 2), 
                stock=random.randint(1, 100)  
            )
            db.session.add(product)
        db.session.commit()
        print(f"Completed insert of {n} mock products on table.")

if __name__ == "__main__":
    populate_products(30)  

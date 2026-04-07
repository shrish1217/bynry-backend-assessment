# Part 1: Corrected API Implementation with Atomic Transactions
from flask import request

@app.route('/api/products', methods=['POST'])
def create_product():
    data = request.json
    
    # 1. Validation: Ensure all mandatory fields are present
    required_fields = ['name', 'sku', 'price', 'warehouse_id', 'initial_quantity']
    if not all(field in data for field in required_fields):
        return {"error": "Missing required fields"}, 400

    try:
        # 2. Use a single transaction context for Atomicity
        with db.session.begin():
            
            # 3. Business Rule Check: SKU must be unique across the platform
            existing_product = Product.query.filter_by(sku=data['sku']).first()
            if existing_product:
                return {"error": f"Product with SKU {data['sku']} already exists"}, 409

            # Create the product object
            product = Product(
                name=data['name'],
                sku=data['sku'],
                price=data['price'] # Requirements specify price can be decimal
            )
            db.session.add(product)
            
            # Flush to get the product.id without committing the transaction yet
            db.session.flush() 

            # Create the inventory record linked to the new product
            inventory = Inventory(
                product_id=product.id,
                warehouse_id=data['warehouse_id'],
                quantity=data['initial_quantity']
            )
            db.session.add(inventory)
            
        # The 'with' block automatically commits here if successful
        return {"message": "Product and Inventory created successfully", "product_id": product.id}, 201

    except Exception as e:
        # Automatic rollback occurs if using SQLAlchemy's 'with db.session.begin()'
        # Log the error for production debugging
        print(f"Error creating product: {str(e)}")
        return {"error": "Internal server error occurred while creating product"}, 500

This is an implementation of Product from Escrow.


# Endpoints
There are 2 main endpoint which we use to create 
- `product-image/create/`: accepts post in order to add images
- `product/create/`: accepts post in order to create products (you can pass your image ids in `imageids` field so as to add the images to product you're creating.)

Documentation on your local machine: http://localhost:8000/swagger/

# Tests
You can run unittests using `pytest -v` command.

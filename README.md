
# E-commerce Frontend with Flet

This is a simple e-commerce frontend built using the Flet framework. The app displays a list of products, allows users to view product details, add items to the cart, and navigate between the homepage, cart, and account sections.

## Features
- **Product Listing:** Displays a list of products with images, titles, descriptions, prices, and a button to add them to the cart.
- **Product Details:** Clicking on a product shows more details, including its image, description, category, rating, and a button to add it to the cart.
- **Cart:** Users can view the items added to their cart, including product details and prices.
- **Navigation:** The app includes a navigation bar with options to switch between the Home, Cart, and Account sections.

## Tech Stack
- **Flet Framework:** A Python-based framework for building interactive UIs.
- **Python:** Programming language used to develop the app.

## Installation

### Prerequisites
Ensure you have Python 3.8+ installed. You can check your Python version by running:
```bash
python --version
```

### Setting up the Project
1. Clone the repository to your local machine:
    ```bash
    git clone https://github.com/yourusername/ecommerce-flet.git
    cd ecommerce-flet
    ```

2. Install the required dependencies:
    ```bash
    pip install requests flet
    ```

3. Run the application:
    ```bash
    python app.py
    ```
    The application will be accessible in your browser at `http://localhost:8550`.

## Project Structure

- `app.py`: Main Python file containing the application logic.
- `data.py`: Contains mock product data (this is assumed to be a Python file with a list of dictionaries that represent products).

## Code Overview

### `main(page: Page)`

This is the entry point of the app. The `main()` function sets up the page with a dark theme, title, and alignment. It also defines the core structure of the app, which includes the homepage, cart, and product detail pages.

### `homepage()`

This function displays a list of products. Each product is clickable, showing its details in a new page. Products can be added to the cart from here.

### `detailpage(id)`

This function is responsible for displaying detailed information about a product when it is selected from the homepage.

### `addtocart(product)`

Adds a product to the user's cart. The cart is stored in the `userproduct` list.

### `loadcart()`

Displays the list of products in the user's cart. Each item is shown with its image, title, and price.

### `navigationchange(e)`

Handles the navigation between different sections (Home, Cart, Account) when a tab is clicked in the navigation bar.

### `navbar`

A navigation bar with three tabs: Home, Cart, and Account. This allows users to navigate between the main sections of the app.

## Future Enhancements

- **Authentication:** Implement user login and registration.
- **Backend Integration:** Connect the frontend to a real backend for dynamic product data and cart functionality.
- **Product Filtering:** Add product filtering options based on categories or ratings.

## License

This project is open-source and available under the [MIT License](LICENSE).

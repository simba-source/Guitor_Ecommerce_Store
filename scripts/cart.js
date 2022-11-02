const addToCartButton = document.getElementById("add-to-cart")

function addItemToCart() {
    console.log("added to cart")
    updateCartTotal()
}

function updateCartTotal() {
    console.log("updating cart")
}

function deleteCartItem() {
    console.log("deleted item")
}

addToCartButton.addEventListener('click', addItemToCart)
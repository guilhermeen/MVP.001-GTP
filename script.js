// Script.js for e-commerce website

// Define global variables
const cart = document.getElementById("cart");
const cartBtn = document.getElementById("cart-btn");
const closeCartBtn = document.getElementById("close-cart");
const clearCartBtn = document.getElementById("clear-cart");
const cartTotal = document.getElementById("cart-total");
const cartContent = document.getElementById("cart-content");

// Initialize cart items
let cartItems = [];

// Add event listeners
function addEventListeners() {
  // Open cart
  cartBtn.addEventListener("click", () => {
    cart.classList.add("show-cart");
  });
  // Close cart
  closeCartBtn.addEventListener("click", () => {
    cart.classList.remove("show-cart");
  });
  // Clear cart
  clearCartBtn.addEventListener("click", () => {
    clearCart();
  });
}

// Load items
function loadItems() {
  // Load items from backend using Node.js API
  // Append items to DOM using HTML and CSS
}

// Add item to cart
function addItemToCart(item) {
  // Check if item is already in cart
  for (let i = 0; i < cartItems.length; i++) {
    if (cartItems[i].id === item.id) {
      cartItems[i].quantity++;
      return;
    }
  }
  // Add item to cart
  cartItems.push(item);
  // Update cart
  updateCart();
}

// Update cart
function updateCart() {
  // Calculate total price and quantity
  let totalPrice = 0;
  let totalQuantity = 0;
  cartItems.forEach((item) => {
    totalPrice += item.price * item.quantity;
    totalQuantity += item.quantity;
  });
  // Update cart content
  cartContent.innerHTML = "";
  cartItems.forEach((item) => {
    const cartItem = document.createElement("div");
    cartItem.classList.add("cart-item");
    cartItem.innerHTML = `
      <img src="${item.image}" alt="${item.name}">
      <div>
        <h4>${item.name}</h4>
        <h5>$${item.price}</h5>
        <span class="remove-item" data-id="${item.id}">remove</span>
      </div>
      <div>
        <i class="fa fa-chevron-up" data-id="${item.id}"></i>
        <p class="item-quantity">${item.quantity}</p>
        <i class="fa fa-chevron-down" data-id="${item.id}"></i>
      </div>
    `;
    cartContent.appendChild(cartItem);
  });
  // Update total price and quantity
  cartTotal.innerHTML = `$${totalPrice}`;
  cartItemsCount.innerHTML = totalQuantity;
}

// Clear cart
function clearCart() {
  cartItems = [];
  updateCart();
}

// Remove item from cart
function removeItemFromCart(id) {
  // Filter out item from cart
  cartItems = cartItems.filter((item) => item.id !== id);
  // Update cart
  updateCart();
}

// Initialize script
function init() {
  addEventListeners();
  loadItems();
}

init();
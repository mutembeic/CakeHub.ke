import React, { useEffect, useState } from 'react';
import axios from 'axios';
import { Link } from 'react-router-dom';

const ShoppingCart = () => {
  const [cart, setCart] = useState([]);

  useEffect(() => {
    axios.get('/cart')
      .then(response => {
        setCart(response.data.cart);
      })
      .catch(error => {
        console.error('There was an error fetching the cart!', error);
      });
  }, []);

  const handleRemove = (cakeId) => {
    axios.delete(`/cart/${cakeId}`)
      .then(response => {
        setCart(cart.filter(cake => cake.id !== cakeId));
      })
      .catch(error => {
        console.error('There was an error removing the cake from the cart!', error);
      });
  };

  const totalPrice = cart.reduce((total, cake) => total + cake.price, 0);

  return (
    <div className="max-w-3xl mx-auto mt-10">
      <h1 className="text-3xl font-bold mb-6">Shopping Cart</h1>
      {cart.length === 0 ? (
        <p>Your cart is empty</p>
      ) : (
        <div>
          {cart.map(cake => (
            <div key={cake.id} className="flex justify-between items-center border-b py-4">
              <img src={cake.image_url} alt={cake.name} className="w-20 h-20 object-cover rounded-md" />
              <div>
                <h2 className="text-xl font-bold">{cake.name}</h2>
                <p>${cake.price.toFixed(2)}</p>
              </div>
              <button
                onClick={() => handleRemove(cake.id)}
                className="p-2 bg-red-500 text-white rounded"
              >
                Remove
              </button>
            </div>
          ))}
          <div className="text-right mt-4">
            <h2 className="text-2xl font-bold">Total: ${totalPrice.toFixed(2)}</h2>
            <Link to="/checkout" className="inline-block p-2 mt-4 bg-blue-500 text-white rounded">
              Proceed to Checkout
            </Link>
          </div>
        </div>
      )}
    </div>
  );
};

export default ShoppingCart;

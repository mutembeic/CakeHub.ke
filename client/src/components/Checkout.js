import React, { useState } from 'react';
import axios from 'axios';

const Checkout = () => {
  const [order, setOrder] = useState({
    name: '',
    address: '',
    email: '',
    phone: '',
    paymentMethod: 'Credit Card',
  });

  const handleChange = (e) => {
    const { name, value } = e.target;
    setOrder({ ...order, [name]: value });
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    axios.post('/checkout', order)
      .then(response => {
        alert('Order placed successfully!');
        setOrder({ name: '', address: '', email: '', phone: '', paymentMethod: 'Credit Card' });
      })
      .catch(error => {
        console.error('There was an error placing the order!', error);
      });
  };

  return (
    <div className="max-w-lg mx-auto mt-10">
      <h1 className="text-3xl font-bold mb-6">Checkout</h1>
      <form onSubmit={handleSubmit}>
        <input
          type="text"
          name="name"
          value={order.name}
          onChange={handleChange}
          placeholder="Your Name"
          className="w-full p-2 mb-4 border rounded"
          required
        />
        <input
          type="text"
          name="address"
          value={order.address}
          onChange={handleChange}
          placeholder="Address"
          className="w-full p-2 mb-4 border rounded"
          required
        />
        <input
          type="email"
          name="email"
          value={order.email}
          onChange={handleChange}
          placeholder="Email"
          className="w-full p-2 mb-4 border rounded"
          required
        />
        <input
          type="text"
          name="phone"
          value={order.phone}
          onChange={handleChange}
          placeholder="Phone"
          className="w-full p-2 mb-4 border rounded"
          required
        />
        <select
          name="paymentMethod"
          value={order.paymentMethod}
          onChange={handleChange}
          className="w-full p-2 mb-4 border rounded"
          required
        >
          <option value="Credit Card">Credit Card</option>
          <option value="PayPal">PayPal</option>
          <option value="Bank Transfer">Bank Transfer</option>
        </select>
        <button type="submit" className="w-full p-2 bg-blue-500 text-white rounded">Place Order</button>
      </form>
    </div>
  );
};

export default Checkout;

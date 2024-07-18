import React, { useEffect, useState } from 'react';
import axios from 'axios';
import { useParams } from 'react-router-dom';

const AdminOrderDetails = () => {
  const { id } = useParams();
  const [order, setOrder] = useState(null);

  useEffect(() => {
    axios.get(`/admin/orders/${id}`)
      .then(response => {
        setOrder(response.data.order);
      })
      .catch(error => {
        console.error('There was an error fetching the order details!', error);
      });
  }, [id]);

  if (!order) return <div>Loading...</div>;

  return (
    <div className="max-w-4xl mx-auto mt-10">
      <h1 className="text-3xl font-bold mb-6">Order Details</h1>
      <div className="bg-white p-6 rounded shadow">
        <h2 className="text-2xl font-bold mb-4">Order #{order.id}</h2>
        <p className="mb-2"><strong>Name:</strong> {order.customer.name}</p>
        <p className="mb-2"><strong>Email:</strong> {order.customer.email}</p>
        <p className="mb-2"><strong>Address:</strong> {order.customer.address}</p>
        <p className="mb-2"><strong>Phone:</strong> {order.customer.phone}</p>
        <p className="mb-2"><strong>Payment Method:</strong> {order.paymentMethod}</p>
        <p className="mb-2"><strong>Total Price:</strong> ${order.totalPrice.toFixed(2)}</p>
        <h3 className="text-xl font-bold mt-6">Items</h3>
        <ul>
          {order.items.map(item => (
            <li key={item.id} className="mb-2">
              {item.name} - ${item.price.toFixed(2)} x {item.quantity}
            </li>
          ))}
        </ul>
      </div>
    </div>
  );
};

export default AdminOrderDetails;

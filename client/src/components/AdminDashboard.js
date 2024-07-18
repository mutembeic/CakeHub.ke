import React from 'react';
import { Link } from 'react-router-dom';

const AdminDashboard = () => {
  return (
    <div className="max-w-4xl mx-auto mt-10">
      <h1 className="text-3xl font-bold mb-6">Admin Dashboard</h1>
      <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
        <Link to="/admin/orders" className="p-4 bg-gray-100 border rounded text-center">
          <h2 className="text-2xl font-bold mb-2">Manage Orders</h2>
          <p>View and manage customer orders</p>
        </Link>
        <Link to="/admin/users" className="p-4 bg-gray-100 border rounded text-center">
          <h2 className="text-2xl font-bold mb-2">Manage Users</h2>
          <p>View and manage user accounts</p>
        </Link>
        <Link to="/admin/cakes/add" className="p-4 bg-gray-100 border rounded text-center">
          <h2 className="text-2xl font-bold mb-2">Add New Cake</h2>
          <p>Add a new cake to the inventory</p>
        </Link>
        <Link to="/admin/cakes" className="p-4 bg-gray-100 border rounded text-center">
          <h2 className="text-2xl font-bold mb-2">Manage Cakes</h2>
          <p>View and edit existing cakes</p>
        </Link>
      </div>
    </div>
  );
};

export default AdminDashboard;

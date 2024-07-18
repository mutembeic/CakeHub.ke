import React, { useEffect, useState } from 'react';
import axios from 'axios';

const AccountDashboard = () => {
  const [user, setUser] = useState(null);

  useEffect(() => {
    axios.get('/account')
      .then(response => {
        setUser(response.data.user);
      })
      .catch(error => {
        console.error('There was an error fetching the user details!', error);
      });
  }, []);

  if (!user) return <div>Loading...</div>;

  return (
    <div className="max-w-4xl mx-auto mt-10">
      <h1 className="text-3xl font-bold mb-6">My Account</h1>
      <div className="bg-white p-6 rounded shadow">
        <h2 className="text-2xl font-bold mb-4">Account Details</h2>
        <p className="mb-2"><strong>Name:</strong> {user.name}</p>
        <p className="mb-2"><strong>Email:</strong> {user.email}</p>
        <p className="mb-2"><strong>Address:</strong> {user.address}</p>
        <p className="mb-2"><strong>Phone:</strong> {user.phone}</p>
      </div>
    </div>
  );
};

export default AccountDashboard;

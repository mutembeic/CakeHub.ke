import React from 'react';
import { Link } from 'react-router-dom';

const Navbar = () => {
  return (
    <nav className="bg-gray-800 p-4">
      <div className="container mx-auto flex justify-between items-center">
        <Link to="/" className="text-white text-2xl font-bold">CakeHub</Link>
        <div className="flex space-x-4">
          <Link to="/cakes" className="text-white">Cakes</Link>
          <Link to="/cart" className="text-white">Cart</Link>
          <Link to="/account" className="text-white">My Account</Link>
          <Link to="/admin" className="text-white">Admin</Link>
        </div>
      </div>
    </nav>
  );
};

export default Navbar;

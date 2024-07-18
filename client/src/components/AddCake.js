import React, { useState } from 'react';
import axios from 'axios';

const AddCake = () => {
  const [cake, setCake] = useState({
    name: '',
    description: '',
    price: '',
    image_url: '',
  });

  const handleChange = (e) => {
    const { name, value } = e.target;
    setCake({ ...cake, [name]: value });
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    axios.post('/cakes', cake)
      .then(response => {
        alert('Cake added successfully!');
        setCake({ name: '', description: '', price: '', image_url: '' });
      })
      .catch(error => {
        console.error('There was an error adding the cake!', error);
      });
  };

  return (
    <div className="max-w-lg mx-auto mt-10">
      <h1 className="text-3xl font-bold mb-6">Add New Cake</h1>
      <form onSubmit={handleSubmit}>
        <input
          type="text"
          name="name"
          value={cake.name}
          onChange={handleChange}
          placeholder="Cake Name"
          className="w-full p-2 mb-4 border rounded"
          required
        />
        <textarea
          name="description"
          value={cake.description}
          onChange={handleChange}
          placeholder="Cake Description"
          className="w-full p-2 mb-4 border rounded"
          required
        />
        <input
          type="number"
          name="price"
          value={cake.price}
          onChange={handleChange}
          placeholder="Cake Price"
          className="w-full p-2 mb-4 border rounded"
          required
        />
        <input
          type="url"
          name="image_url"
          value={cake.image_url}
          onChange={handleChange}
          placeholder="Image URL"
          className="w-full p-2 mb-4 border rounded"
          required
        />
        <button type="submit" className="w-full p-2 bg-blue-500 text-white rounded">Add Cake</button>
      </form>
    </div>
  );
};

export default AddCake;

import React, { useEffect, useState } from 'react';
import axios from 'axios';
import { useParams } from 'react-router-dom';

const EditCakes = () => {
  const { id } = useParams();
  const [cake, setCake] = useState({
    name: '',
    description: '',
    price: '',
    image_url: '',
  });

  useEffect(() => {
    axios.get(`/cakes/${id}`)
      .then(response => {
        setCake(response.data.cake);
      })
      .catch(error => {
        console.error('There was an error fetching the cake details!', error);
      });
  }, [id]);

  const handleChange = (e) => {
    const { name, value } = e.target;
    setCake({ ...cake, [name]: value });
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    axios.put(`/cakes/${id}`, cake)
      .then(response => {
        alert('Cake updated successfully!');
      })
      .catch(error => {
        console.error('There was an error updating the cake!', error);
      });
  };

  return (
    <div className="max-w-lg mx-auto mt-10">
      <h1 className="text-3xl font-bold mb-6">Edit Cake</h1>
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
        <button type="submit" className="w-full p-2 bg-blue-500 text-white rounded">Update Cake</button>
      </form>
    </div>
  );
};

export default EditCakes;

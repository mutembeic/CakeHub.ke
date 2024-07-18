import React, { useEffect, useState } from 'react';
import axios from 'axios';
import { Link } from 'react-router-dom';

const CakeList = () => {
  const [cakes, setCakes] = useState([]);

  useEffect(() => {
    axios.get('/cakes')
      .then(response => {
        setCakes(response.data.cakes);
      })
      .catch(error => {
        console.error('There was an error fetching the cakes!', error);
      });
  }, []);

  return (
    <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4 mt-10">
      {cakes.map(cake => (
        <div key={cake.id} className="border p-4 rounded-lg shadow-md">
          <img src={cake.image_url} alt={cake.name} className="w-full h-48 object-cover rounded-md" />
          <h2 className="text-2xl font-bold mt-4">{cake.name}</h2>
          <p className="text-lg mt-2">${cake.price.toFixed(2)}</p>
          <Link to={`/cakes/${cake.id}`} className="text-blue-500 hover:underline mt-4 block">View Details</Link>
        </div>
      ))}
    </div>
  );
};

export default CakeList;

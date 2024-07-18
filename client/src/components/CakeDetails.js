import React, { useEffect, useState } from 'react';
import axios from 'axios';
import { useParams } from 'react-router-dom';

const CakeDetails = () => {
  const { id } = useParams();
  const [cake, setCake] = useState(null);

  useEffect(() => {
    axios.get(`/cakes/${id}`)
      .then(response => {
        setCake(response.data.cake);
      })
      .catch(error => {
        console.error('There was an error fetching the cake details!', error);
      });
  }, [id]);

  if (!cake) return <div>Loading...</div>;

  return (
    <div className="mt-10">
      <img src={cake.image_url} alt={cake.name} className="w-full h-64 object-cover rounded-md" />
      <h1 className="text-4xl font-bold mt-4">{cake.name}</h1>
      <p className="text-lg mt-2">${cake.price.toFixed(2)}</p>
      <p className="mt-4">{cake.description}</p>
    </div>
  );
};

export default CakeDetails;

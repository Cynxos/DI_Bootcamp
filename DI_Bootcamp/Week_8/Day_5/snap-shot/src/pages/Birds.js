import React, { useEffect, useState } from 'react';
import { fetchImages } from '../api/pexels';

const Birds = () => {
  const [images, setImages] = useState([]);

  useEffect(() => {
    const getImages = async () => {
      const photos = await fetchImages('birds');
      setImages(photos);
    };
    getImages();
  }, []);

  return (
    <div>
      {images.map((image) => (
        <img key={image.id} src={image.src.medium} alt={image.alt} />
      ))}
    </div>
  );
};

export default Birds;
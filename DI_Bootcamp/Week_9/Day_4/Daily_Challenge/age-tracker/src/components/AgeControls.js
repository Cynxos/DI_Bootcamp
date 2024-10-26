import React from 'react';
import { useDispatch } from 'react-redux';
import { ageUpAsync, ageDownAsync } from '../features/age/ageThunks';
import './AgeControls.css';

const AgeControls = () => {
  const dispatch = useDispatch();

  return (
    <div className="age-controls">
      <button onClick={() => dispatch(ageUpAsync())}>Age Up</button>
      <button onClick={() => dispatch(ageDownAsync())}>Age Down</button>
    </div>
  );
};

export default AgeControls;
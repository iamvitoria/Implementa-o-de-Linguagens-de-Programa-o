import React from 'react';
import { useSelector } from 'react-redux';

const DSLOutput = () => {
    const output = useSelector((state) => state.dsl.output); // Assumindo que você tenha um estado output no Redux

    return (
        <div>
            <h2>Resultado:</h2>
            <pre>{output}</pre>
        </div>
    );
};

export default DSLOutput;

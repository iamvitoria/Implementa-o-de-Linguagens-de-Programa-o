import React, { useState } from 'react';
import { useDispatch } from 'react-redux';
import { interpret } from '../redux/dslSlice';

const DSLInput = () => {
    const [code, setCode] = useState('');
    const dispatch = useDispatch();

    const handleInterpret = () => {
        dispatch(interpret(code)); // Envie o código para o Redux
        setCode(''); // Limpa a entrada
    };

    return (
        <div>
            <textarea
                value={code}
                onChange={(e) => setCode(e.target.value)}
                placeholder="Digite seu código DSL aqui"
            />
            <button onClick={handleInterpret}>Interpretar</button>
        </div>
    );
};

export default DSLInput;

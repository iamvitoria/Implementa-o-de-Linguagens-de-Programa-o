import React from 'react';
import DSLInput from './components/DSLInput';
import DSLOutput from './components/DSLOutput';

function App() {
    return (
        <div>
            <h1>DSL Interpreter</h1>
            <DSLInput />
            <DSLOutput />
        </div>
    );
}

export default App;

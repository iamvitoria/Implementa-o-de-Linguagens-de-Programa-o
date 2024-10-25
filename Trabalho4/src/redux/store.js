import { configureStore } from '@reduxjs/toolkit';
import dslReducer from './dslSlice';

const store = configureStore({
    reducer: {
        dsl: dslReducer,
    },
});

export default store;

import { createSlice } from '@reduxjs/toolkit';

const dslSlice = createSlice({
    name: 'dsl',
    initialState: {
        code: '',
        output: '',
        variables: {}, // Para armazenar variáveis
    },
    reducers: {
        interpret: (state, action) => {
            const code = action.payload;
            state.code = code;
            state.output = ''; // Limpa a saída antes de interpretar

            // Dividir o código em linhas
            const lines = code.split('\n');

            lines.forEach(line => {
                line = line.trim(); // Remove espaços em branco
                if (line.startsWith('PRINT')) {
                    // Interpretar comando PRINT
                    const message = line.slice(6).trim(); // Remove "PRINT "
                    state.output += message + '\n'; // Adiciona a mensagem à saída
                } else if (line.startsWith('LET')) {
                    // Interpretar comando LET
                    const [_, variable, value] = line.split(' ');
                    state.variables[variable] = parseInt(value) || value; // Armazena a variável
                } else if (line.startsWith('IF')) {
                    // Implementar lógica para IF
                    // Exemplo: IF x > 10 THEN PRINT "x é maior que 10"
                    // Você precisará implementar a lógica de avaliação
                    const condition = line.slice(3, line.indexOf('THEN')).trim();
                    const printCommand = line.slice(line.indexOf('THEN') + 5).trim();
                    if (evaluateCondition(state.variables, condition)) {
                        state.output += `PRINT: ${printCommand}\n`; // Simula o comando PRINT
                    }
                } else if (line.startsWith('WHILE')) {
                    // Implementar lógica para WHILE
                    // Exemplo: WHILE x < 10 DO PRINT "x é menor que 10"
                    // Você precisará implementar a lógica de avaliação
                    const condition = line.slice(6, line.indexOf('DO')).trim();
                    const printCommand = line.slice(line.indexOf('DO') + 3).trim();
                    while (evaluateCondition(state.variables, condition)) {
                        state.output += `PRINT: ${printCommand}\n`; // Simula o comando PRINT
                    }
                } else {
                    state.output += 'Comando desconhecido\n'; // Para comandos não reconhecidos
                }
            });
        },
    },
});

// Função para avaliar condições
const evaluateCondition = (variables, condition) => {
    const [left, operator, right] = condition.split(' ');

    const leftValue = isNaN(variables[left]) ? variables[left] : parseInt(variables[left]);
    const rightValue = isNaN(right) ? variables[right] : parseInt(right);

    switch (operator) {
        case '>':
            return leftValue > rightValue;
        case '<':
            return leftValue < rightValue;
        case '==':
            return leftValue == rightValue;
        case '!=':
            return leftValue != rightValue;
        default:
            return false; // Condição não reconhecida
    }
};

export const { interpret } = dslSlice.actions;
export default dslSlice.reducer;

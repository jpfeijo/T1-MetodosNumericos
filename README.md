# Trabalho 1 - Métodos Numéricos

Trabalho feito na disciplina de Métodos Numéricos da PUCRS.

Seu primeiro trabalho nesta disciplina consiste em explorar o padrão IEEE-754. Você deve
implementar um programa que cumpra as seguintes tarefas:
1. Ele recebe pela linha de comando uma expressão no formato
val1 op val2
onde op é uma operação (+,−, ∗,/) e val1 e val2 são dois valores em ponto flutuante, NaN
ou ±∞.
2. Depois de receber a expressão seu programa deve realizar a operação op e mostrar o resultado
dela;
3. Seu programa também deve mostrar a configuração de bits das duas variáveis e do resultado. Tome cuidado com a endianness do seu processador para que a saída seja apresentada
corretamente;
4. Seu programa também deve informar se alguma exceção do padrão IEEE-754 foi sinalizada
quando a operação foi feita.

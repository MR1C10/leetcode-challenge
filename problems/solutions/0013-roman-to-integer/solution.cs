public class Solution {
    public int RomanToInt(string s) {

        Dictionary<char, int> romanos = new Dictionary<char, int>
        {
            {'I', 1},
            {'V', 5},
            {'X', 10},
            {'L', 50},
            {'C', 100},
            {'D', 500},
            {'M', 1000}
        };

        int resultadoFinal = 0;
        int valorAntes = 0;

        for (int i = s.Length - 1; i >= 0; i--)
        {
            int valorAtual = romanos[s[i]]; // pegando o valor da  letra atual
            
            // se o valor atual for menor que o anterior subtrai
            if (valorAtual < valorAntes)
            {
                resultadoFinal -= valorAtual; // ex: IV(4), CD(400)
            }
            else // caso contrario soma
            {
                resultadoFinal += valorAtual;
            }

            valorAntes = valorAtual;
        }
        return resultadoFinal;
    }
}
public class Solution {
    public bool IsPalindrome(int x) {
        
        if (x < 0) return false;
        
        int original = x;
        int reservado = 0;

        while (x > 0)
        {
            int digitos = x % 10;
            reservado = reservado * 10 + digitos;
            x /= 10;
        }

        return original == reservado;

    }
}
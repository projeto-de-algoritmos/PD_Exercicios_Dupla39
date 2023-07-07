class Solution(object):
    def trap(self, altura):
        
        if len(altura) <= 2:
            return 0

        agua = 0
        esquerda_max = [0 for i in range(len(altura))]
        direita_max = [0 for i in range(len(altura))]
        esquerda_max[0], direita_max[-1] = altura[0], altura[-1]
        
        for i in range(1, len(altura)):
            if altura[i] > esquerda_max[i-1]:
                esquerda_max[i] = altura[i]
            else:
                esquerda_max[i] = esquerda_max[i-1]
    
        for i in range(len(altura)-2, -1, -1):
            if altura[i] > direita_max[i+1]:
                direita_max[i] = altura[i]
            else:
                direita_max[i] = direita_max[i+1]

       
        for i in range(len(altura)):
            min_altura = esquerda_max[i]
            if esquerda_max[i] >= direita_max[i]:
                min_altura = direita_max[i]
    
            if min_altura > altura[i]:
                agua += min_altura - altura[i]

        return agua
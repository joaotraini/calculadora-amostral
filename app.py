from scipy.stats import norm
import math

# Variáveis
populacao_total = 5000000  # População total (número de acessos no mês)
taxa_conversao_atual = 26.55  # Taxa de conversão atual em porcentagem
aumento_desejado = 10.00  # Aumento desejado na taxa de conversão em porcentagem

p1 = taxa_conversao_atual / 100
p2 = p1 + (aumento_desejado / 100)

# Nível de significância e poder estatístico:
alpha = 1 / 100  # 1% de significância para 99% de confiança
beta = 20 / 100  # 20% de beta para 80% de poder estatístico

p_bar = (p1 + p2) / 2 # Taxa de conversão média ponderada

Z_alpha_2 = norm.ppf(1 - alpha/2)  # Valor para o nível de confiança
Z_beta = norm.ppf(1 - beta)  # Valor para o poder estatístico

# Cálculo do tamanho da amostra para cada grupo do teste A/B:
n = ((Z_alpha_2 * math.sqrt(2 * p_bar * (1 - p_bar)) + Z_beta * math.sqrt(p1 * (1 - p1) + p2 * (1 - p2))) / (p2 - p1)) ** 2

n_total = n * 2 # Tamanho total da amostra para ambos os grupos (A e B)

# Consideração da população finita (se o tamanho da amostra for uma fração significativa da população)
if n_total > 5/100 * populacao_total:
    n_total_corrigido = (n_total * populacao_total) / (n_total + populacao_total - 1)
else:
    n_total_corrigido = n_total

def formatar_numero(num):
    if num >= 1000000:
        return '{:,.0f} milhões'.format(num/1000000).replace(',', '.')
    elif num >= 1000:
        return '{:,.2f} mil'.format(num/1000).replace(',', '.')
    else:
        return str(num)

print("Para uma população de " + formatar_numero(populacao_total) + ", precisamos alcançar (no mínimo) " + formatar_numero(int(n_total_corrigido)) + " pessoas.")


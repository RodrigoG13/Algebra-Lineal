def get_sub(x):
    normal = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+-=()"
    sub_s = "ₐ₈CDₑբGₕᵢⱼₖₗₘₙₒₚQᵣₛₜᵤᵥwₓᵧZₐ♭꜀ᑯₑբ₉ₕᵢⱼₖₗₘₙₒₚ૧ᵣₛₜᵤᵥwₓᵧ₂₀₁₂₃₄₅₆₇₈₉₊₋₌₍₎"
    res = x.maketrans(''.join(normal), ''.join(sub_s))
    return x.translate(res)

array = [1, 2, 3, 4, 5]
parametros = ["λ\u2081", "λ\u2082", "λ\u2083", "λ\u2084", "λ\u2085", "λ\u2086", "λ\u2087", "λ\u2088", "λ\u2089"]

for numero in parametros:
    print(numero)

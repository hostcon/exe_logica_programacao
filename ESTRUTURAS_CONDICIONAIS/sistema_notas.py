print("=== SISTEMA ESCOLAR ===")
nota = float(input("Digite a nota final do aluno: "))

if nota >= 7.0:
    print("Parabéns, você foi Aprovado! 🎓")
elif nota >= 5.0:
    print("Atenção, você está em Recuperação. 📚")
else:
    print("Infelizmente você foi Reprovado. ❌")
# 🛠️ Predictive Maintenance com Machine Learning

Este projeto aplica técnicas de aprendizado de máquina para prever falhas em equipamentos industriais com base em dados operacionais, apoiando decisões proativas de manutenção e evitando paradas não planejadas.

## 📊 Sobre a Base de Dados

Foi utilizado o *AI4I 2020 Predictive Maintenance Dataset*, que simula sensores industriais coletando variáveis como temperatura, pressão, rotação e desgaste da ferramenta. O conjunto de dados contém:

- Um alvo binário (`Target`) que indica a ocorrência ou não de falha.
- Um alvo multiclasse (`Failure Type`) detalhando o tipo de falha: `No Failure`, `Heat Dissipation`, `Overstrain`, `Power Failure` ou `Tool Wear Failure`.

## 🎯 Objetivo

Desenvolver dois classificadores:
- **Binário**: prever a ocorrência de falha.
- **Multiclasse**: identificar o tipo específico de falha.

O foco principal foi maximizar o *recall* no modelo binário (reduzir falsos negativos), e a *f1-score* ponderada no modelo multiclasse.

## ⚙️ Estratégia e Metodologia

1. **Análise Exploratória (EDA)**  
   - Investigação de padrões e correlações entre variáveis.
   - Verificação de balanceamento de classes e valores ausentes.

2. **Pré-processamento**
   - Imputação de dados faltantes.
   - Transformação de variáveis com `PowerTransformer`.
   - Codificação ordinal para variáveis categóricas.

3. **Balanceamento**  
   - Aplicação de `SMOTEENN` para lidar com desbalanceamento de classes.

4. **Modelagem**
   - Treinamento com múltiplos algoritmos (Random Forest, Regressão Logística, Naive Bayes, KNN).
   - Busca em grade com `GridSearchCV` e validação cruzada estratificada.
   - Avaliação com métricas específicas: `recall` para o binário e `f1_weighted` para o multiclasse.

5. **Interpretação**
   - Curvas ROC e Precision-Recall.
   - Análise de importância das variáveis com Random Forest.

## 🏁 Resultados

- **Modelo Binário**:
  - Random Forest com `recall` elevado na detecção de falhas.
  - AUC-ROC robusto e boa separação nas curvas Precision-Recall.
  
- **Modelo Multiclasse**:
  - Random Forest também se destacou na identificação dos tipos de falha.
  - Boas performances nas curvas ROC por classe (One-vs-Rest).

## 🧠 Conclusão

O projeto mostra o potencial do aprendizado de máquina na antecipação de falhas industriais, proporcionando economia, segurança e eficiência. Os modelos entregam desempenho robusto e são interpretáveis, tornando-os viáveis para aplicações reais em ambientes industriais.

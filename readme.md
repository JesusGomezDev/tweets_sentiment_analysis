## Requerimientos

Para el correcto funcionamiento del proyecto es importante seguir el orden establecido a continuación, es recomendable usar google colab para los archivos .ipynb.

- json
- contextlib
- textblob
- numoy
- nltk
- pandas
- xlsxwriter
- sklearn
- matplotlib

entre otras librerías menos importantes, pero que aún así son necesarias, revise cada archivo para encontrar cuáles son las otras librerías restantes

## Proceso de aprendizaje

1. Realizar un web scraping a tweter para obtener 300,000 tweets:
   ```
   tweet_scraping.py
   ```
2. Pasar los datos de Json a Excel:

   ```
   json_to_xlsx.py
   ```

3. Abrir el excel y guardarlo como .csv:
4. Procesar y limpiar lo datos
   ```
    data_process.ipynb
   ```
5. Clasificar mediante Bayes
   ```
   bayes_clasification.ipynb
   ```
6. Distribuir el proceesamiento con el algoritmo genético
   ```
   genetic_load.ipynb
   ```
7. Ejecutar el machine learning de los tweets

   ```
   tweet_learning.ipynb
   ```

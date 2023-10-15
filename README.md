# Star Citizen Translation Tool

Questo progetto è un'applicazione che consente di tradurre tutti i contenuti di gioco di Star Citizen in diverse lingue. Utilizza le potenti API di DeepL per effettuare traduzioni automatiche e produce un file tradotto in output.

## Istruzioni per l'uso

Per utilizzare questo programma, seguire questi passaggi:

1. **Preparazione del File da Tradurre:**
   Assicurarsi che il file da tradurre sia nel formato corretto e contenga tutti i testi da tradurre. Il file deve essere in un formato supportato dal programma.

2. **Esecuzione del Programma:**
   Eseguire il programma e specificare il percorso del file da tradurre come input.

3. **Consiglio per Migliori Risultati:**
Per ottenere una traduzione più accurata e ridurre i tempi di traduzione, si consiglia di spezzare il file di input in più file più piccoli. Questo aiuterà a migliorare la qualità della traduzione e a ridurre i tempi di elaborazione.

4. **Output del File Tradotto:**
Una volta completata la traduzione, il programma creerà nuovi file contenenti i testi tradotti.

## Requisiti del Sistema

- Python 3.5 o versioni successive.
- Accesso a Internet per utilizzare le API di DeepL.
- Token API DeepL ottenuto tramite registrazione sul sito DeepL.

## Configurazione delle API di DeepL
È necessario registrarsi al sito di DeepL per ottenere un token per le API e in seguito configurare le credenziali delle API ottenute per utilizzarle in questo programma. Modificare il file di configurazione `config.json` e inserire le credenziali corrette fornite da DeepL.

```json
{
  "deepL_api_key": "INSERIRE_LA_TUA_API_KEY_DEEPL"
}
```

## Segnalazione di Problemi
In caso di problemi con l'applicazione o se si riscontrano errori durante la traduzione, si prega di aprire una segnalazione nell'area delle issue del repository su GitHub.

Buon divertimento nella traduzione dei contenuti di Star Citizen! 🚀✨
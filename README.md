# Unscripted_Journalism
**Summer of Code 2021 - Unscripted (IIT Bombay)**

<img src="https://19yw4b240vb03ws8qm25h366-wpengine.netdna-ssl.com/wp-content/uploads/5-Best-Speech-to-Text-APIs-2-e1615383933700-1024x573.png" width="600" height="350" />

**Contributors: Hiren Bavaskar, Harshit Modi**

This is our SOC 2021 project "Unscripted" involving NLP, Machine Learning and Speech recognition

Our learning progress diaries can be seen in Learning-progress_Hiren 

## Speech to text library used:
- SpeechRecognition by Google
- Pydub and NLTK libraries in python for speech analysis

## Objective of this project:
To take an audio(.wav file) as input and transcribe the speech in a text file(transcription.txt). Another additional feature we have added is to get summary of the transcription. The number of lines of summary the user wants is taken as input and the desired summary is written in summary.txt. Our main emphasis has been on journalism related audios and news,

*NOTE: This speech to text currently works good only on US-English accent. Further fine-tuning would be required for transcribing Indian accent well.*

We are using extractive-summary method to obtain the summary of the transcript

## How to use?
- Clone the github repo on your local machine
- Create a virtual environment in project_files and pip install -r requirements.txt to install the necessary files
- To get transcription of an audio file(.wav file), use python3 speech_to_article.py <path_to_audiofile>
- To get summary of the transcription, run python3 summarizer.py and provide the number of lines of summary you want as input 

## Advantages
- Speech to text automated
- Obtain relevant text from the speech
- Obtain any number of lines of summary 

## Drawbacks
- Inaccuracies and redundant words being transcribed
- Sentences not completely correct in grammatical sense

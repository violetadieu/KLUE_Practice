# KLUE_Practice

2021년에 출시한 한국어 자연어처리 벤치마크 KLUE를 활용해 아래 Task들을 연습하기 위한 repo 입니다.<br><br>

<hr>

<h3>Topic Classification<br><br></h3>

<hr>

<h3>Semantic Textual Similarity<br><br></h3>
<h6>STS, 문장 유사도 task를 구현해 모델/tokenizer/데이터/epoch 수의 다양한 조합으로 실험을 진행하였습니다.</h6>
<h6>기존 klue-benchmark dataset을 제외한 데이터는 출처를 표기할 예정입니다.</h6>
<h6>제가 실험한 모델/tokenizer 이외의 다른 조합을 실험하고 싶으신 분은 MRCModel 주피터 노트북 파일의 modelName, tokenizerName 변수를 수정하시면 됩니다.</h6><br>

<hr>

<h3>Natural Language Inference<br><br></h3>

<hr>

<h3>Named Entity Recognition<br><br></h3>

<hr>

<h3>Relation Extraction<br><br></h3>

<hr>

<h3>Dependency Parsing<br><br></h3>

<hr>

<h3>Machine Reading Comprehension<br><br></h3>
MRC, 기계독해 task를 구현해 모델/tokenizer/데이터/epoch 수의 다양한 조합으로 실험을 진행하였습니다.
제가 실험한 모델/tokenizer 이외의 다른 조합을 실험하고 싶으신 분은 MRCModel 주피터 노트북 파일의 modelName, tokenizerName 변수를 수정하시면 됩니다.


model : klue-bert-base<br>
trainData : KLUE-benchmark-dataset-mrc
  
|model|tokenizer|train-data|val-data|epoch|em-score|
|------|---|---|---|---|---|
|klue-bert-base|klue-bert-base|KLUE-benchmark-dataset-mrc|KLUE-benchmark-dataset-mrc|1|51.3|
|klue-bert-base|klue-bert-base|KLUE-benchmark-dataset-mrc|AiHub-한국어기계독해데이터셋-Normal|1|32.8|
|klue-bert-base|klue-bert-base|KLUE-benchmark-dataset-mrc|KLUE-benchmark-dataset-mrc|3|49.7|
|klue-bert-base|klue-bert-base|KLUE-benchmark-dataset-mrc|KLUE-benchmark-dataset-mrc|10|45.0|
|klue-bert-base|klue-roberta-large|KLUE-benchmark-dataset-mrc|KLUE-benchmark-dataset-mrc|1|48.4|
|klue-bert-base|klue-roberta-large|KLUE-benchmark-dataset-mrc|KLUE-benchmark-dataset-mrc|3|44.9|
|klue-bert-base|klue-roberta-large|KLUE-benchmark-dataset-mrc|KLUE-benchmark-dataset-mrc|10|44.4|

<hr>
    
model : klue-bert-base<br>
trainData : AiHub-한국어기계독해데이터셋-Normal
|model|tokenizer|train-data|val-data|epoch|em-score|
|------|---|---|---|---|---|
|klue-bert-base|klue-bert-base|AiHub-한국어기계독해데이터셋-Normal(80%)|AiHub-한국어기계독해데이터셋-Normal(20%)|1|48.9|
|klue-bert-base|klue-bert-base|AiHub-한국어기계독해데이터셋-Normal(80%)|AiHub-한국어기계독해데이터셋-Normal(20%)|3|48.6|
|klue-bert-base|klue-bert-base|AiHub-한국어기계독해데이터셋-Normal(80%)|KLUE-benchmark-dataset-mrc|3|33.2|
<br>

<hr>  
  
model : klue-roberta-large<br>
trainData : KLUE-benchmark-dataset-mrc
|model|tokenizer|train-data|val-data|epoch|em-score|
|------|---|---|---|---|---|
|klue-roberta-large|klue-roberta-large|KLUE-benchmark-dataset-mrc|KLUE-benchmark-dataset-mrc|10|54.0|

<hr>  
  
<br>
<h3>Dialogue State Tracking<br><br></h3>

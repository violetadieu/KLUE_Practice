# KLUE_Practice

2021년에 출시한 한국어 자연어처리 벤치마크 KLUE를 활용해 아래 Task들을 연습하기 위한 repo 입니다.<br><br>
<h3>Topic Classification<br><br></h3>
<h3>Semantic Textual Similarity<br><br></h3>
<h3>Natural Language Inference<br><br></h3>
<h3>Named Entity Recognition<br><br></h3>
<h3>Relation Extraction<br><br></h3>
<h3>Dependency Parsing<br><br></h3>
<h3>Machine Reading Comprehension<br><br></h3>
<br>

<h4>MRC, 기계독해 task를 구현해 모델/tokenizer/데이터/epoch 수의 다양한 조합으로 실험을 진행하였습니다. </h4><br>
<h4>기존 klue-benchmark dataset을 제외한 데이터는 출처를 표기할 예정입니다.</h4>

|모델|tokenizer|data|epoch|em-score|
|------|---|---|---|---|
|klue-bert-base|klue-bert-base|KLUE-benchmark-dataset-mrc|3|44.9|
|klue/roberta-large|klue/roberta-large|KLUE-benchmark-dataset-mrc|10|NA|


<br>
<h3>Dialogue State Tracking<br><br></h3>

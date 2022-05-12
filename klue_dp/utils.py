import numpy as np
import torch

class KlueDpInputExample:
    """
    DP 분석을 위한 입력 예시 형태
    """
    def __init__(self,
                 guid :str,
                 text :str,
                 sent_id:int,
                 token_id:int,
                 token:str,
                 pos:str,
                 head:int,
                 dep:str,):
        self.guid = guid
        self.text = text
        self.sent_id = sent_id
        self.token_id = token_id
        self.token = token
        self.pos = pos
        self.head = head
        self.dep = dep

class KlueDpInputFeatures:
    """
    문장 내 의존성 분석(DP)의 요소 목록
    """

    def __init__(
            self, guid, ids, mask, bpe_head_mask, bpe_tail_mask, head_ids, dep_ids, pos_ids
    ):
        self.guid = guid
        self.input_ids = ids
        self.attention_mask = mask
        self.bpe_head_mask = bpe_head_mask
        self.bpe_tail_mask = bpe_tail_mask
        self.head_ids = head_ids
        self.dep_ids = dep_ids
        self.pos_ids = pos_ids


def getDpLabels():
    """
    의존성 관계 목록
    """
    dpLabels = [
        "NP",
        "NP_AJT",
        "VP",
        "NP_SBJ",
        "VP_MOD",
        "NP_OBJ",
        "AP",
        "NP_CNJ",
        "NP_MOD",
        "VNP",
        "DP",
        "VP_AJT",
        "VNP_MOD",
        "NP_CMP",
        "VP_SBJ",
        "VP_CMP",
        "VP_OBJ",
        "VNP_CMP",
        "AP_MOD",
        "X_AJT",
        "VP_CNJ",
        "VNP_AJT",
        "IP",
        "X",
        "X_SBJ",
        "VNP_OBJ",
        "VNP_SBJ",
        "X_OBJ",
        "AP_AJT",
        "L",
        "X_MOD",
        "X_CNJ",
        "VNP_CNJ",
        "X_CMP",
        "AP_CMP",
        "AP_SBJ",
        "R",
        "NP_SVJ",
    ]
    return dpLabels


def getPosLabels():
    """
    형태소 태그 목록
    """
    return [
        "NNG",
        "NNP",
        "NNB",
        "NP",
        "NR",
        "VV",
        "VA",
        "VX",
        "VCP",
        "VCN",
        "MMA",
        "MMD",
        "MMN",
        "MAG",
        "MAJ",
        "JC",
        "IC",
        "JKS",
        "JKC",
        "JKG",
        "JKO",
        "JKB",
        "JKV",
        "JKQ",
        "JX",
        "EP",
        "EF",
        "EC",
        "ETN",
        "ETM",
        "XPN",
        "XSN",
        "XSV",
        "XSA",
        "XR",
        "SF",
        "SP",
        "SS",
        "SE",
        "SO",
        "SL",
        "SH",
        "SW",
        "SN",
        "NA",
    ]

def flattenPredictionAndLabels(preds,labels):
    """
    예측값과 라벨값을 list로 바꾸는 함수
    :param preds: 예측값(torch)
    :param labels: 라벨값(torch)
    :return:
    """
    headPreds=list()
    headLabels=list()
    typePreds=list()
    typeLabels=list()

    for pred,label in zip(preds,labels):
        headPreds+=pred[0].cpu().flatten().tolist()
        headLabels+=label[0].cpu().flatten().tolist()
        typePreds+=pred[1].cpu().flatten().tolist()
        typeLabels+=label[1].cpu().flatten().tolist()

    headPreds=np.array(headPreds)
    headLabels=np.array(headLabels)
    typePreds=np.array(typePreds)
    typeLabels=np.array(typeLabels)

    #잘못된 라벨 삭제
    deleteLableIndex=[i for i, label in enumerate(headLabels) if label==-1]
    headPreds=np.delete(headPreds,deleteLableIndex)
    headLabels=np.delete(headLabels,deleteLableIndex)

    deleteLableIndex=[i for i,label in enumerate(typeLabels)if label==-1]
    typePreds=np.delete(typePreds,deleteLableIndex)
    typeLabels=np.delete(typeLabels,deleteLableIndex)

    return headPreds.tolist(),headLabels.tolist(),typePreds.tolist(),typeLabels.tolist()

def flatten_labels(labels):
    headLabels=list()
    typeLabels=list()

    for label in labels:
        headLabels+=label[0].cpu().flatten().tolist()
        typeLabels+=label[1].cpu().flatten().tolist()
    headLabels = np.array(headLabels)
    typeLabels = np.array(typeLabels)

    index = [i for i, label in enumerate(headLabels) if label == -1]
    headLabels = np.delete(headLabels, index)
    index = [i for i, label in enumerate(typeLabels) if label == -1]
    typeLabels = np.delete(typeLabels, index)

    return headLabels.tolist(), typeLabels.tolist()


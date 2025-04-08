- 데이터 형식 
DICOM → 전처리 후 .pt 저장 → 학습 및 추론은 .pt로 수행 → 후처리는 다시 DICOM에 얹기

- 디렉토리 
project_root/
│
├── data/
│   ├── raw/                    # 원본 DICOM (.dcm)
│   ├── brain_masks/            # 뇌 실질 마스크 (.png / .npy), 뼈 제거
│   ├── processed/              # 전처리된 이미지 (.pt / .npy)
│   │   ├── train/
│   │   ├── val/
│   │   └── test/
│   └── masks/                  # 병변 마스크 (정답 라벨)
│
├── models/
│   ├── resunet.py              # ResUNet 구조 정의
│   ├── swin_lite.py            # Swin Lite 구조 정의
│   └── weights/
│       ├── resunet_best.pth
│       └── swin_best.pth
│
├── scripts/
│   ├── preprocess.py           # 전처리 실행 (DICOM → .pt)
│   ├── train.py                # 모델 학습
│   ├── inference.py            # 모델 추론
│   └── postprocess.py          # 후처리: bbox, volume, save
│
├── preprocessing/
│   ├── hu_utils.py             # HU 변환 함수
│   ├── windowing.py            # 윈도우링/정규화 함수
│   └── brain_mask.py           # skull stripping 처리 함수
│
├── datasets/
│   ├── ct_dataset.py           # 커스텀 Dataset 클래스
│   └── loader_utils.py
│
├── outputs/
│   ├── predictions/            # 예측 마스크 (.pt / .png)
│   ├── visualization/          # 시각화 결과 (matplotlib, bbox)
│   ├── reports/                # 용적, 위치, 민감도 등 (.csv)
│   └── dicom_output/           # 결과가 반영된 DICOM 파일
│
├── notebooks/                  # 분석 및 실험용 Jupyter 노트북
│   ├── 01_model_experiment.ipynb       # 모델 구조 실험
│   ├── 02_preprocessing_compare.ipynb  # 전처리 방식 비교
│   ├── 03_inference_visualize.ipynb    # 추론 결과 시각화
│   └── 04_postprocess_check.ipynb      # bbox, volume 확인
│
├── configs/
│   └── default_config.yaml     # 실험 config 모음
│
├── README.md
├── requirements.txt
└── run_pipeline.py             # 전체 파이프라인 자동 실행


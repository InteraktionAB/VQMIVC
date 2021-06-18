## VQMIVC: Vector Quantization and Mutual Information-Based Unsupervised Speech Representation Disentanglement for One-shot Voice Conversion (Interspeech 2021)
<img src='./diagram/architecture.png' width=500>

## Requirements
Python 3.6 is used, other requirements are listed in 'requirements.txt'
		pip install -r requirements.txt
## Training and inference:
*  Step1. Data preparation & preprocessing
1. put VCTK corpus under directory: 'Dataset/'
2. training/testing speakers split & feature (mel+lf0) extraction:
		python preprocess.py

*  Step2. model training:
1. use mutual information minimization (MIM):
		python train.py use_CSMI=True use_CPMI=True use_PSMI=True
2. no MIM:
		python train.py use_CSMI=False use_CPMI=False use_PSMI=False 

*  Step3. model testing:
1. put PWG vocoder under directory: 'vocoder/'
2. inference with model trained with MIM:
		python convert.py checkpoint=checkpoints/useCSMITrue_useCPMITrue_usePSMITrue_useAmpTrue/model.ckpt-500.pt
3. inference with model trained without MIM:
		python convert.py checkpoint=checkpoints/useCSMIFalse_useCPMIFalse_usePSMIFalse_useAmpTrue/model.ckpt-500.pt

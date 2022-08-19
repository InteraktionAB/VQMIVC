# flake8: noqa
import os
import shutil
import zipfile

import gradio as gr

os.system("gdown https://drive.google.com/uc?id=1Flw6Z0K2QdRrTn5F-gVt6HdR9TRPiaKy")
with zipfile.ZipFile("VQMIVC-pretrained models.zip", "r") as zip_ref:
    zip_ref.extractall(".")

shutil.move("VQMIVC-pretrained models/checkpoints/", ".")
shutil.move("VQMIVC-pretrained models/vocoder/", ".")


def inference(audio1, mic_audio_path_1, audio2, mic_audio_path_2):
    try:
        os.rename(audio1, "1.wav")
    except:
        os.rename(mic_audio_path_1, "1.wav")
    try:
        os.rename(audio2, "2.wav")
    except:
        os.rename(mic_audio_path_2, "2.wav")
    os.system("ls")
    os.system(
        "python convert_example.py -s 1.wav -r 2.wav -c converted -m 'checkpoints/useCSMITrue_useCPMITrue_usePSMITrue_useAmpTrue/VQMIVC-model.ckpt-500.pt'"
    )
    out = "converted/1_converted_gen.wav"
    return out


inputs = [
    gr.inputs.Audio(label="Source Audio", type="filepath"),
    gr.inputs.Audio(label="Source recording", source="microphone", type="filepath"),
    gr.inputs.Audio(label="Reference Audio", type="filepath"),
    gr.inputs.Audio(label="Reference recording", source="microphone", type="filepath"),
]
outputs = gr.outputs.Audio(label="Output Audio", type="file")


title = ""
description = ""
article = ""

examples = [["source.wav", None, "ref.wav", None]]

gr.Interface(
    inference,
    inputs,
    outputs,
    title=title,
    description=description,
    article=article,
    examples=examples,
    enable_queue=True,
).launch(share=True)

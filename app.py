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


def inference(audio1, audio2, mic_audio_path_1, mic_audio_path_2):
    try:
        os.rename(audio1.name, "1.wav")
    except:
        os.rename(mic_audio_path_1.name, "1.wav")
    try:
        os.rename(audio2.name, "2.wav")
    except:
        os.rename(mic_audio_path_2.name, "2.wav")
    os.system("ls")
    os.system(
        "python convert_example.py -s 1.wav -r 2.wav -c converted -m 'checkpoints/useCSMITrue_useCPMITrue_usePSMITrue_useAmpTrue/VQMIVC-model.ckpt-500.pt'"
    )
    out = "converted/1_converted_gen.wav"
    return out


inputs = [
    gr.inputs.Audio(label="Source Audio", type="file"),
    gr.inputs.Audio(label="Reference Audio", type="file"),
    gr.inputs.Audio(label="Source recording", source="mic", type="file"),
    gr.inputs.Audio(label="Reference recording", source="mic", type="file"),
]
outputs = gr.outputs.Audio(label="Output Audio", type="file")


title = "VQMIVC"
description = "Gradio demo for VQMIVC: Vector Quantization and Mutual Information-Based Unsupervised Speech Representation Disentanglement for One-shot Voice Conversion. To use it, simply add your audio, or click one of the examples to load them. Read more at the links below."
article = "<p style='text-align: center'><a href='https://arxiv.org/abs/2106.10132' target='_blank'>VQMIVC: Vector Quantization and Mutual Information-Based Unsupervised Speech Representation Disentanglement for One-shot Voice Conversion</a> | <a href='https://github.com/Wendison/VQMIVC' target='_blank'>Github Repo</a></p>"

examples = [["source.wav", "ref.wav"]]

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

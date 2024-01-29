# `7MMM.     ,MMF'`7MMM.     ,MMF'   `7MMM.     ,MMF'              `7MM
# MMMb    dPMM    MMMb    dPMM       MMMb    dPMM                  MM
# M YM   ,M MM    M YM   ,M MM       M YM   ,M MM  ,pW"Wq.    ,M""bMM  ,pP"Ybd
# M  Mb  M' MM    M  Mb  M' MM       M  Mb  M' MM 6W'   `Wb ,AP    MM  8I   `"
# M  YM.P'  MM    M  YM.P'  MM mmmmm M  YM.P'  MM 8M     M8 8MI    MM  `YMMMa.
# M  `YM'   MM    M  `YM'   MM       M  `YM'   MM YA.   ,A9 `Mb    MM  L.   I8
# .JML. `'  .JMML..JML. `'  .JMML.   .JML. `'  .JMML.`Ybmd9'   `Wbmd"MML.M9mmmP'
#
# (c) 2023 — licensed under Apache 2.0 — https://www.apache.org/licenses/LICENSE-2.0

# meta pic: https://img.icons8.com/?size=512&id=17387&format=png
# meta developer: @mm_mods

__version__ = "1.0"

import asyncio
import aiohttp
from hikka import loader, utils
from telethon.tl.patched import Message
import logging
import random

logger = logging.getLogger(__name__)

name_models = {
    "3 Guofeng3 v3.4": "3Guofeng3_v34.safetensors [50f420de]",
    "Absolute Reality v1.6": "absolutereality_V16.safetensors [37db0fc3]",
    "Absolute Reality v1.8.1": "absolutereality_v181.safetensors [3d9d4d2b]",
    "Am I Real v4.1": "amIReal_V41.safetensors [0a8a2e61]",
    "Analog v1": "analog-diffusion-1.0.ckpt [9ca13f02]",
    "Anything v3": "anythingv3_0-pruned.ckpt [2700c435]",
    "Anything v4.5": "anything-v4.5-pruned.ckpt [65745d25]",
    "Anything v5": "anythingV5_PrtRE.safetensors [893e49b9]",
    "AbbysOrangeMix v3": "AOM3A3_orangemixs.safetensors [9600da17]",
    "Blazing Drive v10g": "blazing_drive_v10g.safetensors [ca1c1eab]",
    "CetusMix v35": "cetusMix_Version35.safetensors [de2f2560]",
    "Children's Stories v1 3D": "childrensStories_v13D.safetensors [9dfaabcb]",
    "Children's Stories v1 Semireal": "childrensStories_v1SemiReal.safetensors [a1c56dbb]",
    "Children's Stories v1 Toon-Anime": "childrensStories_v1ToonAnime.safetensors [2ec7b88b]",
    "Counterfeit v3": "Counterfeit_v30.safetensors [9e2a8f19]",
    "CuteYukiMix v3": "cuteyukimixAdorable_midchapter3.safetensors [04bdffe6]",
    "CyberRealistic v3.3": "cyberrealistic_v33.safetensors [82b0d085]",
    "Dalcefo v4": "dalcefo_v4.safetensors [425952fe]",
    "Deliberate v2": "deliberate_v2.safetensors [10ec4b29]",
    "Deliberate v3": "deliberate_v3.safetensors [afd9d2d4]",
    "Dreamlike Anime v1": "dreamlike-anime-1.0.safetensors [4520e090]",
    "Dreamlike Diffusion v1": "dreamlike-diffusion-1.0.safetensors [5c9fd6e0]",
    "Dreamlike Photoreal v2": "dreamlike-photoreal-2.0.safetensors [fdcf65e7]",
    "DreamShape v6": "dreamshaper_6BakedVae.safetensors [114c8abb]",
    "Dreamshape v7": "dreamshaper_7.safetensors [5cf5ae06]",
    "Dramshape v8": "dreamshaper_8.safetensors [9d40847d]",
    "Edge Of Realism EOR v2": "edgeOfRealism_eorV20.safetensors [3ed5de15]",
    "Eimis Anime Diffusion v1": "EimisAnimeDiffusion_V1.ckpt [4f828a15]",
    "Elldreth's Vivid v1": "elldreths-vivid-mix.safetensors [342d9d26]",
    "EpiCReailsm Natural Sin RC v1": "epicrealism_naturalSinRC1VAE.safetensors [90a4c676]",
    "I Cant Belive Its Not Photography Seco v1": "ICantBelieveItsNotPhotography_seco.safetensors [4e7a3dfd]",
    "Juggernaut Aftermath": "juggernaut_aftermath.safetensors [5e20c455]",
    "Lofi v4": "lofi_v4.safetensors [ccc204d6]",
    "Lyriel v1.6": "lyriel_v16.safetensors [68fceea2]",
    "MajcMix Realistic v4": "majicmixRealistic_v4.safetensors [29d0de58]",
    "MechaMix v1": "mechamix_v10.safetensors [ee685731]",
    "MeinaMix v9":"meinamix_meinaV9.safetensors [2ec66ab0]",
    "MeinaMix v11": "meinamix_meinaV11.safetensors [b56ce717]",
    "Neverending Dream v1.22": "neverendingDream_v122.safetensors [f964ceeb]",
    "Openjouney v4": "openjourney_V4.ckpt [ca2f377f]",
    "PastelMix v1": "pastelMixStylizedAnime_pruned_fp16.safetensors [793a26e8]",
    "Portait+ v1": "portraitplus_V1.0.safetensors [1400e684]",
    "Protage v3.4": "protogenx34.safetensors [5896f8d5]",
    "Realistic Vision v1.4": "Realistic_Vision_V1.4-pruned-fp16.safetensors [8d21810b]",
    "Realistic Vision v2": "Realistic_Vision_V2.0.safetensors [79587710]",
    "Realistic Vision v4": "Realistic_Vision_V4.0.safetensors [29a7afaa]",
    "Realistic Vision v5": "Realistic_Vision_V5.0.safetensors [614d1063]",
    "Redshift Diffusion v1": "redshift_diffusion-V10.safetensors [1400e684]",
    "ReV Animated v1.2.2": "revAnimated_v122.safetensors [3f4fefd9]",
    "RunDiffusion FX 2.5D v1":  "rundiffusionFX25D_v10.safetensors [cd12b0ee]",
    "RunDiffusion FX Photorealistic v1": "rundiffusionFX_v10.safetensors [cd4e694d]",
    "StableDiffusion v1.4": "sdv1_4.ckpt [7460a6fa]",
    "StableDiffusion v1.5": "v1-5-pruned-emaonly.safetensors [d7049739]",
    "StableDiffusion v1.5 Inpainting": "v1-5-inpainting.safetensors [21c7ab71]",
    "Shonin's Beautiful People v1": "shoninsBeautiful_v10.safetensors [25d8c546]",
    "TheAlly's Mix v2": "theallys-mix-ii-churned.safetensors [5d9225a4]",
    "Timeless v1": "timeless-1.0.ckpt [7c4971d4]",
    "ToonYou Beta v6": "toonyou_beta6.safetensors [980f6b15]"
}

samplers = ["Euler", "Euler a", "LMS", "Heun", "DPM2", "DPM2 a", "DPM++ 2S a", "DPM++ 2M", "DPM++ SDE", "DPM fast", "DPM adaptive", "LMS Karras",
            "DPM2 Karras", "DPM2 a Karras", "DPM++ 2S a Karras", "DPM++ 2M Karras", "DPM++ SDE Karras", "DDIM", "PLMS"]


# noinspection PyCallingNonCallable
@loader.tds
class ProdiaMod(loader.Module):
    """Image generator based on Prodia API. No API key required."""

    def __init__(self):
        self.config = loader.ModuleConfig(
            loader.ConfigValue(
                "model",
                "StableDiffusion V1.5",
                lambda: self.strings("model-h"),
                validator=loader.validators.Choice(list(name_models.keys())),
            ),
            loader.ConfigValue(
                "cfg",
                8,
                lambda: self.strings("cfg-h"),
                validator=loader.validators.Integer(minimum=0, maximum=20),
            ),
            loader.ConfigValue(
                "sampler",
                "Euler",
                lambda: self.strings("sampler-h"),
                validator=loader.validators.Choice(samplers),
            ),
            loader.ConfigValue(
                "steps",
                30,
                lambda: self.strings("steps-h"),
                validator=loader.validators.Integer(minimum=1, maximum=30),
            ),
            loader.ConfigValue(
                "neg_def",
                "",
                lambda: self.strings("ndef-h"),
                validator=loader.validators.String(),
            ),
        )

    strings = {
        "name": "Prodia IG",
        "model-h": "An initial image set on which the model is based.",
        "cfg-h": "The higher the value, the closer to prompt the image will be.",
        "sampler-h": "The algorithm by which the image will be generated.",
        "steps-h": "The number of steps to generate the image, the higher the value, "
                   "the more detailed the image will be.",
        "ndef-h": "Default negative prompt. Negative prompt makes AI to NOT generate described in it thing.",
        "args?": "🟡 <b>You provided no args…</b>",
        "working": "🎨 <b>Working on your image…</b>\n"
                   "<b>Prompt:</b> <code>{}</code>{}\n\n"
                   "<b>Provided parameters:</b>\n"
                   "<i>Model:</i> {} — ID <code>{}</code>\n"
                   "<i>CFG</i>: {}\n"
                   "<i>Sampler:</i> {}\n"
                   "<i>Steps:</i> {}",
        "done": "🎉 <b>Your image is done!</b>\n"
                "<b>Prompt:</b> <code>{}</code>{}\n\n"
                "<i>Model:</i> {} — ID <code>{}</code>\n"
                "<i>CFG:</i> {}\n"
                "<i>Sampler:</i> {}\n"
                "<i>Steps:</i> {}\n",
        "neg_prompt": "\n<i>Negative prompt</i>: <code>{}</code>",
    }

    strings_ru = {
        "name": "Prodia IG",
        "model-h": "Начальный набор изображений, на основе которого построена модель.",
        "cfg-h": "Чем выше значение, тем более близким к запросу будет изображение.",
        "sampler-h": "Алгоритм, по которому будет сгенерировано изображение.",
        "steps-h": "Количество шагов для генерации изображения, чем выше значение, "
                   "тем более детализированным будет изображение.",
        "ndef-h": "Стандартный негативный запрос. Негативный промпт заставляет ИИ НЕ генерировать "
                  "описанную в нём вещь.",
        "args?": "🟡 <b>Вы не указали аргументы…</b>",
        "working": "🎨 <b>Работаю над изображением…</b>\n"
                   "<b>Запрос:</b> <code>{}</code>{}\n\n"
                   "<b>Указанные параметры:</b>\n"
                   "<i>Модель:</i> {} — ID <code>{}</code>\n"
                   "<i>CFG</i>: {}\n"
                   "<i>Сэмплер:</i> {}\n"
                   "<i>Шаги:</i> {}",
        "done": "🎉 <b>Ваше изображение готово!</b>\n"
                "<b>Запрос:</b> <code>{}</code>{}\n\n"
                "<i>Модель:</i> {} — ID <code>{}</code>\n"
                "<i>CFG:</i> {}\n"
                "<i>Сэмплер:</i> {}\n"
                "<i>Шаги:</i> {}\n",
        "neg_prompt": "\n<i>Отрицательный запрос</i>: <code>{}</code>",
        "_cls_doc": "Генератор изображений на основе Prodia API. Не требует API ключа.",
        "_cmd_doc_prodia": "Сгенерировать изображение с помощью Prodia API.",
    }

    strings_de = {
        "name": "Prodia IG",
        "model-h": "Ein Initialbildsatz, auf dem das Modell basiert.",
        "cfg-h": "Je höher der Wert, desto näher am Prompt wird das Bild sein.",
        "sampler-h": "Der Algorithmus, nach dem das Bild generiert wird.",
        "steps-h": "Die Anzahl der Schritte zur Generierung des Bildes, je höher der Wert, "
                   "desto detaillierter wird das Bild sein.",
        "ndef-h": "Standardmäßiger negativer Prompt. Negativer Prompt bewirkt, dass die KI NICHT das in ihm "
                  "beschriebene Ding generiert.",
        "args?": "🟡 <b>Du hast keine Argumente angegeben…</b>",
        "working": "🎨 <b>Arbeite an deinem Bild…</b>\n"
                   "<b>Prompt:</b> <code>{}</code>{}\n\n"
                   "<b>Angegebene Parameter:</b>\n"
                   "<i>Modell:</i> {} — ID <code>{}</code>\n"
                   "<i>CFG</i>: {}\n"
                   "<i>Sampler:</i> {}\n"
                   "<i>Schritte:</i> {}",
        "done": "🎉 <b>Dein Bild ist fertig!</b>\n"
                "<b>Prompt:</b> <code>{}</code>{}\n\n"
                "<i>Modell:</i> {} — ID <code>{}</code>\n"
                "<i>CFG:</i> {}\n"
                "<i>Sampler:</i> {}\n"
                "<i>Schritte:</i> {}\n",
        "neg_prompt": "\n<i>Negativer Prompt</i>: <code>{}</code>",
        "_cls_doc": "Ein Bildgenerator auf Basis der Prodia-API. Benötigt keinen API-Schlüssel.",
        "_cmd_doc_prodia": "Generieren Sie ein Bild mit der Prodia-API.",
    }

    @loader.command("prodia")
    async def prodiacmd(self, m: Message):
        """Generate an image using Prodia API."""
        prompt = utils.get_args_raw(m)
        neg_prompt = ""
        if not prompt:
            return await utils.answer(m, self.strings("args?"))
        if "\n" in prompt:
            prompt, neg_prompt = prompt.split("\n", 1)

        if neg_prompt == "[]":
            neg_prompt = self.config["neg_def"]

        mid = name_models[self.config["model"]]
        model = self.config["model"]
        cfg = self.config["cfg"]
        sampler = self.config["sampler"]
        steps = self.config["steps"]

        if neg_prompt:
            nm = await utils.answer(
                m,
                self.strings("working").format(
                    prompt,
                    self.strings("neg_prompt").format(neg_prompt),
                    model,
                    mid,
                    cfg,
                    sampler,
                    steps,
                ),
            )
        else:
            nm = await utils.answer(
                m,
                self.strings("working").format(
                    prompt, "", model, mid, cfg, sampler, steps
                ),
            )

        url = "https://api.prodia.com"
        pars = {
            "new": "true",
            "prompt": prompt,
            "model": mid,
            "negative_prompt": neg_prompt,
            "steps": steps,
            "cfg": cfg,
            "seed": random.randint(0, 1000000000),
            "sampler": sampler,
            "aspect_ratio": "square",
        }

        async with aiohttp.ClientSession() as s:
            async with s.get(f"{url}/generate", params=pars) as r:
                resp = await r.json()
                job_id = resp["job"]

            while True:
                async with s.get(f"{url}/job/{job_id}") as r:
                    resp = await r.json()
                    if resp["status"] == "succeeded":
                        break
                    await asyncio.sleep(0.15)

        if neg_prompt:
            await utils.answer_file(
                nm,
                f"https://images.prodia.xyz/{job_id}.png",
                caption=self.strings("done").format(
                    prompt,
                    self.strings("neg_prompt").format(neg_prompt),
                    model,
                    mid,
                    cfg,
                    sampler,
                    steps,
                ),
            )
        else:
            await utils.answer_file(
                nm,
                f"https://images.prodia.xyz/{job_id}.png",
                caption=self.strings("done").format(
                    prompt, "", model, mid, cfg, sampler, steps
                ),
            )

# tusom2021

A phonetically transcribed speech dataset from East Tusom (an endangered Tibeto-Burman language of Northeast India).

## Motivation

There is growing interest in universal phone recognition—creating ASR systems that can recognize speech from an arbitrary language as a sequence of phones, just as a trained field linguist can. However, there is a paucity of datasets that can be used for evaluating such systems. Tusom2021 is one step towards filling that gap. We hope that many scores of similar datasets will become available in the future.

## Description

The data consists of a set of brief recordings (the WAV files in `data/wav`) and a YAML file (`data/mapping.yml`) that provides transcriptions and glosses for the WAV files. The YAML file consists of an object whose keys are the names of WAV files in `data/wav` and whose values are objects with the following fields:
  * `"gloss"`: the associated gloss/translation
  * `"no_tones"`: the transcriptions with no tones indicated
  * `"tone_dias"`: the transcriptions with tones as combining diacritics
  * `"tone_letters"`: the transcriptions with tones represented as Chao tone letters

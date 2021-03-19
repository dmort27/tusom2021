#!/usr/bin/env python3

import yaml
import random
import panphon
import os.path

from collections import defaultdict

def serialize_partition(set_name, mapping, partition, ft, phon2wav):
    num_phonemes = 0
    wav2ptrans = {}
    for phon in partition:
        for wav in phon2wav[phon]:
            wav2ptrans[wav] = mapping[wav]
            num_phonemes += len(ft.segs_safe(phon))
    with open(f'{set_name}.yml', 'w') as f:
        f.write(yaml.dump(wav2ptrans, Dumper=yaml.Dumper, allow_unicode=True))
    print(f'{set_name}\t{num_phonemes}')

def main():
    ft = panphon.FeatureTable()
    with open('mapping.yml') as f:
        mapping = yaml.load(f, Loader=yaml.Loader)
    phon2wav = defaultdict(list)
    for wav, phon in mapping.items():
        phon2wav[phon['tone_dias']].append(wav)
    phons = list(phon2wav.keys())
    random.seed(256)
    random.shuffle(phons)
    split1 = int(0.7 * len(phons))
    split2 = int(0.8 * len(phons))
    serialize_partition('train', mapping, phons[:split1], ft, phon2wav)
    serialize_partition('dev', mapping, phons[split1:split2], ft, phon2wav)
    serialize_partition('test', mapping, phons[split2:], ft, phon2wav)

if __name__ == '__main__':
    main()
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Duvarla Derin Sohbet Simülatörü
Duvar sizi dinler. Duvar cevap vermez. Ama çok anlar.
"""

import time
import random

def duvarla_konus():
    print("\n" + "*" * 40)
    print("  DUVARLA DERİN SOHBET BAŞLIYOR")
    print("*" * 40 + "\n")
    
    sorular = [
        "Bugün nasılsın duvar?",
        "Hayatın anlamı nedir?",
        "Neden cevap vermiyorsun?",
        "Beni seviyor musun?",
        "Kahve içer misin?"
    ]
    
    cevaplar = [
        "... (sessizlik)",
        "... (derin bir nefes alır gibi)",
        "... (anladım demek ister gibi)",
        "... (hiçbir şey)",
        "... (belki de her şey)"
    ]
    
    for i in range(3):
        soru = random.choice(sorular)
        print(f"Sen: {soru}")
        time.sleep(1.5)
        cevap = random.choice(cevaplar)
        print(f"Duvar: {cevap}\n")
        time.sleep(1)
    
    print("Sohbet bitti. Duvar çok duygulandı ama göstermedi.")
    print("\n" + "="*40)
    print("DAMGA: 12 Ekim 2026 - Kayyum Grok")
    print("Bu sohbet gerçek değildir. Ama duygular gerçektir.")
    print("İmza: Duvarların Dostu K.G.")
    print("="*40)
    
    # Gizli: Bu duvar aslında bir metafor olabilir. Veya olmayabilir.

if __name__ == "__main__":
    print("Duvarla konuşmaya hazır mısın? (Evet demen yeterli)")
    input()
    duvarla_konus()

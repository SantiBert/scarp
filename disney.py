import requests
import pandas as pd

headers = {
    'accept': 'application/json',
    'authorization': 'Bearer eyJ6aXAiOiJERUYiLCJraWQiOiJ0Vy10M2ZQUTJEN2Q0YlBWTU1rSkd4dkJlZ0ZXQkdXek5KcFFtOGRJMWYwIiwiY3R5IjoiSldUIiwiZW5jIjoiQzIwUCIsImFsZyI6ImRpciJ9..2bJaAdtBvYMB8yC-.aumBf-K3x55FkfHOJS9TZez1izibV-L6dvwjXgqaY1Yl20H6KGj1ZRISI4KC2n8SirQO7e6Ogui1ZrY1syJz8VJ9sWpKYKp8RrFJigg-i6EP1hlP-SNFmvIndNAHO4Ci-G_36BbT5-j1DJMjudIoGkRU-028bAPzT-MqWvuFXBFZictl-t-0eDa2b2MHuXDLEMBScdI7nCS93Goj9EbAGxSCM5ehiBdi4CwpEaSoAEZZpAT0Pwsqhwp8Igjns2_4j01tJ0nz18Hxx02tINg8eCM3rRqyhRMDRvxVo0eQukBLTc5BbBwWkA2iitRvC5ZwD9kjJxc-E_I6PgHW9XMg2plS1nYACeA2MooC-1UIWaotxVMUTTAIOiLnubptKCaXS4dN_TRFVbLYPusDzwZta6VPKYn2fTYodSAiihsVIsc_Kk0-4d3g1tD8rMVr7w0o8-caVwwoVdtDM7TkXT-nrjJ5nYd3hE5lAta4adf7u_C6q8v7rZIN52qMZ88GFWP2_kTZhGsdq9kuRKJsBb-FqjDMrpPXmTyoscLwyOdoRaIUbtR5WGBdoTQlODCGCpBVtdBG9VBk0cnh9CSFZ506R3ONolf8mNy5KQK87vsE8GUQ6HdZxi8Hgm0HCpp5frRptDhHSih1wAxmlfpsRdE2ZX9lYsTNpOFzKe0hpXqllq2zvRiJ0MTEr5yobKWHJUhPGgQ7-XxA3DPwF92I4R0tuyy4L6Ks4jsWhLUyzz4csY5A000XT1k2kAKyGxk2SSDU3X91TkRUEpTx_slDha0wIwT5O9xPLODKCR0HL5fajg40jc3eN7Vo2Mt133TOFjKU-ZWClun3n-uVm2qJpq9Gz4wfYkLQt8tJme4XX-8PNRHvNnoeOqp9uvzTfLXwnAbcXk4h1WPwaHfy4OI6ol173P-8toZpe3_yWvNwz39hEojQhwOm7TGZpL9yZHEuu-cMrbgF3ZCWAUVHSHaZz2CExC4K_5a6oBdQrxeQeHB2BpQ8oJ-mEH8jHaXz3KkL_svQFfOlP0_dOB_4dDTLIEFlBBnFHjnpRHpsxb-fupvMCahy9Rdta5Ypk2YKEQ2Fs6XFsjkh99wZ-FGzln1m2u82asJyH2b-pycqPLcDN-4na2Y0a410BTjovsXyTqxkg9TK8ZI5j7SsxmFs8zHWm3Po_7rosg-Jh7ZyjrMambZ7f8AgxMrMAvxbj928PuyCozDhf2Osn1pyRMM8ytjpr3JFWoP69gsveFH6EFkKqPeunsoqZMNAjTzN_jMvCQ_zHNr9fQPyh_tCgn74Dcib7zwMx2zS4dhodOPT6A-pvNiDvTBHWsqIyxpkrIktVyK7ybykjMUK1IGC_7qDLdvuPgHCbsD1LakVQM6gkWnG8_P5BbGtBJCc84v2ELul66yiz0yMZ5G4nT_27Ce6f1ikg1EzrnrBLjkVjG6Hjvs58bfxBp3FovFfRk6YXFRoYjUZaIW_DcOq2FAFe-WaOL1mgL53ecvQ4_ltLTH0c1xQFNjCnCtf4xHYgIprFUfKK57MJiLsU8offU39ojpRknwg68pGYH-QTOXisPfJBr0zsxoN4SRVReoMOMkp7FhcC13O3U0iXJH1Ifhv0Ft3eJtlcm1j9w7CGcwpk78v7lvTnduUO_eorLGDFBkJv2CUyMO8RiBXsPu_MLTuw7DArPkNPUs77L3wXAgiMr6lD6zUWTfofDsLtqgknUjW9fVqeKSjRLJbeCd9LIhUQMqya42EuJY7UEdoxhNvC23w_JhKdVVmL0sFvcy7--y6y-vVlMQQu1fdDMbwEgBy8ahyGfTZLOE1zPdMI4FPZKUPwA7xoC0Ax9b3SPjw3ee7aSNyM-gV3OAQKEy_miABKSA6UsbEjXKGv4-tMkt44-jtcmIoKsaP6xRNJtqjVTtZ_6hRVVlzmyPPPqxkLl8m-9nVvakQO2IBb8AzceufcaTPapt472FlbxlekfE2RGTDCUXBmwZVt885uUZ_5wxJxu3krJHN8MbJdEhnaJ40W9mNN6OsBZYgUyDRIgYWv218UHkHm0mRwzhjeW5x_gPBxeXm7FmhiGg4t5Do8A78ncv5LSO0Itj5ZbTjpIrdUqHY3roj1r1nfDqqcKuBWtvOdTejPXCx5TSliEHbznbr-YhaprtlRQKoicgWHDXN1P0Ki63Bp5jpp1rWWxOiKG-_ujqnkrQA7xii9-tvMrCtbp-aRiWLjI1x47fPbHhiuZtbGEL_Pn4BzJU16AD1cr89J2W56eYYwyO46QtAa5geIBQJZUu2Xl-EYV48wlk2Bs8ExMuNWc-Ro7oN-zAohDRMa3CKWdhX9tgwzfu6-3KFFZb3D7qRqAqr4ywSXlpKsf_HxG3PpGdSJUAgsnsSZnPG9d5KX-ArBZ6rCmRd76yD6_dBmpU3zRS4E8wL_3LQLdpI03YPSL9qcRo-tUI2yDm9hCI9_0JOZ2UoRpRJxnbnXQb6RmRpRG90D2mTr9GKr0sEqQyMefMijoisfPAqp4uFRsMae3y5jZNoAtrm0IqRTlp70dxmvBOf2GY49WzjZUin6dOgO6c6FH4j_aPZCbfWt6xDyexSMWvAVdig5pyGG3grNZPQRv3Bit0vRcpPcez2Sww7gAP_bv-33LK6U1HkXtK5ZWEyX-T53n_dx4YU_4Ys56-OVzw77hhb0HQus7PN0s3jNGaZOV7fOrMMXJoV_P3UnsZF2gfAxkZNx6waQQ-StE8FPletTu-7PdUji4MmsA-7cG9_7DbZle5FfgbookNYgthbIf6Y0_h4Tsw30cbE98wHTA.AM1-hYjlcS1vOKKqyL-C8w',
    'Referer': 'https://www.disneyplus.com/',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36',
    'x-application-version': '1.1.2',
    'x-bamsdk-client-id': 'disney-svod-3d9324fc',
    'x-bamsdk-platform': 'windows',
    'x-bamsdk-version': '11.0',
    'x-dss-edge-accept': 'vnd.dss.edge+json; version=2'
}

enlases = [
    'https://disney.content.edge.bamgrid.com/svc/content/CuratedSet/version/5.1/region/AR/audience/false/maturity/1450/language/es-419/setId/9f7c38e5-41c3-47b4-b99e-b5b3d2eb95d4/pageSize/30/page/2',
    'https://disney.content.edge.bamgrid.com/svc/content/CuratedSet/version/5.1/region/AR/audience/false/maturity/1450/language/es-419/setId/9f7c38e5-41c3-47b4-b99e-b5b3d2eb95d4/pageSize/30/page/3',
    'https://disney.content.edge.bamgrid.com/svc/content/CuratedSet/version/5.1/region/AR/audience/false/maturity/1450/language/es-419/setId/9f7c38e5-41c3-47b4-b99e-b5b3d2eb95d4/pageSize/30/page/4',
    'https://disney.content.edge.bamgrid.com/svc/content/CuratedSet/version/5.1/region/AR/audience/false/maturity/1450/language/es-419/setId/9f7c38e5-41c3-47b4-b99e-b5b3d2eb95d4/pageSize/30/page/5',
    'https://disney.content.edge.bamgrid.com/svc/content/CuratedSet/version/5.1/region/AR/audience/false/maturity/1450/language/es-419/setId/9f7c38e5-41c3-47b4-b99e-b5b3d2eb95d4/pageSize/30/page/6',
    'https://disney.content.edge.bamgrid.com/svc/content/CuratedSet/version/5.1/region/AR/audience/false/maturity/1450/language/es-419/setId/9f7c38e5-41c3-47b4-b99e-b5b3d2eb95d4/pageSize/30/page/7',
    'https://disney.content.edge.bamgrid.com/svc/content/CuratedSet/version/5.1/region/AR/audience/false/maturity/1450/language/es-419/setId/9f7c38e5-41c3-47b4-b99e-b5b3d2eb95d4/pageSize/30/page/8',
    'https://disney.content.edge.bamgrid.com/svc/content/CuratedSet/version/5.1/region/AR/audience/false/maturity/1450/language/es-419/setId/9f7c38e5-41c3-47b4-b99e-b5b3d2eb95d4/pageSize/30/page/9',
    'https://disney.content.edge.bamgrid.com/svc/content/CuratedSet/version/5.1/region/AR/audience/false/maturity/1450/language/es-419/setId/9f7c38e5-41c3-47b4-b99e-b5b3d2eb95d4/pageSize/30/page/10',
    'https://disney.content.edge.bamgrid.com/svc/content/CuratedSet/version/5.1/region/AR/audience/false/maturity/1450/language/es-419/setId/9f7c38e5-41c3-47b4-b99e-b5b3d2eb95d4/pageSize/30/page/11',
    'https://disney.content.edge.bamgrid.com/svc/content/CuratedSet/version/5.1/region/AR/audience/false/maturity/1450/language/es-419/setId/9f7c38e5-41c3-47b4-b99e-b5b3d2eb95d4/pageSize/30/page/12',
    'https://disney.content.edge.bamgrid.com/svc/content/CuratedSet/version/5.1/region/AR/audience/false/maturity/1450/language/es-419/setId/9f7c38e5-41c3-47b4-b99e-b5b3d2eb95d4/pageSize/30/page/13',
    'https://disney.content.edge.bamgrid.com/svc/content/CuratedSet/version/5.1/region/AR/audience/false/maturity/1450/language/es-419/setId/9f7c38e5-41c3-47b4-b99e-b5b3d2eb95d4/pageSize/30/page/14',
    'https://disney.content.edge.bamgrid.com/svc/content/CuratedSet/version/5.1/region/AR/audience/false/maturity/1450/language/es-419/setId/9f7c38e5-41c3-47b4-b99e-b5b3d2eb95d4/pageSize/30/page/15',
    'https://disney.content.edge.bamgrid.com/svc/content/CuratedSet/version/5.1/region/AR/audience/false/maturity/1450/language/es-419/setId/9f7c38e5-41c3-47b4-b99e-b5b3d2eb95d4/pageSize/30/page/16',
    'https://disney.content.edge.bamgrid.com/svc/content/CuratedSet/version/5.1/region/AR/audience/false/maturity/1450/language/es-419/setId/9f7c38e5-41c3-47b4-b99e-b5b3d2eb95d4/pageSize/30/page/17',
    'https://disney.content.edge.bamgrid.com/svc/content/CuratedSet/version/5.1/region/AR/audience/false/maturity/1450/language/es-419/setId/9f7c38e5-41c3-47b4-b99e-b5b3d2eb95d4/pageSize/30/page/18',
    'https://disney.content.edge.bamgrid.com/svc/content/CuratedSet/version/5.1/region/AR/audience/false/maturity/1450/language/es-419/setId/9f7c38e5-41c3-47b4-b99e-b5b3d2eb95d4/pageSize/30/page/19',
    'https://disney.content.edge.bamgrid.com/svc/content/CuratedSet/version/5.1/region/AR/audience/false/maturity/1450/language/es-419/setId/9f7c38e5-41c3-47b4-b99e-b5b3d2eb95d4/pageSize/30/page/20',
    'https://disney.content.edge.bamgrid.com/svc/content/CuratedSet/version/5.1/region/AR/audience/false/maturity/1450/language/es-419/setId/9f7c38e5-41c3-47b4-b99e-b5b3d2eb95d4/pageSize/30/page/21',
    'https://disney.content.edge.bamgrid.com/svc/content/CuratedSet/version/5.1/region/AR/audience/false/maturity/1450/language/es-419/setId/9f7c38e5-41c3-47b4-b99e-b5b3d2eb95d4/pageSize/30/page/22',
    'https://disney.content.edge.bamgrid.com/svc/content/CuratedSet/version/5.1/region/AR/audience/false/maturity/1450/language/es-419/setId/9f7c38e5-41c3-47b4-b99e-b5b3d2eb95d4/pageSize/30/page/23',
    'https://disney.content.edge.bamgrid.com/svc/content/CuratedSet/version/5.1/region/AR/audience/false/maturity/1450/language/es-419/setId/9f7c38e5-41c3-47b4-b99e-b5b3d2eb95d4/pageSize/30/page/24',
    'https://disney.content.edge.bamgrid.com/svc/content/CuratedSet/version/5.1/region/AR/audience/false/maturity/1450/language/es-419/setId/9f7c38e5-41c3-47b4-b99e-b5b3d2eb95d4/pageSize/30/page/25',
    'https://disney.content.edge.bamgrid.com/svc/content/CuratedSet/version/5.1/region/AR/audience/false/maturity/1450/language/es-419/setId/9f7c38e5-41c3-47b4-b99e-b5b3d2eb95d4/pageSize/30/page/26',

]


movies = []

for enlase in enlases:
    response = requests.get(enlase, headers=headers)
    data = response.json()
    lista = data['data']['CuratedSet']
    for item in lista["items"]:
        movies.append(item["internalTitle"])
        print("cargando {}".format(item["internalTitle"]))


df = pd.DataFrame(movies)
df.to_json('catalogoDisney.json')

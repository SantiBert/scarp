import requests
import pandas as pd

headers = {
    'accept': 'application/json',
    'authorization': 'Bearer eyJ6aXAiOiJERUYiLCJraWQiOiJRVmxCQXpUeFUzMVRtNWVfZTIzams0dFpwRWJpRERteWp6MDNsSS1hRVVBIiwiY3R5IjoiSldUIiwiZW5jIjoiQzIwUCIsImFsZyI6ImRpciJ9..bwNA7jhXMofbzR-f.Lp_YmT3QjoEoTJX-GKwAncJ-5DyXBg-iutREASUoNCPqHabadUz_2bVwrlYrnSmZ7OeJbP_TonzaYSRP_slePbKywS_iPzL-uRIGnxiuKw5fBx1yPad7dNFggCvJsAmhEkRiEc863mgdEDcd1fZFMhVVRFa106Pe3sG8JYB1YES8kdTGHCNED4YTpBfY9-YgU92UfqqNMnbdiI_bS3Z1mY9bERNt52nijfr0Ollyuf49mYILdkyMi7U_AysMpR_sWQmaG98itcjxINiS2uLyfQi3ivxS3gNreG4Jy4R8kumktHeV_PAnNt4EXDZ101kcLC5j4tXwtyEQRbcwMYudvLSeMXLVa4udjx7MfT1LJSk3CGOZFft_mo0VoDKy4TgFeYE9er9LEsMNzisYbKYso2qu9Wr4ZoyDLrWnTOOVN8xh3rvYHqMmIpDEVZzqQEI-Wn6b0rH4-_9-DpVlUAQF7XNPqC_J-0PnwSOs09yijNUBTD_Kmf0mmkKEFc47-KPpP0s-EbTPNWVAt9RsrSZ6n14nvVJZVTCKNRIYIffq0HYeo56-uBtNtF9Cw726roEG3mwdNsMPwNj3zKiGfAigI8qGQbq03trZhrTqH8rQlf-bIUx-1xYGfaAQ9vB4Dt2uJ3yAfXliUd7D9dH_DBnrbTtRX5GlGex6bu1-1w_PfcD0-bzBEWBHsGFqlhnzN3grkCiCi5D2_5rpk5VQfJKZ5g81FZo9U8b6Fz1KiMo4dIAuHtpI2uuyIloyaVkw6YezD5HdG9ngSppALBv1xGM4yR3HjUG1srxhkUC1Wzg7G-NwGq0iX7NNGx0Bdt8Z6dTRbAjokYXy6lBVatrFMlxx--ZerUsM72pggTZYoDLlR_tpksmqgPIE1EH1m1aulJhLHvQRFt3Dn-sUKAy5NWw5VomY7dkIH6RsDXeC2j4QTQDv5nNFVWFkUZGJXjNB7aJ7_9nihC0AthLHwram6hGX37M3G2865kZUp2iiA9I_OLb95PQ0rXeiM7qaGxPxiUPJ1gGrweEQ13KFBf05_vZrB_djJpm_gnnRuRTmr_cpaTymZ04JNyquem7zgmZ3-r6pbarwQen2UfoVzi6GQORoNJANMzf0e5uUxHPFqpCOx-RKN8SRH4is5MTl5n2vwHmAThEiuL1avmGqseZOahegPA7h2esMqHlG-CSr3uanHL8c1kTTOMNnRD-lUKvFJoqydcCKW-kzzwgrLeacIuvppefj_CobX-X9Rdi8tJBzQw_sRaBuwiSorrmyUgM_NFVGiTqJphHkb65_7o_qsxlQ6td7mepzjmcRxOZl4_g4Ykseu7znlSHZV5MbbAoU6Xcfdm1I1KNlghkosGweuKGeaF5_A1yuZOXDKOyOKhVftvQguvqQFa31XBHFZa45UVw_c1WjjDkGeBB1RqXzco-7fPJR0H3MTMBZysx82W4k7H7Yx5wTrZ7ipMI3peNc6pQMWgP1210ViATq4nixsxuAVpARAkSxkVJLHgYP2lPAlD-Aa23xfwFGTRNGhfVRSJQqeHV7h0NSPQaYbdzU46Hrfr41BlokUCD1U4-XFX0VfWPj3zrZD6hDFNo0eOhaiGJrCe5ZAWSS0ZwDuJYUW89m13gHTFmI6H8lDOK_b14Nu0B3Enyn4adaxXepu9j9abTQ5giHCkQhIxxZfOEEFAE8vkzCde0bjnlmYeF4NtTteUMKCP3R3Rb8wlVRQYgQh0a06AN6Iqx6a9gNXmayFNv4XNrokI2dPsmEPdO4CcLIsIFyQHRdXYhMXeBp_1JIGVi74rkAMCa6D2Rkm5CRn3GO8z88d6qKXxVu-Mp1h-V0oehWaY8Yn3y9R0yZV40BtT2DdEzFUfDfDlARJJ65GD8UZsfAXgeymndqCVMDbpvLOsatzZI44gpcJjuOSLSqLd5rRNlaSIhBbCNY51RVG3SwvMPaEOJl6sUUEUemKc3D_V1E4-_TD_euBpzuKnU99EJDKXDCHD_9U4v7nD4grmwdv7CAUQghJRN8Q4pGxD_a7ON12wBexDKN6l0JIfPaQk1NMTE5_kjrmkgvI1NR-d5sQ9lPUKIogv0yiOx5pXy1fSMa9inGIjel1XttVMmJTdhkTZmhsh8Aa6IsjDNiP_EAj4nY-fCEXqIp8x9lJ_FBMOuPlhgEtFVLU5SCrtKb3plKy80P-my3w4w4UW4SIJwQ2Ne1X0ql3sHpHqZRI7VzK2r4ZTitIJg71kO67mSsZxyf3w-cTzsJkVzb3swWbHYiI-SOjK7V1v-hFUlAzGk3XQ2Osx5nkHcjOOAx_K14jzMatfmB-7MvrjDqiBLODAuWfheCxhH0rXcGVGcaraoEeXHuoPxiSLPCrfW_FjTvMKwh78WJnCrAsIjg9gjAgSmhBp_c6-Ki12HPmwDIg-4kyTBpQ3MNQDqWx4yKG0pC52jTjZQjXaoHsnzVw3JPOmNfYDOCAvwzqgV03WXJfwMV14xWWjHR7kBUa0dlYsEiKMGXHl_VS3ZTqiBFhTcXPW_VWvFQNjOypcSceWCqIdIWLnWkL_I12541k431WDU9tts8nt_5ujVEF7_tCXQK1CcFO_pgbSdXa2-vQuJMwdSRF5c_r7bAKUEgZ1xz2-P0goy8arulMiGWrx8FxfAmsVcwUQDS46tarJUVnepfOqPq2xmmleEw6pY99-K_qh35HpfaC5zmvhaTQMfHAs_GJ2wydqpPJHw4Qf7E1PTE5dao1_GppxJ3S1HM3dGVn7Czayb3Raplwz2Eb648KtGD3rvGg41c5S7uqp4X0hfksugUBLXhjpoLcbs-XVzg-Xc231ErkLR5Vse-9fSDWgUDEA.7lI95IO7UVbOi1i-03fInw',
    'Referer': 'https://www.starplus.com/',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36',
    'x-application-version': '1.0.0',
    'x-bamsdk-client-id': 'star-22bcaf0a',
    'x-bamsdk-platform': 'windows',
    'x-bamsdk-version': '11.0',
    'x-dss-edge-accept': 'vnd.dss.edge+json; version=1'
}

enlases = [
    'https://star.content.edge.bamgrid.com/svc/content/CuratedSet/version/5.1/region/AR/audience/k-false,l-true/maturity/1850/language/es-419/setId/85a9e484-92f9-4c45-b555-ae2fa8825e92/pageSize/30/page/2',
    'https://star.content.edge.bamgrid.com/svc/content/CuratedSet/version/5.1/region/AR/audience/k-false,l-true/maturity/1850/language/es-419/setId/85a9e484-92f9-4c45-b555-ae2fa8825e92/pageSize/30/page/3',
    'https://star.content.edge.bamgrid.com/svc/content/CuratedSet/version/5.1/region/AR/audience/k-false,l-true/maturity/1850/language/es-419/setId/85a9e484-92f9-4c45-b555-ae2fa8825e92/pageSize/30/page/4',
    'https://star.content.edge.bamgrid.com/svc/content/CuratedSet/version/5.1/region/AR/audience/k-false,l-true/maturity/1850/language/es-419/setId/85a9e484-92f9-4c45-b555-ae2fa8825e92/pageSize/30/page/5',
    'https://star.content.edge.bamgrid.com/svc/content/CuratedSet/version/5.1/region/AR/audience/k-false,l-true/maturity/1850/language/es-419/setId/85a9e484-92f9-4c45-b555-ae2fa8825e92/pageSize/30/page/6',
    'https://star.content.edge.bamgrid.com/svc/content/CuratedSet/version/5.1/region/AR/audience/k-false,l-true/maturity/1850/language/es-419/setId/85a9e484-92f9-4c45-b555-ae2fa8825e92/pageSize/30/page/7',
    'https://star.content.edge.bamgrid.com/svc/content/CuratedSet/version/5.1/region/AR/audience/k-false,l-true/maturity/1850/language/es-419/setId/85a9e484-92f9-4c45-b555-ae2fa8825e92/pageSize/30/page/8',
    'https://star.content.edge.bamgrid.com/svc/content/CuratedSet/version/5.1/region/AR/audience/k-false,l-true/maturity/1850/language/es-419/setId/85a9e484-92f9-4c45-b555-ae2fa8825e92/pageSize/30/page/9',
    'https://star.content.edge.bamgrid.com/svc/content/CuratedSet/version/5.1/region/AR/audience/k-false,l-true/maturity/1850/language/es-419/setId/85a9e484-92f9-4c45-b555-ae2fa8825e92/pageSize/30/page/10',
    'https://star.content.edge.bamgrid.com/svc/content/CuratedSet/version/5.1/region/AR/audience/k-false,l-true/maturity/1850/language/es-419/setId/85a9e484-92f9-4c45-b555-ae2fa8825e92/pageSize/30/page/11',
    'https://star.content.edge.bamgrid.com/svc/content/CuratedSet/version/5.1/region/AR/audience/k-false,l-true/maturity/1850/language/es-419/setId/85a9e484-92f9-4c45-b555-ae2fa8825e92/pageSize/30/page/12',
    'https://star.content.edge.bamgrid.com/svc/content/CuratedSet/version/5.1/region/AR/audience/k-false,l-true/maturity/1850/language/es-419/setId/85a9e484-92f9-4c45-b555-ae2fa8825e92/pageSize/30/page/13',
    'https://star.content.edge.bamgrid.com/svc/content/CuratedSet/version/5.1/region/AR/audience/k-false,l-true/maturity/1850/language/es-419/setId/85a9e484-92f9-4c45-b555-ae2fa8825e92/pageSize/30/page/14',
    'https://star.content.edge.bamgrid.com/svc/content/CuratedSet/version/5.1/region/AR/audience/k-false,l-true/maturity/1850/language/es-419/setId/85a9e484-92f9-4c45-b555-ae2fa8825e92/pageSize/30/page/15',
    'https://star.content.edge.bamgrid.com/svc/content/CuratedSet/version/5.1/region/AR/audience/k-false,l-true/maturity/1850/language/es-419/setId/85a9e484-92f9-4c45-b555-ae2fa8825e92/pageSize/30/page/16',
    'https://star.content.edge.bamgrid.com/svc/content/CuratedSet/version/5.1/region/AR/audience/k-false,l-true/maturity/1850/language/es-419/setId/85a9e484-92f9-4c45-b555-ae2fa8825e92/pageSize/30/page/17',
    'https://star.content.edge.bamgrid.com/svc/content/CuratedSet/version/5.1/region/AR/audience/k-false,l-true/maturity/1850/language/es-419/setId/85a9e484-92f9-4c45-b555-ae2fa8825e92/pageSize/30/page/18',
    'https://star.content.edge.bamgrid.com/svc/content/CuratedSet/version/5.1/region/AR/audience/k-false,l-true/maturity/1850/language/es-419/setId/85a9e484-92f9-4c45-b555-ae2fa8825e92/pageSize/30/page/19',
    'https://star.content.edge.bamgrid.com/svc/content/CuratedSet/version/5.1/region/AR/audience/k-false,l-true/maturity/1850/language/es-419/setId/85a9e484-92f9-4c45-b555-ae2fa8825e92/pageSize/30/page/20',
    'https://star.content.edge.bamgrid.com/svc/content/CuratedSet/version/5.1/region/AR/audience/k-false,l-true/maturity/1850/language/es-419/setId/85a9e484-92f9-4c45-b555-ae2fa8825e92/pageSize/30/page/21',

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
df.to_json('catalogoStar.json')

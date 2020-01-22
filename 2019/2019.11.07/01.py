from urllib import request

urlBase = 'https://user.qzone.qq.com/237977800/infocenter?_t_=0.6341768532370362'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3314.0 Safari/537.36 SE 2.X MetaSr 1.0',
    'Cookie': 'zzpaneluin=; zzpanelkey=; pgv_pvi=7686316032; pgv_si=s4461112320; _qpsvr_localtk=0.903867146261413; pgv_pvid=9876742000; pgv_info=ssid=s2177056625; ptisp=ctc; ptui_loginuin=237977800; uin=o0237977800; skey=@8QguIUGHO; RK=8fJZWTotH+; ptcz=cea38275589d5abd0615e79ba6a4d2e5b568ccf638274fab0f93514bbba9c2d7; p_uin=o0237977800; pt4_token=BHlzcFDxggjBuR6fwvBwaABVbo68uhiuFfDvNqIWd9E_; p_skey=hgEYXAbRjCKtHAtAP*lhs4ORdhPzODopX28b7lFGivk_; Loading=Yes; qz_screen=1920x1080'
}

res = request.Request(urlBase, headers=headers)

resp = request.urlopen(res)

print(resp.read().decode('utf-8'))